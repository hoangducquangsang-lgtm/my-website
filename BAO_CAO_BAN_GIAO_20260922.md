# Báo cáo bàn giao — Cập nhật website VietPaw

**Ngày:** 22–23/09/2026
**Phạm vi:** 10 trang theo hình 3 + các thay đổi toàn site bắt buộc (header, bảng màu, footer)
**Điểm khôi phục:** commit `1830d3e` (trước thay đổi) · commit hiện tại `23401be`

> ⚠️ Website được **sinh tự động** từ `_source/*.py`. Mọi chỉnh sửa phải làm trong `_source/`
> rồi chạy `python3 _source/build.py`. Sửa trực tiếp file `index.html` sẽ bị ghi đè.

---

## 1. Các trang đã biên soạn lại

| Trang | Dung lượng | Ảnh | Cấu trúc GEO đã áp dụng |
|---|---|---|---|
| `/` | 34 KB | 9 | Direct answer · stats · bảng spec · evidence · how-to · bảng "không tuyên bố" · FAQ 6 câu |
| `/about/` | 24 KB | 2 | Direct answer · làm/không làm · nguồn nguyên liệu · bảng pháp nhân · quy tắc bằng chứng · FAQ 5 |
| `/dog-toys/` | 35 KB | 9 | Direct answer · bảng so sánh 4 vật liệu theo kiểu nhai · sizing · suitable/not · steps · FAQ 7 |
| `/guides/` | 26 KB | 3 | "Start here" + direct answer · 4 cụm chủ đề có mô tả · cách viết guide |
| `/contact/` | 24 KB | 1 | Direct answer · bảng kênh liên hệ · "4 dòng cần có trong email" · steps · social · FAQ 6 |
| `/collections/coffee-wood/` | 34 KB | 7 | Định nghĩa · quy trình 5 bước · formats · suitable/not · vận chuyển · FAQ 6 |
| `/collections/coconut-fiber/` | 29 KB | 4 | Định nghĩa · bảng thành phần phải khai báo · steps đặc tả · suitable/not · FAQ 6 |
| `/collections/hemp-fiber/` | 30 KB | 6 | Định nghĩa · bảng 4 format · steps đặc tả rope · suitable/not · FAQ 6 |
| `/products/coffee-wood-dog-chew/` | 45 KB | 8 | Direct answer · bảng size 7 cột · bảng dung sai/quy trình · 5 bước sản xuất · suitable/not · how-to-order · branding · carton & shipping · FAQ 8 |
| `/guides/how-long-do-coffee-wood-chews-last/` | 29 KB | 1 | Direct answer · bảng 4 yếu tố · mẫu câu cho product page · khi nào thay · thu thập feedback · FAQ 6 |

Mỗi trang: 1 H1 duy nhất, H2/H3 logic, meta title + description riêng, internal links, alt ảnh mô tả,
schema Article/Product/FAQPage/BreadcrumbList nơi phù hợp.

**Nội dung mới, khó sao chép (information gain):** dung sai ±3 mm · độ ẩm <14% đo bằng máy kim, chụp ảnh theo lô ·
loại bỏ vết nứt >2 mm tại khâu phân loại · tỷ lệ loại ~1/5 tập trung ở giàn sấy · 5 chốt QC · thùng 51×31×39 cm
(0,062 m³) · 30 thùng/pallet, 429 thùng/cont 20ft, 850/40ft · số lượng/thùng theo size · HS 4421.99 · 30–35 ngày
đường biển · chẩn đoán mốc do đọng hơi trong container (tầng trên/phía cửa) vs đóng hàng ướt (đều cả khối) ·
bảo quản 25–28 °C · giữ 1 túi nguyên seal mở ở tháng thứ 6.

---

## 2. Bảng màu đã dùng

| Token | Mã | Dùng cho | Tương phản |
|---|---|---|---|
| `--forest` | `#2F6B3C` | Xanh lá tự nhiên chủ đạo — viền, nút outline, icon | 6.28:1 trên nền kem |
| `--forest-dark` | `#1E4A2B` | Tiêu đề H1–H4, nền footer | 9.98:1 |
| `--leaf` | `#4E9A4A` | Xanh phụ, chi tiết | — |
| `--terracotta` | `#E08A2B` | Cam ấm — chi tiết trang trí, viền callout, tag | trang trí, không dùng cho chữ |
| `--terracotta-dark` | `#AC5510` | Nút CTA, liên kết, thanh RFQ | 5.09:1 / chữ trắng 5.1:1 |
| `--navy` | `#22384F` | **Dùng tiết chế**: header bảng thông số kỹ thuật | 11.83:1 |
| `--cream` / `--kraft` / `--kraft-dark` | `#FFFDF8` / `#F7F2E7` / `#EDE3CE` | Nền trắng, kem, be nhạt | — |
| `--ink` / `--ink-soft` | `#3A2C1E` / `#6B5B49` | Chữ nâu đậm / phụ | 13.25:1 / 6.42:1 |

