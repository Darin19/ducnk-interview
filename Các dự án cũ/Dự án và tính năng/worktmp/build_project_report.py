from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(r"C:\Users\Kim Duc\Desktop\Dự án và tính năng")
SOURCE = ROOT / "worktmp" / "report_content.md"
OUTPUT = ROOT / "Danh_muc_tinh_nang_va_7_cong_viec_BA_Viettel_Samsung.docx"

NAVY = "0B2545"
BLUE = "2E74B5"
DARK_BLUE = "1F4D78"
TEAL = "2A7F8E"
TEXT = "222222"
MID_GRAY = "6B7280"
LIGHT_BLUE = "E8EEF5"
PALE_BLUE = "F4F7FA"
RULE = "C9D5E3"


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=100, start=120, bottom=100, end=120) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_table_borders(table, color=RULE, size="6") -> None:
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = borders.find(qn(f"w:{edge}"))
        if el is None:
            el = OxmlElement(f"w:{edge}")
            borders.append(el)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), size)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)


def set_repeat_heading(paragraph, keep_next=True) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    if keep_next:
        keep = OxmlElement("w:keepNext")
        p_pr.append(keep)
    keep_lines = OxmlElement("w:keepLines")
    p_pr.append(keep_lines)


def set_paragraph_shading(paragraph, fill: str) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    p_pr.append(shd)


def set_paragraph_border(paragraph, side: str, color: str, size: str = "14", space: str = "6") -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn("w:pBdr"))
    if p_bdr is None:
        p_bdr = OxmlElement("w:pBdr")
        p_pr.append(p_bdr)
    edge = OxmlElement(f"w:{side}")
    edge.set(qn("w:val"), "single")
    edge.set(qn("w:sz"), size)
    edge.set(qn("w:space"), space)
    edge.set(qn("w:color"), color)
    p_bdr.append(edge)


def add_page_field(paragraph) -> None:
    paragraph.add_run("Trang ")
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    paragraph._p.append(fld)


def set_run_font(run, name="Calibri", size=None, color=None, bold=None, italic=None) -> None:
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    if size is not None:
        run.font.size = Pt(size)
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


INLINE_RE = re.compile(r"(\*\*.+?\*\*|`.+?`|\*[^*]+?\*)")


def add_inline(paragraph, text: str) -> None:
    pos = 0
    for match in INLINE_RE.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos:match.start()])
            set_run_font(run)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_run_font(run, bold=True)
        elif token.startswith("`"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, name="Consolas", size=9.5, color=DARK_BLUE)
            shd = OxmlElement("w:shd")
            shd.set(qn("w:fill"), "EEF3F8")
            run._r.get_or_add_rPr().append(shd)
        else:
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, italic=True)
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        set_run_font(run)


