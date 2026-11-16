@title DANH MỤC TÍNH NĂNG HỆ THỐNG
@subtitle 8 dự án Viettel & Samsung — kiến trúc, công nghệ và 7 đầu việc BA nổi bật
@meta Tổng hợp từ toàn bộ tài liệu trong thư mục dự án | Bản tiếng Việt

# Phạm vi và nguyên tắc trình bày

Tài liệu tổng hợp tám hệ thống đã tham gia tại Viettel và Samsung, tập trung vào phạm vi chức năng, luồng nghiệp vụ, kiến trúc, công nghệ và đúng bảy đầu việc BA đặc thù cho từng dự án. Smart Factory được đào sâu ở module Quản lý thiết bị; WMS và Quản lý chất lượng sản xuất đóng vai trò bổ trợ. Samsung Payroll được trình bày ngắn gọn theo mức ưu tiên đã thống nhất.

## Cách đọc mức độ căn cứ

- **Xác nhận từ tài liệu:** nội dung xuất hiện trực tiếp trong CV, SRS, bảng chức năng, báo cáo, sơ đồ, màn hình hoặc tài liệu phỏng vấn tại thư mục dự án.
- **Diễn giải nghiệp vụ:** phân rã chi tiết từ capability đã được xác nhận hoặc từ tài liệu mô tả domain; dùng để giải thích hệ thống đầy đủ hơn, không mặc định rằng từng trường dữ liệu đã chạy production.
- **Kiến trúc logic/đề xuất:** mô hình hợp lý để giải thích cách các khối kết nối; chỉ công nghệ nào có bằng chứng trực tiếp mới được coi là công nghệ đã sử dụng.
- Với CRM, bảng yêu cầu có nhiều trạng thái ký kết/triển khai; danh mục dưới đây phản ánh **inventory yêu cầu**, không đồng nghĩa toàn bộ 420 dòng đều đã production.
- Với OCR & RPA, 25 use case là danh mục **đề xuất/pilot**; không khẳng định tất cả đã được triển khai diện rộng.
- Dữ liệu đăng nhập và thông tin nhạy cảm trong tài liệu nguồn đã được loại khỏi báo cáo.

## Danh mục dự án

- **Viettel:** Smart Safe; HRAI; mChat; CRM; OCR & RPA.
- **Samsung:** AI Hub; Smart Factory; Samsung Payroll.

@pagebreak
# 1. Smart Safe — Nền tảng IoT an toàn và an ninh

## Tổng quan

Smart Safe là nền tảng IoT giám sát cháy, nổ, xâm nhập và tình trạng thiết bị tại mạng lưới điểm bán/tòa nhà. Tài liệu phỏng vấn nêu quy mô khoảng 400 Viettel Store, hơn 5.000 thiết bị và giá trị ước tính khoảng 30 tỷ đồng mỗi năm; các con số này là thông tin tự khai trong hồ sơ dự án. Vai trò đảm nhiệm là BA duy nhất, đồng thời tham gia UI/UX và kiểm thử.

## Danh mục tính năng

### 1. Quản lý site, tòa nhà và phạm vi giám sát

- Quản lý đơn vị, tòa nhà, siêu thị/cửa hàng, khu vực lắp đặt và vị trí thiết bị.
- Hiển thị site và cảnh báo trên Google Maps; xem nhanh thiết bị, vị trí, loại sự cố và trạng thái xử lý.
- Phân công người giám sát theo site; hỗ trợ người dùng phụ trách nhiều điểm, kể cả nhóm có hàng trăm điểm bán.
- Đồng bộ danh mục cửa hàng từ ERP; ghi log và xử lý ngoại lệ khi mã đơn vị, vị trí hoặc phạm vi dữ liệu không hợp lệ.

### 2. Quản lý thiết bị và Gateway

- Khai báo loại thiết bị: Gateway, Fire, Smoke, Door, PIR Motion, Glass Break và AI Camera.
- Onboarding thiết bị theo IMEI, loại, site, vị trí lắp, trạng thái active/inactive, lịch giám sát và người sở hữu vận hành.
- Danh sách, tìm kiếm, phân trang, xem chi tiết, cập nhật, xuất Excel; kiểm tra trùng IMEI và loại bỏ khoảng trắng thừa.
- Theo dõi vòng đời thiết bị, thay thế/di chuyển, ngày kích hoạt và lịch sử thay đổi cấu hình.

### 3. Giám sát thời gian thực

- Nhận heartbeat/telemetry từ Gateway; hiển thị trạng thái kết nối, pin, lỗi phần cứng và điều kiện bất thường.
- Dashboard/map trạng thái theo site, loại thiết bị, mức độ cảnh báo và thời gian phát sinh.
- Cập nhật trạng thái thiết bị theo bản tin mới nhất; lưu lịch sử để truy vết mất kết nối, chập chờn hoặc phục hồi.
- Quy tắc riêng cho thiết bị inactive: không sinh cảnh báo mất kết nối khi `DEVICE.STATUS = 0`.

### 4. Quản lý cảnh báo và sự cố

- Cảnh báo cháy/nổ, khói, mở cửa, chuyển động, vỡ kính, xâm nhập, thiết bị lỗi hoặc mất kết nối.
- Luồng nhận IoT message → kiểm tra hợp lệ/trùng → cập nhật trạng thái thiết bị → tạo cảnh báo mới → gửi thông báo → người dùng tiếp nhận/xử lý → đóng hoặc tự đóng khi nhận tín hiệu phục hồi.
- Danh sách cảnh báo đang hoạt động, chi tiết, lịch sử, bộ lọc theo site/thiết bị/loại/trạng thái/thời gian.
- Gắn chính xác vị trí, thiết bị, loại cảnh báo, thời điểm, người tiếp nhận và lịch sử hành động.
- Xử lý edge case: bản tin trùng hoặc đến sai thứ tự, heartbeat chập chờn, phục hồi đến trước thao tác acknowledge, nhiều cảm biến cùng phản ánh một sự cố.

### 5. Điều khiển thiết bị từ xa

- Gửi mã lệnh điều khiển từ Cloud qua Gateway đến thiết bị; nhận ACK/kết quả và lưu audit.
- Cấu hình tách bật/tắt cảm biến Motion và Door; kiểm soát quyền theo vai trò/site/thiết bị.
- Quản lý tần suất gửi lệnh, timeout, retry và tình huống duplicate ACK.
- Hiển thị trạng thái thực thi để người vận hành biết lệnh đang chờ, thành công hay thất bại.

### 6. Lịch giám sát và cấu hình vận hành

- Cấu hình giờ giám sát theo site, thiết bị/cảm biến và ngày trong tuần.
- Thiết lập tần suất scan/gửi dữ liệu, ngưỡng mất kết nối và cách hiển thị trên bản đồ.
- Hỗ trợ tạm dừng theo thời gian bảo trì để tránh false alarm; lưu phiên bản và lịch sử thay đổi cấu hình.

### 7. Thông báo và escalation

- Gửi thông báo tức thời hoặc hàng loạt qua SMS, email và giao diện hệ thống.
- Quản lý template, người nhận, đơn vị nhận, kênh nhận, mức độ cảnh báo và lịch áp dụng.
- Nội dung chứa site, vị trí lắp, loại thiết bị, loại sự cố và thời gian để người xử lý định vị nhanh.
- Lưu kết quả gửi, lỗi, retry và trạng thái nhận; hỗ trợ xuất tối đa 50.000 cảnh báo theo yêu cầu vận hành trong bảng công việc.

### 8. Người dùng, vai trò và phê duyệt

- Đồng bộ User, Store, Position/Role từ ERP; đối soát lỗi mã chức danh hoặc phạm vi điểm bán.
- Phân quyền theo chức năng và dữ liệu: role, đơn vị, site, nhóm site, thiết bị và hành động.
- Quản lý nhóm người dùng, supervisor nhiều site và phê duyệt nhiều cấp đối với cấu hình/điều khiển nhạy cảm.
- Kiểm tra quyền âm: người không còn phạm vi site không được xem hoặc điều khiển thiết bị tại site đó.

### 9. Camera, bản đồ và tra cứu trực quan

- Tích hợp AI Camera/camera để hỗ trợ xác minh cảnh báo.
- Hiển thị marker, cụm site, tình trạng thiết bị và cảnh báo trên Google Maps.
- Điều hướng từ cảnh báo đến site, thiết bị, hình ảnh camera và lịch sử liên quan.

### 10. Báo cáo, vận hành và audit

- Báo cáo trạng thái thiết bị, kết nối, pin/lỗi, cảnh báo theo loại/site/thời gian và tiến độ xử lý.
- Xuất danh sách thiết bị/cảnh báo; phân trang và tối ưu truy vấn cho supervisor có phạm vi lớn.
- Lưu audit cho cấu hình, quyền, lệnh điều khiển, trạng thái và thao tác xử lý cảnh báo.
- Theo dõi hiệu năng DB/service, sync job, backlog bản tin và lỗi tích hợp phục vụ go-live/vận hành.

## Luồng, quy tắc và KPI quan trọng

- **Onboarding:** đồng bộ/tạo site → đăng ký thiết bị/IMEI → gán loại, vị trí, lịch giám sát và phạm vi → activate → nhận heartbeat/telemetry.
- **Cảnh báo:** Gateway gửi payload chuẩn → validate/deduplicate → cập nhật device state → so rule → tạo incident → notify → acknowledge/assign/process → close hoặc auto-close.
- **Mất kết nối:** hết thời gian heartbeat → kiểm tra thiết bị active → tạo warning; bỏ qua thiết bị inactive/deleted; khi reconnect thì cập nhật và tự đóng theo rule.
- **Remote command:** người có quyền chọn lệnh → Cloud/Gateway/device → ACK/result → cập nhật trạng thái và audit; timeout/retry phải idempotent.
- KPI phù hợp: tỷ lệ thiết bị online, thời gian phát hiện và acknowledge, thời gian xử lý, tỷ lệ false alarm, tỷ lệ tự đóng đúng, tỷ lệ gửi thông báo thành công, uptime Gateway/API và số cảnh báo theo site/loại.

## Kiến trúc, tích hợp và công nghệ