Tất cả cặp màu chữ–nền đạt ≥ 4.5:1 (WCAG AA). Thanh CTA cam trước đây dùng `#C1682F` với chữ trắng
chỉ đạt 3.1:1 — đã đổi sang `#AC5510`.

---

## 3. WINVN INT — đã xử lý

**Đã xoá:**
- Dòng `by WINVN INT CO., LTD.` dưới logo VietPaw — **toàn bộ 67 trang**, cả desktop và mobile.
  CSS `.brand` đã chuyển sang một dòng, căn giữa theo chiều dọc, không còn khoảng trống thừa.
- Toàn bộ liên kết `winvnint.com` trong nội dung trang (9 vị trí ở home, about, materials, factory,
  quality-control, capabilities, 2 guides, 2 services) → thay bằng internal link hoặc diễn đạt trung tính.
- Tên WINVN trong nội dung 5 trang (about, certifications, contact, how-to-order, request-a-quote).

**Còn giữ (có chủ ý):**
- Dòng pháp lý trong footer — như yêu cầu.
- `legalName` trong JSON-LD `Organization` (dữ liệu pháp nhân có cấu trúc, tương ứng dòng footer,
  không hiển thị cho người đọc). **→ cần chị xác nhận có muốn giữ không.**

**Đã thêm kiểm tra tự động** trong `validate_site.py`: build sẽ báo lỗi nếu WINVN xuất hiện lại trong
nội dung trang, trong title/meta description/alt ảnh, hoặc nếu `brand-sub` quay lại.

---

## 4. Mạng xã hội

Thêm ở **footer (toàn site)** và **khu vực Liên hệ** trên `/contact/`. Mỗi liên kết có icon SVG + tên nền tảng,
`aria-label` ("LinkedIn — opens in a new tab"), `rel="me noopener"`, `target="_blank"`, vùng bấm tối thiểu 44 px,
trên mobile xếp 2 cột chiếm nửa chiều ngang.

- LinkedIn — https://www.linkedin.com/in/sarahhue
- Instagram — https://www.instagram.com/sarah.naturalpettoys/
- Facebook — https://www.facebook.com/sarahhue6789
- YouTube — https://www.youtube.com/@HueSarah-n4f

---

## 5. Ảnh

Nguồn: `D:\OneDrive - evnmt\5. Business\2. Pet\2. Document\1. Raw material\1. Image` — **truy cập thành công**,
540 ảnh trong 26 thư mục con.

- **39 ảnh mới** được chọn, đổi tên mô tả (vd `coffee-wood-chew-size-range-xs-to-xxl.jpg`,
  `moisture-reading-before-packing.jpg`, `laser-engraving-coffee-wood-chew.jpg`) và đưa vào `assets/img/`.
- **File gốc trong thư mục của chị không bị thay đổi.** Bản làm việc được giới hạn 2000 px, JPEG q92.
- Build tự sinh **WebP nhiều kích thước** (320/480/640/800/960/1200/1600 px) vào `assets/img/webp/` —
  hiện 284 file dẫn xuất. Mỗi `<img>` có `srcset`, `sizes`, `width`, `height`, `decoding="async"`.
- Ảnh hero: `loading="eager"` + `fetchpriority="high"`. Ảnh dưới màn hình đầu: `loading="lazy"`.
- Ảnh đã chọn ưu tiên loại **không có chữ/logo WINVN trên thùng carton** (đã loại bỏ hàng chục ảnh kho
  có in "WINVN INT CO., LTD" trên thùng).

---

## 6. Kiểm tra đã chạy

| Kiểm tra | Kết quả |
|---|---|
| `validate_site.py` | **0 lỗi**, 0 cảnh báo · 67 trang · 65 URL sitemap |
| `test_brand_urls.py` | PASS (title, canonical, og/twitter, schema, brand markup) |
| `test_google_tag.py` | PASS — 67/67 trang có tag, 0 trùng |
| `test_navigation.cjs` | PASS — menu, bàn phím, Escape, Back |
| `test_rfq.cjs` | PASS — form báo giá, validation, upload, retry, redirect |
| `test_local_preview.cjs` | PASS |
| Chụp màn hình Chromium 1440×900 và 390×844, 10 trang | Không lỗi JS, không 404, **không tràn ngang** |
| Kiểm tra alt ảnh | 47/47 ảnh trên 10 trang đều có alt mô tả |

---

## 7. ⚠️ CẦN CHỊ KIỂM TRA — nguồn mâu thuẫn hoặc chưa đủ căn cứ

