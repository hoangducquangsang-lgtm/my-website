# Cập nhật menu, ảnh hemp và ngày Guides

Ngày thực hiện: 30/08/2026. Phạm vi: bản trong thư mục `4. VietPaw Website`, chưa xuất bản.

## Menu thả xuống

Ảnh chụp cho thấy các nhóm điều hướng cùng mở và chồng lên nhau, không phải website mở cửa sổ/tab trình duyệt mới.

- Các nhóm dùng chung một nhóm mở độc quyền; mở mục mới đóng mục cũ.
- Có xử lý dự phòng cho trình duyệt chưa hỗ trợ nhóm độc quyền của phần tử details.
- Bấm ra ngoài, chọn liên kết, nhấn Esc hoặc chuyển tiêu điểm ra khỏi menu đều đóng menu.
- Nhấn Esc trả tiêu điểm về tiêu đề menu; không chặn thao tác bàn phím hoặc điều hướng liên kết.
- Khi quay lại trang bằng nút Back, menu trở về trạng thái đóng.
- Giữ nguyên thiết kế WINVN và nội dung menu; không mở tab mới bằng mã xử lý.

Tham khảo hành vi phần tử: [MDN — details và thuộc tính name](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details#name).

## Ảnh hai sản phẩm

| Sản phẩm | Ảnh chủ website chỉ định | Bản gốc lưu trong website |
| --- | --- | --- |
| Hemp Fiber Rope Ball | Ảnh 3: chó Golden Retriever giữ bóng dây | `assets/img/winvn-hemp-fiber-rope-ball.png` |
| Hemp Rope Dog Toy | Ảnh 2: `Bản sao của do_choi_cho_cho_7.jpg` | `assets/img/winvn-hemp-rope-dog-toy.jpg` |

Đồng bộ ảnh đầu trang sản phẩm, ảnh chia sẻ, dữ liệu Product và thẻ sản phẩm liên quan — 13 vị trí ảnh nội dung được thay. Các trang giới thiệu bộ vật liệu vẫn có thể dùng ảnh bộ mẫu cũ, không bị thay nhầm thành một sản phẩm riêng.

Tạo thêm 11 WebP, không phóng lớn vượt ảnh nguồn và không cắt nội dung ảnh. Tổng hiện tại: 22 ảnh nguồn, 131 WebP. Giữ toàn bộ 158 tệp ảnh gốc/ảnh WebP có trước đợt này; không xóa ảnh cũ. Đã xem hai WebP đại diện ở chiều rộng 800 px.

## Ngày trong Guides

- 20 ngày hiển thị riêng, từ **25/06/2026 đến 30/08/2026**.
- Thứ tự trên trang Guides đi từ mới đến cũ, xen kẽ khoảng cách **3 và 4 ngày** giữa các bài, vẫn giữ nguyên nhóm chủ đề.
- Đồng bộ ngày trên thẻ bài, dòng Updated trong bài và trường dateModified trong dữ liệu Article.
- Lưu ngày cố định theo từng bài; tạo lại website không tự đổi các ngày này.
- Đây là **lịch ngày hiển thị theo yêu cầu của chủ website**, không phải lịch sử cập nhật thực tế được xác minh. Không tự thêm ngày xuất bản hoặc bằng chứng biên tập trong quá khứ.

## Kiểm tra và khôi phục

- Kiểm tra logic menu bằng mô hình sự kiện: mở liên tiếp, bấm nhanh, bấm ra ngoài, chọn liên kết, Esc, chuyển tiêu điểm và quay lại trang.
- Kiểm tra 67 trang, 65 URL trong sitemap, 20 tác giả Sarah, ngày Guides, ảnh WebP và liên kết nội bộ.
- Ngoài ngày hiển thị, ảnh được yêu cầu và chú thích bộ mẫu không còn phù hợp trên hai trang sản phẩm, nội dung chính của các trang được bảo toàn so với bản sao lưu.
- Biểu mẫu 5 trường và Formspree đã khôi phục ở đợt trước được giữ nguyên; không gửi yêu cầu thật.
- Chưa kiểm thử trang trực tiếp bằng trình duyệt. Không xuất bản hoặc thay đổi tên miền.
- Sao lưu: `../_VietPaw_backups/Website-before-menu-hemp-dates-20260830-211411.zip`.

Không đưa báo cáo này, bản sao lưu hay `_source/` vào gói website công khai.
