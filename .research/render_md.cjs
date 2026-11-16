const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const modules='C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules';
const {chromium}=require(path.join(modules,'playwright'));
const base=path.resolve(__dirname,'..');
(async()=>{
const {marked}=await import(pathToFileURL(path.join(modules,'marked/lib/marked.esm.js')).href);
const browser=await chromium.launch({headless:true,channel:'chrome'});
const page=await browser.newPage({viewport:{width:1440,height:1000}});
const results=[];
for(const [index,name] of ['Đức BA training AI, ML models.md','Đức PO làm dự án VinDynamics.md'].entries()){
const md=fs.readFileSync(path.join(base,name),'utf8');
let html=marked.parse(md).replace(/(src|href)="(C:\/[^\"]+)"/g,(_,attr,p)=>attr+'="'+pathToFileURL(decodeURIComponent(p)).href+'"');
const out=path.join(__dirname,name+'.html');
fs.writeFileSync(out,'<!doctype html><html lang="vi"><meta charset="utf-8"><style>body{font:17px/1.65 Arial;color:#1f2937;max-width:1180px;margin:50px auto;padding:0 32px}h1{font-size:36px}h2{margin-top:56px;color:#123156}h3{margin-top:32px}table{border-collapse:collapse;width:100%;font-size:15px}th,td{border:1px solid #d1d5db;padding:10px;text-align:left;vertical-align:top}th{background:#eff6ff}img{max-width:100%;height:auto}pre{background:#f1f5f9;padding:20px;overflow:auto}blockquote{border-left:4px solid #3b82f6;padding:12px 22px;background:#f8fafc}a{color:#155eab}code{font-size:14px}</style>'+html+'</html>');
await page.goto(pathToFileURL(out).href);await page.waitForLoadState('load');
const quality=await page.evaluate(()=>({images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.naturalWidth})),tables:document.querySelectorAll('table').length,overflow:document.documentElement.scrollWidth>innerWidth}));
await page.screenshot({path:path.join(__dirname,'md-'+index+'-top.png')});
await page.locator('img').first().scrollIntoViewIfNeeded();
await page.screenshot({path:path.join(__dirname,'md-'+index+'-diagram.png')});
results.push({name,...quality});
}
// Diagram thumbnails for a single visual audit of all exported pages.
const imageFiles=fs.readdirSync(path.join(base,'Sơ đồ kiến trúc')).filter(x=>/^\d\d-/.test(x)&&!x.startsWith('00-')&&x.endsWith('.png'));
const gallery='<html><style>body{margin:20px;background:#e2e8f0;display:grid;grid-template-columns:1fr 1fr;gap:20px}img{width:100%;background:white}</style>'+imageFiles.map(n=>'<img src="'+pathToFileURL(path.join(base,'Sơ đồ kiến trúc',n)).href+'">').join('')+'</html>';
const galleryPath=path.join(__dirname,'diagram-gallery.html');fs.writeFileSync(galleryPath,gallery);
await page.setViewportSize({width:1800,height:1000});await page.goto(pathToFileURL(galleryPath).href);await page.waitForLoadState('load');await page.screenshot({path:path.join(__dirname,'diagram-gallery.png'),fullPage:true});
fs.writeFileSync(path.join(__dirname,'render-verification.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify(results));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