**Đã được tài liệu xác nhận:** thiết bị/cảm biến → IoT Gateway → Cloud API; tích hợp ERP, Camera, Google Maps, SMS và email; có ERD/database mapping, payload/command/frequency. Hồ sơ nêu việc tư vấn kiến trúc Microservices, Redis và RabbitMQ để xử lý bất đồng bộ/mở rộng, nhưng không đủ bằng chứng để khẳng định toàn bộ thành phần đã production.

**Kiến trúc logic:** Device/Sensor → Gateway & protocol adapter → API/ingestion → event/alert processing → device/alert/config services → transactional DB/cache/queue → dashboard/map/notification → ERP/Camera/SMS/Email. Các công nghệ time-series hoặc broker khác chỉ là phương án tham khảo, không gán thành stack đã dùng.

## 7 đầu việc BA đặc thù

1. Khảo sát đội lắp đặt, giám sát, PCCC/an ninh và vận hành; xác định URD, capability map, rollout scope, roadmap và kế hoạch triển khai theo site.
2. Chuẩn hóa site–device–user–alert master, taxonomy thiết bị/cảnh báo, IMEI, vị trí, lịch giám sát và ownership; bàn giao data dictionary, ERD và master-data rule.
3. Thiết kế IoT/alert state machine cho heartbeat, new/duplicate/recovery, auto-close, inactive device, acknowledge/close và lost connection; lập rule/exception catalog cùng sequence diagram.
4. Thiết kế permission, phê duyệt nhiều cấp và notification routing theo role/site/device/channel/recipient/schedule; lập permission matrix, BPMN phê duyệt và đặc tả template SMS/email.
5. Đặc tả payload/API và data mapping Gateway–Cloud–ERP–Camera–Maps–SMS–Email, gồm command/ACK/frequency/retry/idempotency; đồng thời review scalability của service/cache/queue.
6. Thiết kế UI/UX trên Figma/Visily cho realtime map, dashboard, device, alert, configuration và export; kiểm chứng usability/performance với supervisor giám sát nhiều site.
7. Xây dựng 300–400 test case UAT cùng functional, regression, integration, API, UI, smoke và performance test; nghiệm thu timing/type/state/location của cảnh báo, đào tạo, go-live và handover.

## Nguồn chính

- `Phỏng vấn BA_đang làm dở.docx`, `Phỏng vấn BA.docx`.
- `CV - dự án và tính năng.pdf`, `Hỏi ChatGPT chi tiết/CV_Ban_Tieng_Viet.docx`.
- `Khác/Tổng hợp công việc cần thực hiện.xlsx`, sheet `SMARTSAFE`.

@pagebreak
# 2. HRAI — Phân tích và QA kết quả AI nhân sự

## Tổng quan

HRAI xử lý dữ liệu nhân sự để tạo kết quả phân tích/cảnh báo. Luồng được tài liệu xác nhận là Airflow điều phối xử lý AI, kết quả được ghi vào DB, hiển thị trên UI và được AI QA đánh giá. Hệ thống hướng đến phân loại nhân sự, nhận diện rủi ro/tiềm năng và cung cấp bằng chứng, giải thích, khuyến nghị cho quản lý; quyết định nhạy cảm vẫn cần con người xác nhận.

## Danh mục tính năng

### 1. Hồ sơ nhân sự hợp nhất

- Hồ sơ nhân viên: mã, đơn vị/phòng ban, chức danh, nhóm chức danh, cấp bậc, quản lý, ngày vào, thâm niên và trạng thái.
- Lịch sử nghề nghiệp: vị trí, khoảng hiệu lực, điều chuyển, đổi đơn vị/manager, thăng chức và thay đổi cấp bậc.
- Hiệu suất và khối lượng: KPI theo kỳ, tỷ lệ hoàn thành/quá hạn, xu hướng, độ biến động, so sánh nhóm, task, OT và dấu hiệu quá tải.
- Nhận xét định tính: manager comment, điểm mạnh/yếu, khen/nhắc nhở, sentiment và tỷ lệ positive/negative.
- Thành tích, kỷ luật, đào tạo, kỹ năng, khung năng lực/gap, lương/bậc và thời gian giữ vị trí.

### 2. Data Quality và Feature Programming

- Kiểm tra null, trùng, khoảng ngày sai, nhiều vị trí hiện hành và dữ liệu mâu thuẫn.
- Chuẩn hóa ngày, text, encoding, null; join nhiều nguồn và kiểm soát input JSON/CSV/DB.
- Tính feature: KPI trend/volatility, months without promotion, manager/department changes, sentiment ratio, overdue ratio, reward–discipline score, workload, promotion readiness, engagement, career mobility và competency gap.
- **Đề xuất quản trị:** Feature Catalog/Feature Store lưu nguồn, công thức, domain, kiểu, version, effective date, confidence và trạng thái `PRESENT`, `MISSING`, `UNKNOWN`, `NOT_APPLICABLE`, `CALCULATION_ERROR`, `PENDING_REVIEW`, `MANUALLY_CONFIRMED`.

### 3. Training/Test Dataset và ground truth

- Tạo ground truth từ kết quả HR thực tế, rule nghiệp vụ và HR expert validation; lưu người/thời gian xác nhận.
- Quản lý train/validation/test/golden regression; split theo employee và thời gian để tránh data leakage.
- Sinh persona/synthetic employee từ tổ hợp performance, sentiment, discipline, tenure, career, workload và completeness.
- Bao phủ nhóm normal, risk, conflict, missing, boundary, multi-risk và high-potential.
- Xác định cả expected và forbidden conclusion/evidence/recommendation; áp dụng decision table, equivalence, boundary, pairwise/combinatorial và risk-based test design.

### 4. AI Prediction và versioning

- Kết quả phân loại: Xuất sắc, Tích cực, Bình thường, Có dấu hiệu tiêu cực.
- Nhóm cảnh báo: nghỉ việc, suy giảm hiệu suất, giảm gắn kết, burnout/quá tải, kỷ luật, tài chính/tuân thủ, không phù hợp vị trí và chậm phát triển nghề nghiệp.
- Nhóm tiềm năng: nhân sự triển vọng/nguồn, readiness thăng tiến, ưu tiên đào tạo/nâng bậc.
- Output gồm class, risk type/level/score/confidence, evidence, reasoning/summary, recommendation, raw response và processing time.
- Metadata gồm employee, input snapshot, model/prompt/feature/rule/data/API version, environment và thời gian; không ghi đè lịch sử prediction.

### 5. QA Review UI

- Điều hướng: Tổng quan, Dự đoán AI, QA Review, Gold Label, Adjudication, Báo cáo và Quản trị.
- Hiển thị prediction ID, employee, model version, snapshot time và feature version.
- Business verdict: `PASS`, `50% PASS/PARTIAL`, `FAIL`; language verdict: `PASS`, `NEEDS REVISION`.
- Chấm từng field: alert, risk level, risk score, evidence, explanation và recommendation.
- QA sửa output thành Gold Label, chọn issue code ngôn ngữ/nghiệp vụ, prohibited phrase, required element, preferred rewrite và ghi note.
- Quản lý draft, request bổ sung, reviewer/verifier, dataset eligibility và chuyển Adjudication khi bất đồng.

### 6. Gold Label, feedback và Adjudication

- `PASS`: dùng output khi QA đã xem đủ; `PARTIAL`: hợp nhất field sửa vào bản hoàn chỉnh; `FAIL`: QA cung cấp corrected output đầy đủ và lưu AI output làm rejected sample.
- Tách business feedback khỏi language/style feedback; chuẩn hóa issue code và lưu original/preferred rewrite.
- Bất đồng giữa QA chuyển cho QA Lead/HR expert; chỉ bản `VERIFIED` mới đủ điều kiện vào dataset.
- **Đề xuất:** snapshot + prediction + verified gold → dataset version/manifest/checksum → candidate model → quality gate → registry → shadow/canary/rollback; không cho model production “học ngay” từ comment thô.

### 7. AI QA, regression và production verification

- Tách luồng `FEATURE_READY` để test inference và `RAW_DATA` để test Feature Programming; sau đó chạy end-to-end.
- Test schema, enum, null, confidence, exact/acceptance matrix cho class/risk, precision/recall/F1, false positive/false negative.
- Kiểm tra grounding/hallucination, consistency giữa field, recommendation safety, missing/conflict/multi-risk, language và latency.
- Đối soát source → staging → cleansing → feature → AI JSON → model/API → result DB → dashboard.
- Batch/API test, golden regression, defect taxonomy theo data/mapping/rule/prompt/model/hallucination/recommendation/UI/performance.
- Production smoke, permission, log, UAT parity, rollback và drift/version monitoring.

## Luồng, quy tắc và KPI quan trọng

- **Luồng hiện tại:** HR data → Airflow DAG/feature build → AI inference → prediction DB → UI → QA Review.
- **Luồng cải tiến:** QA verdict/correction → Gold Label/Adjudication → versioned dataset → training/evaluation → quality gate → controlled deployment.
- Missing/contradictory data phải hạ confidence hoặc trả `UNKNOWN`; không được suy diễn quá mức hay trộn dữ liệu hai nhân viên.
- Không cho AI tự ra quyết định kỷ luật/chấm dứt hợp đồng; khuyến nghị nhạy cảm phải có người có thẩm quyền duyệt.
- KPI: precision/recall/F1 theo risk, false negative/positive, inter-rater agreement, tỷ lệ verdict, tỷ lệ field phải sửa, data completeness, pipeline success/latency, regression pass rate và drift theo version.

## Kiến trúc, tích hợp và công nghệ

**Đã xác nhận:** Airflow điều phối; AI ghi kết quả vào DB; UI/QA Review hiển thị kết quả, model/feature/snapshot version. Tài liệu còn nêu trực tiếp RoBERTa, XGBoost, Qwen3.5 9B, Unsloth, pandas, allpairspy, SQL, CSV, JSON trong bối cảnh xử lý/kiểm thử.

