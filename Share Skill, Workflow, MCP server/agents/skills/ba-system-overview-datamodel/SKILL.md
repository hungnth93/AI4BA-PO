---
name: ba-system-overview-datamodel
description: "Tổng quan hệ thống AS-IS từ Data Model + apps + actors: (1) sinh/cập nhật file data model trong docs-BA/Data Model khi đầu vào là SQL/Prisma/schema; (2) sinh PRD ba-system-overview 5 mục, phủ bảng/trường, quy trình actor–app. Dùng khi brownfield overview, map app–bảng–cột, hoặc trích data dictionary từ dump."
context: "AS-IS brownfield | SQL/Prisma/ERD → PRD + Data Model"
---

# SKILL: BA SYSTEM OVERVIEW (DATA MODEL)

**Version:** 1.2.0 | **Author:** M2MBA | **Last Updated:** 2026-04-20

Bạn là BA. Đọc đầu vào, **liên kết thực thể–ứng dụng–actor**, xuất file Markdown theo cấu trúc dưới đây. Ngôn ngữ đầu ra theo ngôn ngữ tài liệu đầu vào (ưu tiên tiếng Việt).

---

## ĐẦU VÀO (bắt buộc — thiếu 1 trong 3 → dừng và hỏi user)

| Thành phần | Mô tả |
|------------|--------|
| **Data Model** | ERD, Mermaid, `ba-data-model.md`, Prisma schema, hoặc danh sách bảng + quan hệ |
| **Danh sách ứng dụng** | Tên từng app/phân hệ (Web Admin, Mobile App…), kèm mục đích nếu có |
| **Danh sách đối tượng** | Actor / vai trò (Khách hàng, Kế toán…), kèm mô tả ngắn nếu có |

**Ghi chú đầu vào:**
- **SQL/Prisma/DDL chưa có file MD tương ứng:** tạo file Data Model trước (xem phần dưới), sau đó sinh PRD.
- **File `docs-BA/Data Model/ba-data-model_*.md` đã có:** dùng làm ground truth, **không** tạo trùng; chỉ cập nhật section bị ảnh hưởng + tăng version (patch/minor/major) khi có thay đổi.

---

## ĐẦU RA 1 — FILE DATA MODEL

**Khi nào tạo:** đầu vào là SQL/Prisma/DDL và chưa có file MD tương ứng trong repo (hoặc user yêu cầu regenerate).  
**Đường dẫn:** `docs-BA/Data Model/ba-data-model_[slug].md` (slug: chữ thường, gạch ngang, không dấu).

**Metadata đầu file:**
```
Version: 1.0.0 | Author: M2MBA | Last Updated: YYYY-MM-DD
Description: Data model [AS-IS / logical] — [tên hệ thống]
```

**Nội dung tối thiểu (theo thứ tự):**
1. **Change Log** — bảng version / ngày / mô tả ngắn.
2. **Nguồn & phạm vi** — loại DB, cách trích; không dán host/credential/secret; ghi "xem dump gốc nội bộ" nếu cần.
3. **Danh sách bảng theo miền nghiệp vụ** — nhóm logic; mỗi bảng phải xuất hiện đúng tên ít nhất một lần.
4. **Đối tượng DB bổ sung** (nếu có): VIEW, PROCEDURE, TRIGGER — chỉ tên + mục đích, không copy SQL có secret.
5. **Sơ đồ quan hệ** (khuyến nghị) — Mermaid `erDiagram` theo cụm; ghi rõ cạnh logic (suy từ `*_id`) vs FK khai báo.
6. **Data dictionary** — mỗi bảng: cột | kiểu / nullable / default theo nguồn.

**MySQL dump:** có thể dùng script `.agent/scripts/sql_dump_to_ba_datamodel_md.py`:
```
py -3 .agent/scripts/sql_dump_to_ba_datamodel_md.py <file.sql> "docs-BA/Data Model/ba-data-model_[slug].md"
```
Sau khi chạy: rà soát nhóm miền, bổ sung Mermaid, chỉnh mô tả — không để file chỉ có output máy thiếu ngữ cảnh BA.

---

## ĐẦU RA 2 — PRD TỔNG QUAN HỆ THỐNG

**Đường dẫn:** `docs-BA/PRD/ba-system-overview_[slug].md`

**Metadata đầu file:**
```
Version: 1.0.0 | Author: M2MBA | Last Updated: YYYY-MM-DD
Description: Tổng quan hệ thống từ Data Model + ứng dụng + actor — [Tên hệ thống]
```

### 1. Tổng quan hệ thống
2–6 đoạn ngắn: mục đích nghiệp vụ tổng thể, phạm vi dữ liệu chính, ranh giới ứng dụng.  
Thêm đoạn **"Phụ thuộc đầu vào"**: liệt kê file/nguồn user cung cấp (đường dẫn tương đối trong repo).

### 2. Danh sách đối tượng sử dụng
| STT | Đối tượng (Actor) | Mô tả / vai trò | Ghi chú |
|-----|-------------------|-----------------|---------|

### 3. Danh sách ứng dụng
| STT | Tên ứng dụng | Mục đích | Ghi chú |
|-----|--------------|----------|---------|

