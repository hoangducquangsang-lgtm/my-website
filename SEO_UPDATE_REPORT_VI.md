# Báo cáo cập nhật nội dung SEO VietPaw
Ngày thực hiện: 30/08/2026

> Hồ sơ của đợt SEO trước. Sau báo cáo này, chủ website yêu cầu đổi toàn bộ thương hiệu thành WINVN, thay ảnh và viết lại Guides. Thông tin hiện hành được ghi trong **WINVN_UPDATE_REPORT_VI.md**; không lấy tên thương hiệu/contact cũ dưới đây để ghi đè bản mới.

## Kết quả

Đã chỉnh trực tiếp thư mục **4. VietPaw Website**, đồng bộ nội dung HTML và bộ tạo trang trong `_source`. Giữ giao diện, màu thương hiệu và ảnh sẵn có; không xây lại bằng một nền tảng khác, không xuất bản lên internet, không thay đổi website WINVN hoặc website VietPaw đang hoạt động.

- Trước: 56 trang HTML. Sau: **66 trang**, gồm **10 trang mới**.
- Giữ toàn bộ 56 đường dẫn cũ, không tự đặt chuyển hướng.
- Mở rộng 11 danh mục/collection theo nhu cầu sử dụng, 4 collection vật liệu và 6 trang sản phẩm.
- Rà soát, biên tập lại 20 hướng dẫn hiện có; không tạo hàng loạt blog thay từ khóa.
- Bổ sung 3 dịch vụ, trang manufacturer Vietnam, Factory, QC, 2 giải pháp khách hàng và 1 sản phẩm dây hemp.
- Chuẩn bị hub case study ở trạng thái **noindex,follow**, chưa đưa vào sitemap và menu vì chưa có hồ sơ kết quả khách hàng đủ căn cứ.
- Sitemap có **65 URL**. Đây là số URL đề xuất cho crawler, không phải số trang đã được Google lập chỉ mục.
- Bản gốc được sao lưu ở `../_VietPaw_backups/VietPaw-before-SEO-2026-08-30.zip`.

## 1. Nội dung đã thay đổi

### Trang chủ và phân vai từ khóa

Trang chủ dùng H1 “Natural Pet Toy Manufacturer for Global Brands”, nhấn mạnh đề xuất B2B và bốn nhóm vật liệu. Không dùng “sustainable” như một cam kết tuyệt đối cho toàn bộ sản phẩm. Nội dung về vật liệu và môi trường vẫn có nhưng đi kèm phạm vi cụ thể.

Tạo `/pet-toys-manufacturer-vietnam/` để sở hữu nhóm tìm kiếm nhà sản xuất tại Việt Nam. Trang này chưa tồn tại trong bản local trước khi sửa, dù được nêu trong audit website live. Không kết luận cannibalization đã xảy ra vì chưa có dữ liệu Search Console.

Collection coffee wood tập trung supplier/wholesale; trang sản phẩm coffee wood tập trung SKU/thông số; danh mục chew toys tập trung lựa chọn dòng hàng; guide tập trung giải thích và dẫn sang trang thương mại.

### Danh mục, vật liệu và sản phẩm

Mỗi nhóm đã có nội dung mua hàng thực chất: cách chọn dòng, thông số cần xác nhận, MOQ, mẫu, nhãn riêng, bao bì, thời gian, QC, giấy tờ và liên kết tiếp theo. Các trang có nội dung riêng theo mục đích sử dụng, không chỉ thay tên vật liệu.

Thống nhất sáu trang sản phẩm với thành phần, size, MOQ, lựa chọn thương hiệu, yêu cầu kiểm tra, điều kiện đặt hàng và FAQ. Thêm `/products/hemp-rope-dog-toy/`; giữ nguyên trang hemp ball cũ để phân biệt hai cấu trúc sản phẩm.

Bảng coffee wood sử dụng bộ tham chiếu CC01 trong “Thông tin CWC.md”: XS dưới 5 kg; S 5–10 kg; M 10–20 kg; L 20–30 kg; XL 30–40 kg; XXL trên 40 kg. Bảng kích thước/khối lượng được dùng chung giữa sản phẩm và size guide, ghi rõ phải đối chiếu mẫu và bảng hiện hành. Không coi cân nặng là bảo đảm an toàn cho mọi con vật.

Danh mục puppy và strong chewer đã bỏ khuyến nghị mặc định “cứ dùng XS/S” hoặc “cứ tăng lên XL/XXL”. Trang puppy hiện là nội dung định hướng sourcing, không tự nhận đã có SKU dành riêng cho chó con được xác nhận.

### Dịch vụ và khách hàng

`/capabilities/` trở thành hub so sánh wholesale, private label và OEM/ODM. Thêm các trang:

| Trang | Vai trò |
| --- | --- |
| `/services/oem-odm-pet-toy-manufacturing/` | Brief, feasibility, prototype, nghiệm thu thiết kế, quyền sở hữu và thay đổi sản xuất |
| `/services/private-label-pet-toys/` | Sản phẩm hiện có + logo, tag, engraving, bao bì và duyệt mẫu |
| `/services/wholesale-pet-products/` | Báo giá theo SKU, nhiều sản phẩm, carton, mua lại |
| `/solutions/pet-brands/` | Phát triển sản phẩm, bản sắc thương hiệu, quyền thiết kế và kiểm soát phiên bản |
| `/solutions/retail-chains/` | Hồ sơ vendor, đóng gói đơn vị/thùng, triển khai chuỗi và bổ sung hàng |

Bốn giải pháp cũ cũng đã được sửa: Amazon, wholesaler, startup, eco shop. Không cam kết doanh thu, xếp hạng, lợi nhuận hoặc chấp nhận FBA.

### Nhà máy, QC và bằng chứng

Tạo `/factory/` và `/quality-control/`. Dùng sơ đồ sản xuất gốc và quy trình kiểm tra năm bước từ tài liệu WINVN, không tự tạo thông số máy, chu kỳ sấy, AQL, kết quả pull test hoặc tên nhân viên.

Thông tin “3 nhà máy, 5–6 triệu sản phẩm/năm” chỉ giữ ở trang Factory dưới dạng **số liệu do nhà cung cấp mô tả**, không coi là sản lượng đã kiểm toán hoặc công suất còn trống. Không tự chọn một địa chỉ nhà máy làm địa chỉ xác minh khi nguồn đang khác nhau.

Ảnh quy trình/kho là ảnh tham chiếu trong thư viện có sẵn; không gắn ngày chụp, số lô hay quyền sở hữu thiết bị chưa được xác nhận.

### Compliance, môi trường và an toàn

- Phân biệt báo cáo kiểm nghiệm sản phẩm, kiểm tra QC và giấy tờ của lô hàng.
- Bỏ ý rằng mọi pet toy đều có hoặc bắt buộc có CPSIA certificate.
- Bỏ ý rằng vật liệu tự nhiên tự động đáp ứng REACH.
- Bỏ cam kết mỗi đơn hàng chắc chắn có tất cả CO/EUR.1, kiểm dịch, hun trùng và báo cáo độc lập.
- Không khẳng định hàng từ Việt Nam tự động tránh rủi ro UFLPA, hoặc luôn có lợi thế thuế.
- Không gọi cả bốn vật liệu đều là phụ phẩm, không gọi vacuum bag tự động plastic-free.
- Bỏ “splinter-free”, an toàn khi nuốt, trị răng miệng, caffeine-free đã kiểm nghiệm, antimicrobial hoặc hiệu quả sức khỏe chưa có chứng cứ.
- Giữ mô tả thành phần và quy trình ở phạm vi nguồn cho phép, kèm cảnh báo sử dụng có giám sát.

Các điểm pháp lý/kỹ thuật đã đối chiếu thêm hướng dẫn chính thức của CPSC, ECHA, FTC, CBP, ICC và AAHA. Nội dung website là tài liệu hỗ trợ mua hàng, không phải chứng nhận hay ý kiến chuyên môn thay thế.

### Amazon và AOV

