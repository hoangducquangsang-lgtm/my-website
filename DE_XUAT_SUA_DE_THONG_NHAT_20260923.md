# Đề xuất sửa VietPaw để thống nhất với winvnint.com và coffeewoodchew.com

**Ngày:** 23/09/2026
**Cơ sở:** Chị xác nhận nội dung hai site nguồn là chuẩn xác → lấy làm chuẩn.
**Đã đọc thêm lần này:** `story.html`, `compare-coffee-wood-vs-rawhide.html`, `eudr-coffee-wood-dog-chews.html`
(3 trang mới, ngoài 6 trang đã đọc hôm qua).
**Đã đọc lại:** toàn bộ 10 trang đã sửa tối qua, trực tiếp từ file build trên máy.

---

## ⚠️ ĐÍNH CHÍNH MỘT KẾT LUẬN CỦA EM HÔM QUA

Hôm qua em báo rằng câu *"vườn cà phê đốn tỉa thân già để cây mọc lại"* là **lỗi của em**.
Sau khi đọc thêm trang `story.html`, em phải đính chính: **coffeewoodchew.com nói cả hai kiểu**.

| Trang nguồn | Cơ chế mô tả |
|---|---|
| `story.html` | *"as a by-product of coffee tree **pruning cycles**"* → tỉa cành, khớp với VietPaw đang viết |
| `where-coffee-wood-dog-chews-come-from.html` | Cây bị **nhổ bỏ** khi hết năng suất sau 15–20 năm |
| `eudr-coffee-wood-dog-chews.html` | *"Planting year **1996**"* cho nguồn Đắk Lắk → cây ~30 tuổi |

Vậy đây là **mâu thuẫn trong chính nguồn**, không phải lỗi em. Em xin lỗi vì hôm qua đã kết luận vội
khi mới đọc một trang. Mục này chuyển xuống Phần 5 để chị quyết.

---

## PHẦN 0 — KẾT QUẢ RÀ SOÁT "KHÔNG NHẮC WINVN"

Em quét toàn bộ 67 trang:

| Vị trí | Kết quả |
|---|---|
| **Nội dung bài viết, sản phẩm, banner** | ✅ **0 trang** — đã sạch hoàn toàn |
| Tiêu đề SEO, mô tả tìm kiếm, alt ảnh | ✅ **0 trang** |
| Liên kết winvnint.com | ✅ **0 trang** |
| File `winvn-wholesale-catalogue.pdf` | ✅ còn trong thư mục nhưng **không còn được link từ trang nào** |
| Footer (dòng pháp lý) | 67 trang — chị đã đồng ý giữ |
| **JSON-LD trong `<head>`** | ⚠️ **67 trang** — xem mục 0.1 |
| **Tên file ảnh `winvn-*.jpg`** | ⚠️ ~10 file đang dùng — xem mục 0.2 |

### 0.1 — JSON-LD vẫn khai WINVN là tên tổ chức của vietpaw.com

Hiện tại mỗi trang nhúng:

```json
"@type": "Organization", "name": "WINVN INT CO., LTD.", "legalName": "WINVN INT CO., LTD.",
"description": "VietPaw is the international B2B/export brand of WINVN INT CO., LTD., ..."
```

Đây là dữ liệu máy đọc được — Google dùng để dựng Knowledge Panel, và các trợ lý AI đọc trực tiếp.
Với mô hình chị vừa mô tả (**lấy hàng ở kho, không sở hữu sản xuất**), khai WINVN là *tên tổ chức của
vietpaw.com* vừa không đúng vừa ngược với yêu cầu.

**Đề xuất:** đổi `name` thành `VietPaw`, bỏ `legalName` và câu `description` có tên WINVN.
Giữ pháp nhân ở **dòng footer** như hiện tại là đủ về mặt minh bạch.

### 0.2 — Tên file ảnh

10 file `winvn-*.jpg/png` đang được dùng (coffee-wood-single, coffee-wood-sizes, coconut-fiber-balls,
loofah-play-shapes, loofah-growing, hemp-*, moisture-check…). Không hiển thị cho người đọc, nhưng
**Google Images có index tên file**.

**Đề xuất:** đổi tên sang trung tính + thêm redirect. Em làm được tự động trong `_source/`
(khoảng 60 trang tham chiếu), mất ~15 phút. Ưu tiên thấp, làm khi rảnh.

---

## PHẦN 1 — PHẢI SỬA (VietPaw đang tuyên bố MẠNH HƠN nguồn)

### 1.1 🔴 Tuyên bố "không có caffeine" — rủi ro cao nhất

