# Template: Tài liệu Đặc tả Tích hợp

> **Version:** 1.0 | **Author:** M2MBA | **Last Updated:** 2026-04-20

---

# Tài liệu Đặc tả Tích hợp: [Tên đối tác]

> **Phiên bản:** 1.0 | **Ngày:** DD/MM/YYYY | **Người tạo:** [Tên BA]
> **Trạng thái:** Draft / Review / Approved

---

## Lịch sử thay đổi

| Phiên bản | Ngày | Người thực hiện | Nội dung thay đổi |
|----------|------|----------------|------------------|
| 1.0 | DD/MM/YYYY | [Tên BA] | Tạo mới |

---

## 1. Tóm tắt điều hành

> *(3–5 dòng: Tên đối tác, mục đích tích hợp, phạm vi dữ liệu, loại tích hợp, môi trường, timeline dự kiến)*

**Bảng tóm tắt nhanh:**

| Thuộc tính | Giá trị |
|-----------|--------|
| Đối tác | [Tên] |
| Mục đích | [Mục đích nghiệp vụ] |
| Loại tích hợp | REST API / Message Queue / File / SOAP / Hybrid |
| Môi trường hiện tại | Sandbox / Production |
| Số API endpoint | [N] |
| Thực thể thay đổi | [N thực thể thêm mới, M trường bổ sung] |
| Mức độ phức tạp | Thấp / Trung bình / Cao |

---

## 2. Dữ liệu đối tác cần & Mapping nội bộ

*[Bảng từ Bước 2 — đầy đủ trạng thái ✅/⚠️/❌]*

---

## 3. Chức năng cần thay đổi

*[Bảng từ Bước 3 — bao gồm cột Impact nội bộ]*

---

## 4. Quy trình tích hợp đề xuất

*[Nội dung 4 phần từ Bước 4 — đủ 3 giai đoạn [AUTH] → [DATA MAPPING] → [INTEGRATION FLOWS]]*

---

## 5. Sequence Diagram

*[Mermaid từ Bước 5 — có autonumber, Note over phân nhóm 3 giai đoạn E2E]*

---

## 6. Bảng Mapping API ↔ Sequence

*[Bảng từ Bước 5]*

---

## 7. Đặc tả Chi tiết API / Message / File

*[Đặc tả từng item từ Bước 6 — đầy đủ bảng request, response, ví dụ JSON, status codes]*

---

## 8. Non-Functional Requirements

| Thuộc tính | Yêu cầu | Ghi chú |
|-----------|--------|--------|
| Response time | ≤ [X]ms (p95) | |
| Availability | [X]% uptime | |
| Rate limit | [X] req/phút per API Key | |
| Timeout | [X] giây | |
| Retry policy | [X] lần, backoff [Y]s | |
| Data retention | Log lưu [X] ngày | |

---

## 9. Rủi ro & Phụ thuộc

| # | Rủi ro | Khả năng xảy ra | Tác động | Biện pháp giảm thiểu |
|---|--------|----------------|---------|---------------------|
| 1 | *(mô tả rủi ro)* | Cao / TB / Thấp | Cao / TB / Thấp | *(biện pháp)* |

**Phụ thuộc kỹ thuật:**
- [ ] [Team/hệ thống cần phối hợp]
- [ ] [API/service bên thứ ba cần sẵn sàng]

---

## 10. Điểm cần làm rõ với đối tác

*[Bảng từ Bước 7 — đầy đủ cột "Ảnh hưởng nếu không rõ"]*

---

## 11. Danh sách thay đổi thực thể dữ liệu

*[Phần A, B, C từ Bước 3A — đầy đủ cả 3 bảng]*

---

## 12. ERD nghiệp vụ mở rộng

*[Mermaid erDiagram từ Bước 5A — có annotation mô tả nghiệp vụ trên quan hệ, tư duy đa đối tác]*

---

## 13. Giao diện mẫu chức năng nội bộ *(nếu có)*

> Tạo nếu luồng tích hợp phát sinh chức năng nội bộ cần UI thao tác (ví dụ: form cấu hình partner, màn hình quản lý API Key, dashboard theo dõi log tích hợp).

**File HTML mockup:** `docs-BA/Prototype/[TenDoiTac]_[TenChucNang]_mockup.html`

Yêu cầu mockup:
- Wireframe đơn giản, không cần pixel-perfect
- Có label rõ từng field
- Có trạng thái (active/inactive, enabled/disabled)
- Ghi chú tooltip hoặc placeholder cho trường nhạy cảm
- Màu sắc phân biệt: section header (#f0f0f0), action button (màu primary), warning/error (đỏ/vàng)

---

## 14. Checklist go-live *(bắt buộc)*

**Sandbox & Testing**
- [ ] Sandbox test toàn bộ luồng tích hợp (happy path + error path)
- [ ] Kiểm tra retry logic và idempotency
- [ ] Test pagination nếu có

**Security & Compliance**
- [ ] Security review (PII masking, auth mechanism đúng cơ chế đã thiết kế)
- [ ] Rate limit test — đảm bảo client xử lý 429 đúng
- [ ] Kiểm tra data scoping (đối tác không lấy được dữ liệu ngoài phạm vi)

**Non-Functional**
- [ ] NFR validate: response time (p95 ≤ threshold), availability, timeout
- [ ] Load test nếu volume dự kiến cao

**Documentation & Handoff**
- [ ] Documentation sign-off (BA + Tech Lead + đại diện đối tác)
- [ ] Onboarding guide gửi đối tác (endpoint, auth, error codes)

**Operations**
- [ ] Monitoring alert setup (5xx spike, latency cao, queue lag)
- [ ] Rollback plan — cơ chế tắt tích hợp nếu cần, xử lý dữ liệu đang dở
- [ ] Log retention policy đã cấu hình đúng môi trường production