def create_numbering(document: Document):
    numbering = document.part.numbering_part.element

    def next_id(tag: str, attr: str) -> int:
        values = []
        for node in numbering.findall(qn(tag)):
            raw = node.get(qn(attr))
            if raw and raw.isdigit():
                values.append(int(raw))
        return max(values, default=0) + 1

    abstract_id = next_id("w:abstractNum", "w:abstractNumId")
    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    multi = OxmlElement("w:multiLevelType")
    multi.set(qn("w:val"), "multilevel")
    abstract.append(multi)
    for level in range(3):
        lvl = OxmlElement("w:lvl")
        lvl.set(qn("w:ilvl"), str(level))
        start = OxmlElement("w:start")
        start.set(qn("w:val"), "1")
        num_fmt = OxmlElement("w:numFmt")
        num_fmt.set(qn("w:val"), "decimal")
        lvl_text = OxmlElement("w:lvlText")
        lvl_text.set(qn("w:val"), f"%{level + 1}.")
        suff = OxmlElement("w:suff")
        suff.set(qn("w:val"), "space")
        p_pr = OxmlElement("w:pPr")
        tabs = OxmlElement("w:tabs")
        tab = OxmlElement("w:tab")
        tab.set(qn("w:val"), "num")
        tab.set(qn("w:pos"), str(540 + level * 360))
        tabs.append(tab)
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), str(540 + level * 360))
        ind.set(qn("w:hanging"), "270")
        p_pr.extend([tabs, ind])
        lvl.extend([start, num_fmt, lvl_text, suff, p_pr])
        abstract.append(lvl)
    numbering.append(abstract)

    bullet_abs_id = abstract_id + 1
    bullet_abs = OxmlElement("w:abstractNum")
    bullet_abs.set(qn("w:abstractNumId"), str(bullet_abs_id))
    multi2 = OxmlElement("w:multiLevelType")
    multi2.set(qn("w:val"), "multilevel")
    bullet_abs.append(multi2)
    glyphs = ["•", "–", "◦"]
    for level, glyph in enumerate(glyphs):
        lvl = OxmlElement("w:lvl")
        lvl.set(qn("w:ilvl"), str(level))
        start = OxmlElement("w:start")
        start.set(qn("w:val"), "1")
        num_fmt = OxmlElement("w:numFmt")
        num_fmt.set(qn("w:val"), "bullet")
        lvl_text = OxmlElement("w:lvlText")
        lvl_text.set(qn("w:val"), glyph)
        p_pr = OxmlElement("w:pPr")
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), str(540 + level * 360))
        ind.set(qn("w:hanging"), "270")
        p_pr.append(ind)
        r_pr = OxmlElement("w:rPr")
        fonts = OxmlElement("w:rFonts")
        fonts.set(qn("w:ascii"), "Calibri")
        fonts.set(qn("w:hAnsi"), "Calibri")
        r_pr.append(fonts)
        lvl.extend([start, num_fmt, lvl_text, p_pr, r_pr])
        bullet_abs.append(lvl)
    numbering.append(bullet_abs)

    def new_num(abs_id: int) -> int:
        num_id = next_id("w:num", "w:numId")
        num = OxmlElement("w:num")
        num.set(qn("w:numId"), str(num_id))
        abstract_ref = OxmlElement("w:abstractNumId")
        abstract_ref.set(qn("w:val"), str(abs_id))
        num.append(abstract_ref)
        lvl_override = OxmlElement("w:lvlOverride")
        lvl_override.set(qn("w:ilvl"), "0")
        start_override = OxmlElement("w:startOverride")
        start_override.set(qn("w:val"), "1")
        lvl_override.append(start_override)
        num.append(lvl_override)
        numbering.append(num)
        return num_id

    bullet_num_id = new_num(bullet_abs_id)
    return abstract_id, bullet_num_id, new_num


def apply_num(paragraph, num_id: int, level: int = 0) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    num_pr = p_pr.find(qn("w:numPr"))
    if num_pr is None:
        num_pr = OxmlElement("w:numPr")
        p_pr.insert(0, num_pr)
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), str(level))
    num = OxmlElement("w:numId")
    num.set(qn("w:val"), str(num_id))
    num_pr.extend([ilvl, num])


def configure_styles(document: Document) -> None:
    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = "Calibri"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor.from_string(TEXT)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25
    normal.paragraph_format.widow_control = True

    for name, size, color, before, after in (
        ("Heading 1", 16, BLUE, 18, 10),
        ("Heading 2", 13, BLUE, 14, 7),
        ("Heading 3", 12, DARK_BLUE, 10, 5),
    ):
        style = styles[name]
        style.font.name = "Calibri"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.keep_together = True

    title = styles["Title"]
    title.font.name = "Calibri"
    title._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    title.font.size = Pt(25)
    title.font.bold = True
    title.font.color.rgb = RGBColor.from_string(NAVY)
    title.paragraph_format.space_after = Pt(14)

    subtitle = styles["Subtitle"]
    subtitle.font.name = "Calibri"
    subtitle._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    subtitle.font.size = Pt(13)
    subtitle.font.color.rgb = RGBColor.from_string(DARK_BLUE)
    subtitle.paragraph_format.space_after = Pt(8)

    quote = styles["Quote"]
    quote.font.name = "Calibri"
    quote._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    quote.font.size = Pt(10.5)
    quote.font.color.rgb = RGBColor.from_string(DARK_BLUE)
    quote.paragraph_format.left_indent = Inches(0.15)
    quote.paragraph_format.right_indent = Inches(0.12)
    quote.paragraph_format.space_before = Pt(5)
    quote.paragraph_format.space_after = Pt(8)
    quote.paragraph_format.line_spacing = 1.2


