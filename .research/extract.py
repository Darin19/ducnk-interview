from pathlib import Path
import json, re, zipfile, hashlib
import xml.etree.ElementTree as ET
from pypdf import PdfReader
from html.parser import HTMLParser
root=Path(__file__).resolve().parent.parent
out=root/'.research'/'texts';out.mkdir(exist_ok=True)
records=[];seen={}
for p in root.rglob('*'):
    if not p.is_file() or any(x in p.parts for x in ['.research','worktmp']):continue
    if p.suffix.lower() not in ['.pdf','.docx','.md','.txt']:continue
    if 'Offer Letter' in p.name or p.name=='Prompt.txt':continue
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest in seen:
        records.append({'path':str(p.relative_to(root)),'duplicate_of':seen[digest]});continue
    text=''
    try:
        if p.suffix=='.pdf':
            r=PdfReader(p);text='\n'.join(f'\n--- PAGE {i+1} ---\n'+(page.extract_text() or '') for i,page in enumerate(r.pages))
        elif p.suffix=='.docx':
            with zipfile.ZipFile(p) as z:
                doc=ET.fromstring(z.read('word/document.xml'))
                ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                text='\n'.join(''.join(t.text or '' for t in para.findall('.//w:t',ns)) for para in doc.findall('.//w:p',ns))
        else:text=p.read_text(encoding='utf-8-sig',errors='replace')
        name=f'{len(seen):03d}-{p.stem}.txt'; (out/name).write_text(text,encoding='utf-8')
        seen[digest]=name;records.append({'path':str(p.relative_to(root)),'text':name,'chars':len(text)})
    except Exception as e:records.append({'path':str(p),'error':str(e)})
(out.parent/'index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
class P(HTMLParser):
    def __init__(self):super().__init__();self.a=[]
    def handle_data(self,d):
        if d.strip():self.a.append(d.strip())
p=P();p.feed((out.parent/'jd.html').read_text(encoding='utf-8'));s='\n'.join(p.a)
(out.parent/'jd.txt').write_text(s,encoding='utf-8')
print(json.dumps([x for x in records if 'text' in x],ensure_ascii=False,indent=2))
