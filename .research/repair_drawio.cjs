const fs=require('fs'),path=require('path');
const dir=path.join(process.cwd(),'Sơ đồ kiến trúc');
for(const file of fs.readdirSync(dir).filter(n=>n.endsWith('.drawio'))){
 const p=path.join(dir,file);let xml=fs.readFileSync(p,'utf8');
 const diagram=xml.match(/<mxfile[\s\S]*?<\/mxfile>|<mxGraphModel[\s\S]*?<\/mxGraphModel>/);
 if(diagram&&xml.trim()!==diagram[0])xml=diagram[0];
 xml=xml.replace(/="([^"]*)"/g,(m,v)=>'="'+v.replace(/</g,'&lt;').replace(/&(?!(?:amp|lt|gt|quot|apos|#[0-9]+|#x[0-9a-fA-F]+);)/g,'&amp;')+'"');
 xml=xml.replace(/<mxCell id="([^"]+)" parent="\1"\s*\/>/g,'<mxCell id="$1" parent="0"/>');
 fs.writeFileSync(p,xml);
}
console.log('Repair pass completed');
