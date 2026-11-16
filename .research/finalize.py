from pathlib import Path
import re, json, xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'Sơ đồ kiến trúc'
fixes={
'02-agent-workflow':([('g','draft'),('audit','fallback')],[('k','draft','căn cứ'),('commit','wf','workflow')]),
'04-smart-safe-vision':([('human','health')],[('gw','health','heartbeat')]),
'06-smart-factory-azure':([('monitor','security'),('security','release'),('release','report')],[('stream','lake','raw'),('deploy','monitor','metrics'),('release','deploy','artifact'),('sql','report','KPI')]),
'08-vinuni-robot-platform':([('workflow','assistant')],[('assistant','mission','tools'),('mission','workflow','policy')])
}
for name,(remove,add) in fixes.items():
    path=OUT/(name+'.drawio'); model=ET.parse(path).getroot();root=model.find('root')
    existing={}
    for c in list(root):
        if c.get('edge')=='1' and (c.get('source'),c.get('target')) in remove:root.remove(c)
        elif c.get('edge')=='1':existing[(c.get('source'),c.get('target'))]=c
    for i,(s,t,label) in enumerate(add):
        if (s,t) in existing:continue
        c=ET.SubElement(root,'mxCell',{'id':'fixedge'+str(i),'value':label,'style':'edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeWidth=1.6;strokeColor=#64748b;fontFamily=Arial;fontSize=13;fontColor=#334155;labelBackgroundColor=#ffffff;','edge':'1','source':s,'target':t,'parent':'1'})
        ET.SubElement(c,'mxGeometry',{'relative':'1','as':'geometry'})
    # The MCP routing pass will compute fresh routes for the modified topology.
    for c in root.findall('mxCell'):
        if c.get('edge')=='1':
            g=c.find('mxGeometry')
            for child in list(g):g.remove(child)
    xml=ET.tostring(model,encoding='unicode');path.write_text(xml,encoding='utf-8')
    (BASE/'.research'/(name+'.xml')).write_text(xml,encoding='utf-8')

for name in ['Đức BA training AI, ML models.md','Đức PO làm dự án VinDynamics.md']:
    path=BASE/name;s=path.read_text(encoding='utf-8').replace('{{ROOT}}',BASE.as_posix())
    if '## Mục lục' not in s:
        headers=re.findall(r'^## (.+)$',s,re.M)
        def slug(t):
            return re.sub(r'[^\w\- ]','',t.lower()).replace(' ','-')
        toc='## Mục lục\n\n'+'\n'.join(f'- [{h}](#{slug(h)})' for h in headers)+'\n\n'
        pos=s.index('\n## ')+1;s=s[:pos]+toc+s[pos:]
    path.write_text(s,encoding='utf-8')
print('Updated references, contents, and diagram topology.')