### 7.1 Bảng size gỗ cà phê — **mâu thuẫn rõ rệt** (ưu tiên cao)

Site VietPaw hiện tại và `coffeewoodchew.com` đang công bố hai bộ số khác nhau:

| Size | VietPaw (đang dùng) | coffeewoodchew.com | Ghi chú |
|---|---|---|---|
| XS | dưới 5 kg | ≤ 3 kg | lệch |
| S | 5–10 kg | 3–5 kg | lệch |
| M | 10–20 kg | 5–8 kg | lệch |
| L | 20–30 kg · 110–150 g | 8–12 kg · 120–180 g | lệch cả 2 cột |
| XL | 30–40 kg · 150–225 g | 12–20 kg · 230–310 g | lệch nhiều |
| XXL | trên 40 kg · 325–450 g | 20 kg+ · 340–440 g | lệch |

**Em đã giữ nguyên số của VietPaw** (không tự ý đổi số đã công bố). Chị xác nhận bảng nào là hiện hành,
em sẽ cập nhật một lần cho cả `/products/coffee-wood-dog-chew/`, `/` và `/dog-toys/`.

Ngoài ra `winvnint.com` ghi **"four sizes (S–XL)"** trong khi `coffeewoodchew.com` và VietPaw ghi **6 size**.

### 7.2 Giá — **chưa đăng**
`coffeewoodchew.com` công bố khắc laser **$0.10/chiếc** và in hộp bán lẻ **$0.10/bộ**.
Đây là chính sách giá của nhà sản xuất, chưa xác nhận áp dụng cho VietPaw → **em không đưa lên website**.
Trang chỉ ghi "báo giá theo đơn hàng". Chị xác nhận nếu muốn công bố.

### 7.3 Dòng sản phẩm "Gorilla" — **chưa đăng**
`coffeewoodchew.com` có dòng Gorilla 4 size (GRLS, GRLM, GRLL, GRLXL, 155–900 g, 40–60 chiếc/thùng).
VietPaw chưa có SKU này → em chỉ ghi "block/chunk formats available on request" ở trang collection,
không đưa bảng thông số. Chị xác nhận nếu muốn bán dòng này.

### 7.4 Túi hút ẩm — **mâu thuẫn giữa văn bản và ảnh**
`coffeewoodchew.com` viết "charcoal desiccant sachets (**no silica gel**)", nhưng ảnh đóng gói trong thư mục
nguyên liệu có gói ghi rõ **"SILICA GEL"**. → Em chỉ viết "desiccant sachet", không nêu loại,
và thêm dòng "confirm the desiccant type in writing if your market restricts it". Cần chị làm rõ với nhà máy.

### 7.5 Số lượng/thùng — hai bộ số khác nhau (đã xử lý)
- Đóng rời (bulk): S 512 · M 224 · L 126 · XL 85
- Đóng hộp bán lẻ (Amazon FBA): CC01M 120 · S2CC01M 92 · CC01L 100 · CC01XL 50

Đây không phải mâu thuẫn mà là hai cách đóng khác nhau. Em đăng **bộ bulk** kèm ghi chú
"retail-packed and multi-piece sets fit fewer units per carton". Nếu muốn đăng cả bảng FBA, cần chị xác nhận.

### 7.6 Công suất — hai con số khác scope
- `coffeewoodchew.com`: **100.000 sản phẩm/tháng** (riêng dòng gỗ cà phê)
- VietPaw hiện tại: **5–6 triệu units/năm** (toàn bộ nhà máy)

Không mâu thuẫn nhưng khác phạm vi. Em ghi con số gỗ cà phê là *supplier-reported planning figure*, không
phải năng lực dành riêng cho đơn hàng của khách.

### 7.7 Vùng nguyên liệu và tuổi cây
- Vùng: site VietPaw cũ chỉ ghi **Gia Lai**; hai site nhà sản xuất ghi **Đắk Lắk và Gia Lai**.
  → Em dùng "Gia Lai and Dak Lak". Cần chị xác nhận.
- Tuổi cây: `coffeewoodchew.com` "over 20 years", `winvnint.com` "20–25 years".
  → Em **không nêu số tuổi**, chỉ viết "mature Robusta coffee stems".

### 7.8 Chứng từ EUR.1 — **chưa thêm**
`coffeewoodchew.com` liệt kê **EUR.1 movement certificate**. Site VietPaw chưa có mục này.
Do EUR.1 chỉ áp dụng cho EU và phụ thuộc quy tắc xuất xứ, em chưa thêm. Chị xác nhận nếu muốn bổ sung.

### 7.9 Tỷ lệ loại bỏ ~1/5 — nguồn đơn lẻ
Chỉ `coffeewoodchew.com` công bố. Em đăng kèm nhãn rõ "supplier-reported figure". Nếu số này chưa chính xác,
cần bỏ khỏi `/products/coffee-wood-dog-chew/` và `/collections/coffee-wood/`.

