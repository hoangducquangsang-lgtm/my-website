# WINVN — Đồng bộ thông tin doanh nghiệp và thương mại

**Cập nhật nhận diện sau báo cáo này:** VietPaw là commercial/export brand; WINVN INT CO., LTD là legal manufacturer. Xem `VIETPAW_BRAND_PROOF_UPDATE_VI.md`. Các chính sách thương mại bên dưới vẫn được giữ, nhưng quy mô site hiện là 68 trang và có thêm Proof; quy ước chỉ dùng WINVN đã được thay thế theo yêu cầu mới.

Cập nhật ngày 31/08/2026 trong folder `4. VietPaw Website`. Chưa xuất bản lên hosting hoặc tên miền live. Đây là báo cáo hiện hành, thay thế các mức thương mại khác trong báo cáo ngày 30/08; các báo cáo cũ được giữ để tra lịch sử.

## Nội dung đã sửa

| Hạng mục | Nội dung hiện hành |
| --- | --- |
| Năm đăng ký | “WINVN INT CO., LTD, registered in Vietnam in 2019”; About ghi ngày 12 November 2019. Đã bỏ câu pháp nhân sản xuất từ 2018. |
| Biodegradable | Bỏ claim khỏi toàn bộ footer. Không có claim quảng cáo này trong metadata thương mại. Giữ bài Guides giải thích yêu cầu bằng chứng, không biến chúng thành cam kết về sản phẩm. |
| MOQ | Sản phẩm tiêu chuẩn được chọn: từ 50 pcs. Private-label run, hang tags, labels và printed boxes: từ 500 pcs. Khắc laser trên coffee wood phù hợp: tùy chọn riêng từ 50 pcs. |
| Thời gian sản xuất | Đơn dưới 500 pcs: 5–7 days. Full container: 60–80 days. Đơn từ 500 pcs chưa tới container, mixed orders và custom development cần báo lịch riêng. Không cộng vận chuyển vào production lead time; không tự đổi days thành working days. |
| Mẫu | “3 free samples. Buyer covers courier.” Mẫu tiêu chuẩn có thể gửi trong 1 working day sau khi chốt mẫu và courier. Không còn lời hứa hoàn/credit phí courier. Tạo prototype riêng cần xác nhận lịch. |
| Độ ẩm coffee wood | “below 14% before packing”; kiểm tra theo batch và cung cấp reading theo yêu cầu, không đặt cận dưới 12%. |
| QC | “six-stage drying/quality protocol with five QC checkpoints.” Phân biệt số giai đoạn và số điểm kiểm tra; không công bố giả định về nhiệt độ/thời gian sấy hoặc thứ tự chi tiết chưa có nguồn. |
| Địa chỉ pháp lý | Floor 1, 70 Street No. 10, Van Phuc Residence 1, Quarter 22, Hiep Binh Ward, Ho Chi Minh City, Vietnam. Đã đồng bộ footer, About, Contact và dữ liệu Organization. |
| Phạm vi catalogue | Website tập trung bốn collection toys/chews. Home, About, Materials và Wholesale nói rõ catalogue WINVN rộng hơn có Pet Beds, kèm liên kết trang WINVNINT. Không tự tạo trang/spec Pet Bed mới. |
| Chứng từ | Certificate of Origin (CO), Fumigation Certificate, Phytosanitary Certificate, Packing List, Commercial Invoice, Bill of Lading (B/L); giữ “subject to destination/product requirements”. Batch moisture reading theo yêu cầu. |

Giữ thương hiệu WINVN, Sarah, `sarah@vietpaw.com`, điện thoại/WhatsApp `+84 906 111 016`, phạm vi xuất khẩu 40+ và canonical `https://vietpaw.com/`. Không tự chuyển domain hoặc đổi sang contact khác của WINVNINT.

## Phạm vi và kết quả kiểm tra

- Tạo lại **67 trang HTML**; giữ **65 URL sitemap**, 20 Guides, 6 sản phẩm và các trạng thái index/noindex hiện có.
- Footer và dữ liệu Organization được kiểm tra trên **67/67 trang**. Nội dung chính thay đổi trên **46 trang**, gồm **31 bảng điều kiện đặt hàng dùng chung**. Meta description riêng của About, Private Label và Quality Control đã sửa đồng bộ với nội dung.
- Không còn các mức thương mại cũ được nêu trong yêu cầu: 200 pcs, lead time 15–20/25–30, độ ẩm 12–14%, năm pháp nhân 2018, địa chỉ Van Phuc City và “five-stage QC”.
- Bảo toàn **176 tệp assets** so với backup trước lần sửa: ảnh, PDF catalogue, CSS và JavaScript không đổi byte nào. **131 WebP**, **85 vị trí ảnh** và các thuộc tính responsive được kiểm tra lại.
- Menu, form 5 trường, ảnh hemp đã chọn, URL, tác giả Sarah và ngày hiển thị Guides không thay đổi. Kiểm tra logic menu/form bằng bộ test mô phỏng đều đạt; không gửi enquiry thật.
- Kiểm tra HTML, liên kết nội bộ, ảnh, dữ liệu cấu trúc và chính sách thương mại: **không lỗi, không cảnh báo**. Chi tiết nằm tại `_source/validation_report.json`, `_source/review/commercial_policy_validation.json` và `_source/review/webp_validation.json`.
- Chưa kiểm tra trực quan lại bằng trình duyệt, hiệu năng live hoặc việc nhận email thực tế. Không có điểm Core Web Vitals/ranking được đo trong lần này.

## Nguồn và giới hạn

Yêu cầu sửa trực tiếp của chủ website là căn cứ chính. Các mức MOQ, mẫu, lead time, ngày đăng ký, địa chỉ và dòng Pet Beds được đối chiếu với [trang chủ WINVNINT](https://www.winvnint.com/). Thuật ngữ QC và độ ẩm được đối chiếu với [trang coffee wood WINVNINT](https://www.winvnint.com/coffeewoodchew/).

Không lấy dữ liệu OEM cũ trả về từ đường dẫn không dấu slash để ghi đè chính sách mới. Tài liệu PDF catalogue tải xuống được giữ nguyên bản gốc; trang download đã nhắc buyer dùng điều kiện hiện tại trên website và quotation, không dùng nội dung cũ trong PDF làm điều khoản đặt hàng. Chưa biên tập lại PDF.

Bảng size CC01 XS–XXL theo tài liệu của chủ website được giữ nguyên. WINVNINT hiện trình bày thêm dòng Gorilla S–XL khác mã; không tự trộn hai bảng trong lần cập nhật này. Các con số công suất/địa điểm sản xuất khác không nằm trong yêu cầu sửa, vẫn cần xác nhận cho đơn hàng.

## Sao lưu và duy trì

Backup nguyên trạng trước khi sửa: `../_VietPaw_backups/Website-before-commercial-policy-20260831-084003.zip`.

Thông tin dùng chung nằm trong `_source/common.py` và `_source/content_helpers.py`; nội dung riêng nằm trong các module `content_*.py`. Đã cập nhật bộ kiểm tra để phát hiện chính sách cũ quay lại khi tạo trang. Hướng dẫn chạy nằm trong `README.md`.

Giữ báo cáo này, `_source/` và các tài liệu nội bộ ngoài gói public khi xuất bản.