def add_title_page(document: Document, title: str, subtitle: str, meta: str) -> None:
    for _ in range(4):
        p = document.add_paragraph()
        p.paragraph_format.space_after = Pt(4)

    kicker = document.add_paragraph()
    kicker.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = kicker.add_run("HỒ SƠ NĂNG LỰC BUSINESS ANALYSIS")
    set_run_font(run, size=9.5, color=TEAL, bold=True)
    kicker.paragraph_format.space_after = Pt(10)
    set_paragraph_border(kicker, "bottom", TEAL, size="16", space="8")

    p = document.add_paragraph(style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.add_run(title)

    p = document.add_paragraph(style="Subtitle")
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.add_run(subtitle)

    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(meta)
    set_run_font(r, size=10.5, color=MID_GRAY)
    p.paragraph_format.space_after = Pt(22)

    table = document.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    widths = [Inches(2.10), Inches(2.10), Inches(2.10)]
    items = [
        ("08", "Dự án"),
        ("56", "Đầu việc BA"),
        ("03", "Module Smart Factory"),
    ]
    for cell, width, (value, label) in zip(table.rows[0].cells, widths, items):
        cell.width = width
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(cell, PALE_BLUE)
        set_cell_margins(cell, top=150, bottom=150, start=140, end=140)
        p1 = cell.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(value)
        set_run_font(r1, size=19, color=BLUE, bold=True)
        p2 = cell.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(label)
        set_run_font(r2, size=9.5, color=MID_GRAY, bold=True)
    set_table_borders(table, color="D5DFEA", size="6")

    p = document.add_paragraph()
    p.paragraph_format.space_before = Pt(24)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("Trọng tâm nội dung")
    set_run_font(r, size=10, color=MID_GRAY, bold=True)

    bullets = [
        "Full feature map theo nhóm nghiệp vụ và luồng end-to-end.",
        "Kiến trúc/công nghệ phân biệt rõ đã xác nhận và đề xuất.",
        "Bảy đầu việc BA có đầu ra đặc thù cho từng dự án.",
        "Equipment Management được đào sâu; Payroll được rút gọn.",
    ]
    for item in bullets:
        p = document.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.22)
        p.paragraph_format.first_line_indent = Inches(-0.16)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run("•  ")
        set_run_font(r, color=TEAL, bold=True)
        add_inline(p, item)

    document.add_page_break()


def parse_metadata(lines: list[str]) -> tuple[dict[str, str], list[str]]:
    meta = {}
    body = []
    for line in lines:
        if line.startswith("@title "):
            meta["title"] = line[len("@title "):].strip()
        elif line.startswith("@subtitle "):
            meta["subtitle"] = line[len("@subtitle "):].strip()
        elif line.startswith("@meta "):
            meta["meta"] = line[len("@meta "):].strip()
        else:
            body.append(line)
    return meta, body


