from pathlib import Path
import xml.etree.ElementTree as ET
import json

BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'Sơ đồ kiến trúc';OUT.mkdir(exist_ok=True)
COLORS=[('#eff6ff','#2563eb'),('#ecfdf5','#059669'),('#fff7ed','#ea580c'),('#f5f3ff','#7c3aed')]
manifest=[]

def make(name,title,subtitle,rows,edges):
    model=ET.Element('mxGraphModel',{'dx':'1400','dy':'1000','grid':'1','gridSize':'10','guides':'1','tooltips':'1','connect':'1','arrows':'1','fold':'1','page':'0','pageScale':'1','pageWidth':'1400','pageHeight':'1100','math':'0','shadow':'0','background':'#ffffff','adaptiveColors':'none'})
    root=ET.SubElement(model,'root'); ET.SubElement(root,'mxCell',id='0'); ET.SubElement(root,'mxCell',id='1',parent='0')
    def node(id,label,x,y,w,h,style,parent='1'):
        c=ET.SubElement(root,'mxCell',id=id,value=label,style=style,vertex='1',parent=parent)
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    node('title',title,20,10,1240,48,'text;html=1;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=29;fontStyle=1;fontColor=#0f172a;')
    node('subtitle',subtitle,20,66,1240,42,'text;html=1;align=left;verticalAlign=middle;fontFamily=Arial;fontSize=16;fontColor=#475569;whiteSpace=wrap;')
    parents={}
    for ri,(rowname,items) in enumerate(rows):
        fill,stroke=COLORS[ri%len(COLORS)]; lane=f'lane{ri}'
        node(lane,rowname,20,130+ri*205,1240,175,f'swimlane;startSize=35;html=1;horizontal=1;rounded=1;arcSize=6;fontFamily=Arial;fontSize=17;fontStyle=1;align=left;spacingLeft=14;fillColor={fill};swimlaneFillColor=#ffffff;strokeColor={stroke};fontColor=#0f172a;')
        for ci,item in enumerate(items):
            ident,heading,detail=item;parents[ident]=lane
            label=f'<b>{heading}</b><br><font style="font-size:15px">{detail}</font>'
            node(ident,label,25+ci*305,62,270,88,f'rounded=1;arcSize=10;whiteSpace=wrap;html=1;fontFamily=Arial;fontSize=18;fontColor=#0f172a;fillColor={fill};strokeColor={stroke};strokeWidth=1.4;spacing=10;align=center;verticalAlign=middle;',lane)
    for i,edge in enumerate(edges):
        src,tgt,*rest=edge; label=rest[0] if rest else ''; dashed=len(rest)>1 and rest[1]
        parent=parents[src] if parents.get(src)==parents.get(tgt) else '1'
        style='edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;endArrow=block;endFill=1;strokeWidth=1.6;strokeColor=#64748b;fontFamily=Arial;fontSize=13;fontColor=#334155;labelBackgroundColor=#ffffff;'
        if dashed:style+='dashed=1;'
        cell=ET.SubElement(root,'mxCell',id=f'e{i}',value=label,style=style,edge='1',source=src,target=tgt,parent=parent)
        ET.SubElement(cell,'mxGeometry',relative='1',attrib={'as':'geometry'})
    node('footer','THIẾT KẾ THAM CHIẾU • BA / QC interview study • 16.11.2026 • Chi tiết, giả định và giới hạn trong hai tài liệu Markdown.',20,145+len(rows)*205,1240,36,'text;html=1;align=left;fontFamily=Arial;fontSize=13;fontColor=#64748b;')
    mx=ET.Element('mxfile',host='app.diagrams.net',version='29.0.0');d=ET.SubElement(mx,'diagram',id=name,name=title);d.append(model)
    ET.indent(mx)
    path=OUT/(name+'.drawio');path.write_text(ET.tostring(mx,encoding='unicode'),encoding='utf-8')
    (BASE/'.research'/(name+'.xml')).write_text(ET.tostring(model,encoding='unicode'),encoding='utf-8')
    manifest.append({'name':name,'title':title,'path':str(path),'nodes':sum(len(x[1]) for x in rows),'edges':len(edges)})

