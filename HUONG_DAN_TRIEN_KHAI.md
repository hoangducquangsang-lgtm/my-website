# Bản sửa tốc độ vietpaw.com, ngày 12/10/2026

## File trong gói

| File | Thay đổi | Mục đích |
|---|---|---|
| `index.html` | Bỏ CSS inline (bản thiếu, có lỗi dấu nháy `’Segoe UI’`), bỏ cách tải `media="print"`; tải `style.css` bình thường | Sửa CLS 0,41 (di động) / 0,49 (máy tính) |
| `index.html` | Thêm `480w`, `640w` vào srcset mặc định của ảnh hero; thêm `320w`, `480w` cho 4 ảnh card "Four materials" | Desktop tải ảnh nhỏ đúng kích thước (giảm khoảng 200 KiB) |
| `assets/img/vietpaw-logo-96.webp` | 9,1 KB → 2,4 KB | Nén lại, hình nhìn không khác |
| `assets/img/vietpaw-logo-192.webp` | 13,3 KB → 5,2 KB | Nén lại, hình nhìn không khác |
| `.htaccess` | Mới | Cache 30 ngày cho ảnh/CSS/JS trên Namecheap (thay cho TTL 4 giờ) |

Các trang khác **không cần sửa**: chúng vẫn tải `style.css` theo cách thông thường nên không bị lỗi CLS này.

## Các bước triển khai

1. Chép đè `index.html` và 2 file logo vào thư mục website (`my-website/`) theo đúng đường dẫn.
2. `.htaccess`: nếu thư mục gốc trên Namecheap **chưa có** file này thì chép vào. Nếu **đã có**, mở file cũ và dán toàn bộ nội dung file mới vào cuối, không ghi đè.
   - Lưu ý: tên file bắt đầu bằng dấu chấm nên Windows Explorer có thể ẩn. Trong cPanel File Manager, bật "Show Hidden Files".
3. Commit và push lên GitHub, rồi deploy sang Namecheap như thường lệ.
4. Cloudflare → **Caching → Configuration → Browser Cache TTL** → chọn **Respect Existing Headers**.
5. Cloudflare → **Caching → Purge Everything** để xóa bản cũ.
6. Đợi 5–10 phút rồi chạy lại PageSpeed cho cả Mobile và Desktop.

## Kết quả kiểm tra trước khi giao

Đo trong Chromium, có mô phỏng CSS và ảnh tải chậm:

- Desktop: CLS **0,911 → 0,000**. Trình duyệt tải ảnh card 320w thay vì 640w, ảnh hero 640w thay vì 800w.
- Di động: CLS 0,000. Ảnh vẫn tải 480w/640w, đủ nét cho màn hình có mật độ điểm ảnh cao.
- HTML hợp lệ, schema JSON-LD hợp lệ, nội dung trang giữ nguyên.

## Ảnh hưởng cần biết

- FCP trên di động có thể chậm thêm khoảng 0,1–0,3 giây, vì trang chờ file `style.css` (khoảng 7 KiB). LCP vẫn trong ngưỡng tốt.
- Cache 30 ngày:
  - Khi sửa `style.css` hoặc file JS, **phải đổi `?v=`** trong HTML (như đang làm).
  - Khi thay một ảnh, **nên đổi tên file**. Nếu giữ tên cũ, khách quay lại có thể vẫn thấy ảnh cũ tới 30 ngày.
- File `_headers` không có tác dụng trên Namecheap. Có thể giữ, không gây hại.

## Tùy chọn (chưa làm)

- Tắt Cloudflare Web Analytics nếu chỉ dùng GA4: bớt khoảng 10 KiB JS.
- Tắt Cloudflare Email Obfuscation: bớt 1 request, nhưng email dễ bị bot thu thập hơn.
- Giữ nguyên Google Analytics. Trì hoãn sâu hơn sẽ làm mất dữ liệu lượt xem ngắn.