**Đề xuất logic:** HR source/DB → Airflow → feature pipeline → inference service → prediction DB → Review UI → Gold Label/dataset builder → object storage/training/model registry → deploy/monitor. Các thành phần FastAPI/Spring Boot, Kafka/RabbitMQ, MinIO/S3, MLflow, Docker/Kubernetes, KServe, Prometheus/Grafana chỉ là phương án trong tài liệu tham khảo, không coi là production stack nếu chưa có bằng chứng.

## 7 đầu việc BA đặc thù

1. Chuẩn hóa taxonomy HR, class, alert, risk, potential và promotion readiness, gồm ngưỡng và hành động được phép; bàn giao glossary, decision table và acceptance criteria.
2. Phân tích/mapping dữ liệu HR đa nguồn và Data Quality cho null, trùng, thời gian, mâu thuẫn và PII; tạo data dictionary, source-to-feature mapping và DQ/SQL checklist.
3. Đặc tả feature lifecycle theo raw/derived/manual/synthetic, source, formula, validity, status, version và confidence; tạo Feature Catalog, specification và lineage matrix.
4. Thiết kế persona, feature-combination và ground truth cho normal, boundary, missing, conflict, multi-risk và high-potential; tạo generator constraints, expected/forbidden evidence và conclusion.
5. Đặc tả QA Review, Gold Label, language feedback và Adjudication; tạo wireframe, field validation, issue-code catalog và review/verification workflow.
6. Thiết kế human-in-the-loop, dataset lineage, snapshot, split theo employee/time, manifest/version và quality gate; tạo logical data model và DAG specification, ghi rõ phần đề xuất.
7. Điều phối UAT/regression/release giữa HR, Data, AI, Backend và Frontend; bàn giao golden regression suite, defect triage matrix, production verification và release/rollback checklist.

## Nguồn chính

- `HRAI/1. Giới thiệu HRAI.pdf`, `HRAI/2. Luồng Training AI HRAI.pdf`.
- `HRAI/Cách làm BA-QA HRAI.pdf`, `HRAI/HRAI - Cách insert data kiểm thử vào DB.pdf`.
- `HRAI/QA cho HRAI.png`.

@pagebreak
# 3. mChat — Omnichannel Contact Center và Agent Assist

## Tổng quan

mChat/VSS Chat Platform là nền tảng Contact Center/Omnichannel cho Sales và CSKH, hợp nhất hội thoại nhiều kênh trong một workspace; có CRM liên hệ nhẹ, routing/workforce, automation/SLA, social commerce, campaign và analytics. Lớp AI Agent Assist là hướng mở rộng: hiểu hội thoại, dùng dữ liệu sản phẩm để tóm tắt/gợi ý nhưng không tự gửi và không tự phân phối hội thoại.

## Danh mục tính năng hiện hữu

### 1. Conversations

- Bộ lọc `All`, `Mentions`, custom filter; sidebar theo team, type, channel và label.
- Loại `Message`, `Email`, `Comment`; trạng thái `Open`, `Resolved`, `Pending`, `Snoozed`, `All`; phạm vi `Mine`, `Unassigned`, `All`.
- Search, reply, private/internal note, attachment và canned response bằng ký tự `/`.
- Assign/reassign Agent/Team, gắn label, xem/cập nhật contact attribute, xem lịch sử chat và conversation detail.
- Reopen/resolve/unresolved, snooze đến next reply/tomorrow/next week; merge contact trùng.
- Custom filter theo status, assignee, inbox, team, conversation ID, campaign, label, browser language, country, referrer và conversation attribute.

### 2. Contacts/CRM-light

- Danh sách, search, sort, filter, pagination; add/edit/delete/view contact.
- Import CSV/Excel; custom attribute; activity/chat history; khởi tạo message mới.
- Merge duplicate profile và xác nhận trước khi xóa; bảo toàn lịch sử liên quan.

### 3. Channel/Inbox và tích hợp

- Kết nối Zalo OA, Website widget/script và Facebook OAuth/Fanpage.
- Cấu hình tên/avatar inbox, opening message, CSAT, Agent/collaborator và re-authorize channel.
- Màn hình Add channel còn có WhatsApp, Email, Telegram, Line dưới dạng connector có thể chọn; không khẳng định tất cả đã được cấu hình/vận hành.

### 4. User, organization và RBAC

- Vai trò Agent, Supervisor, Admin; add/edit/delete/reset password; gán role, channel và team.
- Bulk đổi role, thêm/xóa channel; hiển thị employee code, title, role, channel, department, team và status.
- Team CRUD, manager, thành viên nhiều team; activate department/user. Activation và Authorization là hai khái niệm riêng.

### 5. Nhãn, canned response, custom attribute và notification

- Label CRUD với tên, mô tả, màu và khả năng dùng trong filter/workflow.
- Canned response có code/content, gọi nhanh trong composer.
- Custom attribute kiểu Text, Number, Link, Date, List, Checkbox; dùng cho contact, conversation và routing.
- Notification center: unread/list/mark completed; tài liệu hướng dẫn song ngữ; account setting về company, language, auto-resolve days, account ID và version.

### 6. Routing, queue và workforce

- Business hours theo channel/ngày/all-day/start-end và quy tắc ngoài giờ.
- Ưu tiên last Agent; route theo contact attribute đến Team, ví dụ VIP/B2B/complaint; preferred team/department.
- Chọn Agent theo least open conversation, fastest response hoặc fair/balanced rotation.
- Capacity riêng cho Message, Comment, Email; fallback sang no-auto support, auto message hoặc waiting list.
- Reassign khi Agent offline/không phản hồi quá ngưỡng; điều tiết tốc độ phân phối khi Agent online.
- Thứ tự xung đột giữa nhiều priority rule chưa được tài liệu chốt đầy đủ và cần BA làm rõ.

### 7. Automation và SLA

- Auto welcome; auto snooze khi chờ khách; auto resolve sau thời gian không hoạt động.
- Cấu hình mode, time, message và status.
- SLA riêng cho Message, Comment, Email với ba chặng: first response, subsequent answer và completion.
- Cảnh báo sắp vi phạm/đã vi phạm; task/status và báo cáo theo SLA.

### 8. Campaign

- Website proactive message dạng ongoing: title, message, inbox, URL, time-on-page, enable và business-hours-only.
- One-off campaign: title, message, inbox, audience label và schedule; create/edit/toggle/delete.
- SRS giới hạn mô tả Campaign chủ yếu ở Website; không mở rộng thành bulk Facebook/Zalo nếu không có bằng chứng.

### 9. Livestream và Auto Comment

- Livestream scenario theo page/name; keyword ↔ product; kiểm cú pháp keyword và số điện thoại Việt Nam.
- Phân phối comment hợp lệ, sai keyword, tất cả hoặc không phân phối trong/sau live.
- Chọn toàn bộ Agent của channel hoặc team; cấu hình auto reply cho valid/invalid/end và enable/disable.
- Auto Comment theo channel/post/script content/status; hỗ trợ nhiều script trên một channel và tùy chọn auto-distribute.

### 10. Báo cáo

- Dashboard Overview, CSAT, Agent, Label, Inbox/Channel, Team, SLA, Livestream và employee performance.
- Filter theo today, 7/30 ngày, 3/6 tháng, last year hoặc custom; download/export.
- Metrics: conversation, inbound/outbound, average first response, average resolution, resolved, CSAT, feedback/comment, SLA phase, response rate, customer received và contact có phone.

## AI Agent Assist — phạm vi mục tiêu/đề xuất

### Hiểu hội thoại

- Phân loại primary/secondary intent, need, entity, sentiment/emotion/trend/urgency, mức độ quan tâm, lead status/score, blocker và evidence.
- Entity gồm product/model/color/capacity/budget/location/phone/order/payment/time; có `UNKNOWN` và confidence.
- Tóm tắt current/handover/interim/final, unresolved item, outcome và follow-up.

### Hỗ trợ Agent

- Gợi ý next-best action, câu hỏi cần hỏi thêm, sales/closing strategy, draft reply, label và kênh fulfillment.
- Product card tra ERP theo SKU, giá, promotion, gift, installment, stock theo store/online, warranty, specification, channel và timestamp.
- Khi dữ liệu thiếu/stale phải ghi “chưa xác minh”; không bịa giá, tồn kho, promotion hoặc cam kết ngoài chính sách.
- UI có loading/empty/error/timeout/retry/stale/low-confidence; Agent có thể edit/accept/reject/ignore/reanalyze; draft chỉ được insert để Agent kiểm tra rồi gửi.

## Luồng, quy tắc và KPI quan trọng

- **Hiện hữu:** Channel → Message/Conversation → Rule/Queue → Agent/Team → reply/note/label/contact/status → SLA/Automation → close → Report.
- **Mục tiêu AI:** webhook/message → dedupe/store → Rule Routing chạy độc lập → AI Trigger/Queue → context + ERP snapshot → model → schema validation → AI result → WebSocket/SSE → Agent UI → feedback.
- Trigger: idle năm phút từ tin Customer cuối, manual “AI gợi ý”, speaker-turn Customer↔Agent; có thể bổ sung open/assign, transfer, pause/interim và resolve/final.
- Priority `MANUAL > speaker change > idle`; dùng idempotency key/target message, một active job mỗi conversation, dirty/stale control; AI không được làm routing/SLA chờ.
- KPI: first response/resolution time, SLA compliance, acceptance/edit/reject rate của gợi ý, accuracy intent/entity, grounded product fact rate, lead conversion, transfer quality, AI latency/backlog/cost.

## Kiến trúc, tích hợp và công nghệ

**Đã xác nhận:** web app tại domain nội bộ, tích hợp Facebook, Zalo, Website widget, OAuth, CSV export và giao diện Contact Center. Đường dẫn/giao diện có nét giống Chatwoot derivative nhưng đây chỉ là suy luận, không phải stack được xác nhận.

**Mục tiêu/đề xuất:** Channel Adapter/Webhook → Conversation DB → Rule Engine/Queue → Agent UI; event đi song song đến AI Orchestrator/priority queue → LLM/NLP + ERP/Product Service → AI result DB → WebSocket/SSE. RabbitMQ/Kafka, Redis, prompt/evaluation tools và test tools như Postman/Newman, Playwright/Cypress, k6/JMeter chỉ là phương án thiết kế/kiểm thử.

