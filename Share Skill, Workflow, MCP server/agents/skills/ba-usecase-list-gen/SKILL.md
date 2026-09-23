---
name: ba-usecase-list-gen
description: "Skill tự động phân tích UC theo 10 nhóm (0-9); tách UC theo Ứng dụng; khai thác exception và pain point từ file elicitation. Đầu ra là 1 file master duy nhất, KHÔNG cần user xác nhận."
---

# HƯỚNG DẪN SKILL: BA USECASE LIST GEN

**Version:** 1.4.1
**Author:** M2MBA
**Last Updated:** 2026-04-13
**Description:** Phân tích UC theo 10 nhóm (0–9), tách UC theo Ứng dụng, khai thác exception từ Elicitation Muc 2 và CV hằng ngày từ Mục 3 để tìm Nhóm 3 & 9; tập trung hoàn toàn vào danh sách Master UC.

## 🎯 Mục đích
- **KHÔNG CẦN** user xác nhận (confirm) qua từng nhóm — One-shot, auto 100%.
- Phân nhóm theo **Epics**, tách rõ từng UC theo **Ứng dụng** (Web HV, Mobile, Web Admin…).
- Cùng tên UC nhưng trên nhiều ứng dụng → tách thành **nhiều dòng riêng biệt**.
- Có **Change log** để theo dõi lịch sử; sinh ra **1 output file duy nhất**.

## 📋 Yếu tố đầu vào (ĐỌC TRƯỚC KHI PHÂN TÍCH)

Agent **BẮT BUỘC** đọc các file sau trước khi sinh UC:
1. **`docs-BA/PRD/ba-product-overview.md`** — Lấy danh sách ứng dụng, actor, hệ thống tích hợp.
2. **`docs-BA/PRD/ba-system-overview_*.md`** (nếu có) — Chức năng chi tiết theo app + actor.
3. **`docs-BA/Elicitation/`** — Đọc file **Summary** và **History** theo bảng ánh xạ bên dưới (nguồn chính cho Nhóm 1, 3, 9).
4. Tài liệu quy trình nghiệp vụ do user cung cấp (BPMN, meeting notes…).

**Bảng ánh xạ: Section trong file Elicitation → Nhóm UC cần khai thác**

| Section (Summary / History) | Nhóm UC khai thác |
|-----------------------------|-------------------|
| Summary **Mục 2 · Quy trình** — cột *Làm gì* (bảng bước) | Nhóm 1 (Phục vụ quy trình) |
| Summary **Mục 2 · Quy trình** — cột ***Tình huống phát sinh*** | **Nhóm 3** (Exception trực tiếp từ stakeholder) |
| Summary **Mục 4 · Quy định & Rule** | Nhóm 3 (điều kiện nề exception) |
| Summary **Mục 3 · Stakeholder & CV hằng ngày** | **Nhóm 9** (CV hằng ngày ngoài quy trình) |
| Summary **Mục 5 · Biểu mẫu & Công thức** | Nhóm 5 (Report) + Nhóm 4 (Reference Data) |
| History — cột *Tình huống phát sinh / Fail case* | Nhóm 3 (Exception bổ sung) |
| History — cột *Pain (🔴/🟠/🟡) + đối tượng* | **Nhóm 9** mức 🔴/🟠 |
| History — cột *Biểu mẫu / Template / Báo cáo* | Nhóm 5 (Report) |

> **Lưu ý:** File Summary và History được tạo bởi skill `ba-elicitation-result-update`. Nếu chưa có thì đọc thẳng meeting notes / stakeholder file do user cung cấp.

---

## ⚙️ Quy trình phân tích của Agent (One-shot Action)

### Bước 0: Xác định Ứng dụng & Actor tham chiếu

Sau khi đọc `ba-product-overview.md`, tạo block tham chiếu đặt ngay trước `## 2. Danh sách Epics`:

```
> **Danh sách ứng dụng & Actor tham chiếu:**
> - **[Tên App 1]** — [Mô tả ngắn + đối tượng]
> - **[Tên App 2]** — ...
> - **— (Backend)** — UC hệ thống tự động, không gắn UI cụ thể
>
> **Actor:** [HV], [Admin], [Khách vãng lai], [Hệ thống], ...
```

### Bước 1: Phân tích 10 Nhóm Use Case

Quét toàn bộ quy trình qua 10 góc nhìn để khai phá trọn vẹn UC:

- **Nhóm 0 (Discovery / Browse công khai):** UC dành cho người dùng **chưa đăng nhập** (Khách vãng lai): duyệt danh sách, xem trang chi tiết, đăng ký nhận thông tin, đọc blog/nội dung công khai. **Thường bị bỏ sót nếu chỉ focus quy trình nội bộ.**
- **Nhóm 1 (Phục vụ quy trình):** Bước người dùng tương tác hệ thống. Gộp các bước cùng đích thành 1 UC (Nhập + Gửi → UC: Tạo yêu cầu).
- **Nhóm 2 (CRUD — RUD):** Đọc, Sửa, Xóa trên Entity tạo ra từ Nhóm 1. Ghi chú rule ai được Xóa/Sửa và trong điều kiện nào.
- **Nhóm 3 (Exception — Tình huống phát sinh):**
  - **Nguồn chính → Summary Mục 2:** Cột ***Tình huống phát sinh*** trong bảng bước quy trình; cột *Quy định cần tuân thủ* (xác định điều kiện nẹi exception).
  - **Nguồn bổ sung → History:** Cột *Tình huống phát sinh / Fail case*; cột *Pain (🔴/🟠🟡)* mức 🔴.
  - **Scan keyword** trong toàn bộ file: *"lỗi", "không khớp", "quên", "nhầm", "thủ công", "xử lý khi", "trường hợp", "ngoại lệ", "fail", "chưa rõ"*.
  - **Lọc:** Chỉ lấy exception tần suất cao — bỏ case hiếm (< 1 lần/tháng).
  - **Gợi ý:** Đặt lại mật khẩu, Gia hạn truy cập, Chuyển lớp/slot, Đối soát thủ công, Cấp lại quyền, Hủy bảo lưu, Reset bài làm, Xử lý đơn ngoại lệ, Khiếu nại thanh toán.
- **Nhóm 4 (Reference Data / CMS):** Cấu hình, danh mục, **nội dung CMS/Blog** cần admin quản lý linh động.
- **Nhóm 5 (Report):** Báo cáo thiết yếu có tên đích danh (Báo cáo doanh thu, Dashboard tiến độ…).
- **Nhóm 6 (Lookup):** Tra cứu thông tin cá nhân/đối tượng đặc thù (hồ sơ HV, lịch sử giao dịch…).
- **Nhóm 7 (User / Permission):** Đăng ký, đăng nhập, phân quyền cho **toàn bộ hệ thống**.
- **Nhóm 8 (System / Backend auto):** UC do **hệ thống tự kích hoạt** — webhook, job, trigger; Ứng dụng = `— (Backend)`.
- **Nhóm 9 (CV hằng ngày / Daily Ops):**
  - **Định nghĩa:** UC **không xuất hiện trong bất kỳ quy trình nào** nhưng là việc stakeholder thực sự làm hằng ngày — có thể chỉ là 1 việc rời cần có chức năng để giải quyết, không nhất thiết phải là "pain point".
  - **Nguồn chính → Summary Mục 3:** Bảng **Stakeholder & Công việc hằng ngày** (`docs-BA/Elicitation/`). Cột *Công việc hằng ngày liên quan tới bài toán* — mỗi công việc là 1 UC tiềm năng.
  - **Nguồn bổ sung → History:** Cột *Pain (🔴/🟠/🟡) + đối tượng* — mức 🔴/🟠 thường ẩn chứa UC cần giải quyết.
  - **Scan keyword** bổ sung trong toàn bộ file: *"hay quên", "mất thời gian", "thủ công", "phải check", "muốn xem nhanh", "xuất ra", "tìm kiếm", "không biết", "chưa có chỗ"*.
  - **Gợi ý UC phổ biến:** Tìm kiếm nhanh, Export DS (Excel/CSV), Gửi thông báo nhắc, Dashboard snapshot, Nhân bản khóa/lớp, Gắn tag/segment, Audit log.
  - **Lưu ý:** Nhóm 9 thường bổ sung UC vào Epic **hiện có** (không tạo Epic riêng) — góc nhìn **operational**, không phải HV-facing.

### Bước 2: Tách UC theo Ứng dụng

**Quy tắc bắt buộc:**

| Tình huống | Xử lý |
|-----------|-------|
| UC chỉ trên 1 app | 1 dòng, cột Ứng dụng = tên app đó |
| UC xuất hiện trên N app | N dòng riêng biệt; STT tăng số |
| UC hệ thống, không có UI | Ứng dụng = `— (Backend)` |
| UC chỉ Admin (Web admin) | 1 dòng, Ứng dụng = Web admin |

