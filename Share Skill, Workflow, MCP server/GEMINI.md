QUY TẮC PHÁT TRIỂN SKILL & WORKFLOW (BA EDITION)
1.Luôn tạo skill cấp dự án, chỉ trừ khi user yêu cầu tạo skill cấp global
1. Cấu trúc & Giới hạn (Atomic Design)
Giới hạn 500 dòng: File Skill.md hoặc Workflow.md tuyệt đối không vượt quá 500 dòng để tối ưu hóa context window.

Tính nguyên tử (Atomic): Mỗi Skill chỉ thực hiện một nhiệm vụ duy nhất (Single Responsibility). Nếu yêu cầu phức tạp, Agent phải chủ động gợi ý chia nhỏ thành các Skill con để tiết kiệm token và dễ tái sử dụng.

Phân tách Reference: Ưu tiên tách các logic phụ hoặc dữ liệu mẫu thành các file reference riêng biệt khi mở rộng tính năng.

Phân loại hệ thống: Khi nhận thấy yêu cầu có tính chất đa bước (multi-step), Agent phải gợi ý chuyển đổi từ Skill sang Workflow.

2. Quản lý Script & Kết nối Hệ thống
Phân vùng lưu trữ: * Script dùng chung/tái sử dụng: Lưu tại .agent/scripts/.

Script đặc thù: Lưu tại thư mục scripts/ riêng bên trong folder của Skill/Workflow đó.

Ưu tiên MCP Server: Luôn gợi ý tạo MCP Server cho các kết nối hệ thống bên ngoài (API, Database) để đảm bảo tính ổn định. Quyền quyết định cuối cùng giữa MCP hay Script trực tiếp thuộc về User.

3. Quy trình Sinh dữ liệu & Kiểm soát lỗi (New)
Cơ chế Incremental Update: Khi thực thi Skill để tạo file .md kết quả, Agent phải sinh nội dung theo từng đoạn (segment) và cập nhật dần.

Chống lỗi Runtime: Tuyệt đối không tạo file tổng dung lượng lớn trong một lần phản hồi để tránh tình trạng ngắt quãng giữa chừng gây lỗi toàn bộ file.

4. Quy chuẩn Định danh & Metadata
Naming Convention: Tên file bắt buộc theo cấu trúc: [loại]-[đối tượng]-[hành động].md (VD: ba-requirement-extract.md, pm-report-gen.md).
5.Đường dẫn tới các file khi sinh ra, hoặc reference chỉ để dạng đường dẫn tương đối, vì có thể copy sang máy khác sử dụng

Metadata Block: Mọi file phải bắt đầu bằng khối thông tin sau:

Version: 1.x.x
Author: M2MBA
Last Updated: YYYY-MM-DD
Description: [Mô tả ngắn gọn chức năng]