## 7 đầu việc BA đặc thù

1. Khảo sát As-is/To-be Omnichannel và chốt ranh giới Rule Engine–AI–Human; bàn giao BPMN/event map, scope/non-scope và nguyên tắc AI không auto-send/auto-route.
2. Chuẩn hóa taxonomy intent, need, entity, sentiment, interest, lead, blocker và outcome, gồm primary/secondary/UNKNOWN/confidence; tạo label guideline, decision table và acceptance criteria.
3. Mô hình hóa Conversation–Message–Contact–Channel–Agent/Team–Label–SLA, gồm sender, order, duplicate webhook và merge; tạo ERD, data dictionary và mapping API/DB/UI/AI.
4. Đặc tả routing/SLA/automation cho Contact Center; lập priority/conflict matrix, capacity, fallback, reassignment, business-hours rule và edge-case acceptance criteria.
5. Đặc tả AI trigger/orchestrator/queue với debounce, priority, idempotency, stale và concurrency; tạo trigger catalog, state machine và API/job contract.
6. Phân tích ERP grounding và product matching/freshness; tạo SKU/price/stock/promotion mapping, validation, fallback và forbidden-fact rule.
7. Thiết kế Agent Assist UI, golden-conversation UAT và KPI; bàn giao wireframe, state/permission matrix, feature test rubric và dashboard đo acceptance, edit rate, response/resolution time, lead conversion.

## Nguồn chính

- `mChat/VSS mChat SRS.docx`, `mChat/3. mChat.pdf`, `mChat/mchat-ba-analysis.md`.
- `mChat/mChat_Dương đăng ký sáng kiến ý tưởng.docx`, `mChat/VSS.mp4`.
- `mChat/mChat.txt` đã được rà soát nhưng credential plaintext không được đưa vào tài liệu.

@pagebreak
# 4. CRM — Customer 360, CSKH và Ticket Platform

## Tổng quan

CRM là nền tảng hợp nhất Customer 360, Customer Data Platform/segmentation, Sales Support, Call Center, Omnichannel, Marketing, Ticket/Case Management và báo cáo. Bảng `DS CHỨC NĂNG CRM.xlsx` có khoảng 420 yêu cầu thuộc chín nhóm nghiệp vụ, với trạng thái ký kết/không làm khác nhau; phần dưới là capability inventory đã đối chiếu với `CRM.docx`, không phải tuyên bố tất cả đều đã production.

## Danh mục tính năng

### 1. Quản lý khách hàng và Customer 360

- Danh sách, tìm kiếm, import khách hàng; quản lý khách tạm thời; tạo/cập nhật thông tin cơ bản.
- Đổi số điện thoại với OTP; API tìm/tạo khách hàng, lấy/xác thực OTP và lấy thông tin/điểm qua VT++.
- Hồ sơ 360 gồm thông tin chung, nhân khẩu học, địa lý và bản đồ nơi mua, tâm lý/hành vi, kinh tế và mức độ hoàn thiện hồ sơ.
- Lịch sử điểm, giao dịch, mua hàng, cuộc gọi, phản ánh/kiến nghị, bảo hành, chat, happy-call và survey.
- Log thay đổi, popup/thông báo, cảnh báo thiếu dữ liệu và tỷ lệ hoàn thiện hồ sơ.

### 2. DP/CDP và phân khúc khách hàng

- Tạo tệp/segment theo điều kiện, preview danh sách, phân loại, xóa và đồng bộ audience theo lịch.
- Đẩy audience sang Facebook, Google, TikTok; Email/SMS có dòng yêu cầu nhưng một số trạng thái đánh dấu không làm.
- Tự phân loại khách hàng theo rule; theo dõi số lượng, điều kiện và lịch sử thay đổi của segment.
- Thu thập/hợp nhất dữ liệu từ ERP, Website/Excel, BankPlus, Ticket, mChat/omnichannel và Call Center.
- Dữ liệu gồm đơn hàng, đổi trả, đặt trước, bảo hành, thành viên, nguồn, phản ánh/kiến nghị, hội thoại và lịch sử gọi.
- One-time migration/merge từ Hoa Sao, BankPlus, Website và ERP; tổng hợp order value/frequency/status/source và ticket theo trạng thái/loại.

### 3. Hỗ trợ bán hàng

- Quản lý đơn hàng và tra cứu ngữ cảnh khách hàng trước/trong khi tư vấn.
- Tích hợp chat đa kênh: danh sách/chi tiết conversation, lịch sử nhanh, popup hội thoại mới và cảnh báo chưa xử lý.
- Chuyển phòng ban/người dùng, ghi chú khi chuyển, tag, quick reply và chat nhanh.
- Hiển thị Customer 360, giao dịch, đơn hàng, ticket và lịch sử tương tác bên cạnh hội thoại.

### 4. CSKH và Call Center

- Danh sách inbound/outbound call, filter/export và CTI screen-pop Customer 360 cho các đầu số CSKH.
- Nghe song song, xem active call, transfer cùng/khác đầu số và quản lý danh sách IP Phone.
- Outbound cho phản ánh/kiến nghị/campaign; phân công call list và tạo Ticket trong khi gọi.
- Bộ tiêu chí chấm chất lượng call/chat; lỗi kỹ năng, nghiệp vụ, ý thức; lưu điểm, tìm kiếm và export.
- Task cho Agent; notification khi Ticket gần/quá SLA hoặc cần phối hợp.

### 5. Survey và campaign CSKH

- Quản lý nhóm câu hỏi, câu hỏi, đáp án và bộ survey.
- Tạo campaign, import audience, phân công khách hàng/Agent, call list và theo dõi kết quả.
- Liên kết kết quả survey/happy-call về Customer 360 và báo cáo Agent/campaign.

### 6. Marketing

- Quản lý kế hoạch Marketing; campaign, ad group, ad, product và địa bàn.
- Campaign Email/SMS/Social; tích hợp/đối soát Facebook, Google và TikTok theo phạm vi yêu cầu.
- Quản lý product group, ad channel, objective và daily job thu thập kết quả.
- So sánh, filter và export hiệu quả theo campaign → ad group → ad → product/địa bàn.

### 7. Tiện ích và Knowledge Base

- Article/Knowledge Base CRUD, phân nhóm/chuyển nhóm, tìm kiếm và tra cứu nâng cao.
- Tra cứu sản phẩm, cửa hàng, IMEI và bảo hành để hỗ trợ tư vấn/CSKH.

### 8. Quản trị, quyền và dữ liệu dùng chung

- Login history; user, role, function và feature management.
- Function permission và data permission theo kho, đơn vị, người dùng, người xử lý và phạm vi Customer/Ticket.
- Đồng bộ user, department, store, employee, position, warehouse, order source, province/district/ward từ ERP.
- Tham số hệ thống; danh mục lỗi CSKH, loại lỗi, điểm phạt và audit log.
- Quản lý notification và cấu hình tích hợp/batch job.

### 9. Dashboard và báo cáo

- Dashboard Customer 360 về call, warranty, transaction, order và Ticket.
- Dashboard doanh nghiệp: tổng/new/cumulative customer, customer type/source, profile completeness, chat, call, order, Ticket và revenue theo kênh.
- Báo cáo Agent/Call Center: volume theo ngày/giờ, served per Agent, status change, login/logout, idle/drop, waiting/end/IVR và productivity.
- Báo cáo phản ánh/kiến nghị theo nội dung, nguồn, chi tiết và tiến độ; báo cáo hiệu suất nhân viên bán hàng, conversation và chất lượng.

### 10. Ticket/Case Management độc lập

- Ticket list/create/view/update với dynamic field; Task có thể sinh từ Ticket hoặc độc lập.
- Dynamic field kiểu text, number, date, dropdown; cấu hình required, search/filter, report, validation và access.
- Ticket template có create/edit/enable/disable, effective date, version, approval và extension.
- Workflow theo template với step, condition, role, SLA, transition, exception, reopen, transfer và escalation.
- Category, custom attribute, mail template, comment/collaboration nhiều đơn vị và full audit trail.
- Đồng bộ organization master từ ERP, data permission, dashboard/home và notification.

## Luồng, quy tắc và KPI quan trọng

- **Customer 360:** source → normalize → match/merge/deduplicate → canonical customer → transaction/interactions → segmentation/profile score → channel consumption.
- **Ticket:** create từ CSKH/Call/Chat/API → chọn template/dynamic field → validate → workflow/SLA → assign/collaborate/transfer/escalate → resolve/reopen/close → survey/audit/report.
- **CTI/Omnichannel:** call/message → identify customer → screen-pop Customer 360 → Agent xử lý → note/task/Ticket → update history/report.
- Rule then chốt: OTP khi đổi phone, deduplication/matching, field visibility/editability theo role/state, SLA pause/resume, template effective/version, exception/reopen và permission theo dữ liệu.
- KPI: completeness Customer 360, duplicate/merge rate, segment sync success, first response/resolution/SLA, ticket backlog/aging/reopen, call handling/quality, campaign conversion, data migration reconciliation và dashboard consistency.

## Kiến trúc, tích hợp và công nghệ

**Đã xác nhận:** tích hợp ERP, Website/Excel, BankPlus, Ticket, mChat, Call Center/Hoa Sao, VT++, Facebook, Google, TikTok, SMS và email; có initial migration cùng các batch/hourly sync, role/data permission và audit.

**Kiến trúc logic:** API/Connector + ingestion/batch → Customer 360/CDP canonical layer → CRM/Marketing/CSKH/Ticket services → Workflow/SLA/Notification → Dashboard/Report. `CRM.docx` cho thấy cách tiếp cận metadata/workflow-driven ở dynamic field, template và Ticket; không đủ bằng chứng để khẳng định Kafka/RabbitMQ/cache/read replica đã được triển khai.

## 7 đầu việc BA đặc thù