### 7.10 Dòng "Contracting manufacturer" trong nội dung trang
Trước đây 5 trang (about, certifications, contact, how-to-order, request-a-quote) ghi rõ tên pháp nhân
ký hợp đồng trong phần nội dung. Theo yêu cầu "WINVN chỉ ở footer", em đã đổi thành
*"Orders are contracted with the Vietnamese manufacturing company named in the footer of this site."*
Thông tin vẫn có trên mọi trang (ở footer), nhưng **đây là thông tin thương mại/pháp lý** —
chị nên xác nhận cách diễn đạt này ổn về mặt hợp đồng.

### 7.11 Tên file ảnh cũ còn tiền tố `winvn-`
Ví dụ `winvn-coffee-wood-sizes.png`, `winvn-loofah-growing.png`. Đây là **tên file**, không phải alt text và
không hiển thị cho người đọc. Đổi tên sẽ làm hỏng liên kết trên ~60 trang và mất index Google Images.
→ Em giữ nguyên. Ảnh mới đều dùng tên trung tính.

### 7.12 Watermark chữ "W" mờ trên vài ảnh mới
Một số ảnh trong thư mục nguồn có watermark tròn chữ W rất mờ, gồm ảnh
`coffee-wood-chew-size-range-xs-to-xxl.jpg` (ảnh dải size XS–XXL — ảnh giá trị nhất, em vẫn dùng),
`hemp-rope-coffee-wood-knot-toy.jpg`, `loofah-cat-toy-shapes-in-basket.jpg`. Nếu chị có bản không watermark,
gửi em thay.

### 7.13 Thiếu ảnh riêng cho xơ dừa và sợi gai
Thư mục nguyên liệu **không có** ảnh riêng cho coconut fiber và hemp fiber (chỉ có gỗ cà phê, xơ mướp,
thú cưng, kho/đóng gói). → Trang coconut-fiber và hemp-fiber dùng lại ảnh có sẵn + ảnh gỗ-kết-hợp-dây thừng.
Nếu chị bổ sung ảnh xơ dừa/sợi gai, em sẽ chèn thêm.

### 7.14 Test cũ fail — không phải lỗi mới
`test_commercial_policy.py`, `test_seo_leads.py`, `test_proof_removal.py`, `test_brand_consistency.py`,
`test_responsive_images.py` là các test **so sánh cây thư mục hiện tại với một file backup cũ** và
assert "không có gì khác thay đổi". Chúng fail theo thiết kế sau **mọi** thay đổi nội dung, và **đã fail
từ trước khi em sửa** (đã kiểm chứng với backup `Website-before-Google-tag-20260901.zip`).
Kiểm tra sống là `validate_site.py` + `test_brand_urls.py` + `test_google_tag.py` — cả ba đều PASS.

Tương tự, cảnh báo `"Replacement is not the supplied original"` trong `validate_site.py` xuất hiện vì thư mục
đối chiếu `1. Raw material/1. Hinh anh/HÌNH ẢNH` không có trên máy này — không liên quan nội dung.

---

## 8. File đã sửa

```
_source/common.py              logo bỏ brand-sub, thêm SOCIAL + social_html(), footer social, CONTRACT_NOTICE
_source/style.css              bảng màu mới, .brand một dòng, .social-links, .spec-table, .answer-box, .fit-grid
_source/content_helpers.py     thêm answer(), fit(), steps(), spec_table(), figure(), media(), CARTON, SEA_TRANSIT
_source/content_home_about.py  viết lại toàn bộ trang chủ và /about/
_source/content_products.py    trang /products/coffee-wood-dog-chew/ + bảng size 7 cột + bảng quy trình + FAQ 8
_source/content_materials.py   3 collection coffee-wood / coconut-fiber / hemp-fiber
_source/content_categories.py  trang /dog-toys/
_source/content_guides.py      hub /guides/ + bài how-long-do-coffee-wood-chews-last + hỗ trợ FAQ/FAQPage schema
_source/content_company.py     trang /contact/ + social
_source/content_manufacturing.py  gỡ liên kết winvnint.com
_source/content_landing.py     gỡ tên WINVN (module không nằm trong build, sửa cho nhất quán)
_source/validate_site.py       kiểm tra mới: brand markup, WINVN ngoài footer, WINVN trong SEO/alt
_source/test_brand_urls.py     cập nhật assert theo header mới
assets/img/                    +39 ảnh gốc mới
assets/img/webp/               +~130 file WebP dẫn xuất
```

**Chưa deploy.** Site đã build xong trong `D:\1. Vietpaw\my-website`, sẵn sàng đẩy lên hosting khi chị duyệt.
