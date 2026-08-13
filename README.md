# VietPaw — B2B Website (v1)

Website tĩnh (static HTML) cho VietPaw — thương hiệu xuất khẩu/bán sỉ của **WINVN INT CO., LTD**, dùng cho khách B2B quốc tế: startup brand, Amazon seller, eco pet shop (EU), wholesaler/distributor.

## Cách xem thử ngay
Mở file `index.html` bằng trình duyệt (double-click) để xem toàn bộ site chạy offline. Menu, link nội bộ, ảnh đều hoạt động vì dùng đường dẫn tương đối.

## Cách deploy thật (khuyến nghị)
Kéo thả cả thư mục này vào [Netlify Drop](https://app.netlify.com/drop) hoặc Vercel/Cloudflare Pages để có link live trong ~1 phút, sau đó trỏ domain `vietpaw.com` (khi đã mua) vào đó. Site không cần build step — publish thẳng thư mục gốc.

## Quy mô đã build
- 56 trang HTML: 35 trang lõi (trang chủ, About, Capabilities, Materials, Certifications, Sustainability, How to Order, Wholesale Catalogue, RFQ, Contact, danh mục Dog/Cat Toys, 4 collection vật liệu thật, 5 trang sản phẩm, 4 trang Solutions theo tệp khách + hub) + 1 Guides hub + 20 bài content hub (19 bài theo kế hoạch gốc + 1 bài size guide bổ sung).
- `sitemap.xml` và `robots.txt` đã có sẵn ở gốc.
- Schema.org: Organization, WebSite, BreadcrumbList, FAQPage, Product (không kèm giá) trên các trang liên quan.
- Ảnh: lấy từ catalog thật (CATALOG WINVN 2026.pdf) và ảnh raw material/xuất hàng bạn cung cấp — không dùng ảnh stock.

## Thông tin đã dùng (xác nhận lại trước khi public)
- Brand hiển thị: **VietPaw** — pháp nhân công khai: **WINVN INT CO., LTD**
- Domain dự kiến: `vietpaw.com` (bạn cần tự đăng ký, tôi chỉ kiểm tra sơ bộ chưa có site đang chạy, không phải WHOIS chính thức)
- Điện thoại: +84 906 111 016 · Email: sarah.winvn@gmail.com
- Địa chỉ: 70 St. 10, Van Phuc City, Hiep Binh Ward, Ho Chi Minh City, Vietnam

## Việc cần làm trước khi public chính thức
1. **Mua domain vietpaw.com** (hoặc domain bạn chọn) và cập nhật `DOMAIN` trong `site_src/common.py` nếu đổi.
2. **Form RFQ** (`/request-a-quote/`) hiện dùng `mailto:` — mở email client của khách, không lưu lead tự động. Nên nối vào Formspree/Google Form/CRM thật khi có domain.
3. **Catalogue PDF** ở `/wholesale-catalogue/` đang là bản catalog WINVN 2026 gốc — nên làm lại bìa/thương hiệu VietPaw nếu muốn tách bạch hoàn toàn.
4. **Rà lại toàn bộ số liệu** (công suất 5–6 triệu sp/năm, 30+ nước, MOQ, thời gian sản xuất...) với đội vận hành trước khi public — đây là số liệu lấy từ tài liệu nội bộ bạn cung cấp, cần xác nhận vẫn đúng thời điểm hiện tại.
5. **Ảnh sản phẩm còn thiếu**: một số sản phẩm (ví dụ Coconut Fiber Dog Ball, Hemp Fiber Ball) đang dùng ảnh gần giống thay vì ảnh chụp riêng — nên bổ sung ảnh chuyên biệt khi có.
6. **Pháp lý**: các câu chuyện "hỗ trợ cộng đồng dân tộc thiểu số", chứng chỉ CPSIA/REACH "có sẵn theo yêu cầu" cần đúng sự thật 100% trước khi đăng — đây là các claim nhạy cảm dễ bị buyer hoặc marketplace kiểm chứng ngược.

## Cấu trúc mã nguồn (để chỉnh sửa sau này)
Toàn bộ site được generate từ Python trong thư mục `_source/` (đã kèm trong bản giao này) — mỗi trang là 1 hàm Python build HTML từ template dùng chung (`common.py`). Nếu cần tôi chỉnh nội dung/thêm trang, cứ nhắn — tôi sửa script và build lại toàn site trong vài giây thay vì sửa tay từng file HTML.