1. Hợp nhất khoảng 420 yêu cầu từ nhiều đơn vị thành capability map, scope, priority, RTM và baseline nghiệm thu; bàn giao feature catalog và gap/status matrix.
2. Thiết kế canonical Customer 360 và mapping ERP/Website/BankPlus/Ticket/Call/Chat, gồm match–merge–dedup, OTP đổi số điện thoại và one-time conversion; tạo ERD, data dictionary, source-to-target mapping và reconciliation rule.
3. Thiết kế metadata-driven dynamic field/template theo data type, validation, required, search, report, access, lifecycle, effective date, version, approval và extension; bàn giao FRD, config catalog, prototype và acceptance criteria.
4. Mô hình hóa Ticket state machine/workflow/SLA/exception/reopen/transfer/cross-unit collaboration/escalation; tạo BPMN/state diagram, SLA matrix và business-rule catalog.
5. Đặc tả CTI/Omnichannel integration cho screen-pop Customer 360, transfer call/chat, new conversation notification, customer context, API sequence, timeout/error/retry; tạo sequence/API mapping và integration test scenarios.
6. Thiết kế function/data/field/workflow-step permission theo role, đơn vị, kho, assignee và state, kèm audit; tạo permission matrix, segregation rule và negative test case.
7. Điều phối data migration và end-to-end UAT/report reconciliation/go-live cho Customer 360–DP–mChat–CTI–Ticket; bàn giao test data, defect triage, reconciliation sheet, SOP và training.

## Nguồn chính

- `CRM/DS CHỨC NĂNG CRM.xlsx` — khoảng 420 yêu cầu, hai sheet baseline/tracking.
- `CRM/CRM.docx` — Dynamic Field, Template, Workflow, SLA, Ticket và Task.
- `Khác/Tổng hợp công việc cần thực hiện.xlsx`, các tờ trình/nâng cấp liên quan; tài liệu CV để kiểm chứng chéo.

@pagebreak
# 5. OCR & RPA — Tự động hóa xử lý chứng từ

## Tổng quan

Dự án đề xuất RPA kết hợp OCR tại Viettel Commerce nhằm giảm nhập liệu/copy–paste/đối chiếu thủ công, chuẩn hóa chứng từ, giảm sai sót, rút ngắn cycle time và tăng khả năng truy vết. Phạm vi khảo sát gồm Trung tâm Xuất nhập khẩu, Phòng Pháp chế & Đầu tư/KCQ và Trung tâm Phân phối. Báo cáo chính thức liệt kê 25 use case đề xuất: 8 XNK, 6 Pháp chế & Đầu tư và 11 Phân phối; định hướng là pilot rồi mở rộng.

## Danh mục 25 use case nghiệp vụ

### A. Xuất nhập khẩu — 8 use case

- **Tạo hồ sơ khai báo hải quan:** nhận Invoice, Packing List, B/L, C/O, Hợp đồng; phân loại và trích seller/buyer/invoice/line item/quantity/value/gross–net/incoterm/HS; chuẩn hóa/gộp line; mapping vào form bằng API/RPA; tạo draft, checklist thiếu và highlight trên ảnh gốc.
- **Đối soát trước khai báo:** so Contract–Invoice–Packing List–draft declaration về tên hàng, số lượng, trị giá, điều kiện giao hàng và HS; sinh bảng chênh lệch/ticket, mức độ ưu tiên và giao diện đối chiếu một trang.
- **Google Sheets theo dõi lô hàng/tờ khai/chứng từ:** ghi/cập nhật theo Shipment, BL, Invoice hoặc Tờ khai; cột “Cần kiểm tra”, kiểm tra trùng/thiếu và link file gốc.
- **Tra cứu/so khớp HS:** chuẩn hóa mã, tra web/biểu thuế/DB nội bộ, gợi ý top mã và lý do; bắt buộc người dùng xác nhận trước khi điền tờ khai.
- **Số hóa biểu thuế:** trích HS, mô tả, thuế suất, điều kiện, ngày hiệu lực; giữ cấu trúc chương/nhóm, version và diff thêm/sửa/xóa/đổi thuế; đánh dấu OCR thấp/bất thường.
- **Hồ sơ chứng từ audit-ready:** nhận dạng loại, gom theo BL/Shipment, đổi tên chuẩn, checklist bắt buộc, phát hiện trùng/sai loại và liên kết hồ sơ vào Sheet.
- **Theo dõi lô hàng/lịch tàu:** BL/container, ETD/ETA, cảng, tàu/chuyến và trạng thái; lấy từ portal/email, lưu lịch sử, cảnh báo hold/rollover/transshipment/thay đổi lớn, ghi log/screenshot khi lỗi.
- **Thu thập/theo dõi gói thầu:** crawl portal/web/email, theo dõi mốc đóng/mở/gia hạn/làm rõ/kết quả/file mới, so với lần chạy trước và cảnh báo deadline.

### B. Pháp chế & Đầu tư/KCQ — 6 use case

- **Tiếp nhận/số hóa hồ sơ đầu tư–mua sắm:** trích đơn vị, dự án/hạng mục, tổng mức/giá trị, thời gian, mục tiêu, loại hình; tạo mã/trạng thái, gán người theo rule và chặn khi thiếu trường bắt buộc.
- **Tổng hợp báo giá/hồ sơ thầu:** trích nhà cung cấp, cấu hình/model, đơn giá, lead time, bảo hành, thanh toán, hiệu lực; chuẩn hóa UOM/currency, lập bảng so sánh, chênh lệch %, xếp hạng và link bằng chứng.
- **Theo dõi mua sắm/dự án:** tổng hợp PO, hợp đồng, kế hoạch, email, portal, biên bản; theo dõi giao–nghiệm thu–bàn giao và cảnh báo chậm/thiếu biên bản.
- **Đối soát nghiệm thu–hóa đơn–hợp đồng/kế hoạch thanh toán:** phân loại đủ điều kiện/chờ bổ sung/chênh lệch/đã trả; cảnh báo theo %/giá trị và mở đúng vùng ảnh để kiểm tra.
- **Nhập hợp đồng và milestone vào QLHĐ:** trích số hợp đồng, đối tác, hiệu lực/hết hạn, giá trị, mốc nghiệm thu/thanh toán; tạo draft/hồ sơ/mốc, đính file, giao đơn vị; tổng tỷ lệ khác 100% phải `Needs Review`.
- **Đối soát thực trả với kế hoạch:** match mã hợp đồng/đối tác/số tiền/cửa sổ ngày; trạng thái paid/partial/overdue/unmatched; nhắc hạn và phát hiện giao dịch trùng/lệch.

### C. Trung tâm Phân phối — 11 use case

- **Nhập chứng từ kho:** trích SKU, quantity, lot/serial, ngày và nhà cung cấp; ghi WMS/ERP/Sheet, phát hiện trùng phiếu/serial và chuyển low-confidence sang review.
- **Đối soát phiếu giao nhà cung cấp với kiểm đếm:** sinh thiếu/thừa/sai và biên bản chênh lệch.
- **Số hóa order đa kênh:** tạo đơn trên DC/WMS, chuẩn hóa khách hàng, địa chỉ, số điện thoại, COD và mapping SKU/tuyến/kho.
- **Tạo lệnh picking/packing:** gom theo tuyến/kho/ca; kiểm tồn và điều kiện trước khi phát lệnh.
- **Tạo vận đơn/nhãn:** đẩy portal hãng vận chuyển, lấy mã cập nhật ngược, retry và lưu log/screenshot.
- **Theo dõi giao/hoàn:** cảnh báo đơn treo, giao thất bại hoặc hoàn bất thường; lưu toàn bộ lịch sử trạng thái.
- **Số hóa đơn B2B đại lý:** tạo Sales Order ERP, gắn đại lý/chính sách giá/chiết khấu; kiểm SKU, khung giá và hạn mức.
- **Phân bổ tồn:** phân loại đủ/thiếu/hẹn giao; áp dụng FIFO, kho gần, ưu tiên đại lý; chặn tồn âm/SKU khóa.
- **Kế hoạch xuất–giao:** gom tuyến/kho/khu vực, tạo lệnh xuất và lịch giao; kiểm cửa sổ giao, năng lực kho–xe và đơn gấp.
- **Số hóa POD:** trích số đơn, ngày, người nhận, thực giao, thiếu/hỏng, chữ ký; cập nhật ERP/DC, mở case và gắn ảnh bằng chứng.
- **Đối soát bốn nguồn:** Sales Order–Goods Issue–Delivery/POD–Invoice; phân loại thiếu giao, xuất dư, hóa đơn sai và ưu tiên lệch giá trị lớn.

> Các ý tưởng booking hãng vận chuyển, hoàn thiện bộ hồ sơ/thanh toán, tổng hợp chi phí logistics và costing xuất hiện ở tài liệu bổ sung nhưng không được nhập vào danh mục 25 use case chính thức.

## Năng lực nền tảng xuyên suốt

### 1. Ingestion và Document Case

- Nhận từ email, folder/Drive, web/mobile upload, scan, API hoặc SFTP.
- Kiểm MIME, virus, password, dung lượng/số trang; tạo `case_id`, `document_id`, version và checksum.
- Lưu raw file bất biến; hash/dedupe/idempotency, metadata, quarantine và audit nguồn nhận.

### 2. Tiền xử lý, phân loại và OCR/KIE

- Render PDF, deskew, rotate, crop, denoise, enhance và chấm chất lượng ảnh.
- Phân loại document/template; route đến pipeline phù hợp.
- Text detection/recognition, layout/table/section/field extraction; chuẩn hóa Unicode, date, currency, UOM và number.
- Output JSON theo schema, kèm raw text, normalized value, confidence, page, bounding box và evidence.

### 3. Rule, reconciliation và Human-in-the-loop

- Business Rule Engine kiểm mandatory, format, arithmetic, date/effective range và cross-document consistency.
- Confidence gating theo field/risk: auto-pass, review hoặc block.
- Review UI đặt field cạnh đúng vùng ảnh; correction task, SLA/escalation, comment và audit.
- Feedback đã xác minh mới đủ điều kiện đưa vào dataset cải tiến model.

### 4. Integration và vận hành

- Ưu tiên API; dùng RPA cho hệ thống legacy/không có API.
- Kết nối QLHĐ, WMS, ERP, DC, Customs, Google Sheets, portal hãng tàu/forwarder/nhà cung cấp/tender.
- Retry, callback/polling, queue, Dead Letter Queue, notification, dashboard, permission, retention và security.

