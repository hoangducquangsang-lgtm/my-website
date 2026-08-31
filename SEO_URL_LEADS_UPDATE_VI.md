# VietPaw — cập nhật URL, nhận diện và B2B leads

Thư mục chính: D:\1. Vietpaw\my-website. Thực hiện theo tệp audit mới do chủ website cung cấp; các bản trước là lịch sử.

## Đã sửa trong mã nguồn

- 68 trang dùng chung header VietPaw / “by WINVN INT CO., LTD.”; footer phân biệt thương hiệu và nhà sản xuất theo audit mới.
- Tên pháp nhân được nêu tại About, Contact, How to Order, Request a Quote, Testing & Export Documents và trong dữ liệu Organization/Product. Không biến VietPaw thành một công ty pháp lý khác.
- Canonical, 66 URL sitemap, breadcrumb, dữ liệu cấu trúc và liên kết nội bộ dùng URL sạch. index.html là tên tệp, không còn được liên kết như URL công khai.
- Giữ một nguồn nội dung hiện hành; không khôi phục bản có 30+, EWX, điều kiện mẫu/MOQ cũ hoặc lời hứa chứng nhận/đổi trả chưa được xác nhận.
- Giữ 40+ countries, đăng ký nhà sản xuất năm 2019, MOQ private label 500, 3 mẫu miễn phí/khách trả courier, lead time theo quy mô, độ ẩm dưới 14% và chứng từ theo sản phẩm/thị trường.
- Giữ 20 Guides và lịch ngày, 89 vị trí ảnh, 31 bảng thương mại. Chỉ alt ảnh Factory đổi theo tiêu đề mới; ảnh gốc không đổi.
- Trang chủ nhấn mạnh wholesale/private label. Trang sản xuất và Factory hướng tới thẩm định cho đơn hàng; liên kết sang website công ty cho lịch sử, đăng ký và danh mục đầy đủ. Không tự đổi WINVNINT hay dùng cross-domain canonical cho nội dung khác nhau.

## Form báo giá và catalogue

Form báo giá bắt buộc: Full name, Business email, Company, Country / destination, Product interest.

Phần mở rộng tùy chọn: Estimated quantity (50–499 / 500–4,999 / 5,000+), Wholesale / Private Label / OEM-ODM, WhatsApp, Message, Upload reference/design. Nút gửi: **Get Samples & Pricing**.

Tệp: một PDF/JPG/PNG/WebP, tối đa 5 MB. Có kiểm tra trước khi gửi và lựa chọn bỏ tệp rồi gửi lại khi dịch vụ từ chối. Không tự gửi lại hoặc tự bỏ tệp. Khi kết quả chưa được xác nhận do mất mạng/timeout, form hướng dẫn liên hệ trực tiếp để tránh gửi trùng.

Catalogue vẫn tải trực tiếp, không cần email. Form bên cạnh nhận Email, Country, Buyer type để yêu cầu MOQ/bảng giá; gửi là lựa chọn của buyer. Không hứa gửi giá tự động hoặc đăng ký newsletter. Hai form giữ endpoint Formspree đã có.

**Chưa kiểm tra gửi/nhận thật hoặc gói tài khoản Formspree.** Upload cần gói/cấu hình hỗ trợ. Chủ website cần kiểm tra domain, thư nhận, chống spam và quy tắc loại/dung lượng tệp phía Formspree. Chỉ gửi thử thật khi được cho phép. [Tài liệu upload Formspree](https://help.formspree.io/articles/building-your-form/file-uploads).

## URL online: điều đã xác minh và giới hạn

DNS và header trực tiếp xác nhận website dùng **GitHub Pages**. Ở lần kiểm tra đầu, /certifications/ và /certifications/index.html cùng trả 200, cùng Content-Length và ETag. Bản trích xuất tìm kiếm cho URL sạch còn hiển thị nội dung cũ, nhưng không được dùng thay phản hồi HTTP hiện tại.

Kết quả GET mới cho 11 cặp URL nằm trong _source/review/live_url_audit.json sau khi chạy check_live_urls.py. Báo cáo ghi thời điểm, mã phản hồi, hash và cụm claim cũ.


Kết quả GET lúc 2026-08-31T09:18:02.903113+00:00: cả 11 cặp đều trả 200 và có cùng hash nội dung trong từng cặp; chưa cặp nào có 301 từ index sang URL sạch. Không phát hiện các cụm claim cũ cụ thể được bộ kiểm tra dò tìm trong 22 phản hồi. Đây không phải xác nhận Google đã cập nhật chỉ mục.

GitHub Pages là hosting tĩnh; _headers, .htaccess hay CSV đặt trong repository không tự tạo HTTP 301. Các thay đổi local **chưa** thay đổi website live. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Hoàn tất P0 sau khi được cấp quyền triển khai

1. Xuất gói public bằng package_public.py. Gói chỉ có trang, tài nguyên được tham chiếu, robots, sitemap, CNAME và .nojekyll; không có _source, báo cáo, nghiên cứu PDF hoặc backup.
2. Đưa toàn bộ gói lên đúng nguồn xuất bản, không ghép từng phần với HTML cũ. Mỗi thư mục chỉ có một index.html hiện hành.
3. Áp dụng lớp HTTP redirect trước GitHub Pages, hoặc hosting hỗ trợ redirect. Đã chuẩn bị:
   - _source/hosting/redirect-map.csv: 272 ánh xạ (68 trang × HTTP/HTTPS × www/non-www).
   - _source/hosting/cloudflare-single-redirects.json: hai rule đề xuất, **chưa cài đặt**. Rule index chạy trước rule host/HTTPS; chỉ GET/HEAD, giữ query string, không redirect URL sạch về chính nó.
4. Nếu dùng Cloudflare, cần quyền DNS/zone và xác nhận proxy/TLS với origin GitHub Pages. Không ghi đè toàn bộ ruleset hiện có; thêm rule vào đúng phase, giữ rule không liên quan và kiểm tra gói hỗ trợ trước khi kích hoạt. [Cloudflare Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/).
5. Kiểm tra URL root, thư mục lồng nhau, query báo giá, http/www và vòng lặp. URL sạch phải trả 200 với bản mới; URL index phải trả 301 với Location đúng. Form POST trực tiếp Formspree, không qua redirect của website.
6. Trong Search Console, gửi sitemap sạch và dùng URL Inspection / Request Indexing cho các trang ưu tiên. Không chặn URL index bằng robots trước khi Google thấy redirect; không noindex tệp phục vụ cả URL sạch. Google thu thập lại cần thời gian, không bảo đảm tức thì. [Hướng dẫn canonical của Google](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## Kiểm tra

Các bộ kiểm tra: validate_site.py, test_seo_leads.py, test_rfq.cjs, test_local_preview.cjs, test_navigation.cjs.

Bao gồm liên kết, nhận diện, trường form/dữ liệu gửi, tải catalogue không bị chặn, lỗi file/mạng/HTTP, timeout, 429, gửi trùng, giữ dữ liệu nhập và mở offline. Không gửi form thật, thao tác Search Console, thay DNS hoặc triển khai live trong lượt này.
