---
name: ba-mockup-prompt-gen-detail
description: "Sinh **một file .md** (`prompt-mh-detail_*.md`): user **copy toàn bộ** dán vào AI gen UI. Nội dung prompt **chỉ nhu cầu nghiệp vụ + dữ liệu (ERD)** — **không** màu, font, spacing, layout style ép buộc, tên component UI, states visual, WCAG, Brand Guideline trong file. **Đầu ra mong muốn của tool: chỉ vùng nội dung MH chi tiết** — không menu điều hướng, sidebar/top bar app, chrome điều hướng ngoài MH (mô tả bắt buộc trong prompt). **Công cụ AI tự quyết** bố cục trong vùng MH. Đầu vào: ERD/data, danh sách MH, `[AI_TOOL]`."
---

# SKILL: BA MOCKUP PROMPT — MH CHI TIẾT

**Version:** 1.8.0 | **Author:** M2MBA | **Updated:** 2026-04-13

**Một dòng cho agent:** File `.md` = prompt **chỉ nhu cầu + data**; **bắt buộc** nêu rõ **Đối tượng**, **Chiến lược**, **User Flow (Mermaid)** và **Các Section cốt lõi** để AI tool gen UI phù hợp; **cấm** mọi **design style ép buộc** (HEX, font, size); **mọi MH phải có User Flow** để user chốt logic.

**Phân biệt:** **`ba-feature-detail-prompt-gen`** — một chức năng / một MH focus, cùng tinh thần “chỉ chức năng + data”. Skill **này** — **nhiều MH** trong **cùng một file** `.md`, vẫn **không** ép design style trong prompt; **bắt buộc** phạm vi đầu ra chỉ nội dung MH (không app shell).

---

## INPUT BẮT BUỘC

Trước khi làm, xác nhận đủ **3** mục sau. Thiếu → DỪNG, hỏi bổ sung:

1. **Tên Ứng dụng** cần thiết kế (vd: Web Học viên, Mobile App, Web Admin).
2. **ERD hoặc mô tả data** của các màn hình mục tiêu.
3. **AI design tool** (vd: Stitch, v0, Figma Make) → lưu vào `[AI_TOOL]`.

**Tuỳ chọn (Danh sách màn hình):**
- Nếu User cung cấp: Làm theo danh sách đó.
- Nếu User **KHÔNG** cung cấp: Agent **bắt buộc** thực hiện **Bước 1 (Audit & Selection)** để đề xuất batch ~5 màn hình dựa trên bảng Tracking.

**Không tự bịa field từ ERD.**

**Cấm:** Đưa **Brand Guideline**, **design system**, **màu/HEX/font/spacing**, **chỉ định pattern bố cục/visual** để ép style (vd. “card grid 3 cột”, “bento layout”), **chỉ định component** (Button Primary, DataGrid…) vào prompt — kể cả khi user có file guideline (agent **không** copy guideline vào file `.md`).

**Bắt buộc (phạm vi đầu ra cho tool):** Trong **mỗi** MH, prompt phải nêu rõ công cụ **chỉ** tạo **nội dung màn hình chi tiết** (vùng chức năng của MH); **không** tạo menu điều hướng, sidebar app, top bar toàn ứng dụng, header shell hay bất kỳ chrome điều hướng nào **ngoài phạm vi MH**. Đặt ở mục *Mục đích & nhu cầu* (bullet **Phạm vi đầu ra**) và nhắc lại ngắn ở *Giao cho công cụ [AI_TOOL]*.

---

## OUTPUT

**Định dạng:** **một file Markdown** (`.md`) duy nhất.

**Đường dẫn:** `docs-BA/Prototype/Prompt/prompt-mh-detail_[tên-app]_[YYYYMMDD].md`. Tạo thư mục `docs-BA/Prototype/Prompt/` nếu chưa có.

**Cách dùng:** User **copy toàn bộ nội dung** file → dán vào `[AI_TOOL]`. Không tách prompt sang báo cáo khác; không thêm meta BA ngoài nhu cầu + data.

**Nội dung:** Append từng MH theo template; auto-continue giữa các MH. Log nội bộ `✅ Đã gen MH` **không** ghi vào file `.md` nếu làm lẫn prompt.

---

## TEMPLATE MỖI MÀN HÌNH