## Luồng end-to-end, rule và KPI

- **Luồng chuẩn:** Receive → Validate/Quarantine/Hash/Dedupe/ID → Raw storage → Normalize → Classify/Route → Async OCR Job → OCR/KIE → Normalize/Schema → Rule & Reconciliation → Auto-pass/Human Review → API/RPA → Callback/Notification → Archive/Audit/KPI.
- **Bộ hồ sơ XNK:** OCR từng file độc lập → aggregator theo Shipment/BL → checklist đủ tài liệu → reconcile chéo → critical gate → draft declaration. Callback lỗi chỉ retry callback/polling, không OCR lại toàn bộ.
- Rule: total bằng tổng line ± tax/discount; quantity × unit price = amount; gross ≥ net; effective ≤ expiry; định dạng VAT/currency/date/tax code; contract unique; Party A khác Party B; milestone %/amount so contract; duplicate payment; đối soát PO/ASN/Invoice/GRN và Sales–Issue–POD–Invoice; HS chuẩn hóa 8/10 chữ số và cần xác nhận.
- Edge case: file lỗi/password/malware/false extension, duplicate version, thiếu/rotated/blurred/multi-page/bilingual/template drift, merged table, nhầm `0/O`, `1/I`, `5/S`, decimal separator, portal timeout/session change, callback fail, queue backlog và concurrent edit.
- KPI: cycle time/giờ công giảm, error rate, completeness/truy vết, exception phát hiện sớm, straight-through/auto-pass rate, human-review rate, field/document exact match, CER/WER, precision/recall/F1, latency, retry/DLQ và cost/page.

## Kiến trúc và công nghệ

**Đã xác nhận ở cấp tích hợp:** Google Sheets API, QLHĐ, WMS/ERP/DC, email/folder/portal, API hoặc UI-RPA, môi trường DEV/UAT/PROD, permission, security và audit.

**Kiến trúc logic:** Channel → Ingestion/Document Case → AI Processing → Validation/Human Review → Integration/Orchestration → Business System; Storage, Queue, Security và Observability là năng lực cắt ngang.

**Công nghệ tham khảo/đề xuất trong tài liệu kỹ thuật:** pipeline OCR-first và VLM fallback; PaddleOCR/PP-OCR/PP-Structure, LayoutLM hoặc Qwen-VL; FastAPI/NGINX/Triton/vLLM; Docker/Kubernetes; PostgreSQL/Oracle; MinIO/S3; RabbitMQ/Kafka/Redis; OpenCV/Poppler/ClamAV; MLflow, CI/CD, Prometheus/Grafana/Loki. Đây không phải bằng chứng toàn bộ stack đã production.

## 7 đầu việc BA đặc thù

1. Khảo sát As-is tại ba đơn vị, inventory loại chứng từ/template/nguồn/volume/SLA/điểm nhập tay/rủi ro; tạo BPMN, Document Inventory, pain-point và priority matrix.
2. Thiết kế To-be và ranh giới OCR–RPA–API–Human cho từng use case; lập UC specification, input/output, pre/post-condition, pilot scope, roadmap và backlog.
3. Xây Document/Field Catalog và canonical schema; đặc tả mandatory/format/risk, mapping OCR đến Tờ khai/QLHĐ/WMS/ERP/DC/Sheet và versioning.
4. Chuẩn bị golden dataset/annotation và tiêu chí AI; tạo guideline cho bbox/table/KIE, train–dev–test/golden set, expected JSON, error taxonomy và field-level metrics.
5. Đặc tả Rule Catalog, confidence và reconciliation; lập validation matrix, cross-document tolerance, threshold theo field, auto-pass/review/block và yêu cầu evidence/explanation.
6. Đặc tả ingestion, integration, reliability và security; tạo naming/folder/manifest/state machine, API/callback/idempotency, retry/quarantine/DLQ, audit/retention/access và error catalog.
7. Thiết kế Review UI, UAT, pilot, KPI và vận hành; bàn giao wireframe, SLA/escalation, golden/regression suite, acceptance/go-live/training/SOP và feedback/retraining loop.

## Nguồn chính

- `OCR & RPA/Báo cáo xây dựng phần mềm RPA v2.docx` — nguồn mạnh nhất về scope 25 use case và KPI.
- `Báo cáo RPA.docx`, `Các usecase áp dụng RPA, OCR (1).docx`, `RPA usecases.docx`, `Kịch bản OCR RPA.docx`.
- `Quản lý ingestion OCR.pdf`, `Phân biệt luồng OCR VLM.pdf`, `AI Document Understanding End-To-End.docx` và các sơ đồ/ảnh — tham khảo kỹ thuật/kiến trúc.

@pagebreak
# 6. AI Hub — Quản trị vòng đời tài sản AI

## Tổng quan

AI Hub là nền tảng nội bộ thuộc Samsung AI Platform, quản trị tập trung vòng đời Dataset, Model, Training, Evaluation, Deployment, Approval, Permission, Audit và Catalog/Reuse. Hồ sơ mô tả vai trò Lead BA khoảng tám tháng từ discovery/idea đến pilot/handover, phối hợp HQ Korea cùng các nhóm Business, AI, Data, Security và Platform.

## Danh mục tính năng

### 1. Dataset Management

- Dataset Card: name, description, owner, sponsor, contributor, department/domain, source, type, format, sensitivity, intended use, license, update frequency, version, schema, labeling và related model/project.
- Template theo domain/type; register/edit/profile; file/source/schema/label; ownership và version history.
- Lineage, status/lifecycle, publish/unpublish, access/share/download và audit/history.

### 2. Data Source Management

- Khai báo DB, API, file, warehouse, data lake, manual upload và external/vendor/purchased source.
- Lưu owner, connection/context, liên kết Dataset; thao tác nhạy cảm chịu Approval/Access Rule.
- Theo dõi trạng thái kết nối, thay đổi schema và tác động đến Dataset liên quan.

### 3. Model Management/Model Registry

- Model Card: name, description, owner/contributor, framework, algorithm, task/domain, artifact/version, intended use, limitation, risk và liên kết Dataset/Training/Evaluation/Deployment.
- Register artifact/version, lineage, ownership/status, publish/catalog, compare/history, usage/access/audit.

### 4. Approval Workflow Engine

- Workflow cho mua tài sản, đăng ký/chia sẻ/sửa/xóa Dataset/Model, Data Source, Training Request và Deployment Request.
- Step theo owner/steward/security/department/sponsor; sequential, parallel, conditional, auto-routing và auto-assignment.
- Delegation/reassign, comment, approve, reject, change request, cancel; SLA, reminder, escalation và email/in-app notification.

### 5. Lifecycle/State Management

- Dataset: Draft → Submitted → Under Review → Change Requested → Approved → Published → In Use → Suspended → Deprecated → Archived → Deleted.
- Model: Draft/Registered → Review/Approved → Training Requested/Running/Completed → Evaluation Pending/Validated → Staging/Production → Deprecated/Archived.
- Training Job: Draft, Submitted, Under Review, Approved, Queued, Running, Failed, Completed, Cancelled, Archived.
- Deployment: Requested, Under Review, Approved for Staging, Staging, Approved for Production, Production, Rollback Requested, Deprecated, Archived.

### 6. Dynamic Permission và Security Governance

- Quyền theo function và data scope, kết hợp role, department, owner/sponsor/contributor/project, sensitivity, usage purpose và asset status.
- Role: Global Admin, Local Admin, Data Owner, Data Steward, Model Owner, AI Engineer/Data Scientist, Reviewer/Approver, Contributor, Viewer và Auditor.
- State–Action Matrix cho view, edit, delete, download, share, approve, train và deploy; cùng role có quyền khác nhau theo trạng thái.

### 7. Catalog, Search và Discovery

- Search keyword; filter/sort theo tag, domain, type, owner, status và sensitivity.
- Browse published asset, bookmark/recent/recommendation, preview Card/Lineage/Quality và request access.
- Visibility và action tuân theo permission/data scope.

### 8. Label và Annotation Management

- Category/label schema, guideline, weight/distribution, version, quality và status.
- Liên kết Dataset version với annotation artifact; theo dõi thay đổi và mức độ hoàn thiện.

### 9. Training Job Management

- Request/configure/approve/queue/run; chọn Dataset/Model/config/resource.
- Progress, log, error, cancel, retry; artifact/output/version, lineage, history và result notification.

### 10. Evaluation Management

- Metrics accuracy, precision, recall, F1, latency, throughput, robustness, fairness và task-specific metric.
- Benchmark, version comparison, report/evidence, threshold/pass–fail, risk/validation status và history.

### 11. Deployment Management

- Request/checklist/evidence; approve Staging/Production; current status/history.
- Rollback Request, Deprecate, Archive; liên kết Model version, Evaluation evidence và owner.

### 12. Module hỗ trợ

- Template Management cho Dataset, Model, Workflow và metadata.
- Notification Center/email/in-app cùng template variable.
- Full Audit Trail cho state, permission, version, approval và access.
- Dashboard về asset, status, approval, training, deployment, quality và usage.

## Luồng, rule và KPI quan trọng

- **End-to-end:** Create from Template → Metadata/Source/Schema/Sensitivity/Ownership → Draft/Validate → Submit Approval → Review/Change/Approve → Publish → Catalog/Search/Request Access/Use → Training → Evaluation → Staging Approval → Production → Monitor/Rollback → Deprecate/Archive.
- **Traceability chain:** Dataset Source/Version → Training Job/Config → Model Artifact/Version → Evaluation Run/Report → Deployment Environment/Version.
- Không Publish khi thiếu approval, mandatory metadata hoặc license; không Train nếu Dataset chưa Approved/Accessible; không Deploy production nếu Model/Evaluation chưa Validated hoặc checklist/evidence không đạt.
- Mọi thay đổi state, permission và version phải audit; quyền thay đổi theo sensitivity/status; owner, steward và auditor có trách nhiệm tách biệt.
- KPI: Draft-to-Approved/Published lead time, approval SLA/bottleneck/rework, metadata completeness, reuse, access turnaround, lineage completeness, training success/queue time, evaluation pass, Staging-to-Production, rollback/deprecation compliance và audit coverage.