make('01-knowledge-rag','01 / Hệ tri thức và RAG có phân quyền','Tài liệu có nguồn, phiên bản, hiệu lực và ACL; câu trả lời luôn gắn với bằng chứng.',[
('A. Ingestion / xuất bản tri thức',[
('source','Tài liệu được duyệt','PDF / SOP / FAQ<br>MinIO + metadata PostgreSQL'),('parse','Extract & normalize','Tika / PaddleOCR<br>Giữ trang, bảng, heading'),('curate','QA & chia đoạn','Owner duyệt • chunk version<br>Hiệu lực + tenant + quyền'),('index','Hybrid index','OpenSearch BM25 + Qdrant<br>bge-m3 embeddings')]),
('B. Truy vấn / trả lời',[
('user','Web / Chat UI','React + SSE<br>Câu hỏi và ngữ cảnh'),('auth','Identity & context','Keycloak + FastAPI<br>Role / site / mốc hiệu lực'),('retrieve','Retrieve & rerank','ACL filter → hybrid search<br>bge-reranker-v2-m3'),('answer','LLM + kiểm tra','Qwen / vLLM → schema<br>Nguồn • hỏi lại • fallback')]),
('C. Quản trị / chất lượng',[
('gold','Golden questions','Câu đúng / không đáp án<br>Role, thời gian, tình huống khó'),('eval','Evaluation runner','Retrieval + answer + leakage<br>SME review và regression'),('release','Versioned release','Corpus / prompt / model<br>Approval và rollback'),('trace','Audit & monitoring','OpenTelemetry / Langfuse<br>Trace đã mask dữ liệu')])
],[('source','parse'),('parse','curate'),('curate','index'),('user','auth'),('auth','retrieve'),('index','retrieve','index'),('retrieve','answer'),('gold','eval'),('eval','release'),('release','trace'),('answer','trace','trace')])

make('02-agent-workflow','02 / AI Copilot: tri thức, công cụ và workflow','LLM đề xuất; backend kiểm tra quyền và trạng thái; thay đổi dữ liệu cần quy trình xác nhận.',[
('A. Hiểu yêu cầu và lấy căn cứ',[
('u','Người dùng / UI','Câu hỏi + screen/case ID'),('a','Xác thực & context','OIDC • scope • state version'),('g','LangGraph','Intent → read tools / RAG'),('k','Nguồn kiểm chứng','KB có nguồn + API nghiệp vụ')]),
('B. Đề xuất → xác nhận → thực thi',[
('draft','Đề xuất có cấu trúc','Action / input / evidence<br>Hỏi lại nếu thiếu dữ kiện'),('policy','Policy validation','OPA + business rules<br>allowed-actions từ backend'),('confirm','Người dùng duyệt','Preview • expected version<br>Không tự xác nhận thay người'),('commit','Tool / API commit','Recheck quyền + version<br>Idempotency / result check')]),
('C. Nghiệp vụ dài hạn và truy vết',[
('wf','Camunda workflow','Human task / SLA / retry<br>Quy trình có version'),('db','PostgreSQL / outbox','State và event nhất quán'),('audit','Audit / trace','Actor • action • nguồn<br>Tool result và phiên bản'),('fallback','Fallback / hỗ trợ','Denied • stale • timeout<br>Không có nguồn → chuyển người')])
],[('u','a'),('a','g'),('g','k'),('g','draft'),('draft','policy'),('policy','confirm'),('confirm','commit'),('commit','db'),('wf','db'),('db','audit'),('audit','fallback'),('commit','fallback','lỗi')])

make('03-ai-training-feedback','03 / Dữ liệu → training → đánh giá → cải tiến','Feedback được sửa thành ground truth trước khi tái sử dụng; test set giữ độc lập.',[
('A. Chuẩn bị dữ liệu',[
('s','Nguồn có quyền dùng','HR / hội thoại / ảnh / tài liệu'),('snap','Snapshot bất biến','SQL / pandas / data checks<br>Schema • cutoff • provenance'),('label','Label & adjudicate','Label Studio / CVAT<br>Guideline • expert review'),('split','Dataset version','DVC + object storage<br>Train / validation / test')]),
('B. Candidate và quality gate',[
('train','Train / fine-tune','XGBoost hoặc PyTorch<br>Transformers / PEFT LoRA'),('registry','Tracking & artifacts','MLflow<br>Code / config / dataset / model'),('evaluation','Đánh giá độc lập','Task metric + error slices<br>Business rules + latency'),('approve','Phê duyệt release','So baseline / risk / regression<br>Không đạt → sửa nguyên nhân')]),
('C. Vận hành và feedback',[
('deploy','Deploy có kiểm soát','Shadow / canary phù hợp<br>Compatibility manifest'),('predict','Prediction & trace','Input snapshot + output<br>Model / prompt / feature'),('review','QA sửa đầu ra','PASS / PARTIAL / FAIL<br>Gold fields + evidence'),('feedback','Gold data vòng sau','Dedupe / quyền / split<br>Không dùng test set để train')])
],[('s','snap'),('snap','label'),('label','split'),('split','train'),('train','registry'),('registry','evaluation'),('evaluation','approve'),('approve','deploy'),('deploy','predict'),('predict','review'),('review','feedback')])