Bỏ tỷ lệ phí Amazon cố định mang tính toàn cầu. Dẫn tới [trang giá chính thức Amazon](https://sell.amazon.com/pricing) và phân biệt chi phí sản phẩm, vận chuyển, marketplace, quảng cáo/hoàn trả.

Không công bố bảng 677/28/100 đơn như dữ liệu hoạt động của VietPaw. Tài liệu gốc ghi là phân tích ví dụ Canophera, chưa cung cấp kỳ đo, marketplace, dữ liệu đơn gốc, phạm vi seller hoặc phương pháp. Các con số được lưu trong sổ nguồn nội bộ để bổ sung sau, không chuyển thành case study “đã thành công”.

### RFQ và trải nghiệm đọc

Bổ sung công ty, website, quốc gia, loại khách, sản phẩm/size, số lượng mỗi SKU, branding/OEM/ODM, điểm đến, ngày cần hàng và yêu cầu bao bì/kiểm nghiệm.

Chỉ 4 trường bắt buộc: tên, email, quốc gia và sản phẩm. CTA sản phẩm tự điền tên sản phẩm vào mẫu.

Biểu mẫu **chỉ chuẩn bị email**, không gửi tự động và không lưu vào CRM. Có lựa chọn tải nội dung yêu cầu thành tệp text, trạng thái giải thích rõ chưa gửi. Giữ nguyên contact VietPaw hiện hữu: `sarah.winvn@gmail.com`, `+84 906 111 016`; không tự đổi sang contact công ty trên WINVN.

Thêm menu Manufacturing, liên kết ngữ cảnh, CTA mẫu/WhatsApp, menu đóng/mở bằng bàn phím/chạm và vùng cuộn cho bảng rộng. Giao diện được giữ theo phong cách hiện tại; chưa thực hiện kiểm thử trình duyệt trực quan/e2e.

## 2. Những điểm cần xác nhận trước khi đăng thật

| Mức ưu tiên | Nội dung cần xác nhận | Cách xử lý hiện tại |
| --- | --- | --- |
| Cao | Pháp nhân WINVN và WYNVN; tài liệu cũ có địa chỉ khác | Giữ tên công ty website hiện có, không dùng chứng từ khác tên làm bằng chứng |
| Cao | `Phytosanitary.png` ghi thông tin ABC và mẫu “DRAFT” | Không công bố như chứng thư thực tế |
| Cao | Chứng nhận SGS/Intertek/CPSIA/REACH thực sự có cho SKU nào | Không gắn badge hoặc tự nhận có chứng nhận hiện hành |
| Cao | Địa điểm/số nhà máy, cơ sở sở hữu hay đối tác; công suất theo SKU | Chỉ trình bày thông tin nguồn và checklist xác minh |
| Cao | Bảng size/chiều dài coffee wood hiện hành, đặc biệt XL/XXL và dung sai | Dùng một bảng tham chiếu có nêu nguồn; yêu cầu duyệt mẫu trước PO |
| Cao | MOQ từng dòng, chi phí engraving/box/media, điều kiện mẫu và hoàn phí | Diễn đạt theo báo giá, không hứa miễn phí toàn bộ |
| Cao | Cam kết xử lý lỗi, đổi hàng, thời hạn khiếu nại | Chuyển sang điều khoản cần thỏa thuận trong đơn hàng |
| Trung bình | Contact bán hàng VietPaw có tiếp tục dùng hay chuyển corporate | Giữ thông tin cũ, ghi rõ vai trò |
| Trung bình | Bộ phận/tác giả/reviewer kỹ thuật và hồ sơ cá nhân | Chưa tự thêm người, chứng chỉ hoặc chức danh |
| Trung bình | Dữ liệu AOV, case study, lời chứng thực có quyền công bố | Hub case study để noindex; có mẫu thu thập hồ sơ trong sổ nguồn |
| Trung bình | Ngôn ngữ trong catalogue PDF cũ | Giữ tệp gốc, đặt cảnh báo là tài liệu tham chiếu, chưa biên tập PDF |

## 3. Kiểm tra đã thực hiện

- 66/66 trang phản hồi HTTP 200 **trên máy chạy thử**, không phải xác nhận server public.
- Một H1 mỗi trang; title và description không trùng nhau.
- Canonical, Open Graph, X metadata và ảnh chia sẻ đúng đường dẫn trang/sản phẩm.
- JSON-LD đọc được; Organization, WebSite, BreadcrumbList, Product, Article theo nội dung hiện có; không thêm giá, review, rating hoặc GTIN giả.
- Không có liên kết/tệp/anchor nội bộ hỏng; không có trang indexable bị cô lập.
- Sitemap trùng khớp 65 trang indexable; hub case study bị loại đúng chủ đích.
- 20 guide có liên kết thương mại theo ngữ cảnh.
- 56 URL cũ còn tồn tại; đối chiếu hash giữ nguyên 30 ảnh/tệp tải gốc.
- Kiểm tra hành vi RFQ ở mức unit: điền sản phẩm từ CTA, trường phân loại, Unicode, kiểm tra bắt buộc, nội dung email và tải tệp.
- Build chạy lại được trên Windows và không xóa thư mục website.

Không tuyên bố đã kiểm tra GSC, số trang Google index, Core Web Vitals thực tế, backlink, lưu lượng, thứ hạng, email được gửi/nhận hay form CRM. Không tạo điểm SEO mới hoặc dự báo tăng trưởng.

## 4. Tài liệu bàn giao

- `index.html`: trang chủ đã cập nhật.
- `_source/review/KEYWORD_MAP.md`: bản đồ từ khóa/ý định cho 66 URL; không tạo search volume.
- `_source/review/SOURCE_REGISTER_VI.md`: sổ nguồn, mâu thuẫn và điều kiện công bố.
- `_source/validation_report.json`: kết quả kiểm tra tự động.
- `_source/build.py`: tạo lại HTML/sitemap từ nguồn.
- `_source/validate_site.py`, `_source/test_rfq.cjs`: kiểm tra lặp lại.

Bước tiếp theo hợp lý là duyệt các thông tin “Cao” ở trên, sau đó thực hiện quy trình đăng lên hạ tầng hiện tại. Không tải nguyên thư mục tài liệu nghiên cứu, báo cáo nội bộ, `_source` hoặc backup lên một hosting tĩnh công khai.