## Kiến trúc và công nghệ

**Đã xác nhận:** AI Hub thuộc Samsung AI Platform; công việc BA có Swagger/API mapping; Data Source gồm DB/API/File/Warehouse/Lake; có email/in-app notification, workflow, registry, catalog, audit và dashboard.

**Kiến trúc logic:** Presentation/Catalog → Asset Management (Dataset/Model/Template) → Workflow & Lifecycle → Training/Evaluation/Deployment Orchestration → Integration/API; các lớp nền gồm Metadata/Registry, Artifact Store, Audit, Notification và IAM. Tài liệu không xác nhận framework frontend/backend, cloud, DB, broker hay Kubernetes; không tự gán Java/Spring, React, AWS/Azure hoặc PostgreSQL.

## 7 đầu việc BA đặc thù

1. Discovery và stakeholder alignment với HQ Korea, Business, AI, Data, Security và Platform; tạo stakeholder map/RACI, interview note, problem statement, scope/roadmap, decision/change log và backlog.
2. Thiết kế AI Asset Information Model; tạo Dataset Card/Model Card, Template Catalog, field/data dictionary, mandatory/validation/dependency rule, ERD và version semantics.
3. Mô hình hóa lifecycle/state machine cho Dataset, Model, Training và Deployment; lập state-transition/action matrix, entry/exit criteria, exception, rollback, deprecate và archive flow.
4. Thiết kế reusable Approval Workflow Engine; đặc tả workflow template, routing, parallel/conditional step, approver resolution, SLA, delegation, escalation, reject/change/cancel và notification matrix.
5. Đặc tả dynamic permission và risk control; lập role–function–data matrix, state-sensitive action, visibility/download/share/train/deploy right, sensitivity/usage-purpose control và segregation-of-duties case.
6. Thiết kế governance, lineage và traceability end-to-end; mapping Dataset Version → Training Job → Model Version → Evaluation → Deployment, cùng audit event, ownership/stewardship, license/privacy/retention/deprecation rule.
7. Đặc tả và xác nhận giải pháp qua BRD/SRS/FRD, Epic/User Story/Acceptance Criteria, BPMN/ERD/Wireframe, Swagger/API mapping, RTM, SIT/UAT, release/handover/training và KPI dashboard.

## Nguồn chính

- `AI Hub/AI Hub – System Feature Description.pdf`, `AI Hub/BA làm gì.docx`.
- `AI Hub/AI Hub interview.docx`, `AI Hub/Full thuyết trình.docx`.
- `AI Hub/AI Hub rút gọn.docx`, `AI Hub/AI Hub tính năng bản ngắn.docx`.

@pagebreak
# 7. Smart Factory — Equipment Management, WMS và QMS

## Tổng quan và mức độ ưu tiên

Smart Factory có ba module: **Equipment Management** là trọng tâm; **Warehouse Management System (WMS)** và **Quality Management System (QMS)** là module phụ nhưng có liên kết trực tiếp tới sản xuất. CV xác nhận các capability chính của Equipment gồm equipment master/status, realtime monitoring, alarm/event, downtime, OEE/performance, preventive maintenance, recipe, fault detection và abnormal alert. Phân rã chi tiết dưới đây là diễn giải domain có kiểm soát.

## A. Equipment Management — trọng tâm

### 1. Equipment Master và hierarchy

- Hierarchy nhà máy → area/line → station/work center → machine/equipment → component/tool.
- Thuộc tính: equipment ID, model, serial, vendor, specification, capacity, criticality, location, owner, commissioning date và status.
- Gán equipment vào line/process/product; quản lý compatibility với recipe, material/tool và effective history.
- Version/audit cho master; deactivate thay vì xóa vật lý khi đã có telemetry, alarm hoặc maintenance history.

### 2. Connectivity, tag và telemetry

- Map signal/tag từ PLC/sensor/SCADA/Edge đến equipment và định nghĩa business meaning, unit, scale, sampling rate, threshold.
- Theo dõi heartbeat, online/offline, signal quality, timestamp, current value và last-known value.
- Lọc duplicate/out-of-order event, kiểm clock skew, counter reset, reconnect và data gap.
- Realtime dashboard theo plant/line/equipment, gồm trạng thái, job/product/shift và critical signal.

### 3. Equipment State Model

- State tham khảo: Running, Idle, Setup, Planned Down, Unplanned Down, Maintenance và Offline.
- State transition theo signal/event, có thời điểm bắt đầu/kết thúc, source, confidence và người xác nhận.
- Liên kết shift/calendar, planned production time, changeover/setup và production order.
- Lịch sử state để tính downtime, utilization, Availability và phân tích loss.

### 4. Alarm và Event Management

- Định nghĩa event/alarm code, condition/threshold, severity, equipment, signal, message và recommended action.
- Lifecycle occurrence → active → acknowledge → assign/escalate → clear → close; tách occurrence và recovery.
- Debounce/dedup/suppression để tránh alarm storm; correlation nhiều alarm vào một incident/fault.
- Alarm history, frequency, duration, Pareto theo line/equipment/code/cause; SLA và escalation cho critical alarm.

### 5. Downtime Management

- Tự sinh downtime từ state hoặc operator khai báo; phân biệt planned/unplanned.
- Reason tree nhiều cấp: category → cause → sub-cause; operator/maintenance xác nhận và bổ sung note/evidence.
- Split/merge overlapping event, xử lý shift boundary, micro-stop, setup và khoảng mất telemetry.
- Tính duration, frequency, loss bucket, MTBF và MTTR; Pareto downtime theo thiết bị/nguyên nhân/ca/sản phẩm.

### 6. OEE và performance

- OEE = Availability × Performance × Quality.
- Availability dựa planned production time và downtime; Performance dựa ideal cycle/target speed và actual output; Quality dựa good count/total count.
- Drill-down theo plant, line, equipment, shift, product, order và period; xem A/P/Q riêng và loss bucket.
- Reconcile input calendar, ideal cycle, counter, good/reject count; xử lý counter reset, rework, overlapping downtime và data correction.
- KPI bổ sung: utilization, throughput, cycle time, output/hour, changeover time, MTBF, MTTR và PM compliance.

### 7. Preventive Maintenance

- Maintenance plan theo calendar, runtime, cycle/count hoặc condition threshold.
- Sinh Work Order, priority, maintenance window, assignee/technician, checklist, required skill, spare part/tool và safety instruction.
- Execute/record actual time, finding, action, part used và result; overdue/reminder/escalation.
- Post-maintenance validation, return-to-service approval, history và next due date.
- Liên kết alarm/fault/downtime → maintenance request/WO → root cause/corrective action.

### 8. Recipe Management

- Recipe/parameter master theo product–equipment compatibility; parameter name, unit, standard value, min/max và criticality.
- Version, effective date, draft/review/approve, permission và audit.
- Deploy recipe đến equipment, nhận ACK/result, so actual với standard, cảnh báo mismatch/out-of-range.
- Rollback về version trước; trace recipe version đã dùng cho lot/order/time window.

### 9. Fault/Abnormal Detection

- Rule theo limit, pattern hoặc kết hợp nhiều signal; fault code, severity, symptom, likely cause và recommended action.
- Liên kết abnormal signal → alarm → downtime → maintenance → validation/close.
- Theo dõi repeated fault, top cause, mean time to detect/repair và hiệu quả corrective action.

### 10. Dashboard, report, audit và quyền

- Equipment map/status wall; realtime alarm, downtime/OEE, PM due/overdue và recipe mismatch.
- Trend signal, Pareto alarm/downtime, OEE A/P/Q, MTBF/MTTR, maintenance compliance và export.
- Function/data permission theo plant/line/equipment/role; audit cho master, threshold, reason, maintenance và recipe.

## B. WMS — module phụ

- Material Master; warehouse/zone/rack/bin; capacity và location rule.
- Inbound: PO/ASN → receipt → quality inspection → release → putaway; dock-to-stock và discrepancy handling.
- Outbound: allocation/reservation → picking → packing → Goods Issue; FIFO/FEFO, expiry và picking accuracy.
- Inventory status: Available, Reserved, Quality Inspection, Quality Hold, Blocked, Damaged, In Transit và WIP.
- Transfer giữa location/warehouse, in-transit, reversal và full movement audit; không cho negative stock.
- Lot/batch/serial traceability; WIP, semi-finished, finished goods và genealogy material → production → finished lot.
- Cycle count/stocktake, adjustment approval; KPI inventory accuracy, turnover, aging, stockout, fulfillment, utilization, count variance và expiry.

## C. QMS — module phụ

- IQC, IPQC, FQC/OQC; Inspection Lot, sample và measurement result.
- Material/Product Master, Inspection Type/Characteristic, Specification, LSL/USL, sampling plan, method/equipment.
- So kết quả với specification → pass/fail → disposition → release/block WMS.
- Defect Code/Category/Severity, defect quantity/rate, evidence và root cause.
- Non-Conformance Report; disposition accept/rework/repair/scrap/return/sort/reinspection/deviation.
- CAPA lifecycle; owner, due date, action, verification và closure.
- SPC/control chart, trend và process capability; KPI defect rate, PPM/DPPM, FPY/final yield, scrap/rework, supplier defect, return, Cost of Poor Quality, NCR aging, CAPA closure, Cp/Cpk và lot pass rate.

## Luồng liên module

- WMS release đúng material/lot → line nhận và tiêu hao vật tư/WIP → Equipment ghi state, recipe, output và downtime → QMS nhận Inspection Lot/result.
- QMS reject/defect → Quality Hold lot trong WMS → chặn cấp phát/xuất → tạo NCR/CAPA; severe defect có thể trigger stop-line/Equipment alarm theo rule.
- Traceability cần nối material lot → production order → equipment/recipe version → finished lot → inspection result/disposition.

## Kiến trúc và công nghệ

