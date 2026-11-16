from pathlib import Path
import re,json,xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'Sơ đồ kiến trúc'
report={'markdown':[],'diagrams':[],'errors':[]}
for filename in ['Đức BA training AI, ML models.md','Đức PO làm dự án VinDynamics.md']:
    p=BASE/filename;s=p.read_text(encoding='utf-8')
    links=re.findall(r'\]\(<([^>]+)>\)',s)
    missing=[x for x in links if not x.startswith('http') and not Path(x).exists()]
    headings=re.findall(r'^## (.+)$',s,re.M)
    images=re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)',s)
    report['markdown'].append({'file':filename,'bytes':p.stat().st_size,'words':len(s.split()),'headings':len(headings),'images':len(images),'missing_links':missing,'code_fences':s.count('```')})
    if missing:report['errors']+=missing
    if '{{ROOT}}' in s or '\ufffd' in s or '\x00' in s:report['errors'].append('Unresolved/invalid content: '+filename)
    if s.count('```')%2:report['errors'].append('Unbalanced fence: '+filename)
combined=ET.Element('mxfile',{'host':'app.diagrams.net','version':'32.6.10'})
for p in sorted(OUT.glob('*.drawio')):
    if p.name.startswith('00-'):continue
    root=ET.parse(p).getroot()
    model=root if root.tag=='mxGraphModel' else root.find('.//mxGraphModel')
    cells=model.findall('./root/mxCell');ids=[c.get('id') for c in cells]
    if len(ids)!=len(set(ids)):report['errors'].append('Duplicate IDs '+p.name)
    for c in cells:
        if c.get('edge')=='1':
            if c.find('mxGeometry') is None or c.get('source') not in ids or c.get('target') not in ids:report['errors'].append('Invalid edge '+p.name)
    d=ET.SubElement(combined,'diagram',{'id':p.stem,'name':p.stem});d.append(model)
    report['diagrams'].append({'file':p.name,'nodes':sum(c.get('vertex')=='1' for c in cells),'edges':sum(c.get('edge')=='1' for c in cells),'png':Path(str(p)+'.png').exists(),'svg':Path(str(p)+'.svg').exists()})
(OUT/'00-all-architectures.drawio').write_text(ET.tostring(combined,encoding='unicode'),encoding='utf-8')
readme=['# Sơ đồ kiến trúc — bộ chuẩn bị phỏng vấn VinDynamics','',
'10 sơ đồ tham chiếu. Các phương án công nghệ không phải xác nhận kiến trúc nội bộ của các doanh nghiệp.','',
f'[Mở toàn bộ 10 trang trong một file draw.io](<{(OUT/"00-all-architectures.drawio").as_posix()}>)','',
'| Sơ đồ | Editable | Ảnh PNG | Vector SVG |','|---|---|---|---|']
for d in report['diagrams']:
    p=OUT/d['file'];title=p.stem
    readme.append(f'| {title} | [.drawio](<{p.as_posix()}>) | [PNG](<{p.as_posix()}.png>) | [SVG](<{p.as_posix()}.svg>) |')
readme+=['','PNG và SVG được xuất bằng draw.io Desktop với XML nhúng. Có thể mở ảnh bằng draw.io để chỉnh sửa. Bộ nguồn cũng có các tệp `.drawio` riêng.','',
'Các connector đã được xử lý bằng drawio MCP. File đa trang dùng cùng nội dung với các ảnh; không gồm mã nguồn hoặc dữ liệu nội bộ để triển khai hệ thống.']
(OUT/'README.md').write_text('\n'.join(readme)+'\n',encoding='utf-8')
(BASE/'.research'/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