Chỉ dùng các mục dưới đây — **không** thêm section Colors, Spacing, Contrast, Components kiểu design.

### HƯỚNG DẪN SKILL: BA UI MOCKUP PROMPT GENERATOR (DETAIL)

## 🎯 Mục đích
Tạo prompt chi tiết cho AI (như Stitch, v0, Figma Make) để gen màn hình giao diện dựa trên nghiệp vụ. Skill này ưu tiên tính hệ thống, đảm bảo các màn hình được gen theo luồng người dùng (User Flow) và được quản trị qua bảng Tracking.

## 📋 Tài liệu tham chiếu
1. **Planning Master**: `docs-BA/ba-development-tracking.md` (Dùng để chọn UC tiếp theo).
2. **User Flow Master**: `docs-BA/PRD/ba-product-overview.md`.
3. **Data Model**: `docs-BA/PRD/ba-data-model.md`.

## 🚀 Quy trình thực hiện (Chế độ Chiến lược)

### Bước 1: Lựa chọn Module/Chặng đường (Audit & Selection)
- Đọc `ba-development-tracking.md` để xác định các UC của ứng dụng mục tiêu (ví dụ: Web Học viên) đang ở trạng thái `🔴 Todo`.
- Đề xuất một cụm **~5 màn hình** liên quan chặt chẽ để tạo thành một User Flow hoàn chỉnh.
- **Dừng và hỏi xác nhận từ User** trước khi tiến hành gen prompt.

### Bước 2: Phân tích luồng (User Flow) cho cụm màn hình
- Với mỗi màn hình trong cụm, vẽ **Mermaid User Flow** để minh họa các tương tác chính và trạng thái chuyển đổi.
- Xác định mục tiêu chiến lược và đối tượng người dùng (Persona) cho từng màn.

### Bước 3: Sinh Prompt Chi tiết
- Tạo file `prompt-mh-detail_[tên-app]_[tên-mh]_[ngày].md`.
- **Nội dung bắt buộc**:
    1. **Target Audience & Goals**: Thiết kế cho ai? Mục tiêu là gì?
    2. **User Flow (Mermaid)**: Luồng tương tác của màn hình này.
    3. **Core Sections**: Danh sách các vùng chức năng (không bao gồm Header/Sidebar của App Shell).
    4. **Data Context**: Tham chiếu trường dữ liệu từ Data Model.

### Bước 4: Cập nhật Tiến độ
- Sau khi tạo file prompt, quay lại cập nhật file `ba-development-tracking.md`:
    - Chuyển `UI Prompt` sang `🟢 Done`.
    - Chèn link file vào cột `Prompt File`.

## ⚠️ Quy tắc quan trọng
1. **Atomic Screen**: Chỉ mô tả nội dung bên trong màn hình (Main Content area), không lặp lại phần khung (App Shell).
2. **Vietnamese Only**: Toàn bộ nhãn và mô tả UI dùng tiếng Việt.
3. **Traceability**: Mỗi màn hình phải ứng với ít nhất một UC ID trong bảng tracking.

```markdown
### MH [N]: [Tên Màn Hình]

#### Mục tiêu & Chiến lược
- **Đối tượng:** [Ai là người dùng chính của màn hình này? VD: Khách vãng lai, Học viên, Admin]
- **Mục tiêu:** [Hành động hoặc kết quả nghiệp vụ quan trọng nhất trang này hướng tới. VD: Chuyển đổi, Xây dựng niềm tin, Tăng thời gian on-site]
- **Chiến lược UI:** [Định hướng cách bố cục thông tin để đạt mục tiêu. VD: Bố cục dạng Sales Page dài, Tối ưu khoảng trắng cho trải nghiệm đọc]

#### User Flow (Quy trình người dùng)
```mermaid
graph TD
    [Bước 1] --> [Bước 2]
    ...
