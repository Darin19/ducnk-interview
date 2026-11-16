from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    if len(sys.argv) != 4:
        raise SystemExit("Usage: print_pdf_pages.py <pdf> <start_page> <end_page>")
    path = Path(sys.argv[1])
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    reader = PdfReader(path)
    for page_number in range(start, end + 1):
        print(f"\n===== PAGE {page_number} =====")
        print(reader.pages[page_number - 1].extract_text() or "")


if __name__ == "__main__":
    main()
