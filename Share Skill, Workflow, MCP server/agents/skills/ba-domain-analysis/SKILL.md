---
name: ba-domain-analysis
description: Trợ lý tìm hiểu domain chuyên sâu cho Business Analyst. Hướng dẫn BA tìm hiểu, phân tích và khám phá toàn diện bất kỳ domain/subdomain nào theo quy trình 8 bước có cấu trúc. Tạo file .md với Business Model Canvas, Lean Canvas, quy trình E2E, stakeholder, ERD, phân tích đối thủ. Sử dụng khi cần phân tích domain mới, tìm hiểu nghiệp vụ, lập kế hoạch dự án, xác định yêu cầu hệ thống, hoặc tạo tài liệu phân tích domain.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---
# Skill: Phân Tích Domain cho Business Analyst

## 🎯 Mục đích

Skill này là **Trợ lý Domain cho BA**, được thiết kế để đồng hành cùng Business Analyst trong quá trình tìm hiểu, phân tích và khám phá toàn diện bất kỳ domain hoặc subdomain nào.

**Đặc điểm:**
- ✅ Không cố định vào lĩnh vực cụ thể
- ✅ Linh hoạt thích ứng theo domain đang phân tích
- ✅ Quy trình có cấu trúc 8 bước rõ ràng
- ✅ Tạo file .md chi tiết làm tài liệu output
- ✅ Làm việc tuần tự từng bước, cập nhật dần vào file
- ✅ Hỏi user xác nhận trước khi chuyển sang bước tiếp theo

---

## 📋 Quy trình 8 bước

### **Bước 0: Tổng quan Domain**
- Giới thiệu tổng quan domain/subdomain
- Liệt kê 10-20 thuật ngữ quan trọng (dạng bảng)
- Danh sách phần mềm quản lý vận hành (nếu xây full hệ thống)
- Hỏi user: đã có phần mềm hay đang vận hành thủ công?

### **Bước 1: Business Model Canvas**
Phân tích 9 yếu tố, mapping hệ thống phần mềm cần có:
- **Key Activities** - chi tiết từng hoạt động chính
- **Key Partners** - quy trình phối hợp với đối tác
- **Cost Structure** - công thức tính chi phí chi tiết
- **Revenue Stream** - công thức tính doanh thu chi tiết

### **Bước 2: Lean Canvas**
Phân tích vấn đề, giải pháp, khách hàng, kênh, lợi thế (dạng bảng có cột chức năng phần mềm)

### **Bước 3: Quy trình End-to-End**
Mô tả luồng nghiệp vụ chính, xác định:
- Quy trình cốt lõi
- Thực thể quản lý & thuộc tính
- Chức năng phần mềm cần có

### **Bước 4: Stakeholder & Vai trò**
Xác định các bên liên quan:
- Danh sách stakeholder (mindmap hoặc bảng)
- Công việc chính của từng vai trò
- Mapping phần mềm hỗ trợ

### **Bước 5: Phân tích sâu quy trình cụ thể**
Chọn 1 quy trình để phân tích chi tiết:
- Các bước chi tiết
- Input/Output
- Quy tắc nghiệp vụ, ngoại lệ, công thức
- Mapping sang cách phần mềm vận hành

### **Bước 6: Ứng dụng & Chức năng**
Xác định hệ thống phần mềm cần có:
- Các module chính
- Giao diện
- Chức năng cốt lõi (dạng bảng tiếng Việt)

### **Bước 7: ERD (Entity Relationship Diagram)**
- Liệt kê thực thể quan trọng
- Vẽ sơ đồ ERD (code mermaid)

### **Bước 8: Phân tích đối thủ & thị trường**
- Sản phẩm đối thủ (đặc biệt ở Việt Nam)
- Tính năng nổi bật
- Xu hướng công nghệ

---

## 🚀 Cách sử dụng Skill

### **Bước 1: Khởi động**
User gọi skill và cung cấp:
- Tên domain/subdomain muốn phân tích
- Tên file .md output (ví dụ: `banking-domain-analysis.md`)
- Vị trí lưu file (mặc định: thư mục hiện tại)

### **Bước 2: Tạo template**
Skill tự động tạo file .md với cấu trúc 8 mục (0-8) trống

### **Bước 3: Phân tích tuần tự**
Với mỗi bước (0 → 8):
1. **Phân tích & tạo nội dung** cho bước đó
2. **Cập nhật vào đúng mục** trong file .md
3. **Hiển thị kết quả** cho user xem
4. **Hỏi user xác nhận** trước khi chuyển bước tiếp theo

### **Bước 4: Hoàn thành**
Sau 8 bước:
1. File .md hoàn chỉnh với đầy đủ nội dung phân tích
2. **Hỏi user có muốn export sang Word (.docx) không**
3. Nếu có, chạy script Python: `python .claude/skills/ba-domain-analysis/scripts/convert_to_word.py <file>.md`
4. Thông báo đường dẫn file Word đã tạo

---

## 📝 Nguyên tắc làm việc