make('04-smart-safe-vision','04 / Smart Safe: AI Camera và sự cố IoT','Camera phát hiện tín hiệu; rule và người vận hành xác minh; cloud không thay cơ chế an toàn thiết bị.',[
('A. Thiết bị và edge',[
('cam','Camera / cảm biến','RTSP video • door/PIR/smoke<br>Site / device / timestamp'),('edge','Edge inference','GStreamer → YOLOX<br>ByteTrack • ONNX/TensorRT'),('rule','Zone & time rules','Polygon / lịch / dwell<br>Model + config version'),('gw','IoT Gateway','MQTT TLS / EMQX<br>Buffer • heartbeat • event ID')]),
('B. Event và lưu trữ',[
('ingest','Event ingestion','Validate / dedupe / ordering'),('incident','Incident service','Spring Boot + RabbitMQ<br>Correlate sensor + camera'),('store','Dữ liệu & bằng chứng','PostgreSQL / TimescaleDB<br>MinIO event clips'),('ui','Dashboard & notify','React / map / SMS / email<br>Site scope + event timeline')]),
('C. Vận hành và đánh giá',[
('human','Bảo vệ xác minh','Acknowledge / assign<br>Resolve / close / reopen'),('health','Device health','Online ≠ healthy<br>Freshness / fault / recovery'),('data','Dataset camera','CVAT • chia theo site/time<br>Đêm / chói / che khuất'),('qa','Nghiệm thu event','Precision / recall<br>False alarms/camera-hour')])
],[('cam','edge'),('edge','rule'),('rule','gw'),('gw','ingest'),('ingest','incident'),('incident','store'),('store','ui'),('ui','human'),('human','health'),('data','qa')])

make('05-document-ai-rpa','05 / Document AI → review → RPA','Output OCR/VLM là dữ liệu ứng viên; chỉ cho phép thực thi khi qua validation và quyền.',[
('A. Nhận và đọc chứng từ',[
('upload','Upload / connector','Invoice / contract / BL<br>Quarantine + ClamAV'),('raw','Raw & job','MinIO + RabbitMQ<br>Hash / version / job ID'),('ocr','OCR + layout','OpenCV → PaddleOCR<br>PP-Structure • bảng / trang'),('vlm','VLM khi cần','Qwen2.5-VL<br>Layout khó / vùng chưa rõ')]),
('B. Chuẩn hóa và kiểm chứng',[
('extract','Field extraction','Value + page / bounding box<br>Model / extractor version'),('validate','Schema & rules','Pydantic • currency/date<br>Tổng dòng • cross-document'),('review','Human review','Critical field / conflict<br>Sửa gold và ghi lý do'),('approved','Approved data','Bản dữ liệu đã duyệt<br>Mapping sang hệ thống đích')]),
('C. Tự động hóa và đối soát',[
('rpa','API / UiPath RPA','Credentials qua vault<br>Checkpoint + idempotency'),('erp','ERP / QLHĐ','Tạo bản nháp / giao dịch<br>Theo quyền nghiệp vụ'),('recon','Reconciliation','SQL / reference ID<br>Không ghi trùng sau timeout'),('metrics','Quality & feedback','Field exact match • review rate<br>Trace → dataset vòng sau')])
],[('upload','raw'),('raw','ocr'),('ocr','vlm'),('ocr','extract'),('vlm','extract','fallback'),('extract','validate'),('validate','review'),('review','approved'),('approved','rpa'),('rpa','erp'),('erp','recon'),('recon','metrics')])