| | Nội dung |
|---|---|
| **VietPaw đang viết** (trang sản phẩm) | *"It contains no coffee beans, **no caffeine-bearing cherry**…"* · *"it contains no coffee bean and **no caffeine**"* |
| **VietPaw đang viết** (trang vật liệu) | *"**carries no caffeine into the finished chew**"* |
| **Nguồn nói** (`compare-coffee-wood-vs-rawhide`) | Không thể tuyên bố caffeine-free **nếu chưa có kết quả phòng thí nghiệm** — con số này *"not confirmed"* |

**VietPaw đang tuyên bố thứ mà chính nhà máy nói là chưa xác nhận được.** Đây là tuyên bố thành phần
sản phẩm — ở EU và Mỹ, tuyên bố sai loại này là rủi ro pháp lý thật, không chỉ là vấn đề văn phong.

**Câu thay thế đề xuất:**
> *"Chew sticks are cut from the stem wood, not from the bean or the cherry. We do not publish a
> caffeine-free claim: no laboratory result has been produced for this material, and we would rather
> say so than print a figure nobody has measured. Ask us if your market requires a test."*

**Vị trí:** `/products/coffee-wood-dog-chew/` (2 chỗ), `/collections/coffee-wood/` (1 chỗ).

---

### 1.2 🔴 Lead time 60–80 ngày đang bị gán sai nghĩa — **36 trang**

| | Nội dung |
|---|---|
| **VietPaw** | *"5–7 days for orders under 500 pcs; **60–80 days for a full container**"* |
| **Nguồn** (2 trang độc lập) | *"Stock packaging: 5–7 days"* · *"**Custom label/box/engraving: 60–80 days**"* — và giải thích *"mostly artwork approval and tooling"* |

Khách đặt **nguyên container hàng tiêu chuẩn** đang bị VietPaw báo 60–80 ngày, trong khi theo nguồn
đơn đó vẫn thuộc nhóm nhanh. Đây là **36 trang** vì dùng chung biến `LEAD`.

**Câu thay thế đề xuất:**
> *"Production lead time: 5–7 days for stock packaging. 60–80 days when the order carries your own
> label, printed box or engraving — most of that window is artwork approval and tooling, not production.
> Add 30–35 days sea transit. Production time is not an arrival date."*

---

### 1.3 🟡 "Six-stage drying protocol" — không có ở cả hai nguồn — **39 trang**

"Five QC checkpoints" khớp nguồn ✅. Nhưng **"six-stage drying"** không xuất hiện ở đâu, và nguồn còn
nói rõ trình tự sấy là **bí mật, không công bố**.

**Đề xuất:** đổi thành *"the coffee wood drying and quality protocol with five QC checkpoints"* —
bỏ chữ "six-stage", giữ phần có căn cứ. Nếu con số 6 là thật, chị cho em nguồn thì em giữ lại.

---

### 1.4 🟡 Mô tả cách gỗ mòn đang thiên về mặt xấu

| | Nội dung |
|---|---|
| **Nguồn** (`compare-vs-rawhide`, `sizing-by-dog-weight`) | *"the surface **wears into soft frayed fibres rather than breaking into hard fragments**"* — kèm ghi chú đây là quan sát, không phải bảo đảm, và *"a powerful chewer can break a piece off"* |
| **VietPaw** | Chỉ có vế cảnh báo (dẫn ghi nhận của một huấn luyện viên về việc gãy thành mảnh cứng), **0 trang** có vế "mòn thành sợi mềm" |

Cả hai vế đều là của nguồn; VietPaw đang chỉ lấy một nửa xấu. Không sai, nhưng làm sản phẩm nghe tệ
hơn thực tế và lệch với hai site kia.

**Câu thay thế đề xuất:**
> *"In normal chewing the surface wears into soft frayed fibres rather than breaking into hard
> fragments. That is an observation about how the material behaves, not a guarantee: a powerful chewer
> can break a piece off a stick, and no supplier in this category has published test data behind the
> phrase 'splinter-free'."*

---

## PHẦN 2 — THỐNG NHẤT SỐ LIỆU THEO NGUỒN

### 2.1 🔴 Bảng size — sửa theo nguồn (kích thước đã khớp, chỉ lệch khối lượng và trọng lượng chó)