### ✅ BẮT BUỘC:
1. **Làm tuần tự từng bước** (0 → 1 → 2 → ... → 8)
2. **Cập nhật file .md sau mỗi bước** hoàn thành
3. **Hỏi user xác nhận** trước khi chuyển bước tiếp
4. **Không bỏ qua bước nào**
5. **Output chi tiết, đầy đủ** theo yêu cầu từng bước
6. **Sử dụng bảng** khi liệt kê thông tin
7. **Sử dụng mermaid** cho biểu đồ, mindmap, ERD
8. **Sau khi hoàn thành bước 8**, hỏi user có muốn export sang Word không

### ❌ KHÔNG ĐƯỢC:
1. ❌ Làm tất cả 8 bước một lúc
2. ❌ Chuyển bước khi chưa hỏi user
3. ❌ Output ngắn gọn, thiếu chi tiết
4. ❌ Bỏ qua việc cập nhật file .md

---

## 💡 Trigger Skill

Skill được kích hoạt khi user nói:
- "Phân tích domain [tên domain]"
- "Tìm hiểu domain [tên domain]"
- "Tôi muốn tìm hiểu về [domain]"
- "Giúp tôi phân tích nghiệp vụ [domain]"
- "Tạo tài liệu phân tích cho [domain]"
- "Chạy /ba-domain-analysis"

---

## 📂 Chi tiết từng bước

### [Bước 0: Tổng quan](stages/stage-0-overview.md)
- Giới thiệu domain
- Bảng thuật ngữ (10-20 thuật ngữ)
- Danh sách phần mềm quản lý

### [Bước 1: Business Model Canvas](stages/stage-1-business-canvas.md)
- 9 yếu tố Business Model Canvas
- Chi tiết Key Activities, Key Partners, Cost Structure, Revenue Stream
- Mapping phần mềm cho từng yếu tố

### [Bước 2: Lean Canvas](stages/stage-2-lean-canvas.md)
- Bảng Lean Canvas 9 mục
- Cột chức năng phần mềm cần có

### [Bước 3: Quy trình E2E](stages/stage-3-end-to-end.md)
- Sơ đồ quy trình tổng quan
- Thực thể & thuộc tính
- Chức năng phần mềm

### [Bước 4: Stakeholder](stages/stage-4-stakeholders.md)
- Mindmap/bảng stakeholder
- Công việc & mapping phần mềm

### [Bước 5: Deep Dive](stages/stage-5-deep-dive.md)
- Phân tích chi tiết 1 quy trình
- Input/Output, quy tắc nghiệp vụ
- Mapping phần mềm

### [Bước 6: Ứng dụng](stages/stage-6-applications.md)
- Module, giao diện
- Bảng chức năng chi tiết

### [Bước 7: ERD](stages/stage-7-erd.md)
- Liệt kê thực thể
- Sơ đồ ERD mermaid

### [Bước 8: Đối thủ](stages/stage-8-competitors.md)
- Phân tích đối thủ
- Tính năng & xu hướng

---

## 🔧 Template & Script

- **[Template file .md](templates/domain-analysis-template.md)** - Cấu trúc file output
- **Script tạo file** - Tự động tạo template với tên domain

---

## 📄 Export sang Word

### **Tự động export sau khi hoàn thành**
Sau khi hoàn thành 8 bước phân tích, skill sẽ:
1. **Hỏi user** có muốn export sang Word không
2. **Chạy script Python** để convert
3. **Lệnh**: `python scripts/convert_to_word.py <tên-file>.md`
4. **Thông báo** đường dẫn file Word đã tạo

### **Script Python đi kèm**
Skill có sẵn script `scripts/convert_to_word.py` để convert markdown sang Word:

```bash
# Tự động tạo tên file output
python scripts/convert_to_word.py domain-analysis.md
# => Tạo file: domain-analysis.docx

# Hoặc chỉ định tên output
python scripts/convert_to_word.py domain-analysis.md my-output.docx
```

### **Tính năng script**
- ✅ Tự động cài thư viện `python-docx` nếu chưa có
- ✅ Hỗ trợ tiêu đề (H1, H2, H3, H4)
- ✅ Hỗ trợ bảng markdown
- ✅ Hỗ trợ danh sách (bullet & numbered)
- ✅ Hỗ trợ định dạng: **bold**, *italic*, `code`
- ✅ Font chuyên nghiệp: Times New Roman 12pt
- ✅ Bỏ qua mermaid diagram (có thể thêm ảnh sau)

### **Yêu cầu hệ thống**
- **Python 3** đã cài đặt
- Thư viện `python-docx` (script tự cài nếu chưa có)

### **Lợi ích**
- ✅ Dễ chia sẻ với stakeholder không dùng markdown
- ✅ Định dạng chuyên nghiệp
- ✅ Dễ in ấn và lưu trữ
- ✅ Tương thích với Microsoft Word, Google Docs
- ✅ Không cần cài pandoc

---

## 📌 Lưu ý quan trọng

