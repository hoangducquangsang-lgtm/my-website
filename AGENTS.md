# Ghi chú vận hành — repo vietpaw.com

Đọc phần "Hosting & deploy" trước khi đụng tới bất cứ thứ gì liên quan đến
cache, redirect hay sitemap. Ba file cấu hình trong repo này **không chạy**, và
chúng đã từng làm nhiều lượt phân tích đi sai hướng.

## Hosting & deploy

Đo trực tiếp ngày 01/11/2026 bằng `curl -I` trên cả `www` lẫn apex:

- **Tên miền:** mua tại Namecheap — Namecheap chỉ làm registrar/DNS, **không host**.
- **Host thật:** GitHub Pages (xem file `CNAME`), có **Cloudflare proxy** đứng trước.
- **Luồng request:** Cloudflare → Fastly (CDN của GitHub Pages) → GitHub Pages.
- **Deploy = commit + push lên `origin/main`.** Push bằng GitHub Desktop là xong;
  **không có** bước upload thủ công nào. Site lên sau khoảng 1–2 phút.
- **Redirect `www` → apex do GitHub Pages phát, mã 301.** Không phải Cloudflare:
  phản hồi 301 mang đủ header `x-github-request-id` và `x-fastly-request-id`,
  nghĩa là request đã đi xuyên Cloudflare tới tận origin.
- **Cloudflare không cache `sitemap.xml`** (`cf-cache-status: DYNAMIC`), nên
  **không cần purge** sau khi deploy. GitHub Pages đặt `Cache-Control: max-age=600`,
  tức bản mới lan truyền trong vòng ~10 phút.

## Ba file cấu hình KHÔNG có tác dụng

| File | Dành cho | Trạng thái trên GitHub Pages |
|---|---|---|
| `.htaccess` | Apache / LiteSpeed (Namecheap cPanel) | Bị bỏ qua hoàn toàn |
| `_headers` | Netlify / Cloudflare Pages | Bị bỏ qua hoàn toàn |
| `_source/hosting/cloudflare-single-redirects.json` | Cloudflare zone rules | Chưa bao giờ áp dụng (`deployment_status: prepared_not_applied`), và không cần vì GitHub Pages đã trả 301 |

Giữ lại để tham khảo nếu sau này đổi host. **Muốn đổi cache hoặc redirect thật thì
phải vào dashboard Cloudflare** — sửa ba file này không có tác dụng gì.

## sitemap.xml và `<lastmod>`

`sitemap.xml` do `_source/build.py` sinh ra. Ngày `<lastmod>` lấy từ
`_source/lastmod.py`, dựa trên sổ đăng ký `_source/page_lastmod.json`.

Cách hoạt động: mỗi trang được băm vùng `<main>` thành một "vân tay". Vân tay
không đổi thì giữ nguyên ngày cũ; đổi thì ngày nhảy sang ngày build. Lý do phải
làm vậy: build ghi đè lại **toàn bộ** file HTML mỗi lần chạy, nên cả `mtime` lẫn
ngày commit git đều cho ra **cùng một ngày cho cả 67 URL** — mà sitemap có
`lastmod` đồng loạt như thế thì Google bỏ qua, coi là không đáng tin.

Quy tắc phải nhớ:

1. **Sửa nội dung một guide thì cập nhật ngày trong `_source/guide_dates.py` trước
   khi build.** Quên thì build tự dừng và gọi đúng tên slug. Làm vậy để `lastmod`
   trong sitemap, thẻ `<time>` hiển thị và `dateModified` trong schema luôn trùng nhau.
   Các trang không phải guide thì hoàn toàn tự động.
2. **`_source/page_lastmod.json` phải luôn được commit.** Mất hoặc bị revert thì
   lần build kế tiếp coi cả 67 trang là vừa đổi và dồn hết về ngày build. Lỡ xảy ra
   thì chạy `python3 _source/backfill_lastmod.py` để dựng lại từ lịch sử git.
3. **Không bao giờ sửa tay `lastmod` cho "tươi".** Google phát hiện và sẽ bỏ qua
   cả sitemap.