| Size | Dài | Đ.kính | **Khối lượng: VietPaw → nguồn** | **Trọng lượng chó: VietPaw → nguồn** | Pcs/thùng |
|---|---|---|---|---|---|
| XS | 10 cm | 1,5–2,0 | 23–30 g ✅ giữ | dưới 5 kg → **≤ 3 kg** | on request |
| S | 13–14 | 2,0–2,5 | 35–45 g ✅ giữ | 5–10 kg → **3–5 kg** | 512 ✅ |
| M | 17–18 | 2,5–3,5 | 90–110 g ✅ giữ | 10–20 kg → **5–8 kg** | 224 ✅ |
| L | 19–20 | 3,5–4,5 | 110–150 → **120–180 g** | 20–30 kg → **8–12 kg** | 126 ✅ |
| XL | 21–22 | 4,5–5,5 | 150–225 → **230–310 g** | 30–40 kg → **12–20 kg** | 85 ✅ |
| XXL | 22–23 | 5,5–7,0 | 325–450 → **340–440 g** | trên 40 kg → **20 kg+** | on request |

Ảnh hưởng: `/products/coffee-wood-dog-chew/`, `/` (bảng rút gọn), `/dog-toys/`.

**Bổ sung lời khuyên chọn size của nguồn** (VietPaw chưa có, rất hữu ích):
> *"When a dog sits at the top of a band, or is known to be a determined chewer, go up one size. The
> consequence of being one size too large is a chew that lasts longer. The consequence of being one
> size too small is the thing everybody is actually trying to avoid."*

### 2.2 🟡 Incoterms

| | Nội dung |
|---|---|
| **VietPaw + winvnint.com** | EXW, CIF, DAP |
| **coffeewoodchew.com** | EXW, **FCA**, **FOB**, **DDP**, DAP — **không có CIF**, cảnh báo *"FOB is the wrong term for an air shipment"* |

Hai nguồn tự mâu thuẫn. **Đề xuất:** lấy danh sách rộng hơn của coffeewoodchew (có DDP là điểm bán
hàng mạnh với khách EU nhỏ), và thêm bảng giải thích ngắn: DDP cho khách nhập khẩu lần đầu,
DAP cho khách có VAT, FCA cho hàng air. Chị xác nhận thực tế VietPaw chào những điều kiện nào.

### 2.3 🟡 Định vị sản xuất

| | Nội dung |
|---|---|
| **VietPaw** (`/factory/`) | *"a **three-factory network** and indicative capacity of 5–6 million units per year"* |
| **Nguồn** (`story.html`) | *"the production and finishing sites **WINVN works from** in Gia Lai, Dak Lak and Ho Chi Minh City"* — nói **"works from"**, không nói sở hữu |
| **Nguồn** (công suất) | 100.000 chiếc/tháng, ~1,2 triệu/năm — **riêng dòng gỗ cà phê** |

Nguồn thận trọng hơn VietPaw. Và điều này khớp với mô hình chị vừa nói: **lấy hàng ở kho**.

**Đề xuất:** đổi thành *"production and finishing sites in Gia Lai, Dak Lak and Ho Chi Minh City"*,
bỏ "three-factory network". Với công suất, ghi rõ 100.000/tháng (~1,2 triệu/năm) là **riêng gỗ cà phê**;
nếu 5–6 triệu là tổng cả 5 dòng thì nói rõ như vậy, hoặc bỏ hẳn.

---

## PHẦN 3 — BỔ SUNG NỘI DUNG NGUỒN CÓ MÀ VIETPAW THIẾU

### 3.1 🔴 EUDR — nguồn có hẳn một trang, VietPaw **không có gì**. Hạn 30/12/2026 còn ~3 tháng.

Nội dung nguồn, đáng đưa gần như nguyên vẹn:

- EUDR **có áp dụng** — *"a coffee wood dog chew is a wood article"*, không được miễn vì là sản phẩm thú cưng
- **30/12/2026** áp dụng cho sản phẩm gỗ **bất kể quy mô công ty**
- Nghĩa vụ due diligence thuộc **nhà nhập khẩu EU**, không phải nhà cung cấp — *"does not file, holds no TRACES account and cannot file on a buyer's behalf"*
- Cung cấp được cho khách: **toạ độ lô đến 6 số thập phân (theo NDA)**, **năm trồng** (1996 với nguồn Đắk Lắk), **giấy khai thác có xác nhận UBND xã**, **định danh thực vật qua giấy kiểm dịch thực vật**
- **Không cấp** "deforestation-free certificate" — *"the regulation creates no such supplier document"*; xác nhận của xã *"is not a forest-cover assessment"*

Đây là nội dung khó sao chép nhất, đúng chuẩn GEO, và khách EU chắc chắn sẽ hỏi trong 3 tháng tới.
**Đề xuất: tạo trang mới `/guides/eudr-coffee-wood-chews/`** + link từ `/certifications/` và `/collections/coffee-wood/`.

