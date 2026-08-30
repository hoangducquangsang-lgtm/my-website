"""Read-only image analysis; contact sheets are review aids, not website assets."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT.parent / '1. Raw material/1. Hinh anh/HÌNH ẢNH'
OUT = Path(__file__).resolve().parent
records = []
for path in sorted((RAW / 'GỖ NHAI CÀ PHÊ').iterdir()):
    if path.suffix.lower() not in ('.jpg', '.png', '.jpeg'):
        continue
    if not any(word in path.name for word in ('do_choi', 'thanh_go', 'go_ca_phe', 'go_ ca_phe', 'IMG_', '178')):
        continue
    with Image.open(path) as im:
        records.append({'id':len(records), 'path':str(path), 'size':im.size})
for start in range(0,len(records),30):
    sheet = Image.new('RGB',(1250,1200),'#f0f0ec')
    draw = ImageDraw.Draw(sheet)
    for j,item in enumerate(records[start:start+30]):
        x,y=(j%5)*250,(j//5)*200
        with Image.open(item['path']) as im:
            thumb=ImageOps.contain(ImageOps.exif_transpose(im).convert('RGB'),(240,170))
            sheet.paste(thumb,(x+(250-thumb.width)//2,y))
        draw.text((x+6,y+175),str(item['id']),fill='black')
    sheet.save(OUT/f'raw-candidates-{start//30}.jpg')
(OUT/'raw-candidates.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(records)} raw candidates; {(len(records)+29)//30} contact sheets')
for path in sorted((ROOT/'assets/img').iterdir()):
    with Image.open(path) as im:
        im=im.convert('RGB').resize((80,80))
        dark=sum(max(px)<28 for px in im.getdata())/6400
    if dark>0.20:
        print(path.name, round(dark,3))