### Bước 3: Gom Epic & Định nghĩa

- Gom UC chung mục tiêu / nhóm Entity thành **Epic**.
- Ghi rõ **Ý nghĩa Epic** (1–2 câu, nêu đặc điểm nghiệp vụ chủ chốt + BR nếu có).
- Đặt Epic theo thứ tự: Nhóm 0 → Nhóm 7 → Nhóm 8/9 (backend/admin sau cùng).

### Bước 4: Sinh & Cập nhật File Output

- **File:** `docs-BA/epics-US/ba-epics-and-user-stories.md`
- **Nếu file chưa có:** Tạo mới đúng template bên dưới.
- **Nếu file đã có:** Đọc file → chỉ sửa/chèn `## 2` và Change log; **không xóa** `## 3` nếu đã có US.
- **Incremental:** Sinh từng đoạn nếu nội dung dài — tránh lỗi truncate.

---

## 📄 Template File Output (BẮT BUỘC)

```markdown
Version: 1.0.0
Author: M2MBA
Last Updated: yyyy-mm-dd
Description: Danh sách Epics và Use Case (file master — workflow ba-prd-create).

# DANH SÁCH EPICS & USE CASES (MASTER)

## 1. Change Log
| Version | Ngày cập nhật | Người thực hiện | Nội dung cập nhật chi tiết |
|---------|----------------|-----------------|----------------------------|
| 1.0.0 | [Ngày] | Agent | Tạo mới UC từ quy trình [Tên quy trình] |

---

> **Danh sách ứng dụng & Actor tham chiếu** (theo `ba-product-overview.md`):
> - **[App 1]** — [Đối tượng / mục đích]
> - **[App 2]** — ...
> - **— (Backend)** — UC hệ thống tự động, không gắn UI cụ thể
>
> **Actor:** [Actor 1], [Actor 2], Khách vãng lai, Hệ thống

---

## 2. Danh sách Epics và Use Case chi tiết

### Epic 1: [Tên Epic]
**Ý nghĩa Epic:** [Mô tả nghiệp vụ bao quát; BR liên quan nếu có]

| STT | Actor | Tên Use Case | Ứng dụng | Mô tả tóm tắt |
|-----|-------|--------------|----------|---------------|
| 1.1 | [Actor] | [Hành động + Mục tiêu] | [Tên app] | [Ghi chú / BR] |
| 1.2 | [Actor] | [Tên UC] | [Tên app khác] | [Ghi chú] |

### Epic 2: [Tên Epic]
...

```

---

## ⚠️ Checklist Bắt Buộc Dành Cho Agent

1. **Đọc PRD + Elicitation trước:** Đọc `ba-product-overview.md`, `ba-system-overview` (nếu có) và `docs-BA/Elicitation/` để xác định app, actor, exception thực tế và pain point.
2. **Nhóm 0 bắt buộc:** Luôn phân tích UC Discovery/Browse cho **Khách vãng lai** — thường bị bỏ sót nhất.
3. **Nhóm 3 từ elicitation:** Scan từ khóa exception trong lời stakeholder; đối chiếu bảng gợi ý — không chỉ liệt kê Hủy/Hoàn trả.
4. **Nhóm 8 bắt buộc:** Luôn liệt kê UC Backend/hệ thống tự động với Ứng dụng = `— (Backend)`.
5. **Nhóm 9 bắt buộc:** Đọc **Summary Mục 3 (CV hằng ngày)** — mỗi dòng công việc hằng ngày là 1 UC tiềm năng; kết hợp cột Pain 🔴/🟠 trong History; không giới hạn ở "pain point".
6. **Tách UC theo app:** Mỗi UC phải gắn 1 app cụ thể; nhiều app → nhiều dòng.
7. **Format bảng đúng:** `STT | Actor | Tên Use Case | Ứng dụng | Mô tả tóm tắt` — **không dùng cột "Thuộc Nhóm"**.
8. **Block Actor/App:** Đặt block tham chiếu ngay sau `---` cuối Change log, trước `## 2`.
9. **Auto 100%:** Không dừng hỏi user giữa chừng — hoàn thành file 1 lần.
10. **Change log:** Mọi lần chạy phải ghi log vào `## 1`.
11. **Đúng tên file:** `ba-epics-and-user-stories.md` tại `docs-BA/epics-US/`.