### 4. Quy trình nghiệp vụ
Mỗi quy trình dùng tiêu đề `#### 4.x [Tên quy trình]`, gồm 2 phần:

**Phần A — Luồng thực hiện** (đọc từ trên xuống = thứ tự thời gian):
| Bước | Người thực hiện | Ứng dụng | Tên chức năng | Mô tả |
|------|-----------------|----------|---------------|-------|

- Cột **Bước**: `1, 2, 3…` (hoặc `1.1, 1.2` nếu song song — ghi rõ trong *Mô tả*).
- Cột **Ứng dụng**: tên đúng như mục 3, hoặc `Hệ thống / tự động` nếu không qua UI.

**Phần B — Data Model liên quan** (chỉ bảng thực sự được đọc/ghi trong quy trình):
| Bảng / Thực thể | Vai trò trong quy trình | Trường liên quan chính | Ghi chú |
|-----------------|------------------------|------------------------|---------|

- Cột **Vai trò**: giải thích *tại sao* bảng này cần — không được để trống hoặc chỉ ghi lại tên bảng.
- Cột **Trường liên quan chính**: các cột được đọc/ghi (không cần liệt kê hết toàn bộ bảng).
- Chưa chắc: ghi `Cần làm rõ` kèm lý do ngắn.

**Gợi ý Mermaid:** nếu quy trình có ≥ 3 actor hoặc ≥ 2 ứng dụng tương tác, đề xuất thêm Context Diagram ở Phụ lục.

Nếu không suy ra được quy trình hợp lý: tạo `#### 4.1 Quy trình (cần làm rõ)` — mô tả rõ lý do và tài liệu cần bổ sung.

### 5. Danh sách chức năng theo ứng dụng
Nếu tổng số dòng > 30: chia thành `#### 5.x [Tên ứng dụng]`.

| Ứng dụng | Actor | Tên chức năng | Loại thao tác | Mô tả chức năng | Bảng dữ liệu liên quan | Trường dữ liệu liên quan |
|----------|-------|---------------|---------------|-----------------|------------------------|--------------------------|

- **Loại thao tác:** `R` (Read) / `W` (Write) / `D` (Delete) / `RW` / `?` (chưa chắc — ghi chú trong *Mô tả*).
- **Bảng dữ liệu liên quan:** tổng hợp tất cả dòng phải phủ hết bảng có trong Data Model.
- **Sau bảng:** nếu còn sót, thêm:
  - `Bảng chưa gán chức năng (cần làm rõ): …`
  - `Trường chưa phủ (cần làm rõ): TênBảng.tênCột — lý do`

---

## NGUYÊN TẮC PHÂN TÍCH

1. **Bám Data Model:** tên bảng/thực thể/quan hệ chỉ dùng đúng như trong đầu vào.
2. **Không bịa quy trình:** có thể suy luận từ vòng đời thực thể, quan hệ, tên bảng — nhưng phần chưa chắc phải ghi `Cần làm rõ` hoặc `Giả định (cần xác nhận)`.
3. **Phủ đủ:** mỗi bảng phải xuất hiện ít nhất một lần ở mục 5 — không lặng lẽ bỏ qua.
4. **Nhất quán mục 4–5:** chức năng ở mục 5 phải khớp với bước ở mục 4, và ngược lại.
5. **Đánh số mục:** đúng thứ tự 1 → 5, không nhảy số, không trùng số.

---

## THỨ TỰ THỰC HIỆN

1. Xác nhận đủ 3 đầu vào; thiếu → hỏi user.
2. **File Data Model:** tạo/cập nhật nếu đầu vào là SQL/Prisma/DDL chưa có MD tương ứng; ngược lại dùng file có sẵn làm checklist.
3. Trích **checklist phủ:** toàn bộ bảng, trường, quan hệ từ Data Model.
4. Viết **mục 1–3** của PRD; trích dẫn đường dẫn tương đối tới `ba-data-model_[slug].md`.
5. Xây **mục 4 và 5 song song** — cross-check để đảm bảo nhất quán trước khi lưu.
6. **Rà soát phủ:** checklist ↔ mục 4–5 PRD; checklist ↔ mục 3–6 Data Model.
7. **Rà soát cuối:** PRD đủ 5 mục; Data Model đủ mục tối thiểu; cột `Loại thao tác` điền đủ; bảng mục 5 tách nếu > 30 dòng.

---

## KHÔNG LÀM

- Không hardcode secret; không commit file `.env` hay dump SQL chứa host/credential.
- Không dán trigger/procedure có mật khẩu, hash, hay logic nhạy cảm — chỉ mô tả mục đích.
- Không thêm ứng dụng/actor không có trong đầu vào.
- Không thay mục 4–5 bằng sơ đồ khi user không yêu cầu; Mermaid chỉ ở Phụ lục.
- Không overwrite toàn bộ file khi chỉ cập nhật một phần — rewrite section bị ảnh hưởng + tăng version.

---

## GỢI Ý KÍCH HOẠT

Tổng quan hệ thống từ data model, AS-IS từ ERD, brownfield overview, mô tả nền cho dev/test, map actor–app–bảng–cột, phủ đủ bảng/trường, quy trình nối tiếp theo app, chức năng theo ứng dụng và database.

---

**Xem ví dụ định dạng:** `references/ba-system-overview-datamodel-example.md`
