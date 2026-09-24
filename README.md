# VietPaw — Natural Pet Toys from Vietnam

Website B2B tiếng Anh của **VietPaw** (vietpaw.com) dành cho buyer quốc tế: wholesale, private label và OEM/ODM cho đồ chơi thú cưng từ gỗ cà phê, xơ dừa, sợi gai (hemp) và xơ mướp (loofah).

Cập nhật lần cuối: **24/09/2026**.

## Nhận diện đang áp dụng

- **VietPaw tự sản xuất** tại **3 nhà máy riêng: Đắk Lắk, Gia Lai, Bình Dương**. Văn phòng, kho và chuẩn bị xuất khẩu tại TP. Hồ Chí Minh.
- **Công suất: 100.000 chiếc/tháng** — ghi thống nhất trên trang About và Factory (và các trang có nhắc tới công suất).
- Phạm vi sản phẩm: 4 dòng vật liệu (gỗ cà phê, xơ dừa, hemp, loofah). **Không** có đệm/nệm, võng, thảm trên website.
- Tên pháp nhân chỉ xuất hiện ở **một dòng chân trang** (hằng `FOOTER_LEGAL` trong `_source/common.py`). `validate_site.py` báo lỗi nếu tên này xuất hiện ở bất kỳ chỗ nào khác trên trang.
- Liên hệ: sarah@vietpaw.com · +84 906 111 016 (WhatsApp).
- Mạng xã hội: LinkedIn, Instagram, Facebook (https://www.facebook.com/sarahhue6789), YouTube — khai báo trong `SOCIAL` của `_source/common.py`.
- Google Analytics 4: mã `G-XTXJ45XN8B`, gắn đúng 1 lần trong `<head>` của cả 67 trang (`GOOGLE_TAG_ID` trong `common.py`; kiểm tra bằng `test_google_tag.py`).

## Form báo giá (/request-a-quote/)

Gửi tới Formspree `https://formspree.io/f/mvkpbvlb`.

| Trường | Bắt buộc |
|---|---|
| Full name | ✔ |
| Business email | ✔ |
| Phone / WhatsApp | ✔ |
| Company | — (không bắt buộc) |
| Country / destination | ✔ |
| I am a… (Amazon seller, Startup, Eco shop, Business owner, Wholesale, Importer, Sourcing, Other) | ✔ |
| Product interest — ô tích chọn: Coffee wood chew, Coconut, Hemp, Loofah | ✔ (ít nhất 1) |

Không còn mục "Optional project details". Khi khách bấm từ trang sản phẩm (`?product=...`), ô sản phẩm tương ứng được tích sẵn (`assets/rfq.js`).

## Catalogue

`assets/downloads/vietpaw-catalogue-2026.pdf` (Catalog 2026, 8 trang), tải trực tiếp từ `/wholesale-catalogue/`. Bản cũ nằm trong `_to_delete/`.

## Guides

20 bài, tác giả Sarah. Mỗi bài có 1 ảnh đầu bài đúng chủ đề (khai báo trong `FEATURE` của `_source/content_guides.py`) và 2–3 ảnh minh hoạ trong bài; ảnh đầu bài cũng là ảnh thẻ ở trang /guides/ và ảnh chia sẻ. Mọi ảnh được phục vụ dưới dạng **WebP** responsive (`srcset` 320–1600 px).

**Ngày hiển thị của bài viết giữ cố định** trong `_source/guide_dates.py` — không đổi theo ngày build.

## Hiển thị trên điện thoại

- Menu thu gọn (nút ☰) dưới 1050 px.
- Bảng ≤ 4 cột chuyển thành thẻ xếp dọc có nhãn trên điện thoại; bảng rộng hơn cuộn ngang, có gợi ý "Swipe sideways".
- Nút "Request Sample" cố định ở góc phải dưới, gọn, không che nội dung.
- Kiểm tra ở 360 px, 390 px và 1440 px: không tràn ngang, không lỗi JS, không 404.

## Sửa và build

Mọi nội dung sinh từ `_source/*.py`. **Không sửa trực tiếp các file `index.html`** — lần build sau sẽ ghi đè. CSS sửa ở `_source/style.css` (build tự chép sang `assets/style.css`).

```text
python _source/build.py
python _source/validate_site.py
python _source/test_google_tag.py
python _source/test_brand_urls.py .
node _source/test_rfq.cjs
node _source/test_navigation.cjs
node _source/test_local_preview.cjs
```

Cần Python 3 + Pillow (có WebP) và Node.js. Xem thử: mở `index.html` hoặc chạy static server trong thư mục này.

Các file test lịch sử (`test_brand_consistency.py`, `test_responsive_images.py`, `test_commercial_policy.py`, `test_seo_leads.py`, `test_proof_removal.py`) kiểm tra ảnh chụp các phiên bản cũ; không phải tiêu chí chấp nhận cho bản hiện hành.

## Tệp và thư mục

- `_source/` — bộ sinh trang, CSS, test.
- `_source/review/` — nguồn ảnh, keyword map, manifest WebP.
- `_to_delete/` — ảnh/tệp đã rút khỏi website (watermark, catalogue cũ, ảnh có tên pháp nhân). Không được deploy; xoá khi đã xem lại.
- `tmp/` — tệp tạm, không deploy.
- Các file `*_VI.md`, `BAO_CAO_*.md` — báo cáo các đợt sửa trước, chỉ để tham khảo lịch sử.

## Trạng thái

Đã build trên máy, **chưa deploy**. Sau khi deploy, kiểm tra GA4 Realtime và link Facebook trên site thật.