### 3.2 🔴 Bốn mục nên đưa ngay (hai nguồn nhất quán, khách B2B luôn hỏi)

| Nội dung | Nguồn |
|---|---|
| **Thanh toán**: đặt cọc 30% đơn tiêu chuẩn / 50% đơn private label, còn lại đối chứng từ. Hàng air thanh toán đủ trước khi giao tại sân bay | CWC + WIN, khớp nhau |
| **Chứng từ thứ 7 — Forest-Product Declaration**: chứng minh nguồn gốc hợp pháp, **là điều kiện để cấp C/O** | CWC |
| **Các form C/O**: EUR.1 (EU, theo EVFTA) · Form B (chuẩn) · Form VJ (Nhật) | CWC |
| **Không cấp**: giấy thú y (đây là sản phẩm gỗ, không phải phụ phẩm động vật) · FSC (cây nông nghiệp, ngoài phạm vi) · lab test (có riêng nếu yêu cầu) | CWC |

### 3.3 🟡 Số liệu kỹ thuật bổ sung

| Nội dung | Nguồn |
|---|---|
| Đóng hộp bán lẻ giảm mạnh số lượng/thùng: **M 224→120, L 126→100, XL 85→50** (M giảm 46%) | CWC |
| **20ft xếp pallet ≈ 300 thùng** (so với 429 xếp rời) | CWC |
| **Giới hạn thùng Amazon 50 lb (22,7 kg)** | CWC + WIN |
| **Đo độ ẩm 5 điểm mỗi lần kiểm** | CWC |
| **Billet cắt 50–70 cm tại vườn**, ủ ~1 năm **trong bóng râm thông gió** | CWC |
| **Công suất ~1,2 triệu chiếc/năm** (riêng gỗ cà phê) | CWC |
| **Mất ~20% nguyên liệu đầu vào do nứt** — khớp con số "1/5" VietPaw đang dùng ✅ | CWC |

### 3.4 🟡 Sản phẩm và bậc đặt hàng nguồn có, VietPaw chưa có

| Nội dung | Ghi chú |
|---|---|
| **Khắc laser $0,10/chiếc, từ 50 pcs** | Giá — chị xác nhận có áp dụng cho VietPaw không |
| **Bộ sản phẩm**: Twin Pack (2 thanh, túi kraft/sleeve có thương hiệu) · Variety Combo Box (3 size, hộp quà bán lẻ) · Amazon Starter Bundle (có FNSKU + nhãn an toàn) | Sản phẩm bán lẻ sẵn sàng — dễ bán hơn thanh rời |
| **Bậc đặt hàng**: Trial Box 100 pcs · Starting Box 500 pcs | Hạ rào cản đơn đầu |
| **Dòng Gorilla** 4 size: GRLS 5–6×8 cm 155–230 g (60/thùng) · GRLM 6–8×10 cm 260–350 g (52) · GRLL 8–10×12 cm 350–480 g (40) · GRLXL 10–12×15 cm 550–900 g (đóng theo khối lượng) | Chỉ đưa nếu kho có hàng |
| **Vì sao GRLXL không công bố số chiếc/thùng**: chênh lệch khối lượng tới 64% trong cùng một size, nên đóng theo khối lượng mục tiêu và trả số thực trong packing list | Chi tiết rất tăng độ tin cậy |

### 3.5 🟡 Ba điểm yếu nguồn tự nêu — VietPaw nên nêu luôn

Trang so sánh với rawhide của nguồn tự nhận 3 điểm thua. Đưa lên sẽ tăng độ tin cậy rất nhiều:

1. **Giá**: rawhide là phụ phẩm của ngành quy mô cực lớn nên nguyên liệu rẻ; gỗ cà phê mất ~20% do nứt
2. **Không hợp mọi chó**: gỗ cứng, chó nhai khoẻ có thể bẻ gãy mảnh
3. **Khách chưa quen**: rawhide có 40 năm hiện diện trên kệ, khách biết nó là gì

---

## PHẦN 4 — ĐIỀU CHỈNH THEO MÔ HÌNH "LẤY HÀNG Ở KHO"

Chị cho biết khi khách đặt thì lấy hàng ở kho. Hai điều chỉnh để nội dung khớp thực tế:

**4.1** Rà lại mọi câu ngụ ý VietPaw vận hành sản xuất. Hiện **không trang nào** nói "nhà máy của chúng
tôi" ✅, nhưng menu vẫn có mục **"Our Factory"** (`/factory/`) và **"Manufacturing"**.
**Đề xuất:** đổi nhãn menu thành *"Production & Sourcing"* và tiêu đề trang thành
*"Production and Sourcing"*. Nội dung bên trong giữ nguyên (đã trung tính).

**4.2** Có hàng sẵn trong kho là **lợi thế bán hàng** mà site đang không nói. Nguồn nói lead time
5–7 ngày cho hàng tiêu chuẩn — nếu thực tế là lấy từ kho thì còn nhanh hơn.
**Đề xuất:** thêm một dòng ở trang chủ và `/how-to-order/`:
> *"Standard sizes are held in stock. A trial order of 50–500 pcs in stock packaging normally ships
> within 5–7 days of payment, without waiting for a production run."*

Chị xác nhận con số này đúng với thực tế kho thì em đưa lên.

---

## PHẦN 5 — MÂU THUẪN TRONG CHÍNH NGUỒN, CẦN CHỊ QUYẾT

| # | Vấn đề | Các phiên bản |
|---|---|---|
| 5.1 | **Tuổi cây** | CWC trang chủ "over 20 years" · CWC sourcing "15–20 years" · CWC EUDR "trồng năm 1996" (~30 tuổi) · WIN "20–25 years" |
| 5.2 | **Cơ chế lấy gỗ** | CWC story "pruning cycles" (tỉa) · CWC sourcing "nhổ bỏ cây hết năng suất" |
| 5.3 | **Vùng nguyên liệu** | CWC sourcing "Đắk Lắk, Gia Lai **và Đắk Nông**" · CWC story "Gia Lai, Đắk Lắk, TP.HCM" (nơi sản xuất) · VietPaw hiện "Gia Lai và Đắk Lắk" |
| 5.4 | **Incoterms** | WIN "EXW, CIF, DAP" · CWC "EXW, FCA, FOB, DDP, DAP" (không CIF) |
| 5.5 | **Túi hút ẩm** | CWC "than hoạt tính, **không dùng silica gel**" · ảnh nhà máy có gói ghi **"SILICA GEL"** |

Với 5.1–5.3, em đề xuất dùng bản **chi tiết nhất** (trang sourcing + EUDR): Robusta, trồng 1996 với
nguồn Đắk Lắk, 15–20 năm khi thu, ba tỉnh Đắk Lắk – Gia Lai – Đắk Nông, cây được nhổ bỏ khi hết năng
suất. Nhưng vì nó mâu thuẫn với trang chủ của chính nguồn, chị nên chốt một bản rồi sửa đồng bộ cả
ba site.

---

## THỨ TỰ THỰC HIỆN ĐỀ XUẤT

| Mức | Mục | Số trang ảnh hưởng |
|---|---|---|
| 🔴 1 | **1.1** Bỏ tuyên bố không-caffeine | 2 |
| 🔴 2 | **1.2** Sửa nghĩa lead time 60–80 ngày | 36 |
| 🔴 3 | **2.1** Cập nhật bảng size theo nguồn | 3 |
| 🔴 4 | **3.2** Thêm 4 mục chứng từ & thanh toán | 5–8 |
| 🔴 5 | **3.1** Trang EUDR mới (hạn 30/12/2026) | +1 trang mới |
| 🟡 6 | **0.1** JSON-LD đổi sang VietPaw | 67 |
| 🟡 7 | **1.3** Bỏ "six-stage" · **1.4** cân bằng mô tả mòn gỗ | 39 + 8 |
| 🟡 8 | **2.3 + 4.1** Định vị sản xuất & nhãn menu | 5–10 |
| 🟡 9 | **3.3** Số liệu kỹ thuật bổ sung · **3.5** ba điểm yếu | 3–5 |
| 🟢 10 | **2.2** Incoterms · **3.4** sản phẩm & bậc đặt hàng · **4.2** hàng sẵn kho | cần chị xác nhận trước |
| ⚪ 11 | **0.2** Đổi tên file ảnh + redirect | 60 |

**Mục 1–5 và 7–9 em làm được ngay** — toàn bộ đều là lấy số liệu từ nguồn chị đã xác nhận là chuẩn.
**Mục 6, 10 cần chị xác nhận** vì liên quan chính sách bán hàng và nhận diện pháp nhân.
**Phần 5 cần chị chốt** trước khi em sửa, vì nguồn tự mâu thuẫn.

Chị trả lời "duyệt 1–5, 7–9" là em chạy luôn, hoặc chị đánh dấu từng mục.
