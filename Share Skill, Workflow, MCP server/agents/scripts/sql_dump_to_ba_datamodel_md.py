"""Parse MySQL dump (CREATE TABLE) -> BA Data Model markdown. No network."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def parse_tables(text: str) -> dict[str, list[tuple[str, str]]]:
    tables: dict[str, list[tuple[str, str]]] = {}
    for m in re.finditer(
        r"CREATE TABLE `([^`]+)`\s*(\(.*?\))\s*ENGINE\s*=",
        text,
        re.DOTALL | re.IGNORECASE,
    ):
        name, inner = m.group(1), m.group(2)
        cols: list[tuple[str, str]] = []
        for raw in inner.split("\n"):
            line = raw.strip().rstrip(",")
            if not line or line in ("(", ")"):
                continue
            if line.startswith(
                ("PRIMARY KEY", "UNIQUE ", "KEY ", "INDEX ", "CONSTRAINT ", "FULLTEXT ")
            ):
                continue
            cm = re.match(r"`([^`]+)`\s+(.+)", line)
            if cm:
                cols.append((cm.group(1), cm.group(2).strip()))
        tables[name] = cols
    return tables


def domain_of(table: str) -> str:
    t = table.lower()
    if t.startswith("__") or t == "system_config" or t == "job_configs":
        return "Kỹ thuật & cấu hình"
    if t.startswith("cat_") or t in ("topic", "sharing_type"):
        return "Danh mục & CMS meta"
    if t in ("courses", "classrooms") or t.startswith("classrooms_copy"):
        return "Khóa học & lớp"
    if "course_" in t or t in ("videos",):
        return "Nội dung khóa học"
    if t in ("users", "user_logs", "students", "old_student"):
        return "Người dùng & học viên"
    if t in ("registers", "reserve", "promotions", "promotion_users"):
        return "Đăng ký & khuyến mãi"
    if t in ("bank_statement", "sepay_transactions", "files"):
        return "Thanh toán & file"
    if "homework" in t:
        return "Bài tập"
    if t.startswith("test_") or t in ("test_objects",):
        return "Kiểm tra (test)"
    if t.startswith("quiz_"):
        return "Quiz sự kiện"
    if t in ("post", "post_courses", "comment"):
        return "Bài viết & bình luận"
    if t in (
        "email_logs",
        "notification_emails",
        "logSendEmailRegister",
        "share_docs",
    ):
        return "Email & chia sẻ"
    if t in ("surveys", "case_studies"):
        return "Khảo sát & case study"
    return "Khác"


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: sql_dump_to_ba_datamodel_md.py <input.sql> <output.md>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    text = src.read_text(encoding="utf-8")
    tables = parse_tables(text)
    if not tables:
        print("No CREATE TABLE found.", file=sys.stderr)
        return 1

    lines: list[str] = []
    lines.append("Version: 1.0.0")
    lines.append("Author: M2MBA")
    lines.append("Last Updated: 2026-04-12")
    lines.append(
        "Description: Data model AS-IS — schema MySQL `course` (trích từ export SQL), Trung tâm M2MBA"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# Data model AS-IS — schema `course` (M2MBA)")
    lines.append("")
    lines.append("## 1. Change Log")
    lines.append("")
    lines.append("| Version | Ngày | Nội dung |")
    lines.append("|---------|------|----------|")
    lines.append("| 1.0.0 | 2026-04-12 | Khởi tạo từ export SQL (cấu trúc bảng/cột); quan hệ logic suy từ tên cột + FK khai báo trong DB |")
    lines.append("")
    lines.append("## 2. Nguồn & phạm vi")
    lines.append("")
    lines.append(
        "- **Nguồn cấu trúc:** file SQL dump (Navicat / MySQL 8.x) do stakeholder cung cấp — **không** lưu bản dump chứa host DB, mật khẩu hay trigger nhạy cảm trong repo."
    )
    lines.append(
        "- **Phạm vi:** chỉ mô tả **vật lý AS-IS** (tên bảng, cột, kiểu trong dump); không thay thế tài liệu logical rebuild (`ba-data-model.md`)."
    )
    lines.append(
        "- **FK trong DB:** chỉ bảng `comment` có `FOREIGN KEY` rõ ràng (`user_id` → `users`, `post_id` → `post.uuid`); các quan hệ khác là **logic** (ứng dụng enforce)."
    )
    lines.append("")
    lines.append("## 3. Danh sách bảng theo miền")
    lines.append("")
    lines.append("| Miền | Bảng |")
    lines.append("|------|------|")

    by_dom: dict[str, list[str]] = {}
    for t in sorted(tables.keys()):
        d = domain_of(t)
        by_dom.setdefault(d, []).append(t)
    for d in sorted(by_dom.keys()):
        names = ", ".join(f"`{x}`" for x in sorted(by_dom[d]))
        lines.append(f"| {d} | {names} |")

    lines.append("")
    lines.append("## 4. Đối tượng DB bổ sung (view / procedure / trigger)")
    lines.append("")
    lines.append("| Loại | Tên | Ghi chú |")
    lines.append("|------|-----|--------|")
    lines.append("| VIEW | `register_by_day` | Gom `registers` theo ngày + `status` |")
    lines.append("| VIEW | `revenue` | Doanh thu theo ngày duyệt (`approved_at`) |")
    lines.append("| VIEW | `successRegister` | Lọc `registers.status = 'SUCCESS'` |")
    lines.append("| PROCEDURE | `InsertStudent` | Đồng bộ `students` từ `registers` (trừ CANCEL/WAIT_PAYMENT/RESERVE) |")
    lines.append("| PROCEDURE | `InsertReserve` | Đồng bộ `students` cho trạng thái RESERVE + `reserve` |")
    lines.append("| TRIGGER | `migrateData` | Sau INSERT `old_student` — migrate legacy (chi tiết SQL: xem dump gốc; có logic nhạy cảm) |")
    lines.append("")
    lines.append("## 5. Sơ đồ quan hệ logic (Mermaid — một phần)")
    lines.append("")
    lines.append("> Các cạnh sau phản ánh **quan hệ nghiệp vụ thường gặp** từ tên khóa `*_id`; không phải tất cả FK đều khai báo trong MySQL.")
    lines.append("")
    lines.append("```mermaid")
    lines.append("erDiagram")
    lines.append("  users ||--o{ registers : places")
    lines.append("  users ||--o{ students : enrolled_as")
    lines.append("  courses ||--o{ classrooms : has")
    lines.append("  courses ||--o{ registers : for_course")
    lines.append("  classrooms ||--o{ registers : for_class")
    lines.append("  registers ||--o| students : spawns")
    lines.append("  courses ||--o{ course_contents : contains")
    lines.append("  courses ||--o{ homeworks : assigns")
    lines.append("  homeworks ||--o{ homework_classrooms : per_class")
    lines.append("  homeworks ||--o{ homework_answers : submissions")
    lines.append("  users ||--o{ homework_answers : submits")
    lines.append("```")
    lines.append("")
    lines.append("## 6. Data dictionary — cột theo bảng")
    lines.append("")

    for tname in sorted(tables.keys()):
        lines.append(f"### `{tname}`")
        lines.append("")
        lines.append("| Cột | Kiểu / định nghĩa (theo dump) |")
        lines.append("|-----|--------------------------------|")
        for cname, typ in tables[tname]:
            typ_esc = typ.replace("|", "\\|")
            lines.append(f"| `{cname}` | {typ_esc} |")
        lines.append("")

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(tables)} tables to {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
