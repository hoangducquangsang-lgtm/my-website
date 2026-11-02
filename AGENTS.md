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

## Title trang chủ — đã khoá (02/11/2026)

Title trang chủ là `Natural Pet Toys Wholesale from Vietnam | VietPaw`.
**Không đổi cho tới 02/05/2027.**

Lý do: GA4 Pages & Screens ghi nhận trang chủ mang 3 title khác nhau trong 90 ngày
(263 / 210 / 130 lượt xem). Mỗi lần đổi title, Google phải đánh giá lại trang từ
đầu nên thứ hạng không bao giờ ổn định.

Title được khai ở hai chỗ, phải luôn trùng nhau:

- `_source/common.py` — bảng title theo đường dẫn, khoá `"/"`
- `_source/page_manifest.json` — mục đầu tiên

`<title>`, `og:title` và `twitter:title` trong `index.html` là do build sinh ra từ
hai file trên, nên không sửa tay trong `index.html`.

Kiểm tra sau 30 ngày: GA4 → Pages & Screens, lọc trang chủ — chỉ còn **một** title.

**Đổi title nào cũng phải chạy `test_brand_urls.py`.** File đó có bảng
`EXPECTED_TITLES` ghi cứng title của 5 route (`/materials/`, `/factory/`,
`/quality-control/`, `/services/wholesale-pet-products/`,
`/pet-toys-manufacturer-vietnam/`). `validate_site.py` **không** bắt lỗi này — chỉ
`test_brand_urls.py` mới bắt, nên phải chạy cả bộ test chứ không riêng validate.

## 18 title đã rút ngắn — đã khoá (02/11/2026)

Đợt 1 của mục 1.4 trong audit SEO: 18 title từ 61–75 ký tự rút còn ≤55, và 2 meta
description từ 161–163 rút còn 124–139. Lý do: Google cắt title trong SERP, cả 18
trang đều đang 0 click.

Khai báo ở `_source/common.py` — `TITLE_OVERRIDES` và `META_OVERRIDES`, có ghi chú ngày.
`<title>`, `og:title`, `twitter:title` và `meta description` trong từng `index.html` là
do build sinh ra từ đó, **không sửa tay trong `index.html`**.

**Không đổi cho tới 02/05/2027.** Cùng lý do với title trang chủ: mỗi lần đổi title,
Google phải đánh giá lại trang từ đầu. Cần 2–4 tuần để ổn định.

Còn lại đợt 2, cố ý hoãn: `/products/coffee-wood-dog-chew/` (65) và
`/collections/coffee-wood/` (63). Đây là hai trang **duy nhất** trong nhóm đang thực sự
ra click (CTR 5,2% và 5,4%), nên để riêng sau 2 tuần để đo được tác động, không lẫn
với 18 trang kia. Nội dung đề xuất nằm ở `../DUYET_TITLE_MUC_1.4.md`.

Lưu ý: đổi title **không** làm `lastmod` nhảy — vân tay băm vùng `<main>`, title nằm
trong `<head>`. Đúng điều mình muốn, xem mục `sitemap.xml` quy tắc 4.

Đo sau 30 ngày: GSC → Performance, so CTR từng URL với baseline 02/11/2026.

## 5 trang CTR 0% — title/meta đã sửa và khoá (02/11/2026)

Mục 1.5 của audit SEO: `/guides/how-long-do-coffee-wood-chews-last/`, `/guides/`,
`/capabilities/`, `/guides/coffee-wood-chew-size-guide/`, `/pet-toys-manufacturer-vietnam/`.
4 title + 4 meta. **Không đổi cho tới 02/05/2027.**

### Hai khẳng định KHÔNG được đưa vào title/meta

Audit mục 3.4 có đề xuất sẵn hai câu, cả hai đều **sai so với chính website**. Đã bị
loại, đừng áp dụng lại khi đọc audit:

1. **Không nói chew đã được "tested" hay đo tuổi thọ.** Audit đề xuất
   *"Tested by Dog Size"* / *"measured on our own XS–XXL range"*. Chính trang
   `/guides/how-long-do-coffee-wood-chews-last/` viết: *"We do not publish a figure in
   days or weeks... durability testing for chew toys would mean testing on animals and
   nobody in this category has done it."*

