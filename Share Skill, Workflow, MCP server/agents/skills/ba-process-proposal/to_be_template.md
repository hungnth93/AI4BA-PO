# Phân tích đề xuất & Thiết kế quy trình TO-BE: [Tên quy trình]

## 1. Phân tích định hướng & Tác động

**(Lưu ý Agent: Cần đặt câu hỏi với người dùng (BA/Stakeholder) trên giao diện chat hoặc sử dụng thông tin từ file input/context nếu có để điền vào phần này, thay vì tự bịa số liệu).**

### 1.1. Định hướng kinh doanh
- **Mục tiêu trong thời gian tới:** [Điền mục tiêu kinh doanh, ví dụ 6-12 tháng tới]
- **Thay đổi đối với mô hình kinh doanh:** [Có kế hoạch mở rộng hay thay đổi nào không?]
- **Chiến lược, Hiệu quả mong đợi:** [Kỳ vọng về tăng trưởng, giảm lãng phí, hiệu suất]

### 1.2. Định hướng sản phẩm / Chuyển đổi số
- **Chuyển đổi số:** [Mức độ ưu tiên để tự động hóa/chuyển đổi số]
- **Công nghệ mới áp dụng:** [AI, IoT, Hệ thống CRM/ERP mới...]
- **Tích hợp:** [Các hệ thống dự kiến sẽ liên kết/tích hợp]

### 1.3. Năng lực, Ngân sách và Tuân thủ (Compliance)
- **Năng lực tổ chức:** [Số lượng nhân sự dự kiến, kỹ năng cần có, kế hoạch đào tạo]
- **Ngân sách:** [Dự trù hoặc ràng buộc về kinh phí triển khai]
- **Compliance & Bảo mật:** [Yêu cầu về kiểm toán (audit trail), bảo mật dữ liệu, tuân thủ PCI-DSS, GDPR...]

### 1.4. Yếu tố ảnh hưởng & Roadmap
- **Mức độ ưu tiên:**
  - Cao (Cần ngay): [Yếu tố 1], [Yếu tố 2]
  - Trung bình: [Yếu tố 3]
  - Thấp: [Yếu tố 4]
- **Roadmap triển khai (Dự kiến):**
  - Giai đoạn 1: [Mục tiêu ngắn hạn, ROI nhanh]
  - Giai đoạn 2: [Cải tiến tiếp theo]
  - Giai đoạn 3: [Định hướng dài hạn]

---

## 2. Bảng So sánh AS-IS và TO-BE

Lập bảng so sánh, nêu bật sự khác biệt giữa hiện tại và tương lai.

| Hạng mục / Tiêu chí | Quy trình AS-IS | Quy trình TO-BE | Lợi ích / Cải tiến |
|---------------------|-----------------|-----------------|--------------------|
| [Tiêu chí 1] | [Thực trạng] | [Đề xuất TO-BE] | [Lợi ích mang lại] |
| [Tiêu chí 2] | [Thực trạng] | [Đề xuất TO-BE] | [Lợi ích mang lại] |

---

## 3. Thiết kế quy trình TO-BE

### 3.1. Lưu đồ BPMN (Placeholder)

*Mặc định tạo placeholder cho hình ảnh lưu đồ BPMN. Khi được approve, cần sử dụng tính năng tạo BPMN để xuất file SVG kèm XML.*

![Lưu đồ TO-BE]([tên-quy-trình]-to-be.svg)

*Lưu ý: Mã nguồn lưu đồ được đính kèm ở file `[tên-quy-trình]-to-be.bpmn` dùng cho các chỉnh sửa tiếp theo.*

### 3.2. Bảng mô tả chi tiết các bước quy trình

**QUY TẮC MAPPING ĐẶC BIỆT:**
Các bước phải được mapping 1-1 với quy trình hiện tại (AS-IS). Không được cắt gọn bước đi. Ví dụ: Nếu quy trình AS-IS bắt đầu từ bước 1, thì TO-BE phải chỉ rõ bước 1 của AS-IS trở thành thao tác nào trong TO-BE. Nếu một bước AS-IS bị loại bỏ do thay đổi nghiệp vụ, thì mới không cần đưa vào (nhưng nên ghi chú việc bỏ bước đó nếu cần).

| Bước TO-BE | Mapping Bước AS-IS | Người thực hiện | Tên bước | Thủ công / Hệ thống | Mô tả chi tiết | Ràng buộc |
|------------|--------------------|----------------|----------|-------------------|----------------|-----------|
| 1 | [Bước AS-IS tương ứng, vd: Bước 1] | [Actor] | [Tên bước] | [Thủ công / Hệ thống] | [Giải thích ngắn gọn cách bước thao tác diễn ra trên quy trình TO-BE] | [Điều kiện, rule, validation] |
| 2 | [Bước AS-IS tương ứng, vd: Bước 2] | [Actor] | [Tên bước] | [Thủ công / Hệ thống] | [...] | [...] |
