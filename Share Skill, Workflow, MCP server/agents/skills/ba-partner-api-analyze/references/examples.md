# Ví dụ Output: BA Partner Integration Analysis

> **Version:** 1.0 | **Author:** M2MBA | **Last Updated:** 2026-04-20

---

## Ví dụ Bước 4 — Mô tả quy trình tích hợp

**Phần 1 — Chuẩn bị đầu vào:** `[AUTH]`
Đối tác (hệ thống giao vận) cần chuẩn bị:
- API Key được cấp khi hoàn thành onboarding
- Danh sách `order_code` hoặc khoảng thời gian lấy đơn (from_date, to_date)
- Biết endpoint môi trường đang dùng (sandbox: `api-staging.example.com`, production: `api.example.com`)

**Phần 2 — Xác thực:** `[AUTH]`
Bước 1 — Gửi API Key: Đính kèm vào header `X-API-Key: [key]` trong mọi request, không cần bước đăng nhập riêng.
Bước 2 — Hệ thống xác thực: Kiểm tra key, định danh đối tác, kiểm tra phạm vi quyền theo partner scope.
Bước 3 — Từ chối: Key sai/hết hạn → HTTP 401 + error code `INVALID_API_KEY` → hướng dẫn liên hệ để cấp lại.

**Phần 3 — Luồng chính:** `[DATA MAPPING]` → `[INTEGRATION FLOWS]`

*[DATA MAPPING] Bước 0 — Thiết lập partner scope (nếu lần đầu):*
  → Hành động: Admin nội bộ cấu hình `partner_code`, phạm vi dữ liệu, rate limit cho đối tác
  → Xử lý: Lưu vào bảng `PartnerConfig`; đối tác không gọi bước này trực tiếp
  → Kết quả: `partner_code` được bind với API Key, mọi request sau được filter theo scope này

*[INTEGRATION FLOWS] Bước 1 — Lấy danh sách đơn (REST API):*
  → Hành động: Đối tác gọi `GET /api/v1/orders?from_date=2026-01-01&to_date=2026-01-31&page=1&per_page=50`
  → Xử lý: Hệ thống lọc đơn thuộc partner scope, phân trang, trả danh sách
  → Kết quả: Danh sách `order_id` + meta pagination để dùng cho Bước 2
  → Điều kiện: Luôn thực hiện trước, lấy `order_id` cho bước tiếp theo

*[INTEGRATION FLOWS] Bước 2 — Lấy chi tiết đơn (REST API):*
  → Hành động: Đối tác gọi `GET /api/v1/orders/{order_id}` với từng `order_id` từ Bước 1
  → Xử lý: Validate `order_id` thuộc partner scope, trả chi tiết
  → Điều kiện: Chỉ gọi với `order_id` từ Bước 1; nếu 404 thì bỏ qua và tiếp tục

**Phần 4 — Xử lý lỗi:**
- 401 `INVALID_API_KEY`: Key sai/hết hạn → liên hệ admin để cấp lại
- 403 `FORBIDDEN`: Đơn không thuộc phạm vi đối tác → bỏ qua, xử lý đơn tiếp theo
- 404 `NOT_FOUND`: `order_id` không tồn tại → bỏ qua, ghi log
- 429 `RATE_LIMIT_EXCEEDED`: Vượt giới hạn → xem header `Retry-After`, chờ rồi retry
- 500 `SERVER_ERROR`: Lỗi hệ thống → retry sau 60s, tối đa 3 lần với exponential backoff; báo nếu kéo dài > 5 phút

---

## Ví dụ Bước 6 — Đặc tả API chi tiết

### API 1 — Lấy danh sách đơn hàng

| Thuộc tính | Giá trị |
|-----------|--------|
| Mục đích | Trả danh sách đơn hàng trong khoảng thời gian, phân theo đối tác |
| Method | GET |
| Endpoint | `/api/v1/orders` |
| Authentication | API Key (Header: `X-API-Key`) |
| Idempotency | Không áp dụng (GET) |

*Query Parameters:*

| Field | Type | Required | Default | Description | Example |
|-------|------|---------|---------|-------------|---------|
| from_date | string (ISO 8601) | Có | — | Ngày bắt đầu lọc | `2026-01-01` |
| to_date | string (ISO 8601) | Có | — | Ngày kết thúc lọc | `2026-01-31` |
| status | string | Không | all | Lọc theo trạng thái đơn | `confirmed`, `shipped`, `delivered` |
| page | integer | Không | 1 | Trang hiện tại | `1` |
| per_page | integer | Không | 20 | Số bản ghi mỗi trang (max 100) | `50` |

```json
// Response 200 OK
{
  "data": [
    {
      "orderId": "ORD-2026-001",
      "orderCode": "DH001",
      "status": "confirmed",
      "createdAt": "2026-01-15T08:30:00+07:00",
      "totalAmount": 250000
    }
  ],
  "meta": {
    "total": 150,
    "page": 1,
    "per_page": 20,
    "total_pages": 8
  }
}

// Response lỗi
{
  "error": {
    "code": "INVALID_DATE_RANGE",
    "message": "Khoảng thời gian không hợp lệ. from_date phải nhỏ hơn to_date.",
    "details": [
      { "field": "from_date", "issue": "must be before to_date" }
    ]
  }
}
```
