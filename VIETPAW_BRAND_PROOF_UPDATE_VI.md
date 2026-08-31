# VietPaw — Natural Pet Products by WINVN INT CO., LTD.

Cập nhật ngày 31/08/2026 theo chỉ định mới của chủ website. Đã sửa thư mục local `4. VietPaw Website`; chưa xuất bản lên hosting/live.

**Cập nhật tiếp theo:** chủ website đã yêu cầu công khai ảnh. Trang Proof hiện hiển thị đủ bốn ảnh, có nút “View full-size PNG” và “Download original PNG”. Bản xem trước là WebP responsive; PNG tải xuống giữ nguyên byte so với tệp nguồn. Các liên kết không mở thêm tab. Chỉ cập nhật bản website trong thư mục; chưa tải thay đổi lên hosting live.

## Nhận diện đã áp dụng

- **VietPaw:** thương hiệu thương mại/xuất khẩu.
- **WINVN INT CO., LTD:** nhà sản xuất pháp lý.
- Dòng chữ ký đúng yêu cầu: **Natural Pet Products by WINVN INT CO., LTD.**

Đã đồng bộ trên 68 trang: header, footer, điều hướng, tiêu đề tìm kiếm, metadata chia sẻ, nội dung thương mại, tác giả/brand trong Guides và nội dung email subject của form. About và Contact giải thích vai trò của hai tên. Sáu trang sản phẩm có hai dòng riêng “Commercial / export brand” và “Legal manufacturer”.

Dữ liệu SEO dùng Brand = VietPaw, Organization = WINVN INT CO., LTD; mỗi Product liên kết đúng brand/manufacturer. Favicon chữ VP thay favicon chữ W trong website; tệp cũ được giữ để phục hồi. Không sửa tên/đường dẫn ảnh hoặc pixel của ảnh sản phẩm.

## Manufacturing → Proof

Đã thêm `/proof/`, mục **Proof** trong menu Manufacturing và footer. Các trang About, Factory, Quality Control và Testing & Export Documents cùng các khối kiểm tra nhà cung cấp có liên kết tới đây. Nút yêu cầu hồ sơ dùng form hiện có và điền sẵn nội dung; không tự gửi email.

| Hồ sơ được cung cấp | Quan sát trực tiếp | Cách thể hiện |
| --- | --- | --- |
| CO.png | Form VJ năm 2022, tên exporter **WYNVN INT CO., LTD** | Tham chiếu lịch sử; chưa xác nhận cùng pháp nhân với WINVN |
| Fumigation Certificate.png | Vietnamcontrol, tháng 12/2021, lô wooden pet toys; không thể hiện WINVN là exporter | Tham chiếu xử lý một lô hàng; không dùng như chứng nhận an toàn cho mọi sản phẩm |
| Phytosanitary.png | Dùng công ty mẫu ABC, thông tin dạng mẫu, ngày hiển thị tháng 5/2024 | Tài liệu minh họa, không trình bày là chứng từ lô hàng của VietPaw/WINVN |
| Surrendered.png | B/L tháng 8/2022, tên shipper **WYNVN INT CO., LTD** | Tham chiếu lịch sử; không khẳng định WINVN đã vận chuyển lô đó |

Trang Proof hiện là **gallery bốn ảnh có chú thích phạm vi**, không phải danh sách chứng chỉ đã xác thực. Theo yêu cầu công khai, các bản PNG gốc được đặt trong `assets/img/proof/`; ảnh trong `7. Proof` không đổi. Không sửa tên pháp nhân/chữ ký/con dấu hoặc tự che thêm dữ liệu trên bản công khai. Việc công khai các ảnh này không biến hồ sơ khác pháp nhân/tài liệu mẫu thành chứng nhận hiện hành của WINVN INT CO., LTD.

## Kiểm tra và bảo toàn

- 68 trang HTML, 66 URL sitemap; giữ toàn bộ 67 URL cũ.
- 68/68 trang có VietPaw, dòng chữ ký và phân vai pháp nhân; sáu Product có brand/manufacturer đúng.
- 31 bảng điều kiện thương mại không thay đổi so với backup: năm đăng ký 2019, MOQ private label 500, 3 mẫu miễn phí/khách trả courier, lead time theo quy mô, độ ẩm dưới 14%, QC sáu giai đoạn/năm checkpoints và địa chỉ pháp lý được giữ.
- 175 assets cũ ngoài stylesheet giữ nguyên byte; stylesheet bổ sung chữ ký dài và bố cục ảnh Proof nguyên khung. Hiện có 155 ảnh WebP/89 vị trí ảnh: 24 bản WebP và 4 vị trí mới dành cho Proof; 85 vị trí ảnh trước đó giữ nguyên.
- 20 tác giả Sarah và lịch ngày Guides được giữ. Form năm trường và đích Formspree không đổi; chỉ subject chuyển sang VietPaw. Logic menu/form qua bộ test mô phỏng, không có enquiry thật được gửi.
- Kiểm tra mã, ảnh, nội dung, dữ liệu cấu trúc và liên kết nội bộ không lỗi/cảnh báo. Chưa kiểm tra trực quan lại trong trình duyệt hoặc đo hiệu năng live.

Catalogue PDF giữ nguyên bản nhà sản xuất. Trang download ghi rõ đây là tài liệu gốc của WINVN INT CO., LTD, chưa thay artwork thành VietPaw; không giả định bản PDF đã đổi nhận diện.

## Sao lưu và hồ sơ kiểm tra

Backup trước thay đổi: `../_VietPaw_backups/Website-before-VietPaw-export-brand-20260831-090828.zip`.

Backup trước khi công khai ảnh: `../_VietPaw_backups/Website-before-public-proof-images-20260831-093007.zip`.

Kiểm tra hiện tại: `_source/validation_report.json`, `_source/review/brand_proof_validation.json`, `_source/review/webp_validation.json`. Hướng dẫn tạo lại và kiểm tra nằm trong `README.md`.

Chỉ bốn bản PNG được duyệt trong `assets/img/proof/` và các ảnh WebP dẫn xuất thuộc gói website công khai. Không đưa `_source/`, báo cáo nội bộ, backup hoặc nguyên folder tài liệu `7. Proof` lên hosting.
