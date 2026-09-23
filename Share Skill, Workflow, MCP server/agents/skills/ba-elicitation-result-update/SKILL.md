---
name: ba-elicitation-result-update
description: "Chuyên trách cập nhật kết quả khơi gợi yêu cầu từ Meeting Notes hoặc Stakeholder files."
---

# HƯỚNG DẪN SKILL: CẬP NHẬT KẾT QUẢ KHƠI GỢI YÊU CẦU

**Version:** 1.5.0
**Author:** M2MBA
**Last Updated:** 2026-04-13
**Description:** Cập nhật kết quả khơi gợi từ meeting / stakeholder → tracking, history, summary (5 mục bắt buộc).

## Mục đích
Cập nhật trạng thái đã làm rõ từ input BA. **Atomic:** chỉ cập nhật kết quả, không sinh câu hỏi mới — **ngoại trừ** trường hợp thiếu thông tin để hoàn chỉnh Summary (bắt buộc sinh câu hỏi làm rõ).

## Nguyên tắc

1. **Phân tích input**: Trích I/O, quy trình, công thức (meeting notes, tài liệu stakeholder).
2. **Ground truth**: Chỉ đánh ✅ khi là kết quả **làm việc trực tiếp với stakeholder** — **không** đánh ✅ từ "file tìm hiểu domain" của BA.
3. **Module**: Gán đúng nhóm nghiệp vụ (Bán hàng, Mua hàng, Kho, Tổng quan…).
4. **Tracking** `docs-BA/Elicitation/listQA/`: đúng file; một ý chạm nhiều module → cập nhật **tất cả** file liên quan.
5. **Summary** `docs-BA/Elicitation/`: tên file = chủ đề; link history liên quan; cùng chủ đề → update; chủ đề mới → file mới.

   **Cấu trúc bắt buộc của file Summary — tối thiểu 5 mục:**

   **Mục 1 · Tổng quan**
   Bối cảnh buổi làm việc, phạm vi nghiệp vụ, stakeholder tham gia, ngày thực hiện, link history.

   **Mục 2 · Các quy trình liên quan**
   Tổng hợp toàn bộ quy trình được trích xuất từ kết quả khơi gợi. Mỗi quy trình gồm:
   - **(a) Tên quy trình**
   - **(b) Mục đích** (1–2 câu)
   - **(c) Bảng các bước** — 1 hàng = 1 bước:

   | Bước | Ai thực hiện | Làm gì | Mô tả chi tiết cách làm | Input data | Output / File biểu mẫu | Quy định cần tuân thủ |
   |------|-------------|--------|--------------------------|------------|------------------------|-----------------------|

   > ⚠️ Nếu bất kỳ cột nào **không đủ thông tin**: ghi `[CHƯA RÕ]` vào ô đó;
   > **bắt buộc** liệt kê câu hỏi khơi gợi ngay cuối mục 2 (mục con `### Câu hỏi làm rõ quy trình`);
   > note vào Summary: *"⚠️ [Tên cột / tên bước] của quy trình [X] chưa rõ — cần bổ sung sau."*

   **Mục 3 · Danh sách Stakeholder & Công việc hằng ngày**
   Liệt kê từng stakeholder tham gia hoặc liên quan trực tiếp tới bài toán:

   | Stakeholder | Vai trò / Chức danh | Công việc hằng ngày liên quan tới bài toán |
   |-------------|---------------------|--------------------------------------------|

   > Chưa xác định được → ghi `[CHƯA RÕ]` và bổ sung câu hỏi làm rõ.

   **Mục 4 · Quy định & Rule nghiệp vụ cần tuân thủ**
   Liệt kê toàn bộ rule / constraint / điều kiện (NB, giới hạn dữ liệu, quyền, SLA…) — cơ sở ERD & Business Rule.

   **Mục 5 · Biểu mẫu & Công thức tính toán**
   - Danh sách biểu mẫu / template (tên, mục đích, ai dùng).
   - Công thức tính toán (ký hiệu, điều kiện áp dụng).
   - Chưa có → ghi `[CHƯA CÓ / CẦN BỔ SUNG]`.

6. **History** `docs-BA/Elicitation/history/YYYYMMDD_[stakeholder]_[chu_de].md`: viết như **tài liệu vận hành** (không phải bảng tick):
   - Bảng bước: STT, Ai, Việc, Hệ thống/tool, mô tả, I/O, tình huống phát sinh, công thức/logic, quy định, quyền, template, báo cáo, trao đổi liên bộ phận
   - Tham số cố định; **Hiện trạng** vs **Định hướng**; Pain (🔴/🟠/🟡) + đối tượng; tài liệu cần thêm + câu mở + stakeholder follow-up
7. **Tag ngày**: Câu mới/follow-up trong tracking — cột Mục: `[FOLLOW-UP · YYYY-MM-DD]`.
8. **Incremental**: Sửa từng đoạn nhỏ; không ghi đè cả file lớn một lần.
9. **Cuối mỗi `listQA` đã sửa**: luôn có/cập nhật `## Danh sách các câu hỏi cần follow-up` — tổng hợp câu **mới** hoặc **còn follow-up**. Không có → *Không có follow-up mới trong lần cập nhật này.*

## Guard (bắt buộc trước khi kết thúc phiên — trừ user chỉ định ngoại lệ)

| # | Đầu ra | Yêu cầu |
|---|--------|---------|
| **1** | **History** | ≥1 file `docs-BA/Elicitation/history/YYYYMMDD_[stakeholder]_[chu_de].md` (Nguyên tắc #6). |
| **2** | **Summary** | File trong `docs-BA/Elicitation/`, tên theo chủ đề. **Bắt buộc đủ 5 mục**: Tổng quan · Quy trình (bảng bước 7 cột) · Stakeholder & CV hằng ngày · Quy định & Rule · Biểu mẫu & Công thức. Thiếu thông tin → `[CHƯA RÕ]` + sinh câu hỏi khơi gợi + note vào file. |
| **3** | **Tracking** | Đã sửa `listQA` + mục cuối `## Danh sách các câu hỏi cần follow-up` (#9). |

## Quy trình

**Input** → **Quét** `listQA/` → **Phân loại** module/chủ đề → **Sửa tracking** (⬜→✅, #7, #9) → **History** (#6) → **Summary** (#5): update hoặc tạo + link history + **5 mục bắt buộc**; thiếu thông tin → `[CHƯA RÕ]` + câu hỏi làm rõ + note trực tiếp trong file; summary quá lớn → tách theo chủ đề (không trùng tên).