2. **Không nói "factory direct" hay "our factory" theo nghĩa sở hữu.** Audit đề xuất
   *"Factory Direct"* / *"A Vietnam pet toy factory"*. FAQ `/about/` viết:
   *"Does VietPaw own its factories? No, and we do not claim to. We work with two
   factories, in Dak Lak and Gia Lai."* (Link điều hướng "Our Factory" là tên menu,
   không phải khẳng định sở hữu — đừng dựa vào đó để viết title.)

Nếu thực tế kinh doanh đã khác thì **sửa `/about/` trước**, rồi mới đổi title/meta.

### Meta description của guide nằm ở đâu

**Guide thì sửa trong `content_guides.py`, KHÔNG dùng `META_OVERRIDES`.**
Guide có Article schema, và `validate_site.py` bắt `description` trong schema phải
trùng meta description. `META_OVERRIDES` được áp dụng **sau** khi schema đã dựng xong,
nên đặt meta của guide ở đó sẽ làm build ra lỗi `article description mismatch`.
Các trang không phải guide thì dùng `META_OVERRIDES` bình thường.

Lưu ý kèm theo: trang hub `/guides/` in lại description của từng guide trong `<main>`,
nên sửa meta một guide sẽ làm `lastmod` của `/guides/` nhảy. Đó là đúng — nội dung
hiển thị của hub thực sự đã đổi.

## Đo lường GA4 — code nằm ở đâu (02/11/2026)

Mục 1.6 của audit. Trước đợt này repo **không có một dòng code đo lường nào** — chỉ
có thẻ gtag cơ bản. `submit_quote` không nằm trong repo: đó là custom event tạo trong
GA4 Admin từ `page_view` của `/request-a-quote/thank-you/`.

### Ranh giới giữa hai file — giữ đúng

- **`assets/rfq.js` không được chứa `gtag(`.** `test_rfq.cjs` có hẳn một assertion chặn
  điều này. Khi gửi thành công, nó chỉ bắn một DOM event `vietpaw:lead` (bubbles).
- **`assets/track.js` giữ toàn bộ GA4 event.** Nạp trên cả 69 trang, đặt sau `</main>`
  nên không ảnh hưởng `lastmod`.

Tách như vậy để module xử lý dữ liệu người mua không dính gì tới analytics, và để
mọi quyết định "gửi gì lên GA4" nằm đúng một chỗ, dễ rà soát.

### Luật cứng: không bao giờ gửi PII lên GA4

`name`, `email`, `phone`, `company` **không được** xuất hiện trong bất kỳ tham số GA4 nào.
Vi phạm chính sách Google và có thể bị xoá property. Cả `test_rfq.cjs` lẫn
`test_track.cjs` đều có assertion chặn. Chỉ gửi: `buyer_type`, `country`, `products`,
`enquiry_type`, `form_id`, `lead_source`, `page_location`.

### Event đang bắn

`generate_lead` (lúc Formspree xác nhận, **không** phụ thuộc trang thank-you),
`contact_whatsapp`, `contact_email`, `form_view` (≥50% trong viewport, một lần),
`scroll_75` (một lần).

**`request_sample` cố ý KHÔNG bắn.** `enquiry_type` là trường ẩn giá trị cố định
`samples_and_pricing` trên form duy nhất, nên event này sẽ trùng 1:1 với `generate_lead`
và thổi phồng số key event. Bật lại khi có form xin mẫu riêng, hoặc khi `enquiry_type`
thực sự biến thiên.

### Phần KHÔNG nằm trong repo

Key events và custom dimensions phải cấu hình trong **GA4 Admin**, code không làm thay
được. **GA4 không hồi tố**: gắn sao hôm nay chỉ tính từ hôm nay. Đó là lý do
`form_start` có 25 sự kiện mà tổng key events chỉ bằng 2.

Cũng lưu ý: site **chưa có trang privacy policy và chưa có banner consent**, trong khi
khách chính ở EU/DE/UK. GA4 đã chạy từ trước đợt này, nhưng đây là nợ cần xử lý.

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