4. **Tránh gộp một đợt sửa chữ nhỏ cho toàn site vào một commit.** Đợt 30/10/2026
   đã đẩy 44 trang về cùng một ngày. Cảnh giác nhất với các đợt **rải link nội bộ
   hàng loạt**: link nằm trong `<main>` nên bị tính là đổi nội dung.
5. **Không thêm `<changefreq>` và `<priority>`.** Google đã bỏ qua từ lâu.
6. **GSC: giữ đúng một entry sitemap, ở property apex.** Không nộp lại ở property
   `www` — sitemap ở đó chỉ nhận redirect, tuy vẫn đọc được nhưng làm loãng báo cáo.

## Trước mỗi lần push

```
python3 _source/validate_site.py
```

Mất khoảng 10 giây. Nó kiểm cả `lastmod`: đủ trên mọi URL, đúng định dạng W3C,
không ở tương lai, không quá đồng nhất, và mỗi guide khớp với `dateModified` của nó.

## Về 5 test "fail"

`test_proof_removal.py`, `test_brand_consistency.py`, `test_commercial_policy.py`,
`test_responsive_images.py`, `test_seo_leads.py` sẽ báo lỗi nếu chạy thẳng. **Đây là
bình thường, không phải hỏng.** Như `README.md` đã ghi, chúng kiểm tra ảnh chụp các
phiên bản cũ và **không phải tiêu chí chấp nhận cho bản hiện hành**. Hai lý do cụ thể:

- Chúng nhận tham số là **đường dẫn tới file ZIP backup** của phiên bản cũ, không
  phải thư mục site. Không có file ZIP đó thì không chạy được.
- Một số khẳng định đã cũ hơn site: `test_proof_removal.py` chờ 67 trang trong khi
  site đã có 69; `test_brand_consistency.py` chờ một câu brand trong `common.py` đã
  được viết lại từ lâu.

Bộ test thực sự dùng để kiểm tra bản hiện hành (xem `README.md`):

```
python3 _source/validate_site.py
python3 _source/test_google_tag.py
python3 _source/test_brand_urls.py .
node _source/test_rfq.cjs
node _source/test_navigation.cjs
node _source/test_local_preview.cjs
```

## Mọi file trong repo đều public trên vietpaw.com

GitHub Pages phục vụ **toàn bộ** file trong nhánh, không chỉ HTML. Đã kiểm chứng
01/11/2026: `https://vietpaw.com/README.md` trả về đầy đủ nội dung README nội bộ.
Nghĩa là các file sau cũng tải được công khai:

- `README.md`, `AGENTS.md`, `BAO_CAO_*.md`, `*_VI.md`, `DE_XUAT_*.md`, `HUONG_DAN_*.md`
- Toàn bộ `_source/` — mã build, `common.py`, danh sách test
- `Nghiên cứu thị trường quốc tế.pdf` (~29 MB) ở thư mục gốc

`robots.txt` chỉ chặn *thu thập* `/_source/`, **không chặn truy cập**. Ai biết đường
dẫn vẫn tải được.

Thư mục `_to_delete/` thì an toàn — nằm trong `.gitignore` nên không lên GitHub.

Cân nhắc khi có thời gian: chuyển GitHub Pages sang phục vụ từ thư mục `/docs` hoặc
một nhánh riêng, để tài liệu nội bộ ở gốc repo không bị phục vụ công khai nữa.
**Không** thêm thông tin nhạy cảm (khoá, mật khẩu, giá vốn, tên khách) vào bất kỳ
file nào trong repo này.

## Nợ kỹ thuật khác (tính đến 01/11/2026)

- `validation_report.json` từng bị commit ở trạng thái cũ hơn code một commit,
  nghĩa là có lần push mà không chạy validate trước. Xem mục "Trước mỗi lần push".
- `HUONG_DAN_TRIEN_KHAI.md` (12/10/2026) mô tả quy trình deploy qua Namecheap +
  purge Cloudflare — đã lỗi thời, xem mục "Hosting & deploy" ở trên.