make('06-smart-factory-azure','06 / Smart Factory + Machine Learning trên Azure','Giải pháp mở rộng đề xuất: bảo trì dự đoán và phát hiện lỗi ngoại quan; không phải stack Samsung đã xác nhận.',[
('A. OT và edge / điều khiển giữ tại nhà máy',[
('ot','PLC / sensor / camera','OPC UA • Modbus adapter<br>Tag / unit / machine / time'),('gateway','Industrial PC','.NET / Python + Docker<br>SQLite buffer • local inference'),('hub','Azure IoT Hub + DPS','X.509 device identity<br>Desired / reported twin'),('stream','Event Hubs / Stream','IoT routing → Stream Analytics<br>Window / late event / dedupe')]),
('B. Dữ liệu và nghiệp vụ',[
('lake','ADLS Gen2','Raw / curated snapshots<br>Dataset & image provenance'),('adx','Azure Data Explorer','Telemetry / time-series<br>Freshness / anomaly queries'),('sql','Azure SQL / API','Master / work order / QMS<br>ASP.NET + Container Apps'),('erp','ERP integration','API Management / Service Bus<br>Mapping / reconciliation / DLQ')]),
('C. Hai use case ML',[
('feature','Feature & labels','Máy / lot / cutoff / horizon<br>Label từ bảo trì và QMS'),('ml','Azure ML + MLflow','XGBoost: failure risk<br>YOLOX/PatchCore: visual defect'),('deploy','Serving / edge model','Endpoint hoặc ONNX runtime<br>ACR • model/preprocess version'),('decision','Human decision','Kiểm tra bảo trì / chất lượng<br>Không tự điều khiển máy')]),
('D. Vận hành và phát hành',[
('monitor','Monitor / App Insights','Health • trace • alert<br>Latency / backlog / drift'),('security','Entra ID / Key Vault','Role / site / secrets<br>Private endpoints'),('release','Azure DevOps / ACR','Signed artifacts • staged rollout<br>Compatibility / rollback'),('report','Power BI','OEE / downtime / defect<br>ML value và chi phí')])
],[('ot','gateway'),('gateway','hub'),('hub','stream'),('stream','adx'),('adx','sql'),('sql','erp'),('lake','feature'),('feature','ml'),('ml','deploy'),('deploy','decision'),('monitor','security'),('security','release'),('release','report'),('decision','report')])

make('07-ai-data-hub','07 / AI Data Hub: governance và MLOps','Quản trị tài sản AI và workflow; không cần tự có một model dự đoán để là nền tảng AI.',[
('A. Đăng ký và quyền khai thác',[
('catalog','Catalog / asset cards','React • dataset / model<br>Owner / license / sensitivity'),('meta','Metadata & versions','Spring Boot + PostgreSQL<br>MinIO immutable artifacts'),('policy','Permission & policy','Keycloak + OPA<br>Role / scope / lifecycle'),('approval','Approval workflow','Camunda<br>Conditional / parallel / audit')]),
('B. Training và đánh giá',[
('request','Training request','Dataset/model version<br>Code / config / resource quota'),('run','Training job','Kubernetes Job / Argo<br>Queued / running / terminal'),('registry','MLflow registry','Run → model artifact<br>Metric / version / alias'),('eval','Evaluation report','Benchmark version / slices<br>Reviewer / quality gate')]),
('C. Promote và vận hành',[
('promote','Deployment approval','Model + evidence + target<br>Separation of duties'),('serving','KServe / adapter','Compatible deployment bundle<br>Health / rollout / rollback'),('monitor','Monitor / feedback','Model + service metrics<br>Deprecate / archive'),('lineage','Lineage & audit','Dataset → run → model<br>Evaluation → deployment')])
],[('catalog','meta'),('meta','policy'),('policy','approval'),('approval','request'),('request','run'),('run','registry'),('registry','eval'),('eval','promote'),('promote','serving'),('serving','monitor'),('monitor','lineage')])

make('08-vinuni-robot-platform','08 / Đội robot an ninh VinUni: kiến trúc tham chiếu','Case giả định • Mission, AI và workflow không thay bộ điều khiển an toàn cục bộ của robot.',[
('A. Người dùng và nền tảng nghiệp vụ / cloud',[
('ops','Bảo vệ / Operations UI','React • fleet / incidents<br>Human verification'),('mission','Mission & fleet backend','ASP.NET Core + PostgreSQL<br>Schedule / assignment / state'),('workflow','Policy & workflow','OPA + Camunda<br>Industry pack / scope / SLA'),('assistant','AI assistant / KB','LangGraph + RAG + Qwen<br>Tools có kiểm soát')]),
('B. Tích hợp site và dữ liệu',[
('site','Site gateway','Camera/VMS / doors / BMS<br>Adapter • buffer'),('bus','Event / command channel','MQTT TLS / IoT Hub<br>ID / TTL / epoch / ACK'),('cloud','Cloud data services','Blob/ADLS • Service Bus<br>Evidence / audit / registry'),('observ','Monitoring & release','OpenTelemetry / Azure Monitor<br>Manifest / rollout / rollback')]),
('C. Robot runtime / edge',[
('sensor','Sensor & perception','Camera / IMU / LiDAR nếu có<br>YOLOX / tracking / health'),('ros','ROS 2 & robot adapter','Topics / services / actions<br>Freshness / QoS / capability'),('skill','Skill execution','BehaviorTree / navigation<br>Vendor locomotion adapter'),('control','Controller & actuators','Real-time motion / balance<br>Vendor control stack')]),
('D. An toàn, phản hồi và dữ liệu học',[
('safety','Local safety / E-stop','Độc lập với cloud / LLM<br>Giới hạn theo platform'),('feedback','Mission feedback','Goal / progress / result<br>Physical state + evidence'),('data','Robot dataset','Episode / rosbag2 / MCAP<br>Map / robot / policy versions'),('eval','Evaluation & approval','Offline → SIL/HIL → field<br>Safety + quality evidence')])
],[('ops','mission'),('mission','workflow'),('workflow','assistant'),('site','bus'),('bus','cloud'),('cloud','observ'),('mission','bus','mission'),('bus','ros','command'),('sensor','ros'),('ros','skill'),('skill','control'),('safety','control','priority'),('ros','feedback','status'),('feedback','data'),('data','eval')])

