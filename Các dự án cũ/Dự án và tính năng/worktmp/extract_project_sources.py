from __future__ import annotations

import json
import sys
from pathlib import Path

from docx import Document
from pypdf import PdfReader


TEXT_EXTENSIONS = {".txt", ".md", ".svg"}


def extract_docx(path: Path) -> dict:
    doc = Document(path)
    parts: list[str] = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:
            parts.append(text)
    for table_index, table in enumerate(doc.tables, start=1):
        parts.append(f"[TABLE {table_index}]")
        for row in table.rows:
            values = [cell.text.replace("\n", " | ").strip() for cell in row.cells]
            parts.append("\t".join(values))
    for section_index, section in enumerate(doc.sections, start=1):
        for label, container in (("HEADER", section.header), ("FOOTER", section.footer)):
            values = [p.text.strip() for p in container.paragraphs if p.text.strip()]
            if values:
                parts.append(f"[{label} {section_index}] " + " | ".join(values))
    return {
        "kind": "docx",
        "paragraphs": len(doc.paragraphs),
        "tables": len(doc.tables),
        "text": "\n".join(parts),
    }


def extract_pdf(path: Path) -> dict:
    reader = PdfReader(path)
    pages: list[dict] = []
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # preserve auditability of partial failures
            text = f"[EXTRACTION ERROR: {type(exc).__name__}: {exc}]"
        pages.append({"page": index, "text": text})
    return {
        "kind": "pdf",
        "pages": len(reader.pages),
        "text": "\n\n".join(f"[PAGE {p['page']}]\n{p['text']}" for p in pages),
    }


def extract_text(path: Path) -> dict:
    return {"kind": path.suffix.lower().lstrip("."), "text": path.read_text(encoding="utf-8", errors="replace")}


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: extract_project_sources.py <workspace> <output.json>")
    workspace = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    records: list[dict] = []
    for path in sorted(p for p in workspace.rglob("*") if p.is_file()):
        suffix = path.suffix.lower()
        if suffix not in {".docx", ".pdf", *TEXT_EXTENSIONS}:
            continue
        try:
            if suffix == ".docx":
                data = extract_docx(path)
            elif suffix == ".pdf":
                data = extract_pdf(path)
            else:
                data = extract_text(path)
            records.append({"path": str(path), "relative_path": str(path.relative_to(workspace)), **data})
        except Exception as exc:
            records.append({
                "path": str(path),
                "relative_path": str(path.relative_to(workspace)),
                "kind": suffix.lstrip("."),
                "error": f"{type(exc).__name__}: {exc}",
                "text": "",
            })
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "workspace": str(workspace),
        "output": str(output),
        "records": len(records),
        "errors": [r["relative_path"] for r in records if "error" in r],
        "characters": sum(len(r.get("text", "")) for r in records),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
