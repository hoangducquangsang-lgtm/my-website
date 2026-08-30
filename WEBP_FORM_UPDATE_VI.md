# Cập nhật biểu mẫu và ảnh WebP — WINVN

Ngày: 30/08/2026. Chỉ cập nhật thư mục `4. VietPaw Website`, chưa xuất bản. Folder cũ tại `D:/1. Vietpaw/my-website - Copy/` chỉ được đọc, không chỉnh sửa.

## Biểu mẫu theo bản cũ

- Khôi phục nguyên văn đoạn giới thiệu bên dưới “Tell us about your project”.
- Khôi phục 5 trường theo đúng thứ tự: Full name, Company & role, Email, I am a..., Products of interest.
- Giữ các lựa chọn khách hàng và gợi ý nội dung như bản cũ; chỉ Full name và Email bắt buộc.
- Khôi phục nút **Send Enquiry** và điểm nhận có sẵn `https://formspree.io/f/mvkpbvlb`; không tạo tài khoản hoặc dịch vụ nhận mới.
- Có trạng thái đang gửi, khóa gửi trùng, giữ nội dung khi lỗi, giới hạn chờ phản hồi và thông báo email dự phòng.
- Chỉ chuyển đến `/request-a-quote/thank-you/` sau khi dịch vụ nhận trả phản hồi thành công. Trang cảm ơn dùng WINVN và `noindex,follow`, không đưa vào sitemap.
- Giữ giao diện hiện tại, thương hiệu WINVN, footer 40+ countries và email `sarah@vietpaw.com`. Không nhập lại menu, thương hiệu VietPaw, số liệu cũ hoặc mã Google Analytics của folder cũ.
- Đã kiểm thử bằng phản hồi mô phỏng; **không gửi yêu cầu thật** và không xác nhận hộp thư nào đang liên kết với tài khoản Formspree. Cần chủ website kiểm tra gửi/nhận trên tên miền triển khai.

## Ảnh cho máy tính và điện thoại

- 20 ảnh nội dung/chia sẻ đang dùng được tạo thành **120 bản WebP**.
- Các mốc chiều rộng 320, 480, 640, 800, 960, 1200 và 1600 px, cộng kích thước gốc khi nhỏ hơn mức tối đa; không phóng lớn ảnh vượt nguồn.
- Giữ toàn bộ bố cục ảnh, không cắt lại; không đổi ảnh thú cưng trang chủ, ảnh kiểm tra độ ẩm hoặc số hiển thị trên thiết bị.
- 85 vị trí ảnh trên website dùng phiên bản WebP, có tập ảnh theo độ phân giải, quy tắc kích thước theo bố cục và chiều rộng/cao để dành chỗ trước khi tải.
- Các ảnh chia sẻ và ảnh trong dữ liệu cấu trúc cũng dùng bản tối ưu của đúng ảnh trước đó.
- Giữ nguyên 38 tệp ảnh trước đợt sửa, gồm các ảnh cũ dự phòng. Favicon PNG và tài liệu PDF không bị chuyển đổi. Vì giữ bản gốc, dung lượng toàn thư mục không phản ánh dung lượng người xem phải tải.

### Ước tính dung lượng ảnh trang chủ

Tổng các tệp ảnh được tham chiếu trước tối ưu: **13.792.857 byte** (~13,79 MB).

| Kịch bản chọn ảnh theo kích thước màn hình | Tổng ảnh sau tối ưu | Giảm so với các tệp gốc |
| --- | ---: | ---: |
| Điện thoại rộng 390 px, mật độ điểm ảnh 2× | 822.660 byte (~0,82 MB) | 94,04% |
| Máy tính rộng 1440 px, mật độ 1× | 351.166 byte (~0,35 MB) | 97,45% |
| Máy tính rộng 1440 px, mật độ 2× | 803.364 byte (~0,80 MB) | 94,18% |

Đây là tổng dung lượng tệp ảnh trên **toàn trang** theo mô hình chọn ảnh; không phải đo lưu lượng thực, dung lượng tải ngay khi mở trang hoặc Core Web Vitals. Trình duyệt có thể chọn khác tùy mật độ điểm ảnh, bộ nhớ đệm và điều kiện mạng.

## Kiểm tra và khôi phục

- 67 trang HTML, 65 URL trong sitemap, 20 Guides có tác giả Sarah; không có lỗi trong bộ kiểm tra liên kết, ảnh, footer và dữ liệu cấu trúc cơ bản.
- Nội dung của 65 trang ngoài biểu mẫu giữ nguyên so với bản sao lưu; không thay đổi các ảnh đã chọn.
- 120 WebP mở/giải mã được, kích thước và tỷ lệ ảnh đúng; mọi đường dẫn ảnh responsive tồn tại, kể cả trang nằm nhiều cấp thư mục.
- Đã xem ảnh WebP đại diện: thú cưng ở trang chủ, thiết bị kiểm tra độ ẩm và giỏ xơ mướp. Chưa kiểm thử hiển thị trang trực tiếp bằng trình duyệt.
- Sao lưu trước sửa: `../_VietPaw_backups/Website-before-form-webp-20260830-203740.zip`.
- Kết quả chi tiết: `_source/validation_report.json`, `_source/review/responsive_images.json`, `_source/review/webp_validation.json`.

Tham khảo kỹ thuật: [Formspree — gửi biểu mẫu bằng JavaScript](https://help.formspree.io/articles/building-your-form/submit-forms-with-javascript-ajax/). Không đưa báo cáo nội bộ hoặc `_source/` vào gói website công khai.
