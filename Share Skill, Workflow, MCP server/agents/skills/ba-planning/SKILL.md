---
name: ba-planning
description: "Quản trị lộ trình phát triển BA: Theo dõi tiến độ UI Prompt và User Story Specification cho từng chức năng."
---

Version: 1.0.0
Author: M2MBA
Last Updated: 2026-04-13
Description: Skill quản trị "Command Center" giúp theo dõi toàn bộ vòng đời của User Story từ lúc là backlog đến khi có thiết kế UI và đặc tả chi tiết.

# HƯỚNG DẪN SKILL: BA DEVELOPMENT PLANNING

## 🎯 Mục đích
Đảm bảo tính nhất quán, không sót yêu cầu và quản lý tiến độ sản xuất tài liệu BA (Mockup Prompt & US Specification) dựa trên danh sách Master Use Case.

## 📋 Tài liệu tham chiếu
1. **Master UC**: `docs-BA/epics-US/ba-epics-and-user-stories.md`
2. **Tracking File**: `docs-BA/ba-development-tracking.md`
3. **Artifact Folders**:
    - Prompts: `docs-BA/Prototype/Prompt/`
    - US Specs: `docs-BA/Epics/`

## 🚀 Quy trình thực hiện

### Hành động 1: Sync (Đồng bộ danh sách - BẮT BUỘC)
- Đọc file Master UC.
- **BẮT BUỘC**: Khởi tạo `ba-development-tracking.md` bằng cách lấy **toàn bộ** danh sách Use Case từ Master file ngay lần chạy đầu tiên.
- Nếu đã tồn tại -> Cập nhật các thay đổi mới nhưng phải bảo toàn trạng thái của các dòng cũ.

### Hành động 2: Global Audit (Rà soát tổng thể)
- Quét toàn bộ project (Prompt và US Spec).
- Cập nhật tất cả các hàng trong `ba-development-tracking.md` dựa trên các file thực tế tìm thấy.
- Mục đích: Đảm bảo bảng Tracking luôn phản ánh đúng 100% hiện trạng folder project.

### Hành động 3: Project Health Dashboard (Báo cáo sức khỏe)
- Phân tích bảng Tracking để đưa ra báo cáo:
    - Tổng số UC / Số UC đã có Prompt / Số UC đã có US Spec.
    - Cảnh báo các UC có Prompt nhưng chưa có US Spec (hoặc ngược lại).
    - Nhận diện các Epic đang bị chậm tiến độ.

## 📊 Cấu trúc Bảng Tracking
| Epic | UC ID | Name | App | Actor | UI Prompt | US Spec | Prompt File | US Spec File |
|------|-------|------|-----|-------|-----------|---------|-------------|--------------|
| [Num] | [X.Y] | [Name] | [App] | [Actor] | `🟢 Done` / `🔴 Todo` | `Backlog`/`Draft`/`Ready`/`Done` | [Link] | [Link] |

## ✅ Quy tắc thực thi
1. **Tuyệt đối không xóa dữ liệu cũ**: Khi Sync hoặc Audit, chỉ được ghi đè hoặc bổ sung, không được xóa các hàng đã có dữ liệu.
2. **Link tương đối**: Luôn sử dụng đường dẫn tương đối để đảm bảo tính di động của project.
3. **Ngôn ngữ**: Tiếng Việt chuyên ngành.