**Đã xác nhận:** capability realtime monitoring cùng phạm vi Equipment/WMS/QMS. CV có danh sách kỹ năng chung như Java/Spring Boot, REST, Microservices, Redis, Kafka/RabbitMQ, SQL/NoSQL/Time-series nhưng không mapping trực tiếp từng công nghệ vào Smart Factory.

**Kiến trúc logic:** PLC/Sensor/SCADA/Edge → Industrial Adapter/Gateway → Event/Stream Ingestion → Telemetry Time-series + Transactional Master/WO DB → Status/Alarm/OEE/Downtime/Maintenance/Recipe Services → API Gateway/Dashboard → MES/WMS/QMS/ERP. Không khẳng định MQTT, OPC-UA, Kafka, InfluxDB hay TimescaleDB là implementation khi tài liệu chưa xác nhận.

## 7 đầu việc BA đặc thù

1. Khảo sát Gemba với Production, Maintenance và Automation để chuẩn hóa equipment hierarchy, tag/signal, state model và master governance; bàn giao Equipment Dictionary, Tag List và State-transition Matrix.
2. Đặc tả realtime monitoring/alarm với event schema, threshold, severity, debounce/dedup, acknowledge/escalate/close, offline/fault exception; tạo Event Catalog, Alarm Matrix và Sequence/State Diagram.
3. Chuẩn hóa downtime/OEE gồm planned-time exclusion, reason tree, split/merge event, công thức A/P/Q, dimension shift/product/equipment và KPI reconciliation; tạo KPI Dictionary, Formula Sheet và sample calculation/UAT oracle.
4. Thiết kế Preventive Maintenance theo calendar/runtime/cycle, WO/checklist/spare/overdue/post-validation; bàn giao BPMN, Rule Catalog, Wireframe và acceptance criteria.
5. Thiết kế Recipe Governance với parameter/bound, machine–product compatibility, version/effective/approval/deploy/rollback và traceability; tạo Recipe Data Model, Lifecycle và Permission Matrix.
6. Đặc tả integration/lineage giữa Equipment–Production–WMS–QMS, gồm event/API mapping, lot/WIP/equipment correlation và quality-hold/stop-line exception; tạo Context/Sequence Diagram, source–target mapping, idempotency và error rule.
7. Xây UAT bằng telemetry simulation và edge case như out-of-order/duplicate/lost event, reconnect, shift boundary, overlapping downtime, counter reset và recipe mismatch; reconcile Alarm/OEE/Downtime, đào tạo operator và lập go-live/SOP.

## Nguồn chính

- `CV - dự án và tính năng.pdf`, `Hỏi ChatGPT chi tiết/CV_Ban_Tieng_Viet.docx`.
- `Hỏi ChatGPT chi tiết/CV - Chi tiết dự án CV.pdf`, trang mô tả WMS/QMS và domain Smart Factory.
- Các technology mapping trong tài liệu chi tiết chỉ được dùng như tham khảo/diễn giải, không gán thành stack đã triển khai.

@pagebreak
# 8. Samsung Payroll — Quản lý hợp đồng và tính lương

## Tổng quan

Samsung Payroll là hệ thống HRM/Payroll nội bộ, tập trung quản lý hợp đồng, cấu hình lương, tính lương tháng, kiểm tra/đối soát thanh toán, phát hành phiếu lương và báo cáo. Phần này được rút gọn theo yêu cầu ưu tiên; thiết kế Payroll Engine từ link chia sẻ chỉ là tài liệu tham khảo, không phải bằng chứng kiến trúc Samsung đã triển khai.

## Danh mục tính năng cốt lõi

### 1. Hợp đồng và hồ sơ lương

- Contract type/status, effective date, start/end, salary basis, attachment và approval.
- Amendment, renewal, termination, expiry alert và full effective history.
- Kiểm chồng lấn/gap hợp đồng, thay đổi lương giữa kỳ và ownership dữ liệu.

### 2. Dữ liệu đầu vào Payroll

- Hồ sơ nhân viên, hợp đồng, chấm công/ca, nghỉ phép, OT, phụ cấp, thưởng/phạt, tạm ứng và khấu trừ.
- Source mapping, cutoff, missing data, validation và reconciliation trước khi tính.

### 3. Cấu hình thành phần và rule lương

- Income/deduction component; variable dictionary theo Source, Formula, Parameter, Decision Table, Rate Table, Aggregation hoặc Custom.
- Formula/policy/rate/decision table, eligibility, priority, effective date, version, no-match/default và dependency.
- Không hard-code tỷ lệ pháp lý trong báo cáo; mọi mức thuế/bảo hiểm phải configurable và cập nhật theo policy có hiệu lực.

### 4. Monthly Payroll Run

- Mở kỳ, build Payroll Context, resolve policy/variable, lập dependency plan và chạy batch.
- Gross, deduction, tax/insurance, net; proration, rounding, retro adjustment, recalculate và exception handling.
- Validation, variance compare với kỳ trước/source, freeze/lock/unlock và phê duyệt.

### 5. Kiểm tra, thanh toán và kế toán

- Calculation trace từ kết quả về source/rule/formula/version.
- Maker–Checker, payment verification, bank export/confirmation và accounting reconciliation.
- Xử lý partial/unmatched/rejected payment, rerun sau điều chỉnh và segregation of duties.

### 6. Payslip, báo cáo và bảo mật

- Sinh/phát hành payslip, employee detail và payroll summary/component/variance/audit report.
- Permission theo role/đơn vị/period, bảo vệ dữ liệu lương, log download/export và audit thay đổi.

## Luồng và kiến trúc tham khảo

- **Luồng nghiệp vụ:** HR/Contract/Time/Input → Validate/Cutoff → Payroll Context → Policy/Variable Resolution → Formula/Decision Engine → Result + Trace → Review/Approve/Lock → Bank/Accounting/Payslip/Report.
- **Thiết kế tham khảo từ link:** Payroll Context Builder, Policy Resolver, Variable Resolver, Formula Engine, Decision Engine, Calculation Plan, Result Store và Trace Store; dependency graph, effective date, version, priority và no-match rule.
- Link `6a7127ca-...` là cuộc hội thoại thiết kế Payroll có thể đọc được và đã dùng có kiểm soát. Link `6a712749-...` thực tế là nội dung SMAS, không liên quan Payroll nên không sử dụng.

## 7 đầu việc BA đặc thù

1. Mapping Contract Lifecycle vào Salary-effective Timeline và Data Ownership; tạo BPMN vòng đời hợp đồng cùng Field/Effective-date Matrix.
2. Xây Pay Component/Variable Dictionary và Source Mapping từ HR, Contract, Time/Attendance; tạo Component Catalog, Data Dictionary và Source-to-target Mapping.
3. Mô hình hóa Policy, Formula, Decision/Rate Table với eligibility, priority, effective/version, default/no-match; tạo Decision Table, Rule Catalog và Approval/Version Flow.
4. Đặc tả Monthly Calculation Dependency, proration, rounding, retro adjustment, recalculate, freeze và exception; tạo Calculation Flow, Formula Specification và Dependency Graph.
5. Thiết kế Verification/Approval/Payment Reconciliation và Segregation of Duties; tạo Reconciliation Matrix, Maker–Checker BPMN và Control Checklist.
6. Đặc tả Traceability, Payslip, Report, Data Privacy, Access và Audit; tạo mockup, Permission Matrix và Calculation-explainability Schema.
7. Chuẩn bị Golden Payroll Scenario/Boundary Case và đối soát với tính toán của C&B trước UAT Sign-off; tạo Golden Dataset, Expected-result Workbook và Variance/UAT Log.

## Nguồn chính

- `CV - dự án và tính năng.pdf`, `Hỏi ChatGPT chi tiết/CV_Ban_Tieng_Viet.docx`.
- Link tham khảo: `https://chatgpt.com/share/6a7127ca-7e3c-83ec-9b8c-645f1ac10382`.
- Link `https://chatgpt.com/share/6a712749-8100-83ec-b34d-d3fc7309a0fb` đã kiểm tra nhưng là SMAS, không dùng cho Payroll.

@pagebreak
# Phụ lục — Nguồn đã rà soát và giới hạn sử dụng

## Nguồn cấp dự án

- **AI Hub:** sáu file DOCX/PDF trong thư mục `AI Hub` đã được đọc và đối chiếu.
- **CRM:** `CRM.docx` và `DS CHỨC NĂNG CRM.xlsx`; cả hai sheet của spreadsheet đã được kiểm tra.
- **HRAI:** bốn PDF hướng dẫn/luồng/QA, một ảnh màn hình QA.
- **mChat:** SRS, PDF phân tích AI, tài liệu sáng kiến, Markdown phân tích, video giao diện và text bổ trợ. Credential trong text đã bị loại khỏi báo cáo.
- **OCR & RPA:** toàn bộ báo cáo, use case, tài liệu ingestion/OCR/VLM, tài liệu end-to-end và sáu ảnh/sơ đồ trong thư mục.
- **Smart Safe/Smart Factory/Payroll:** CV tổng hợp, hai tài liệu phỏng vấn BA và các tài liệu CV chi tiết.

## Nguồn bổ trợ trong thư mục `Khác`

- Các bảng vận hành, KPI, tờ trình, chi phí, giá trị làm lợi, so sánh nhà cung cấp, checklist đối thủ, CDP tracking và architecture SVG đã được rà soát.
- Chỉ thông tin có liên quan trực tiếp đến capability/edge case của dự án mới được đưa vào báo cáo; KPI cá nhân, nội dung không thuộc tám dự án và nhận định không có bằng chứng được loại khỏi phần mô tả.

## Giới hạn

- Báo cáo ưu tiên mô tả nghiệp vụ/đầu việc BA, không phải tài liệu As-built hay xác nhận pháp lý.
- Tên công nghệ chỉ được trình bày là “đã xác nhận” khi nguồn dự án nêu trực tiếp; phần còn lại được gắn nhãn logic/đề xuất.
- Các tỷ lệ thuế, bảo hiểm, lương tối thiểu và quy định Payroll thay đổi theo thời điểm nên không ghi cứng trong tài liệu.
- Khi dùng cho CV/phỏng vấn, nên điều chỉnh cách xưng hô, thời lượng và mức độ ownership theo hồ sơ cá nhân thực tế.