def build() -> None:
    raw = SOURCE.read_text(encoding="utf-8")
    lines = raw.splitlines()
    meta, lines = parse_metadata(lines)

    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)
    section.different_first_page_header_footer = True

    configure_styles(document)
    number_abs_id, bullet_num_id, new_num = create_numbering(document)

    # Header/footer kept intentionally minimal.
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    hr = hp.add_run("VIETTEL & SAMSUNG  |  DANH MỤC TÍNH NĂNG VÀ ĐẦU VIỆC BA")
    set_run_font(hr, size=8, color=MID_GRAY, bold=True)
    set_paragraph_border(hp, "bottom", RULE, size="6", space="4")

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    set_run_font(fp.add_run("Tài liệu tổng hợp  •  "), size=8, color=MID_GRAY)
    add_page_field(fp)
    for run in fp.runs:
        set_run_font(run, size=8, color=MID_GRAY)

    add_title_page(
        document,
        meta.get("title", "DANH MỤC TÍNH NĂNG HỆ THỐNG"),
        meta.get("subtitle", "Viettel & Samsung"),
        meta.get("meta", "Tổng hợp từ tài liệu dự án"),
    )

    current_num_id = None
    last_was_numbered = False
    last_h1 = None
    current_h2 = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            last_was_numbered = False
            continue
        if stripped == "@pagebreak":
            # Project headings control their own page breaks. Ignoring the
            # marker avoids a blank page when the marker itself is pushed to
            # the next page by preceding content.
            last_was_numbered = False
            continue

        heading_match = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            p = document.add_paragraph(style=f"Heading {level}")
            add_inline(p, text)
            set_repeat_heading(p)
            if level == 1:
                last_h1 = text
                set_paragraph_border(p, "bottom", RULE, size="8", space="4")
                current_h2 = None
                if re.match(r"^\d+\.\s", text):
                    p.paragraph_format.page_break_before = True
            elif level == 2:
                current_h2 = text
                if text == "Nguồn chính":
                    p.paragraph_format.space_before = Pt(8)
                    p.paragraph_format.space_after = Pt(4)
            last_was_numbered = False
            continue

        if stripped.startswith("> "):
            p = document.add_paragraph(style="Quote")
            add_inline(p, stripped[2:])
            set_paragraph_shading(p, PALE_BLUE)
            set_paragraph_border(p, "left", TEAL, size="20", space="6")
            last_was_numbered = False
            continue

        bullet_match = re.match(r"^(\s*)-\s+(.+)$", line)
        if bullet_match:
            level = min(len(bullet_match.group(1)) // 2, 2)
            p = document.add_paragraph()
            apply_num(p, bullet_num_id, level)
            if current_h2 == "Nguồn chính":
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.1
            else:
                p.paragraph_format.space_after = Pt(4)
                p.paragraph_format.line_spacing = 1.25
            add_inline(p, bullet_match.group(2))
            last_was_numbered = False
            continue

        num_match = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
        if num_match:
            if not last_was_numbered or current_num_id is None:
                current_num_id = new_num(number_abs_id)
            level = min(len(num_match.group(1)) // 2, 2)
            p = document.add_paragraph()
            apply_num(p, current_num_id, level)
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.line_spacing = 1.25
            add_inline(p, num_match.group(2))
            last_was_numbered = True
            continue

        p = document.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.25
        add_inline(p, stripped)
        last_was_numbered = False

    # Core properties.
    props = document.core_properties
    props.title = "Danh mục tính năng hệ thống và 7 đầu việc BA — Viettel & Samsung"
    props.subject = "Tổng hợp Smart Safe, HRAI, mChat, CRM, OCR & RPA, AI Hub, Smart Factory và Samsung Payroll"
    props.author = "Tổng hợp từ tài liệu dự án"
    props.keywords = "Business Analyst, Viettel, Samsung, Smart Factory, AI Hub, CRM, OCR, RPA"

    # Document-level language and compatibility settings.
    settings = document.settings.element
    lang = settings.find(qn("w:themeFontLang"))
    if lang is None:
        lang = OxmlElement("w:themeFontLang")
        settings.append(lang)
    lang.set(qn("w:val"), "vi-VN")
    lang.set(qn("w:eastAsia"), "vi-VN")

    document.save(OUTPUT)

    # Structural QA at source level.
    ba_sections = re.findall(
        r"^## 7 đầu việc BA[^\n]*\n(.*?)(?=^## |^# |^@pagebreak|\Z)",
        raw,
        flags=re.MULTILINE | re.DOTALL,
    )
    counts = [len(re.findall(r"^\d+\.\s", block, flags=re.MULTILINE)) for block in ba_sections]
    if len(ba_sections) != 8 or counts != [7] * 8:
        raise RuntimeError(f"BA section QA failed: sections={len(ba_sections)}, counts={counts}")
    if "6a712749" not in raw or "SMAS" not in raw:
        raise RuntimeError("Payroll link disposition is missing")
    print(f"Created: {OUTPUT.name}")
    print(f"Source characters: {len(raw):,}")
    print(f"BA sections: {len(ba_sections)} | counts={counts}")


if __name__ == "__main__":
    build()
