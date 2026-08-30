# WINVN — Website nội dung B2B

Bản cập nhật thương hiệu, hình ảnh và Guides ngày **30/08/2026**. Website tĩnh tiếng Anh dành cho buyer quốc tế. Đã sửa trong thư mục local; chưa đăng lên website live. Toàn bộ thương hiệu hiển thị là **WINVN**.

## Xem kết quả

Mở `index.html` hoặc chạy một static server tại thư mục này. HTML/ảnh/liên kết nội bộ dùng đường dẫn tương đối để giữ cách xem offline. Trang có canonical theo `https://vietpaw.com/`.

Xem **WEBP_FORM_UPDATE_VI.md** để đọc cập nhật biểu mẫu và ảnh mới nhất. **WINVN_UPDATE_REPORT_VI.md** ghi nhận đợt đổi thương hiệu; **SEO_UPDATE_REPORT_VI.md** ghi nhận đợt SEO trước đó.

## Quy mô

- **67 trang HTML**, gồm trang cảm ơn cho biểu mẫu vừa khôi phục; các URL đã có được giữ nguyên.
- 20 guide, 6 sản phẩm, 4 collection vật liệu, 6 giải pháp khách hàng.
- 65 URL trong sitemap; `/case-studies/` và `/request-a-quote/thank-you/` dùng `noindex,follow`.
- Cấu trúc SEO: Organization, WebSite, BreadcrumbList, Product, Article. Không tự tạo giá, rating, GTIN hay chứng nhận.
- Đã thay mọi tham chiếu tới 8 ảnh nền đen bằng ảnh trong thư mục được cung cấp; ảnh kiểm tra độ ẩm dùng đúng `Bản sao của kiem_go_9.jpg`.
- 20 bài Guides được viết lại và ghi tác giả Sarah trong nội dung lẫn metadata.
- Chân trang theo nội dung chủ website yêu cầu, gồm 40+ countries và email `sarah@vietpaw.com`.
- 30 tài nguyên cũ vẫn còn để phục hồi/giữ liên kết cũ, nhưng ảnh nền đen không còn được trang nào gọi. Ảnh mới giữ nguyên dữ liệu ảnh gốc.
- Biểu mẫu 5 trường và nút **Send Enquiry** được khôi phục từ folder cũ; gửi đến điểm nhận Formspree có sẵn `https://formspree.io/f/mvkpbvlb`. Chưa kiểm tra gửi/nhận email thật hoặc trạng thái tài khoản nhận.
- 20 ảnh nội dung/chia sẻ có 120 phiên bản WebP trong `assets/img/webp/`; 85 vị trí ảnh dùng `srcset`, `sizes` và kích thước nội tại. Ảnh gốc và favicon PNG được giữ nguyên.

## Chỉnh sửa và tạo lại trang

Nội dung và bố cục chung nằm trong `_source/`; `assets/rfq.js` xử lý biểu mẫu tại máy khách. Chỉnh CSS tại `_source/style.css`, không chỉ sửa bản sao `assets/style.css`.

Bộ tạo trang dùng Python 3 và Pillow có hỗ trợ WebP, không cần cài framework:

```text
python _source/build.py
python _source/validate_site.py
node _source/test_rfq.cjs
python _source/test_responsive_images.py "../_VietPaw_backups/Website-before-form-webp-20260830-203740.zip"
```

Nếu có local server tại 127.0.0.1:8765, có thể thêm `--http` vào lệnh kiểm tra. Không dùng lệnh build cũ trỏ tới `/tmp/site_build`: đã thay bằng đường dẫn dựa trên vị trí project. Build không xóa thư mục, không ghi lại ảnh gốc/catalogue; các bản WebP được tạo hoặc tái sử dụng khi nguồn chưa thay đổi. Chỉnh quy tắc ảnh trong `_source/responsive_images.py`; khi đổi cách mã hóa, tăng `SETTINGS.version` để tạo lại các bản dẫn xuất.

Đừng sửa riêng HTML nếu muốn giữ thay đổi qua lần build tiếp theo.

## Hồ sơ nội bộ

- `_source/review/SOURCE_REGISTER_VI.md`: nguồn và quyết định sử dụng/không sử dụng từng claim.
- `_source/review/KEYWORD_MAP.md`: intent cho toàn bộ URL, chưa có search volume xác minh.
- `_source/validation_report.json`: kiểm tra nội bộ và local HTTP.
- `_source/review/image_replacements.json`: đối chiếu từng ảnh cũ với ảnh nguồn mới.
- `_source/review/responsive_images.json`: nguồn gốc, kích thước và dung lượng từng bản WebP.
- `_source/review/webp_validation.json`: kiểm tra bảo toàn ảnh/nội dung và ước tính dung lượng theo màn hình.
- Backup trước khi sửa: `../_VietPaw_backups/VietPaw-before-SEO-2026-08-30.zip`.
- Backup trước đợt đổi thương hiệu: `../_VietPaw_backups/Website-before-WINVN-2026-08-30.zip`.
- Backup trước đợt biểu mẫu/WebP: `../_VietPaw_backups/Website-before-form-webp-20260830-203740.zip`.

## Trước khi đăng lên hosting

Chưa có thao tác xuất bản trong lần chỉnh này. Tên miền canonical vẫn là `https://vietpaw.com/`: chủ website yêu cầu đổi thương hiệu, chưa yêu cầu chuyển tên miền. Email `sarah@vietpaw.com` được giữ đúng chỉ định. Không đổi tên thư mục dự án để tránh ảnh hưởng đường dẫn đang dùng.

Kiểm tra trước khi public: địa điểm/công suất, size hiện hành, MOQ/chính sách mẫu, đổi trả và hồ sơ testing. Tuyên bố biodegradable trong footer được chép theo yêu cầu trực tiếp của chủ website, không đồng nghĩa với việc đã có kiểm nghiệm cho mọi SKU/bao bì. Bộ Proof có tài liệu tên công ty khác và mẫu DRAFT; không dùng như chứng chỉ đã xác minh.

Khi triển khai, chỉ đưa các trang HTML, assets cần thiết, robots.txt và sitemap.xml vào gói public. **Không đưa `_source/`, các báo cáo nội bộ, tài liệu nghiên cứu PDF ở root hoặc backup lên public.** robots.txt không phải cơ chế bảo mật. Bản catalogue đang được liên kết có tên `winvn-wholesale-catalogue.pdf`, nội dung giữ nguyên tài liệu WINVN đã cung cấp.

Điểm nhận Formspree cũ đã được khôi phục trong mã, nhưng cần chủ website kiểm tra tài khoản, hộp thư nhận, giới hạn tên miền và gửi một yêu cầu thật trên tên miền triển khai. Không tự động nhập lại mã Google Analytics từ bản cũ. Việc kết nối CRM, đăng lên server/domain hiện hành, GSC và kiểm tra Core Web Vitals cần một bước triển khai riêng được cho phép. Không có điểm SEO hoặc kết quả ranking được đo trong lần này.