make('09-vinuni-mission-flow','09 / Event → mission → evidence → người xác minh','Mỗi ô là một bước có owner và trạng thái; incident và mission có vòng đời riêng.',[
('A. Phát hiện và phân công',[
('event','Camera / sensor event','Validate • dedupe • time/site'),('incident','Incident OPEN','Policy + nguồn bằng chứng<br>Chưa kết luận vi phạm'),('eligible','Fleet eligibility','ODD / capability / health<br>Energy / route / permission'),('assign','Assign & send','Lease / reservation / epoch<br>Command ID + TTL')]),
('B. Robot thực hiện nhiệm vụ',[
('ack','Robot recheck / ACK','Chấp nhận ≠ hoàn tất<br>Reject khi điều kiện thay đổi'),('nav','Navigate / observe','ROS Action + local safety<br>Goal / feedback / cancel'),('evidence','Thu bằng chứng','Clip / location / time<br>Model + map version'),('guard','Bảo vệ xác minh','Đúng / sai / cần hỗ trợ<br>Giữ lịch sử quyết định')]),
('C. Kết quả và ngoại lệ',[
('fallback','Không đủ điều kiện','Không robot / mất mạng / lỗi<br>Chuyển người theo policy'),('unknown','Execution unknown','Không retry/giao trùng mù<br>Kiểm tra robot + quyền lệnh'),('missiondone','Mission terminal','Success / failed / cancelled<br>Result và evidence'),('close','Incident closure','Người có thẩm quyền đóng<br>Audit → feedback → backlog')])
],[('event','incident'),('incident','eligible'),('eligible','assign'),('assign','ack'),('ack','nav'),('nav','evidence'),('evidence','guard'),('eligible','fallback','không đạt'),('ack','unknown','mất phản hồi'),('guard','missiondone'),('missiondone','close')])

make('10-robot-evaluation-release','10 / Data factory và cổng phát hành robot AI','Tăng dần mức tiếp xúc thực tế; thành công trong simulation không tự chứng minh an toàn ngoài hiện trường.',[
('A. Dữ liệu và candidate',[
('task','Task / ODD / rubric','Success • abort • failure<br>BA + Robotics + QC'),('capture','Capture & curate','Episodes / sensor / action<br>Time sync • labels • privacy'),('split','Dataset version / split','Theo site / time / episode<br>Holdout độc lập'),('train','Train candidate','Vision / LLM LoRA / VLA<br>Engineer + tracking')]),
('B. Cổng kiểm chứng',[
('offline','Offline evaluation','Metric theo điều kiện<br>Latency trên target hardware'),('sim','Simulation / SIL','Scenario + fault injection<br>Kiểm tra integration'),('hil','HIL / controlled field','Hardware thật • protocol duyệt<br>Physical outcome evidence'),('signoff','Release decision','QC + Tech Lead + Safety/Ops<br>PO theo thẩm quyền')]),
('C. Rollout và học từ thực địa',[
('manifest','Compatibility manifest','Firmware / model / skill<br>Map / policy / test run'),('rollout','Staged rollout','Lab → một robot → một zone<br>Giám sát và rollback'),('monitor','Field monitoring','Intervention / false alarms<br>Health / drift / task success'),('feedback','Triage & re-validation','Defect / gap / AI limitation<br>Deployment issue → backlog')])
],[('task','capture'),('capture','split'),('split','train'),('train','offline'),('offline','sim'),('sim','hil'),('hil','signoff'),('signoff','manifest'),('manifest','rollout'),('rollout','monitor'),('monitor','feedback')])

(BASE/'.research'/'diagrams.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