```

#### Các Section/Thành phần cốt lõi (Bắt buộc thiết kế)
1.  [Section 1]: [Mô tả ngắn chức năng/data hiển thị]
2.  [Section 2]: ...
3.  [Section 3]: ...

#### Phạm vi đầu ra (bắt buộc)
- Chỉ thiết kế **nội dung MH chi tiết** (vùng chức năng của màn này). **Không** bao gồm menu điều hướng, sidebar app, top bar toàn app, header shell ứng dụng hay khung layout bao ngoài chỉ để điều hướng giữa các module.

#### Phạm vi dữ liệu (từ ERD)
| Field | Kiểu / mô tả | PK/FK | Ràng buộc (nullable, enum, format nghiệp vụ) |
|---|---|---|---|
| … | … | … | … |

#### Quan hệ dữ liệu (nếu có)
- [Entity A] ↔ [Entity B]: [1-N / N-N / FK …] — **chỉ sự kiện dữ liệu**, không gợi ý control UI

#### Luồng hành vi mong muốn (nghiệp vụ, không mô tả UI)
| Bước / sự kiện | Kết quả nghiệp vụ mong đợi |
|---|---|
| … | … |

#### Giao cho công cụ [AI_TOOL]
Thiết kế giao diện màn hình **[Tên MH]** cho ứng dụng **[Tên app]** đáp ứng **mục đích & nhu cầu** và **dữ liệu** trên. **Chỉ xuất ra nội dung màn hình chi tiết** (khu vực chức năng của MH này); **không** tạo menu điều hướng, sidebar, top bar toàn app hay bất kỳ chrome điều hướng nào ngoài phạm vi MH. **Không có ràng buộc design style khác trong prompt này** — bạn tự chọn bố cục nội dung trong vùng MH, thành phần giao diện, màu sắc và trạng thái tương tác phù hợp.
```

---

## KIỂU DỮ LIỆU ERD (tham chiếu nội bộ cho agent — **không** chép bảng “Component UI” vào prompt)

Agent map type → **chỉ ghi kiểu trong cột Field** (string, number, datetime, FK→X, 1-N…). **Không** ghi “dùng Date picker”, “dùng Table” trong file đầu ra.

---

## CHECKLIST (sau khi gen xong)

- [ ] **Một file `.md`**; copy full → AI gen UI
- [ ] **Không** có mục: màu, HEX, font, px spacing, WCAG, layout style ép buộc, tên component Material/Ant, states hover/active, Brand Guideline
- [ ] **Có** đủ: nhu cần nghiệp vụ, **phạm vi đầu ra** (chỉ nội dung MH — không app shell/menu/sidebar/top bar toàn app), bảng field từ ERD, luồng hành vi nghiệp vụ (nếu cần)
- [ ] Field lấy đúng ERD — không bịa
- [ ] `[AI_TOOL]` điền tên thật
- [ ] Không placeholder `[…]` sót (trừ user chấp nhận)

---

## QUY TẮC THỰC THI

1. **Bắt buộc:** ERD/data, danh sách MH, `[AI_TOOL]`. Prompt **chỉ nhu cầu + data** — **công cụ AI tự xử lý** design **trong vùng nội dung MH**.
2. **Bắt buộc (Ngữ cảnh chiến lược):** Mỗi MH phải nêu rõ **Đối tượng người dùng**, **Chiến lược UI**, **User Flow (vẽ bằng Mermaid)** và danh sách **Các Section cốt lõi** để AI tool có đủ dữ kiện để gen ảnh phù hợp và user dễ dàng chốt logic nghiệp vụ.
3. **Bắt buộc (phạm vi mockup):** Mỗi MH phải yêu cầu tool **chỉ** gen **nội dung MH chi tiết**; **không** tạo menu điều hướng, sidebar app, top bar toàn app, header shell hay chrome điều hướng ngoài MH (ghi ở *Luồng hành vi* hoặc *Giao cho công cụ*).
4. **Cấm** cung cấp **design style ép buộc** trong prompt: màu, typography, spacing số, contrast, mô tả pattern layout/visual để ép style, bảng component + states, map ERD→tên component UI. *(Không nhầm với mục “không app shell” — đó là **phạm vi đầu ra**, không phải chỉ định visual.)*
5. **Không** đọc/nhúng **Brand Guideline** / **DS** vào file `.md` (có thể dùng nội bộ để hiểu domain — **không** đưa vào prompt).
6. Reference ERD thực tế — không tự bịa field.
7. Sinh từng MH, append, auto-continue.
8. File đầu ra là **nội dung prompt duy nhất** cho tool; không thêm file “hướng dẫn copy” song song trừ khi user yêu cầu.
