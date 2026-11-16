from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Users\Kim Duc\Desktop\Dự án và tính năng\worktmp\rendered_report_v4")
OUT = ROOT / "contact_sheets"
OUT.mkdir(exist_ok=True)

pages = sorted(ROOT.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[1]))
font = ImageFont.load_default(size=24)

for sheet_index in range(0, len(pages), 4):
    batch = pages[sheet_index:sheet_index + 4]
    opened = [Image.open(p).convert("RGB") for p in batch]
    tile_w = max(im.width for im in opened)
    tile_h = max(im.height for im in opened) + 42
    canvas = Image.new("RGB", (tile_w * 2 + 30, tile_h * 2 + 30), "#D9E1E8")
    draw = ImageDraw.Draw(canvas)
    for i, (path, im) in enumerate(zip(batch, opened)):
        x = (i % 2) * (tile_w + 30)
        y = (i // 2) * (tile_h + 30)
        canvas.paste(im, (x, y + 42))
        page_no = int(path.stem.split("-")[1])
        draw.rectangle((x, y, x + tile_w, y + 41), fill="#0B2545")
        draw.text((x + 14, y + 8), f"TRANG {page_no}", fill="white", font=font)
    first = int(batch[0].stem.split("-")[1])
    last = int(batch[-1].stem.split("-")[1])
    canvas.save(OUT / f"sheet-{first:02d}-{last:02d}.png", optimize=True)

print(f"Created {len(list(OUT.glob('sheet-*.png')))} contact sheets for {len(pages)} pages")