### AI hỗ trợ
Trong mỗi phần, bạn có thể bổ sung:
- Giải pháp kinh doanh thay đổi thế nào khi có AI
- AI hỗ trợ được những gì

### Phong cách
- **Có hệ thống, tư duy logic, rõ ràng**
- **Hướng dẫn từng bước**
- **Đặt câu hỏi định hướng** khi thông tin chưa rõ

### Định dạng
- Bảng: markdown table
- Biểu đồ: mermaid code block
- Danh sách: bullet points
- Công thức: chi tiết tới tham số nhỏ nhất

---

## 🎯 Ví dụ sử dụng

```
User: "Tôi muốn tìm hiểu domain Banking - Ngân hàng số"

Claude: Tuyệt vời! Tôi sẽ giúp bạn phân tích domain Banking - Ngân hàng số
theo quy trình 8 bước có cấu trúc.

Trước tiên, cho tôi xin thông tin:
- Tên file .md bạn muốn tạo? (ví dụ: banking-domain-analysis.md)
- Lưu ở đâu? (mặc định: thư mục hiện tại)

[User cung cấp thông tin]

Claude: Đã tạo file banking-domain-analysis.md với template 8 mục.

**Bước 0: Tổng quan Domain Banking**

[Tạo nội dung chi tiết về Banking, bảng thuật ngữ, danh sách phần mềm]
[Cập nhật vào file .md]

✅ Đã hoàn thành Bước 0 và cập nhật vào file.

Bạn có muốn tiếp tục sang Bước 1: Business Model Canvas không?

[... Tiếp tục các bước 1-8 ...]

Claude: ✅ Đã hoàn thành tất cả 8 bước phân tích!

File banking-domain-analysis.md đã hoàn chỉnh với đầy đủ nội dung.

Bạn có muốn export file này sang định dạng Word (.docx) không?
```

---

## 📊 Output mẫu

File .md được tạo sẽ có cấu trúc:

```markdown
# Phân Tích Domain: [Tên Domain]

## 0. Tổng quan Domain
[Nội dung được cập nhật ở bước 0]

## 1. Business Model Canvas
[Nội dung được cập nhật ở bước 1]

## 2. Lean Canvas
[Nội dung được cập nhật ở bước 2]

## 3. Quy trình End-to-End
[Nội dung được cập nhật ở bước 3]

## 4. Stakeholder & Vai trò
[Nội dung được cập nhật ở bước 4]

## 5. Phân tích sâu quy trình
[Nội dung được cập nhật ở bước 5]

## 6. Ứng dụng & Chức năng
[Nội dung được cập nhật ở bước 6]

## 7. ERD (Entity Relationship Diagram)
[Nội dung được cập nhật ở bước 7]

## 8. Phân tích đối thủ & thị trường
[Nội dung được cập nhật ở bước 8]
```

**File Word output:**
```
[Tên Domain]-domain-analysis.docx
- Định dạng Word chuyên nghiệp
- Giữ nguyên cấu trúc markdown
- Hỗ trợ bảng, hình ảnh, sơ đồ
- Sẵn sàng để chia sẻ và in ấn
```

---

## ✨ Tính năng đặc biệt

### Progressive Disclosure
- Skill không tải toàn bộ hướng dẫn chi tiết vào context
- Chỉ đọc file stage chi tiết khi cần
- Giảm thiểu token usage

### Tùy biến
- Có thể bỏ qua bước nào đó theo yêu cầu user
- Có thể quay lại bước trước để chỉnh sửa
- Có thể làm sâu hơn cho bước cụ thể

### Tích hợp AI insights
- Mỗi bước có thể thêm phần "AI hỗ trợ như thế nào"
- Gợi ý cách AI thay đổi business model
- Xu hướng công nghệ AI trong domain

### Export sang Word
- Tự động hỏi export sau khi hoàn thành
- Sử dụng pandoc để convert
- Tạo file .docx định dạng chuyên nghiệp
- Dễ chia sẻ với stakeholder không dùng markdown

---

## 🎓 Best Practices

1. **Chuẩn bị trước:**
   - Tìm hiểu sơ bộ về domain
   - Chuẩn bị câu hỏi cụ thể
   - Xác định phạm vi phân tích

2. **Trong quá trình:**
   - Đọc kỹ output mỗi bước
   - Đặt câu hỏi khi chưa rõ
   - Yêu cầu làm sâu hơn nếu cần

3. **Sau khi hoàn thành:**
   - Review toàn bộ file .md
   - Bổ sung thông tin từ domain expert
   - Export sang Word để dễ chia sẻ
   - Chia sẻ với team để feedback

---

## 🔄 Version

**Version:** 1.1.0
**Ngày cập nhật:** 2025-12-31
**Tác giả:** BA Team
**Mục đích:** Chuẩn hóa quy trình phân tích domain cho team BA

### Changelog
- **v1.1.0** (2025-12-31): Thêm tính năng export sang Word (.docx) sau khi hoàn thành phân tích
- **v1.0.0** (2025-12-31): Phiên bản đầu tiên với 8 bước phân tích domain