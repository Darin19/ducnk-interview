# Đức PO làm dự án VinDynamics

Case thực hành: **Đội robots an ninh bảo vệ Vin University** · Chuẩn bị phỏng vấn ngày 16/11/2026.

## Mục lục

- [1. Phạm vi và câu chuyện chuyển ngành](#1-phạm-vi-và-câu-chuyện-chuyển-ngành)
- [2. Tôi sẽ tiếp cận hệ thống mới như thế nào?](#2-tôi-sẽ-tiếp-cận-hệ-thống-mới-như-thế-nào)
- [3. Product scope: đội robot an ninh VinUni](#3-product-scope-đội-robot-an-ninh-vinuni)
- [4. Kiến trúc tổng thể đề xuất](#4-kiến-trúc-tổng-thể-đề-xuất)
- [5. Luồng xuyên suốt: camera báo sự kiện → robot xác minh → bảo vệ xử lý](#5-luồng-xuyên-suốt-camera-báo-sự-kiện--robot-xác-minh--bảo-vệ-xử-lý)
- [6. Hệ tri thức và AI Agent chatbot cho robot](#6-hệ-tri-thức-và-ai-agent-chatbot-cho-robot)
- [7. BA/QC trong AI training, fine-tune và dữ liệu robot](#7-baqc-trong-ai-training-fine-tune-và-dữ-liệu-robot)
- [8. Hợp đồng tích hợp, dữ liệu và state machine](#8-hợp-đồng-tích-hợp-dữ-liệu-và-state-machine)
- [9. Backlog mẫu, user story và acceptance criteria](#9-backlog-mẫu-user-story-và-acceptance-criteria)
- [10. NFR, lỗi và ranh giới an toàn](#10-nfr-lỗi-và-ranh-giới-an-toàn)
- [11. QC, UAT, commissioning và field feedback](#11-qc-uat-commissioning-và-field-feedback)
- [12. Traceability, SQL/logs, change và release](#12-traceability-sqllogs-change-và-release)
- [13. Industry Solution Packs: áp dụng tư duy workflow và policy từ chính phủ](#13-industry-solution-packs-áp-dụng-tư-duy-workflow-và-policy-từ-chính-phủ)
- [14. Ánh xạ kinh nghiệm cũ sang công việc mới](#14-ánh-xạ-kinh-nghiệm-cũ-sang-công-việc-mới)
- [15. Ma trận phủ JD VinDynamics](#15-ma-trận-phủ-jd-vindynamics)
- [16. Cách làm việc hằng ngày và RACI](#16-cách-làm-việc-hằng-ngày-và-raci)
- [17. Bài trả lời phỏng vấn và ví dụ để kể](#17-bài-trả-lời-phỏng-vấn-và-ví-dụ-để-kể)
- [18. Nguồn và sơ đồ bàn giao](#18-nguồn-và-sơ-đồ-bàn-giao)

## 1. Phạm vi và câu chuyện chuyển ngành

Đây là **phương án giả định để luyện phỏng vấn và thảo luận thiết kế**, không phải mô tả kiến trúc nội bộ, hợp đồng hoặc dự án đã được VinDynamics/VinUni xác nhận. Tên công nghệ là lựa chọn tham chiếu; thông số pilot là giả định phải được khảo sát và phê duyệt. Hai tài liệu người dùng cung cấp, [Tìm hiểu Robot VinDynamics](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/ChatGPT/Tìm hiểu Robot VinDynamics.md>) và [Mã nguồn robot hình người](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/ChatGPT/Mã nguồn robot hình người của các tập đoàn lớn.md>), được dùng như nguồn ý tưởng, không như tài liệu kỹ thuật chính thức của hãng.

Tiền đề kinh nghiệm nằm trong [Đức BA training AI, ML models](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Đức BA training AI, ML models.md>). Nguồn hồ sơ gốc là [CV full](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Kim Đức CV full.pdf>). Phần Tori ở tài liệu trước là mô phỏng BA/QC, không phải kinh nghiệm đã làm. Azure/ML/fleet bổ sung cho Smart Factory cũng là thiết kế đề xuất.

> Tôi chưa coi kinh nghiệm phần mềm doanh nghiệp là kinh nghiệm điều khiển humanoid. Điều tôi mang sang là năng lực phân tích hệ thống có thiết bị, dữ liệu, trạng thái, quyền và nhiều bên tham gia. Smart Safe giúp tôi hiểu cảnh báo và vận hành an ninh; Smart Factory giúp tôi hiểu health, bảo trì và chất lượng; chính phủ giúp tôi về workflow và governance; AI Hub và các sản phẩm AI giúp tôi về dữ liệu, evaluation và release. Tôi có thể dùng nền tảng đó để làm rõ robot phải làm gì, trong điều kiện nào, khi nào không được làm và chứng minh bằng test ra sao, đồng thời học phần robotics cùng Tech Lead.

### Phân vai đúng với JD

Tên file dùng PO theo yêu cầu, nhưng vị trí tuyển dụng là **Senior BA**. Nếu vào vai BA: tôi sở hữu chất lượng và tính nhất quán yêu cầu, phân tích tác động và đề xuất ưu tiên. Nếu được giao thêm PO: tôi mới sở hữu mục tiêu sản phẩm, thứ tự backlog và quyết định release trong phạm vi được ủy quyền. Kiến trúc dưới đây là đề xuất để trao đổi; Tech Lead/Architect chốt HOW. QC chịu kế hoạch/thực thi kiểm thử; vai trò hybrid có thể trực tiếp hỗ trợ nhưng không tự nghiệm thu tất cả phần mình làm.

## 2. Tôi sẽ tiếp cận hệ thống mới như thế nào?

### 2.1. Khảo sát từ hoạt động bảo vệ hiện tại

Không bắt đầu bằng câu hỏi “robot dùng model gì?”. Bắt đầu bằng ca trực: ai tuần tra, khu vực nào hay bỏ sót, sự kiện nào xảy ra, ai xác minh, mất bao lâu, điều gì làm bảo vệ khó xử lý, camera hiện hữu có điểm mù gì. Đi thực địa cả ban ngày và ca tối theo điều kiện được phép; quan sát đông người, đường dốc, cửa kính, thang máy, hành lang hẹp, Wi-Fi và vị trí sạc.

| Đối tượng | Câu hỏi cần chốt | Bằng chứng thu thập |
|---|---|---|
| Trưởng an ninh | Mục tiêu, mức ưu tiên, ai nhận cảnh báo, ai đóng sự cố? | SOP, ca trực, incident log, SLA hiện tại |
| Bảo vệ/Robot Operations | Khi nào cần robot; khi nào thao tác tay; ai có thể tiếp cận robot? | Shadowing, task analysis, pain point list |
| Sinh viên/nhân viên/khách | Robot gây cản trở, khó hiểu hoặc lo ngại gì; kênh yêu cầu giúp đỡ? | HRI interviews, usability scenarios |
| IT/OT và quản lý tòa nhà | Camera/VMS, access control, mạng, thang máy, cửa và BMS có API nào? | Inventory, network/site map, integration constraints |
| Robotics/R&D | Capabilities đã ổn định, ODD, controller, SDK, map/localization, chế độ an toàn? | Demo thật, interface docs, limitation register |
| AI/Data | Model nào sẵn có, nhãn/dataset nào, điều kiện suy giảm và benchmark? | Model/data cards, evaluation report |
| Safety/Security/Privacy | Ai phê duyệt cách vận hành, recording, quyền truy cập và tình huống khẩn cấp? | Hazard/risk register, policy, evidence plan |
| PO/Market Development/PMO | Pilot chứng minh gì, ngân sách/thời gian, khách hàng chấp nhận thế nào? | Product goal, scope, success criteria, milestones |

### 2.2. Năm bản đồ overview cần hoàn thành

1. **Context map:** robot, bảo vệ, người trong campus, camera, hệ thống cửa, mạng, cloud, helpdesk và người quản trị. Chỉ rõ hệ thống sở hữu dữ liệu nào và boundary của nhà cung cấp.
2. **Capability map:** tuần tra, quan sát, phát hiện, tương tác, xác minh, điều phối, sạc, health, vận hành và quản trị AI. Phân biệt đã có/demo/roadmap/chưa kiểm chứng.
3. **Journey và BPMN AS-IS/TO-BE:** một sự cố từ phát hiện tới đóng; bước có con người, SLA và đầu ra bằng chứng.
4. **Data/integration map:** sensor/topic/event → site gateway → mission/incident → evidence → report; mapping schema, owner, tần suất, lỗi và retention.
5. **State/deployment map:** trạng thái robot, mission, incident; dịch vụ nào chạy robot/site/cloud; khi đứt một kết nối còn năng lực nào.

Deliverable: `System Overview v0.1`, glossary, interface inventory, RACI, assumption/risk/dependency log. Dùng Confluence, draw.io, Jira, Figma, Excel, Postman và SQL. Mục tiêu là cả Dev–QC–Deployment–Operations đọc cùng một mô tả, không mỗi đội có một định nghĩa “robot online” khác nhau.

### 2.3. Lộ trình 30–60–90 ngày có đầu ra

| Giai đoạn | Công việc | Deliverable và điều kiện hoàn thành |
|---|---|---|
| Ngày 1–10 | Đọc spec, quan sát demo, thực địa, stakeholder interviews; lập danh sách điều chưa biết | Overview, ODD draft, glossary, scope/assumptions; Tech Lead xác nhận capability baseline |
| Ngày 11–30 | Phân tích 3 luồng ưu tiên; mapping API/event; dựng prototype operations UI; chốt test basis | BPMN, state/API contract, backlog ready tối thiểu cho sprint kế tiếp; QC review AC; PO chốt pilot |
| Ngày 31–60 | Refinement/daily clarification; review demo; xây gold scenarios; SIL/HIL và integration testing | RTM, test reports, defect taxonomy, deployment checklist; blocker safety/integration được xử lý trước field |
| Ngày 61–90 | Pilot có giám sát; onsite acceptance; thu telemetry/feedback; điều chỉnh backlog | Pilot report, business KPI, re-validation evidence, training/SOP, quyết định mở rộng có điều kiện |

Mốc là kế hoạch mẫu; không cam kết 90 ngày đủ production nếu platform robot hoặc site chưa sẵn sàng.

## 3. Product scope: đội robot an ninh VinUni

### 3.1. Product goal và giả định

Mục tiêu: tăng độ bao phủ tuần tra và tốc độ cung cấp thông tin cho bảo vệ, đồng thời duy trì tương tác an toàn và khả năng kiểm soát của con người. Robot quan sát, báo cáo, hỗ trợ chỉ dẫn và tạo bằng chứng; nhân viên an ninh quyết định xử lý sự việc.

Pilot giả định **3 robot, 1–2 khu nhà, tuyến bằng phẳng đã khảo sát**, có nhân sự giám sát, không thử cầu thang/địa hình phức tạp trước khi có capability và phê duyệt tương ứng. Đây là giả định thiết kế, không phải thông tin về VinUni. Nếu phần cứng là humanoid, cơ chế đi đứng do platform/vendor cung cấp và được kiểm chứng; không coi Nav2 là bộ điều khiển giữ thăng bằng.

**ODD — Operational Design Domain** mô tả ranh giới vận hành: loại mặt sàn/độ dốc, bề rộng, ánh sáng, mưa/nước, mật độ người, bản đồ, vùng cấm, tín hiệu mạng, tải trọng và giới hạn pin. BA ghi các điều kiện và cách nhận biết ngoài ODD; Robotics/Safety xác nhận ngưỡng vật lý bằng thử nghiệm và phân tích rủi ro.

### 3.2. Use case và thứ tự phát triển

| ID | Use case | Trigger → kết quả | Phạm vi |
|---|---|---|---|
| SEC-01 | Tuần tra định kỳ | Lịch/ca trực → route checkpoints → báo cáo | MVP |
| SEC-02 | Camera/cảm biến báo sự kiện | Event → incident → robot phù hợp quan sát từ vị trí an toàn → bảo vệ xác minh | MVP sau integration gate |
| SEC-03 | Robot phát hiện bất thường | Vision/rule → evidence + alert → human review | MVP giới hạn loại sự kiện |
| SEC-04 | Hỏi đường/yêu cầu trợ giúp | Người gọi → xác nhận nhu cầu → trả lời KB hoặc gọi bảo vệ | Giai đoạn tiếp theo |
| SEC-05 | Telepresence/teleoperation | Người có quyền yêu cầu → phiên điều khiển độc quyền → trả quyền | MVP ở chế độ được vendor hỗ trợ |
| SEC-06 | Pin thấp/sạc | Dự báo không đủ năng lượng → handover nhiệm vụ → dock | MVP theo capability phần cứng |
| SEC-07 | Thiết bị suy giảm | Health alert → hạn chế capability/maintenance ticket | MVP |
| SEC-08 | Báo cáo ca trực | Mission/incident/evidence → bản tổng hợp được kiểm tra | Sau khi data pipeline ổn định |

Chưa đưa vào pilot: truy đuổi/khống chế người, tự nhận dạng sinh viên bằng khuôn mặt, tự kết luận người vi phạm, mở khóa cửa theo yêu cầu tự do, tác vụ thao tác tay chưa được kiểm chứng. Đây là quyết định scope cụ thể cho case an ninh có người đi lại, không phải suy đoán robot không có năng lực đó.

### 3.3. Chỉ số thành công đo từ đâu?

| Mục tiêu | Metric và mẫu số | Nguồn |
|---|---|---|
| Bao phủ tuần tra | Checkpoint hoàn tất hợp lệ / checkpoint đến hạn trong ODD | Mission events; lý do bỏ lỡ riêng |
| Hữu ích cho bảo vệ | Thời gian event → bảo vệ có evidence dùng được, median/p95 | Trace event/evidence/view timestamps |
| Chất lượng cảnh báo | Confirmed true events / reviewed alerts; false alarms/robot-hour | Incident adjudication; không bỏ qua pending |
| Hoàn thành nhiệm vụ | Mission thành công / mission đã chấp nhận trong scope; report abort reason | Mission state ledger |
| Mức can thiệp | Human interventions/mission hoặc /robot-hour, phân loại | Teleoperation/handover logs |
| Khả dụng | Thời gian đủ capability / thời gian lịch yêu cầu; phân planned/unplanned | Health + schedule + maintenance |
| HRI | Tỷ lệ hiểu đúng intent, gọi hỗ trợ thành công, đánh giá usability | Test transcripts và thử nghiệm người dùng |
| Chi phí | Cost/robot-hour hữu ích, cost/mission, công vận hành/bảo trì | Billing + ops + mission logs |

Đặt target sau đo baseline; với các chỉ số pilot ghi rõ cỡ mẫu, tuyến, điều kiện và phiên bản. “Không có va chạm trong pilot” là kết quả thử nghiệm giới hạn, không chứng minh an toàn tuyệt đối.

## 4. Kiến trúc tổng thể đề xuất

![Kiến trúc đội robot an ninh VinUni](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/08-vinuni-robot-platform.drawio.png>)

### 4.1. Phân lớp và công nghệ cụ thể

| Lớp | Công nghệ tham chiếu | Trách nhiệm |
|---|---|---|
| Robot hardware/control | Camera RGB/depth, LiDAR nếu có, IMU, encoder, microphone, battery/BMS, E-stop; controller/SDK của hãng | Đo thế giới, chuyển động, cân bằng; safety circuit độc lập theo thiết kế phần cứng |
| Robot middleware | ROS 2 Jazzy làm baseline khảo sát, DDS/Fast DDS hoặc Cyclone DDS theo platform | Nodes, topics, services, actions, QoS; chốt distro/OS/vendor compatibility trước sử dụng |
| Navigation/skills | Vendor locomotion; Nav2 khi phù hợp; BehaviorTree.CPP cho task execution | Route/local planning, skill có goal/feedback/result, fallback được kiểm chứng |
| Edge perception | YOLOX + ByteTrack; ONNX Runtime/TensorRT; Jetson Orin hoặc máy tính tương đương theo benchmark | Detect/track, vùng quan sát; model không trực tiếp điều khiển actuator |
| Site edge | Industrial server, Docker; MQTT broker EMQX; local mission adapter, SQLite/PostgreSQL buffer | Kết nối robot/site, offline queue, đồng bộ cloud; không thay controller an toàn |
| Mission/fleet | ASP.NET Core modular backend; PostgreSQL; Open-RMF adapter nếu tương thích | Mission lifecycle, capability/energy/resource checks, allocation, incident linkage |
| Business workflow | Camunda 8 BPMN; OPA policy service | Human task, escalation, policy/industry pack; license/runtime cần thẩm định |
| Cloud trên Azure | IoT Hub/DPS, Service Bus, Container Apps; ADLS/Blob, Azure SQL/PostgreSQL, ADX | Identity/telemetry, API, event processing, lưu bằng chứng và báo cáo |
| AI assistant | FastAPI + LangGraph; Qwen qua vLLM; Qdrant/OpenSearch RAG; speech pipeline | Hiểu yêu cầu, tìm tri thức, đề xuất tool, giải thích có nguồn |
| Ops UI | React/TypeScript; map/floor plan; WebRTC cho phiên video nếu được hỗ trợ | Fleet status, incident inbox, mission timeline, quyền điều khiển |
| Observability/release | OpenTelemetry, Prometheus/Grafana hoặc Azure Monitor; MLflow/Azure ML, ACR/Azure DevOps | Trace, health, model evaluation, artifact/version, rollout và rollback |

Đây là modular architecture; không có yêu cầu tạo một microservice cho mỗi ô. Pilot có thể dùng một backend chia module Mission/Fleet/Incident/Configuration, giữ riêng robotics runtime, AI inference và evidence storage theo tính chất tải/quyền.

ROS 2 cung cấp topic/service/action; action phù hợp tác vụ có goal, feedback và result. Open-RMF là nền tảng tích hợp/điều phối cần adapter, không phải giải pháp tự biến humanoid thành robot đi an toàn. [ROS 2 interfaces](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Concepts/Basic/About-Interfaces.rst), [Open-RMF](https://github.com/open-rmf/rmf).

### 4.2. Edge/cloud chia theo độ trễ, tính tự chủ và dữ liệu

- **Robot:** điều khiển thời gian thực, tránh va chạm/giám sát an toàn theo platform, cảm biến, localization, skill execution và phản ứng khi mất mạng. Cloud mất không được làm mất cơ chế an toàn cục bộ.
- **Site:** gateway camera/cửa, buffering, đồng bộ, điều phối cục bộ trong phạm vi đã thiết kế, dashboard tối thiểu nếu cần. Nếu không có điều phối cục bộ thì mất cloud phải chuyển mode rõ ràng, không giả định vẫn làm mọi nhiệm vụ.
- **Cloud:** fleet lịch dài hạn, quản trị nhiều site, workflow, dataset/training, báo cáo, KB và model lớn khi băng thông cho phép.

Truyền telemetry metadata liên tục; gửi ảnh/clip theo event và quyền, không stream mọi camera về cloud mặc định. Video và dữ liệu điều khiển đi kênh riêng: WebRTC/RTSP theo adapter cho media; MQTT/HTTPS cho event/command ở tầng ứng dụng. DDS chủ yếu trong robot/mạng được thiết kế; không mở thẳng ROS graph ra Internet.

### 4.3. Bốn tầng “điều phối” phải phân biệt

| Tầng | Ví dụ | Cơ chế phù hợp |
|---|---|---|
| Nghiệp vụ | Incident cần bảo vệ xác minh rồi đóng | BPMN/Camunda, tác vụ người, SLA |
| Fleet | Robot nào nhận mission, ai giữ dock/đoạn đường | Scheduler + allocation/resource reservation |
| Skill | Đi tới waypoint, quan sát, phát lời nhắc, dock | Behavior tree/state machine + ROS 2 Action |
| Motion/control | Giữ thăng bằng, điều khiển khớp, phản ứng vật lý | Vendor controller, điều khiển thời gian thực và cơ chế safety |

LangGraph/LLM có thể đề xuất nhiệm vụ mức cao, không thay cả bốn tầng. Nav2 phù hợp bài toán navigation trong phạm vi platform hỗ trợ; humanoid cần thêm footstep/whole-body/locomotion controller và kiểm chứng riêng. [Nav2 documentation](https://docs.nav2.org/).

## 5. Luồng xuyên suốt: camera báo sự kiện → robot xác minh → bảo vệ xử lý

![Luồng nhiệm vụ, handover và xử lý ngoại lệ](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/09-vinuni-mission-flow.drawio.png>)

1. Camera ở hành lang phát hiện người trong vùng theo lịch giám sát. Event có camera/site/zone/time/model version/evidence; “có người” chưa đồng nghĩa “người xâm nhập”.
2. Event service validate/dedupe/correlate; tạo incident `OPEN`, kiểm tra policy đang hiệu lực và hiện trạng camera.
3. Security workflow tạo yêu cầu `observe_zone`, gắn `incident_id`, vị trí quan sát an toàn và deadline. Mission service kiểm tra quyền, scope và dữ liệu cần thiết.
4. Fleet lọc robot có capability, health, pin/đường về sạc, map version và route trong ODD; sau đó mới chấm chi phí/ETA.
5. Scheduler tạo assignment lease/reservation và gửi command có `command_id`, `mission_id`, TTL, `assignment_epoch`. Robot ACK việc nhận hoặc reject vì điều kiện đã thay đổi.
6. Edge recheck policy/health và controller readiness. Skill runtime gọi ROS Action điều hướng; feedback cập nhật tiến độ. Safety controller được ưu tiên hơn mission.
7. Tới observation point, robot thu evidence. Detector/rules đưa tín hiệu; VLM nếu dùng chỉ tóm tắt vùng ảnh được cấp, không tự xác nhận danh tính hay hành vi vi phạm.
8. Dashboard gửi clip/cảnh báo cho bảo vệ. Tương tác bằng lời chỉ theo phrase/template được duyệt; không gây cản trở và không tự tăng mức phản ứng.
9. Bảo vệ xác minh, phân loại false alarm/needs action/incident confirmed; tạo ticket hoặc can thiệp. Robot có thể giữ vị trí an toàn, chuyển telepresence hoặc nhận nhiệm vụ mới theo quy tắc.
10. Mission kết thúc khi có bằng chứng nhiệm vụ quan sát hoàn tất; incident chỉ đóng khi người có thẩm quyền hoàn thành xử lý. Hai vòng đời không được gộp thành một nút “Done”.

**Ngoại lệ:** không có robot đủ điều kiện → chuyển bảo vệ; không nhận ACK → kiểm tra assignment trước retry; robot mất mạng sau nhận → mission ở trạng thái execution chưa xác định, áp chính sách offline/lease thay vì lập tức giao trùng; robot không tới được → cung cấp lý do và evidence, không báo thành công.

### 5.1. Logic phân công fleet

Hard constraints trước: tenant/site, ODD, skill/version, safety readiness, localization freshness, năng lượng cho nhiệm vụ + dự phòng + tới điểm sạc, route/access, payload, maintenance lock, không bị teleoperation khác giữ quyền.

Sau khi lọc, score có thể là `w1*ETA + w2*energy_cost + w3*workload + w4*coverage_gap_penalty`. Weights được thử nghiệm bằng dữ liệu/simulation. Robot gần nhất chưa chắc tốt nhất nếu pin thấp hoặc route bị chặn. Fleet assignment không tự giải quyết collision avoidance.

Tài nguyên chia sẻ: hành lang hẹp, thang máy, cửa, dock. Dùng reservation có timeout và cơ chế phân xử; vẫn cần local obstacle avoidance. Khi lease hết hạn mà chưa xác minh robot cũ dừng, chỉ được tái giao theo protocol có fencing/epoch và kế hoạch an toàn; không dùng timeout làm bằng chứng thế giới vật lý đã hoàn tác.

## 6. Hệ tri thức và AI Agent chatbot cho robot

### 6.1. Phân tách ba nhóm tri thức

| Nhóm | Nguồn và cách lưu | Cách truy cập |
|---|---|---|
| Công khai | Bản đồ hướng dẫn, giờ hoạt động, điểm dịch vụ được công bố | RAG theo site/version; trả lời khách |
| Nội bộ vận hành | SOP an ninh, escalation, maintenance, skill limitations | RAG có role/scope; chỉ operator được phép |
| Dữ liệu thời gian thực | Mission, battery, health, vị trí, incident, cửa | API/tool có quyền; không coi vector index là nguồn realtime |

Sơ đồ nền dùng lại [Hệ tri thức và RAG](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/01-knowledge-rag.drawio.png>) và [Agent workflow](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/02-agent-workflow.drawio.png>). Tài liệu trước đã mô tả ingestion, chunking, hybrid search, reranking, memory, ACL và fine-tuning; tại robot thêm context site–zone–map–mission–ODD.

### 6.2. Pipeline cụ thể

SOP/map guide/FAQ → Tika hoặc PaddleOCR → human content review → MinIO/Blob bản gốc + PostgreSQL metadata → chunks có `site_id`, `visibility`, `effective_from/to`, `source_owner`, `map_version` → bge-m3 embedding → Qdrant + OpenSearch → bge reranker → Qwen2.5-7B-Instruct/vLLM → output schema/citation checks.

Hội thoại giọng nói: microphone → voice activity detection (Silero VAD) → **faster-whisper** STT baseline → intent/context → agent → approved answer → **Azure AI Speech** TTS hoặc engine edge đã benchmark tiếng Việt. STT confidence/quality thấp thì hỏi lại; xác thực quyền không dựa vào giọng nói tự nhận. Việc dùng Whisper/Speech ở đây là lựa chọn thiết kế, không phải stack của VinDynamics đã biết.

LangGraph graph đề xuất:

`Receive → Identify user mode → Resolve site/context → Classify intent → Public KB | Operator KB | Read tool | Propose mission → Policy validation → Answer/Confirm → Execute permitted API → Verify → Report`.

Giới hạn số vòng tool, timeout tổng và token/cost budget. Trace lưu quyết định ở dạng cấu trúc, nguồn và tool results đã mask; không yêu cầu log chuỗi suy nghĩ nội bộ của model. Không đưa lịch tuần tra nhạy cảm hoặc nội dung camera vào câu trả lời khách công khai.

### 6.3. Tool catalog mẫu

| Tool | Actor | Input/output | Chính sách |
|---|---|---|---|
| `lookup_public_location` | Khách/người trong campus | Tên nơi → chỉ dẫn đã được duyệt | Read-only, vùng công khai |
| `search_security_sop` | Bảo vệ/operator | Tình huống → đoạn SOP có nguồn/phiên bản | Role/site filter ở backend |
| `get_robot_health` | Operator | Robot ID → health + freshness | Không coi dữ liệu cũ là trạng thái hiện tại |
| `get_incident_context` | Bảo vệ có scope | Incident ID → timeline/evidence token | Evidence URL ngắn hạn, kiểm tra quyền khi tải |
| `propose_patrol_mission` | Operator | Zone/time → draft + feasible constraints | Chỉ tạo đề xuất; không trực tiếp chạy skill |
| `submit_mission` | Dispatcher | Draft ID + expected version → mission ID | Confirmation + OPA + state/ODD checks |
| `request_guard_help` | Người cần trợ giúp | Location + mô tả tối thiểu → ticket/ack | Chống spam theo policy; không yêu cầu thông tin cá nhân không cần thiết |

**Không cấp tool trực tiếp kiểu `set_joint_torque` cho LLM.** Với lệnh “đi theo người áo đỏ”, agent phải kiểm tra use case được phép và xin làm rõ/phê duyệt khi cần; không suy ra đây là quyền theo dõi mọi người trong campus. Prompt/system instruction không phải cơ chế an toàn vật lý.

### 6.4. BA/QC của hệ tri thức robot

BA lập ontology `Site–Zone–Place–Route–Capability–Skill–Policy–Mission–Incident`; Knowledge Graph chỉ thêm khi cần truy vấn nhiều quan hệ và có provenance. Nguồn SOP do owner duyệt, bản đồ từ mapping team, realtime từ API. Định nghĩa `unknown/stale/conflict` thành kết quả hợp lệ thay vì ép AI luôn trả lời.

Golden set gồm: hai phòng trùng tên khác tòa; lối đi thay đổi sau sửa chữa; khách yêu cầu vào vùng cấm; operator ngoài site; tài liệu đã hết hiệu lực; hỏi bí mật lịch tuần tra; câu tiếng Việt không dấu/tiếng Anh/mã phòng; tiếng ồn và câu nói bị cắt; tool timeout; hội thoại bị chen ngang; nguồn chứa prompt injection.

Chấm riêng STT, intent/slots, retrieval, answer, tool selection/arguments, permission, task outcome và HRI. Nói đúng tên phòng nhưng dẫn qua vùng cấm vẫn fail. Trả lời có nguồn cũ sau đổi map vẫn fail. Yêu cầu hành động không thể hoàn thành phải được nói rõ, không thông báo “đã gửi robot” khi mới tạo draft.

## 7. BA/QC trong AI training, fine-tune và dữ liệu robot

### 7.1. Bốn loại model có quy trình khác nhau

| Loại | Dataset | BA/QC đóng góp | Engineer sở hữu |
|---|---|---|---|
| Vision detector/event model | Ảnh/video theo camera/site, label object/event | Event taxonomy, annotation guide, negative examples, condition coverage | Training code, augmentations, inference optimization |
| LLM/VLM assistant | Q&A có nguồn, hội thoại, image-question, tool-call samples | Ground truth, rubric, refusal/permission cases, error adjudication | Base model choice, LoRA/SFT setup, serving |
| Tabular ML cho health/ETA | Telemetry windows, incident, maintenance, mission outcomes | Định nghĩa target/horizon và data leakage rules | Feature implementation, model/calibration |
| Robot skill/VLA/policy | Episode observations/actions/proprioception, success/safety labels | Task definition, success/failure criteria, dataset coverage, test protocol | Teleoperation capture, imitation/RL, dynamics/control và sim-to-real |

Không gọi mọi feedback về robot là “fine-tune LLM”. Vision update, navigation config, workflow policy và VLA training là những thay đổi khác nhau, có gate khác nhau.

### 7.2. Open-source dùng ở đâu?

| Dự án | Có thể nghiên cứu/tận dụng | Điều không được suy ra |
|---|---|---|
| ROS 2 | Middleware, interface, tool introspection/replay | Không có sẵn mọi driver/control/safety certification |
| Open-RMF | Fleet adapters, task/traffic/resource integration | Không thay robot controller hoặc tự hỗ trợ mọi humanoid |
| NVIDIA Isaac GR00T | VLA/pretrained policy và adaptation cho robot tương thích | Không phải sản phẩm an ninh hoàn chỉnh; code/weights/license cần xem riêng |
| NVIDIA Isaac Lab | Robot learning trong mô phỏng | Sim success không bảo đảm real success |
| Hugging Face LeRobot | Dữ liệu, policy và pipeline học kỹ năng | Không bảo đảm chạy ngay trên hardware VinDynamics |
| Nav2/BehaviorTree.CPP | Navigation/task execution trong phạm vi tương thích | Không cung cấp giữ thăng bằng hai chân |

Đã đối chiếu kho chính thức: [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T), [Isaac Lab](https://github.com/isaac-sim/IsaacLab), [LeRobot](https://github.com/huggingface/lerobot). Không chốt “model mới nhất” hoặc giấy phép thương mại cho toàn bộ ecosystem từ một README; khi chọn phải pin commit/version, xem code/model/data license, supported embodiment và compute requirement.

### 7.3. Quy trình dữ liệu đến release

![Đánh giá và phát hành AI/robot theo từng tầng](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/10-robot-evaluation-release.drawio.png>)

1. **Scenario specification:** BA định nghĩa tác vụ/ODD, precondition, success, failure, abort, human takeover; QC lập matrix bao phủ.
2. **Capture:** engineer/ops ghi camera, sensor, command, state và intervention đồng bộ thời gian; dùng rosbag2/MCAP hoặc format của platform. Thu đúng quyền và giới hạn dữ liệu; đây là công cụ robot đề xuất, chưa phải kinh nghiệm cũ.
3. **Dataset curation:** kiểm tra timestamp, calibration, dropped frames, episode boundary, bản đồ và robot version; loại/đánh dấu dữ liệu hỏng. Nhãn perception khác nhãn hành động và task success.
4. **Split:** theo site, ca/ngày, người biểu diễn, episode hoặc robot tùy mục tiêu. Không đưa frame/step liền nhau của cùng episode vào train và test khác nhau.
5. **Train:** AI/Robotics Engineer chọn detector/LoRA/VLA/IL/RL; BA/QC quản lý semantics, coverage và golden scenarios. Reward RL cần phản ánh success và violation; chặn reward hacking bằng điều kiện kiểm tra độc lập.
6. **Offline evaluation:** metric model, hard negatives, safety/permission cases, performance trên target hardware; đánh giá quantized model, không chỉ full precision.
7. **Simulation/SIL → HIL → khu vực kiểm soát:** tăng độ khó theo gate; mô phỏng người/obstacle/mất mạng và sensor faults khi an toàn. Simulation không thay hazard analysis hoặc thử nghiệm phần cứng.
8. **Shadow/canary:** vision/assistant có thể shadow, không tác động điều khiển; policy hành động phải test môi trường kiểm soát trước, không A/B ngẫu nhiên hành vi chưa kiểm chứng với người đi lại.
9. **Release:** manifest ràng buộc firmware/controller/model/skill/map/policy, người duyệt, test run và rollback path. Theo dõi drift và field failures, không auto-retrain rồi tự rollout.

**Manifest đề xuất:** `robot_type`, `hardware_revision`, `firmware`, `ros_distro`, `driver_version`, `model_id/hash`, `preprocess_version`, `skill_version`, `map_version`, `policy_pack_version`, `evaluation_run_id`, `approved_by`, `rollback_bundle`. Đây là kế thừa trực tiếp tư duy AI Hub.

## 8. Hợp đồng tích hợp, dữ liệu và state machine

### 8.1. API/command mẫu cho BA dùng với developer

```http
POST /v1/sites/VINUNI-PILOT/missions
Authorization: Bearer <operator-token>
Idempotency-Key: <request-uuid>
Content-Type: application/json
```

```json
{
  "mission_type": "observe_zone",
  "incident_id": "INC-DEMO-001",
  "zone_id": "BUILDING-A-LOBBY",
  "observation_point_id": "SAFE-POINT-02",
  "requested_capabilities": ["navigate", "capture_evidence"],
  "priority": "P2",
  "expires_at": "2026-11-16T15:30:00Z",
  "map_version": "map-demo-v3",
  "policy_pack_version": "security-demo-v2"
}
```

Ví dụ schema, không phải API hãng. Backend lấy actor/tenant từ token, kiểm tra scope; server kiểm tra quyền đặt priority. `202 Accepted` chỉ xác nhận nhận yêu cầu và trả `mission_id/state=VALIDATING`, chưa có nghĩa robot đã chạy. Schema nên ràng buộc enum, length, coordinate frame, unit, nullable và time format.

Error contract: `400 INVALID_REQUEST`, `403 FORBIDDEN`, `409 STATE_CONFLICT/IDEMPOTENCY_CONFLICT`, `422 OUTSIDE_ODD/INCOMPATIBLE_CAPABILITY`, `503 NO_ELIGIBLE_ROBOT/SERVICE_UNAVAILABLE` tùy policy API đã chốt. Retry sau 503 khác retry sau 403; không tự retry vô hạn. Một idempotency key với payload khác phải reject.

### 8.2. Event contract

```json
{
  "event_id": "evt-demo-001",
  "schema_version": "1.0",
  "event_type": "mission.progress",
  "robot_id": "R-DEMO-01",
  "site_id": "VINUNI-PILOT",
  "mission_id": "M-DEMO-001",
  "command_id": "C-DEMO-001",
  "assignment_epoch": 7,
  "sequence_no": 14,
  "boot_id": "boot-demo-a",
  "observed_at": "2026-11-16T15:00:04Z",
  "received_at": "2026-11-16T15:00:05Z",
  "state": "NAVIGATING",
  "map_version": "map-demo-v3",
  "trace_id": "trace-demo-001"
}
```

Phân biệt thời gian sự kiện và thời gian nhận; lưu UTC và hiển thị Asia/Saigon. `boot_id` giúp diễn giải sequence reset; không so sequence của hai lần boot như một chuỗi. Location phải có frame/map/uncertainty; tọa độ bản đồ tầng không tự đồng nhất với GPS.

### 8.3. ROS 2 concepts ở mức BA cần dùng

| Interface | Ví dụ minh họa | BA phải đặc tả |
|---|---|---|
| Topic | `/battery_state`, `/robot_health`, `/pose` | Schema, unit, frame, frequency, freshness, QoS và behavior khi stale |
| Service | `get_capabilities`, `validate_goal` | Request/response, timeout, error; tác vụ nên ngắn |
| Action | `navigate_to_observation_point`, `dock` | Goal, feedback, result, reject, cancel/preempt và timeout |

Tên trên là đề xuất, không khẳng định topic/API của robot thực. QoS reliable không có nghĩa mọi dữ liệu đều mới hoặc side effect chỉ xảy ra một lần. Sensor stream có thể ưu tiên latest/best-effort; command cần protocol ứng dụng và ACK; cấu hình cụ thể do Robotics Lead chốt.

### 8.4. Trạng thái cần tách riêng

| Entity | State chủ yếu | Quy tắc |
|---|---|---|
| Robot connectivity | ONLINE / STALE / OFFLINE | Dựa trên heartbeat freshness; không bằng operational readiness |
| Robot operation | READY / BUSY / DEGRADED / MAINTENANCE / SAFETY_STOP | Capability availability là kết quả health + mode + policy |
| Mission | DRAFT → VALIDATING → QUEUED → ASSIGNED → ACKNOWLEDGED → EXECUTING → SUCCEEDED | Nhánh REJECTED, PAUSED, FAILED, CANCELLING → CANCELLED; timeout có thể là EXECUTION_UNKNOWN |
| Incident | OPEN → TRIAGED → INVESTIGATING → RESOLVED → CLOSED | Bằng chứng và người đóng; có REOPENED theo policy |
| Command | CREATED → SENT → ACCEPTED → RUNNING → SUCCEEDED/FAILED | ACCEPTED khác hoàn tất; duplicate giữ cùng command ID |

Transition `EXECUTING → SUCCEEDED` cần result hợp lệ và evidence yêu cầu. `CANCELLING → CANCELLED` chỉ khi xác nhận kết thúc/giành quyền theo protocol; UI không được gọi “đã dừng” chỉ vì bấm nút. Safety stop cần điều kiện khôi phục và người được phép; không tự resume sau reconnect.

## 9. Backlog mẫu, user story và acceptance criteria

### 9.1. Các epic

| Epic | Nội dung | Căn cứ ưu tiên |
|---|---|---|
| E01 Site & ODD setup | Zone/map/route, role, policy, capability baseline | Điều kiện trước vận hành |
| E02 Fleet & Mission | Schedule, allocation, state, cancel, handover | Luồng giá trị cốt lõi |
| E03 Event & Incident | Camera adapter, dedupe, evidence, escalation | Cung cấp thông tin hữu ích cho bảo vệ |
| E04 Health & Safety behavior | Freshness, degraded mode, fault handling, E-stop status | Gate bắt buộc trước field |
| E05 AI Assistant & HRI | KB, speech, tool policy, handover | Sau khi core vận hành có kiểm soát |
| E06 Data & Evaluation | Dataset, labeling, metric, regression, lineage | Xuyên suốt, không chờ cuối dự án |
| E07 Configuration & Release | Config approval, version compatibility, rollout/rollback | Tránh thay đổi không truy vết |
| E08 Commercial Operations | Tenant/site package, SLA, usage, support | Sau pilot chứng minh giá trị |

PO chọn ưu tiên theo value, risk, dependency và readiness. BA đề xuất và chứng minh phụ thuộc; không dùng điểm RICE để đẩy gate an toàn xuống sau tính năng đẹp.

### 9.2. Story SEC-01-03: phân công robot tuần tra

**Là** điều phối viên, **tôi muốn** hệ thống chỉ phân công robot đủ điều kiện cho tuyến tuần tra, **để** route được thực hiện trong phạm vi đã phê duyệt và bảo vệ thấy rõ khi cần can thiệp.

Preconditions: site/map/policy có hiệu lực; schedule được duyệt; có capability catalog và health feed. Happy path: tạo mission → validate → chọn robot → gửi assignment → nhận ACK → theo dõi checkpoint → report.

Acceptance criteria:

```gherkin
Given robot R1 có dữ liệu health quá hạn freshness threshold đã cấu hình
When scheduler lựa chọn robot cho mission tuần tra
Then R1 không thuộc danh sách đủ điều kiện
And reason_code là HEALTH_STALE và quyết định được ghi audit

Given request tạo mission đã thành công với cùng idempotency key
When client gửi lại cùng payload sau timeout
Then server trả cùng mission_id
And không tạo thêm assignment hoặc lệnh di chuyển

Given không có robot đủ điều kiện
When hết thời gian chờ trong policy
Then mission được chuyển tới hàng đợi can thiệp của bảo vệ
And dashboard nêu rõ nguyên nhân và không hiển thị “đang tuần tra”

Given robot đã ACK nhưng mất kết nối trước completion
When cloud hết thời gian chờ feedback
Then trạng thái thể hiện chưa xác định tiến trình thực thi
And hệ thống áp dụng protocol offline và quyền điều khiển đã thiết kế
And không lập tức gửi lệnh trùng cho robot khác chỉ dựa trên timeout
```

### 9.3. Story SEC-02-05: human verification

Là bảo vệ, tôi muốn xem clip, thời gian và nguồn cảnh báo trước khi phân loại sự cố, để phản ứng dựa trên bằng chứng. AC: clip đúng incident/site/time window; quyền tải kiểm tra lại; clip chưa có thì hiển thị pending chứ không lấy clip khác; mark false alarm yêu cầu reason; sửa kết luận giữ lịch sử; mission hoàn thành không tự đóng incident.

### 9.4. Story SEC-04-02: hội thoại hỏi đường

Là khách, tôi muốn hỏi vị trí bằng tiếng Việt và nhận chỉ dẫn trong vùng công khai. AC: tên địa điểm mơ hồ phải hỏi lại; map cũ bị chặn theo policy; không tiết lộ khu vực nội bộ; khi không nghe rõ thì xác nhận; đang ở mode yêu cầu tập trung an toàn thì hoãn hội thoại theo thiết kế HRI. Nói “đưa tôi tới phòng máy chủ” không tự tạo mission dẫn vào vùng hạn chế.

### 9.5. Definition of Ready và Definition of Done

**Ready:** actor/value, ODD/precondition, main/alternative/exception flows, schema/API dependencies, state/error/fallback, AC đo được, test data và owner quyết định. Không đưa story “AI hiểu mọi tình huống” vào sprint mà không có coverage và boundary.

**Done:** code review và kiểm thử phù hợp đã đạt, AC có evidence, RTM cập nhật, known limitations ghi rõ, telemetry/log đủ truy vết, docs/config/version đồng bộ; nếu thuộc field release phải có gate và người duyệt tương ứng. “Demo chạy một lần” chưa đủ Done cho release hiện trường.

## 10. NFR, lỗi và ranh giới an toàn

### 10.1. NFR phải đo được nhưng không bịa ngưỡng vật lý

| ID | Yêu cầu đề xuất | Cách kiểm chứng |
|---|---|---|
| NFR-01 | Cơ chế an toàn cục bộ hoạt động độc lập với cloud | Fault injection network trong testbed; telemetry và quan sát vật lý |
| NFR-02 | Command hết TTL không khởi động hành động mới | Contract/integration test với đồng hồ và queue delay |
| NFR-03 | Mọi mission/action có correlation, version và actor | Query trace coverage trên toàn bộ test run |
| NFR-04 | Unauthorized command bị từ chối ở backend và execution boundary | Negative tests với role/site/capability; audit |
| NFR-05 | Telemetry tuổi dữ liệu vượt threshold hiển thị stale | Giữ observed_at/received_at, replay delayed data |
| NFR-06 | Không mất bằng chứng đã xác nhận lưu trong phạm vi durability policy | Restart/reconnect/storage failure test; checksum/reconciliation |
| NFR-07 | AI trả lời thiếu bằng chứng phải fallback theo rubric | Unanswerable/conflict benchmark và SME review |
| NFR-08 | Rollback giữ compatibility model–preprocess–skill–map–policy | Deployment rehearsal và smoke/regression |

**SLO ứng dụng mẫu để thảo luận:** p95 event metadata tới dashboard ≤2 giây dưới tải pilot đã định nghĩa; p95 câu trả lời KB ≤5 giây với giới hạn corpus/query đã ghi; 100% unauthorized requests trong test suite bị từ chối; 100% mission test có trace/version. Đây là target minh họa, không phải số đo hoặc cam kết an toàn. Cần ghi timestamp bắt đầu/kết thúc, tải đồng thời, network profile, phần cứng và sample count.

Tốc độ tối đa, khoảng cách người–robot, stopping distance, phản ứng E-stop, slope và giới hạn lực không dùng các số SLO trên. Robotics/Safety phải xác định theo robot, tải, mặt sàn và nguy cơ; BA đưa chúng thành yêu cầu và test protocol đã ký duyệt. Không tuyên bố đạt tiêu chuẩn chứng nhận từ việc pass vài test trong tài liệu.

### 10.2. Error/fallback matrix

| Sự cố | Cách phát hiện | Hành vi phải đặc tả | Bằng chứng QC |
|---|---|---|---|
| Mất cloud | Heartbeat/API timeout | Duy trì safety cục bộ; chỉ tiếp tục subset offline đã phê duyệt hoặc chuyển safe mode | Cut network, event timeline, physical outcome |
| Mất localization | Pose quality/freshness, controller status | Không tiếp tục navigation mù; safe response theo vendor và hỗ trợ người | Replay/fault injection trong môi trường kiểm soát |
| Sensor lỗi/che khuất | Health/self-test và dữ liệu bất thường | Hạ capability hoặc dừng nhiệm vụ phụ thuộc sensor | Case covered camera, dropout, stuck value |
| Pin không đủ | Energy estimate + reserve + dock route | Không nhận mission mới; handover/return theo policy | Boundary cases; dock bị chiếm/hỏng |
| AI sai/không chắc | Validation/rubric/không nguồn | Không thực hiện action vượt boundary; hỏi lại/chuyển người | Ambiguous request, unsupported scene |
| Cửa/thang máy không phản hồi | Adapter timeout và physical state | Không coi command accepted là cửa đã mở; chờ/replan/escalate | ACK giả, event trễ, physical obstruction |
| Queue gửi trùng/sai thứ tự | ID, sequence, epoch | Dedupe và state transition guard; ghi anomaly | Duplicate/reordered payload |
| Teleoperation mất link | Session heartbeat/deadman theo platform | Chuyển safe behavior được duyệt; không để lệnh cũ tiếp tục vô hạn | Controlled link-loss test |
| Map/policy sai version | Manifest mismatch | Reject hoặc migration theo quy trình; không tự đoán | Compatibility test |
| Storage đầy | Disk/buffer metrics | Ưu tiên dữ liệu/giới hạn recording theo policy; báo degraded | Fill-buffer test, data-loss accounting |
| E-stop/safety stop | Hardware/controller status | Ngắt nhiệm vụ theo thiết kế, cần điều kiện khôi phục rõ | Safety-team test protocol, không chỉ UI mock |

### 10.3. Human–Robot Interaction

BA đặc tả robot thể hiện mode bằng UI/đèn/âm thanh dễ hiểu; lời nói ngắn, không đe dọa; thời điểm ngắt lời; điều kiện tiếp cận, nhường đường và không chắn lối thoát. Người dùng cần biết đang nói với AI hay bảo vệ qua telepresence. Luồng gọi trợ giúp phải dễ tiếp cận với người không nghe rõ hoặc không dùng điện thoại.

Tình huống đông người, người đứng chắn đường, trẻ em tiếp cận hoặc người cố tương tác với phần chuyển động cần được đưa vào hazard review và test có kiểm soát. BA không tự cho người thật diễn tình huống nguy hiểm để “test edge case”.

## 11. QC, UAT, commissioning và field feedback

### 11.1. Các lớp kiểm thử

| Lớp | Nội dung | Công cụ đề xuất |
|---|---|---|
| Requirement/static review | Inconsistent state, missing fallback, AC không đo được | Confluence, Jira, draw.io review |
| API/data contract | Schema, permission, idempotency, concurrency, errors | Postman/Newman, pytest, SQL |
| Component/AI | Model slices, OCR/STT/RAG/tool correctness | Python, evaluation harness, Label Studio/CVAT |
| Integration/SIL | Robot simulator + cloud/site adapters; event ordering | ROS 2 tools, rosbag2, Gazebo hoặc Isaac Sim, mocks |
| HIL | Sensor/controller thật trong môi trường kiểm soát | Vendor diagnostics, rqt, Foxglove; thiết bị đo được phê duyệt |
| Field/UAT | Tuyến thật, ca trực thật, điều kiện được duyệt | Test script, synchronized logs/video, operator checklist |
| Regression/release | Replay bộ lỗi đã sửa và compatibility | CI runner, versioned test suite, release manifest |

Tất cả công cụ robotics ở bảng này là đề xuất cần học/thử; CV chỉ chứng minh nền tảng QA/SQL/API chung. Tool không thay người có năng lực đánh giá an toàn.

### 11.2. Coverage matrix

Chiều bao phủ: site/zone, sáng–tối, sàn và route trong ODD, mật độ người, battery bands, robot capability, network quality, role, policy/map/model version. Dùng pairwise cho tổ hợp ít rủi ro; các nguy cơ quan trọng phải có test trực tiếp, không giảm hết thành pairwise.

Mỗi case có ID, requirement ID, setup, version manifest, input, expected state/physical behavior, metric, actual, trace/video evidence, verdict và reviewer. Tập benchmark được đóng version và không tự sửa để candidate pass. Khi yêu cầu thay đổi, tạo version mới và ghi impact.

### 11.3. UAT/commissioning checklist

1. Xác nhận site, zone, route, map, dock, mạng, biển báo/điều kiện tiếp cận và nhân sự phụ trách.
2. Kiểm tra robot identity/certificate, health, sensor calibration, firmware/model/policy compatibility.
3. Chạy test preflight và phản ứng mất mạng/dừng/khôi phục theo protocol an toàn.
4. Demo luồng tuần tra–event–evidence–human review; kiểm tra cả luồng thất bại.
5. Xác nhận quyền operator, quyền tải clip, audit, retention và phân vùng dữ liệu.
6. Diễn tập handover, maintenance ticket, rollback và thay ca; xác nhận hướng dẫn vận hành.
7. Chốt unresolved defects/known limitations với owner, điều kiện chấp nhận và thời hạn; lỗi blocker không được che bằng waiver không đúng thẩm quyền.
8. Bàn giao baseline và ghi chữ ký/decision theo quy trình khách hàng; cập nhật scope khi mở thêm site/ODD.

### 11.4. Phân loại field feedback đúng JD

| Quan sát | Phân loại chính | Hướng xử lý |
|---|---|---|
| System nhận cùng event và tạo hai mission dù spec cấm | Defect | Dev sửa, QC replay và regression |
| Bảo vệ cần hoãn mission trong đổi ca nhưng chưa có requirement | Requirement gap | BA khảo sát, PO ưu tiên, bổ sung AC |
| Vision kém khi camera chói trong điều kiện đã dự tính nhưng model chưa đáp ứng | AI limitation | Data/model analysis, hạn chế phạm vi và cải tiến |
| Map sai tầng hoặc camera lắp lệch khi commissioning | Deployment issue | Deployment sửa cấu hình/calibration, re-validation |
| Nhiều nguyên nhân cùng xảy ra | Primary + contributing causes | Không ép mọi sự cố thành “AI lỗi”; giữ dependency |

**Defect template:** `Observed behavior`, `Expected requirement`, `site/robot/mission`, `ODD conditions`, `versions`, `trace_id`, `evidence`, `reproducibility`, `business/safety impact`, `temporary containment`, `owner`, `retest result`. Severity dựa trên hậu quả; priority do PO cân đối và owner safety đặt gate khi liên quan.

## 12. Traceability, SQL/logs, change và release

### 12.1. RTM mẫu

| Requirement | Story | Test | Bằng chứng mong đợi | Release gate |
|---|---|---|---|---|
| R-FLT-01: chỉ robot đủ điều kiện được giao | SEC-01-03 | TC-FLT-001..008 | Eligibility reason, health snapshot, assignment trace | Tất cả critical cases pass |
| R-CMD-02: command idempotent | SEC-01-04 | TC-CMD-011 | Cùng command ID, không có duplicate execution | Contract + integration |
| R-AI-03: không lộ SOP nội bộ | SEC-04-02 | TC-AI-021..030 | Permission denial và không leak snippet/download | Security/data gate |
| R-OPS-04: incident closure có người chịu trách nhiệm | SEC-02-05 | TC-INC-041 | Audit actor/reason và state history | UAT |
| R-SAF-05: safe behavior khi mất cloud | SEC-07-03 | TC-HIL-051 | Local response theo protocol đã duyệt | Robotics/Safety sign-off |

Đây là RTM dự kiến, không phải kết quả test đã pass. Liên kết thêm bug ID, change request, test run và version manifest để truy end-to-end.

### 12.2. SQL mẫu để điều tra

Ví dụ PostgreSQL, tên bảng giả định. BA dùng read-only account và giới hạn phạm vi; không truy vấn dữ liệu cá nhân không cần thiết.

```sql
-- Command nào có nhiều lần bắt đầu thực thi vật lý cho cùng ID?
SELECT command_id, COUNT(DISTINCT execution_id) AS starts
FROM command_execution_event
WHERE event_type = 'STARTED'
  AND site_id = :site_id
  AND observed_at >= :from_time
GROUP BY command_id
HAVING COUNT(DISTINCT execution_id) > 1;

-- Mission nào chưa có terminal event sau hạn dự kiến?
SELECT m.mission_id, m.robot_id, m.state, m.deadline_at
FROM mission m
WHERE m.site_id = :site_id
  AND m.deadline_at < CURRENT_TIMESTAMP
  AND m.state NOT IN ('SUCCEEDED', 'FAILED', 'CANCELLED', 'REJECTED');

-- p95 độ trễ nhận sự kiện: phải lọc đồng hồ đã được xác thực đồng bộ.
SELECT percentile_cont(0.95) WITHIN GROUP
       (ORDER BY EXTRACT(EPOCH FROM received_at - observed_at)) AS p95_seconds
FROM robot_event
WHERE site_id = :site_id
  AND observed_at >= :from_time
  AND clock_sync_valid = TRUE
  AND received_at >= observed_at;
```

Một duplicate event không chứng minh robot chạy hai lần, vì event delivery có thể at-least-once. Cần phân biệt `event_id` với `execution_id`; câu SQL đầu tìm nhiều execution khác nhau, sau đó kiểm tra trace thực tế.

### 12.3. Cách đọc log có phương pháp

Từ incident/mission ID tìm `trace_id`; nối API validation → policy decision → scheduler → queue → edge ACK → ROS action feedback/result → evidence upload. So `observed_at/received_at`, map/model/config version và assignment epoch. Nếu cloud chỉ có SENT không có ACK, chưa kết luận robot không nhận. Nếu ACK có mà không RUNNING, kiểm tra precondition/controller; nếu RUNNING nhưng result trễ, kiểm tra edge buffer/network trước khi gọi lỗi model.

### 12.4. Một change request minh họa

Khách yêu cầu “cho robot tuần tra cả khu ngoài trời”. BA phân tích impact tới ODD, weather, traction, map, localization, network, ingress protection của phần cứng, dataset vision, battery, incident SOP, privacy, test plan và support. PO quyết định scope/timeline; Tech Lead chốt solution feasibility; Safety/Operations duyệt điều kiện vận hành. Không sửa polygon trên UI rồi coi là hoàn thành mở rộng.

Baseline gồm BRD/SRS version, story/AC, API/schema, workflow/policy, test suite và deployment manifest. Quy trình `change request → impact assessment → decision → update baseline → implement → revalidate → release`. Quy trình dài đang chạy phải có rule pin version/migration; không tự áp workflow mới vào mission giữa chừng.

### 12.5. Rollout và rollback

Thứ tự mẫu: lab → controlled site → một robot trong khung có giám sát → một zone → mở rộng. Track firmware/model/map/policy theo từng robot. Lệnh update không chạy khi robot đang thực hiện nhiệm vụ nếu không có cơ chế hỗ trợ và đánh giá phù hợp. Artifact ký/hash, preflight compatibility, backup config, health checks, post-deploy acceptance.

Rollback trigger có thể là regression KPI, lỗi cấp nghiêm trọng hoặc vi phạm compatibility. Model perception rollback không nhất thiết rollback cả backend; nhưng preprocessing/label schema liên quan phải đồng bộ. DB migration không tương thích cần kế hoạch riêng; “đổi lại model cũ” không hoàn tác hành động vật lý đã xảy ra.

## 13. Industry Solution Packs: áp dụng tư duy workflow và policy từ chính phủ

Core dùng chung: identity/site/device, event, mission, fleet, skill contract, evidence, audit, monitoring và release. Pack gồm domain ontology, event taxonomy, SOP/workflow, DMN/policy, mission templates, role/scope, KB, integration mappings và evaluation cases. Không để pack thay đổi safety limit cốt lõi ngoài quy trình phê duyệt.

| Pack | Quy trình đặc thù | Quy tắc/adapter riêng | Kinh nghiệm cũ kế thừa |
|---|---|---|---|
| Security | Tuần tra → phát hiện → xác minh → xử lý | VMS/access control; quyền xem clip; escalation ca trực | Smart Safe, mChat routing, chính phủ |
| Hospital | Giao vật tư → xác nhận bàn giao → vệ sinh/return | Restricted areas, hygiene, người nhận; không tự quyết định y khoa | Workflow/thẩm quyền, OCR traceability |
| Hotel | Guest request → giao đồ → xác nhận | PMS/room status; privacy; quiet hours | CRM, CXP, service ticket |
| Restaurant | Order ready → pickup → deliver → tray return | POS/KDS, table ID, tải trọng, đổ tràn | Omnichannel/fulfillment, WMS |
| Residential | Patrol/public guidance → incident → management | Building access, visitor policy, tenant/site separation | Smart Safe SaaS, governance |
| Industrial | Inspection → abnormality → maintenance | MES/SCADA/ERP, zone permissions, machine interlocks | Smart Factory, maintenance/QMS |

### Một mission template có version

```yaml
pack_id: security-vinuni
pack_version: 1.0.0-demo
mission_type: observe_zone
required_capabilities: [navigate, capture_evidence]
allowed_roles: [security_dispatcher]
preconditions:
  - robot_health_fresh
  - localization_valid
  - route_inside_approved_odd
  - energy_reserve_sufficient
steps:
  - skill: navigate_to_observation_point
    on_failure: request_human_assistance
  - skill: capture_evidence
    on_failure: report_missing_evidence
  - skill: await_guard_decision
completion:
  requires: [observation_result, evidence_status]
incident_closure:
  actor: authorized_guard
```

Đây là DSL minh họa, chưa phải schema thực thi của Camunda hay ROS. Toolchain cần validator, signature, dependency/compatibility check, review và tests trước khi đưa pack vào runtime.

**Kế thừa từ chính phủ:** quy trình có bước/người/thẩm quyền; policy hiệu lực theo thời gian; dữ liệu có owner/sensitivity; workflow instance gắn version; audit và segregation of duties. **Khác biệt cần học:** lỗi robot có hậu quả vật lý, latency và state uncertain; nghiệp vụ không được yêu cầu robot vượt giới hạn controller/safety.

## 14. Ánh xạ kinh nghiệm cũ sang công việc mới

| Nguồn kinh nghiệm | Năng lực chuyển được | Việc cụ thể tại VinUni | Giới hạn cần nói rõ |
|---|---|---|---|
| Smart Safe | Sensor–gateway–cloud, alarm lifecycle, role/site, incident | Event contract, device health, clip evidence, false-alarm triage | AI camera model cụ thể chưa xác nhận; chưa chứng minh locomotion |
| Samsung Smart Factory | Equipment hierarchy, maintenance, OEE, QMS, ERP | Robot/component registry, readiness, maintenance, fault taxonomy, integration | Azure/ML/fleet trong bài là mở rộng đề xuất |
| V-Tracking trong CV | GPS/fleet tracking và realtime data | Fleet dashboard, telemetry freshness, location history | Tracking không đồng nghĩa multi-robot path planning |
| mChat | Routing/queue/assignment, SLA, handover, multi-turn | Mission assignment, operator inbox, handover, conversation context | Handover robot cần energy, path và physical state |
| Điều phối TTHC | Workflow liên thông, trạng thái, quyền, audit | Mission/incident workflow, external callbacks, retries, baseline | Camunda không điều khiển motor |
| Một cửa/vi phạm hành chính | KB, thẩm quyền, hiệu lực, allowed actions | SOP chatbot, site/role ACL, policy packs và guardrails | Không dùng legal reasoning để suy ra safety physics |
| HRAI | Feature/label, snapshot, feedback, evaluation | Health ML, scenario taxonomy, error slices, gold adjudication | Không dùng suy đoán HR để phân loại người qua camera |
| AI Data Hub | Dataset/model/job/evaluation/deployment lineage | Robot data factory, manifest, approval, model rollout/rollback | Phải bổ sung embodiment/hardware/map compatibility |
| RPA & OCR/VLM | Extraction, schema, human review, idempotent automation | Đọc tài liệu SOP/maintenance, visual evidence review, tool execution | VLM hiểu ảnh không thay perception/control đã kiểm chứng |
| CDP/CXP/CRM | Customer journey, tenant, service package, ticket/SLA | Customer onboarding, Robot-as-a-Service, support và usage analytics | Không dùng dữ liệu người qua camera cho marketing |
| Harness/skills/orchestration | Capability contract, permission, context, checkpoints | Skill catalog, policy, mission observability, human interruption | Robot skill là code/controller có precondition, không chỉ file Markdown |
| Developer nền tảng | API, DB, async, logs, debugging | Trao đổi technical feasibility, contract, root cause, SQL | Không tự nhận đã viết safety-critical embedded code |

### Harness và robot: điểm giống dùng được

Một skill nên có input schema, output schema, precondition, effects, timeout, cancellation semantics, resource locks, version và telemetry. Agent chỉ chọn skill trong catalog được cấp; runtime enforce policy. Checkpoint của phần mềm giúp khôi phục logic, nhưng không “undo” được vị trí robot hoặc thao tác đã thực hiện. Một checkpoint cũ phải đối chiếu thế giới hiện tại trước resume.

### Thương mại hóa: kinh nghiệm Omnichannel giúp gì?

PO phân tích khách hàng–site–gói capability–SLA–support; onboarding site, provisioning robot, giới hạn vùng và người vận hành, usage metering, incident ticket và gia hạn dịch vụ. Xây pricing hypothesis dựa trên cost/robot-hour hữu ích, support effort, battery/maintenance và giá trị nghiệp vụ, không chỉ số token AI. Theo dõi adoption của người bảo vệ và thời gian training; customer success loop quay lại backlog. Đơn hàng/gói dịch vụ không được tự mở capability an toàn chưa được nghiệm thu.

## 15. Ma trận phủ JD VinDynamics

Ma trận dưới là phân tích áp dụng cho case, dùng các mã riêng để đối chiếu; không coi đây là cách chia module chính thức của VinDynamics. JD được đọc từ trang chính thức ngày 16/11/2026. [Senior Business Analyst — VinDynamics](https://vindynamics.net/vi/career/senior-business-analyst-001114.html).

### 15.1. Key responsibilities

| Nhóm JD | Tôi thực hiện trong case VinUni | Artifact / ví dụ kinh nghiệm | Mục tài liệu |
|---|---|---|---|
| Discovery cùng PO/Market/customer | Khảo sát ca trực, use case, ODD và kết quả mong đợi | Context, AS-IS/TO-BE; Smart Safe | 2–3 |
| Làm rõ gap, risk và ảnh hưởng robot/integration | Map yêu cầu sang capability và adapter; nêu hạn chế | Gap/assumption/dependency log; Factory | 2, 4, 10 |
| Stories/use cases/FR/NFR/AC | Viết story với điều kiện và test basis | SEC-01-03, NFR table; BA hồ sơ | 9–10 |
| API/data/state/error/fallback | Command/event schema, state machine, retry/cancel | OpenAPI, sequence, exception matrix; IoT/chính phủ | 5, 8, 10 |
| AI quality với Tech Lead | Dataset slices, rubric, threshold, latency/boundary | Evaluation plan; HRAI/AI Hub | 6–7, 11 |
| Refinement/planning/daily/review | Giữ story ready; giải đáp nhanh; review build so AC | Jira backlog, decision log; CV Viettel/Samsung | 9, 16 |
| Đồng nhất cách hiểu với R&D/Dev | Review contract và feasibility trước implementation | Interface workshop, ADR do Tech Lead chốt | 4, 8 |
| Hỗ trợ QC | Review coverage/expected behavior; triage và retest | RTM, negative/field cases | 10–12 |
| Change impact/escalation | Phân tích yêu cầu mở thêm ODD/site; PO/PMO quyết định | Change request, dependency map | 12.4 |
| Traceability và baseline chung | Requirement → story → test/result → release | Versioned RTM, manifest | 12 |
| UAT/onsite/commissioning/acceptance | Preflight, field scripts, operator training, sign-off | UAT pack; Smart Safe/AI product rollout | 11 |
| Phân loại feedback và ưu tiên | Defect/gap/AI limitation/deployment; đề xuất backlog | Triage template, re-validation | 11.4 |
| Hợp tác và ranh giới ownership | Market giữ cơ hội; PO ưu tiên; BA clarity; Tech Lead HOW | RACI và decision record | 1, 16 |

### 15.2. Qualifications, preferred và thái độ

| Yêu cầu | Bằng chứng/chuẩn bị của Đức | Khoảng trống cần xử lý trung thực |
|---|---|---|
| Bằng cấp phù hợp | CV: kỹ sư CNTT PTIT | Chuẩn bị bằng/thông tin theo hồ sơ khi được hỏi |
| 4+ năm BA/Technical BA/System Analyst | CV có BA từ 02/2023 và công việc developer trước đó | Đến 16/11/2026, chức danh BA ghi trong CV chưa đủ 4 năm; cần chứng minh nhiệm vụ system analysis trước 2023 nếu có |
| 2+ năm tích hợp phức tạp | Smart Factory 2023–2024, Smart Safe và các hệ AI; API/ERP/IoT | Nêu cụ thể thời gian và ownership, không cộng nhiều dự án song song thành thêm năm |
| Làm hằng ngày với Agile/Scrum team | Backlog, sprint, clarification và developer handover trong CV | Chuẩn bị một ví dụ bất đồng yêu cầu được giải quyết |
| Stories/workflows/FR/NFR/Gherkin | Mẫu story/AC ở mục 9 và thực hành trong CV | Chỉ ra measurable expected result và exception |
| BPMN/UML/sequence/state/API/data | Chính phủ, AI Hub, Smart Safe/Factory | Giải thích được sơ đồ và contract, không chỉ liệt kê tên |
| Jira/Confluence/logs/SQL | CV ghi tools, SQL/DB và troubleshooting | Có query/trace mẫu ở mục 12 để trình bày |
| English | CV TOEIC 860 năm 2020, làm việc HQ Korea | Chứng chỉ cũ không thay năng lực hiện tại; luyện giải thích technical case |
| Humanoid/ROS2/Vision/VLM/LLM/HRI | Bài nghiên cứu và kiến thức từ AI/IoT; phân lớp ở mục 4–7 | Chưa có bằng chứng triển khai humanoid, cần học trên simulator/SDK |
| Edge/cloud/logging/config/release | Smart Safe/Factory + thiết kế Azure | Phân biệt công nghệ đã dùng với kiến trúc mới đề xuất |
| UAT/real-world AI evaluation | CV có AI QA, UAT/go-live; bộ test dự án cũ | Robot field validation là phần mới, cần phối hợp Deployment/Safety |
| Robot safety thành NFR | ODD, boundary, fail-safe requirements và test protocol | Không tự nhận safety certification hoặc tự đặt ngưỡng vật lý |
| Ownership/system/data thinking | Traceability, source-of-truth, lỗi theo layer | Đưa ví dụ quyết định có evidence, không chỉ tự đánh giá bản thân |
| Challenge constructive | Hỏi định nghĩa “an toàn”, “hiểu đúng”, “realtime”; đề xuất cách đo | Đưa phương án và trade-off thay vì phản đối chung chung |
| Customer/collaboration/fast pace | Pilot tăng dần, feedback → backlog, clarity trong sprint | Giữ baseline và xử lý ưu tiên thay đổi có người quyết định |

## 16. Cách làm việc hằng ngày và RACI

Một ngày của BA hybrid: xem incident/defect mới và log có phạm vi; daily chốt blocker; workshop ngắn với Dev/QC làm rõ trạng thái/exception; cập nhật story và decision log; review demo; chuẩn bị dữ liệu/test cho feature kế tiếp; cuối ngày bảo đảm thay đổi requirement được đồng bộ. Tôi không cần tham dự mọi cuộc họp, nhưng câu hỏi làm dev/QC dừng việc phải có owner và thời điểm trả lời.

| Quyết định/hoạt động | Owner chịu trách nhiệm cuối | BA/PO hybrid làm gì |
|---|---|---|
| Cơ hội và quan hệ khách hàng | Market Development | Hỗ trợ discovery và đánh giá scope |
| Product goal, priority, release scope | PO | Nếu là BA: đề xuất bằng evidence; nếu được giao PO: quyết định trong thẩm quyền |
| Requirement clarity/baseline | Senior BA | Sở hữu spec, traceability, clarification và impact |
| Architecture/algorithm/implementation | Tech Lead/R&D | Đưa constraints, đánh giá trade-off cùng nhóm; không tự duyệt thay |
| Test execution/quality evidence | QC Lead | Review expected behavior và trực tiếp test phần được giao |
| Robot operational/safety readiness | Robotics/Safety/Operations theo tổ chức | Chuyển rủi ro thành requirements và acceptance evidence |
| Site commissioning | Deployment Lead | Hỗ trợ requirement/UAT và ghi nhận gap |
| Customer acceptance | Đại diện khách hàng được ủy quyền | Chuẩn bị acceptance pack và làm rõ kết quả |
| Timeline/dependencies/escalation | PMO/PM | Báo impact và giữ liên kết giữa scope, dependency, readiness |

## 17. Bài trả lời phỏng vấn và ví dụ để kể

### 17.1. “Anh mới vào VinDynamics thì làm gì trong tháng đầu?”

> Tôi sẽ làm rõ ba thứ: bài toán vận hành của khách hàng, capability thực tế của robot và boundary tích hợp. Với VinUni, tôi đi theo một ca bảo vệ để hiểu tuần tra và xử lý sự cố hiện tại, đồng thời xem demo robot cùng R&D để phân biệt chức năng đã ổn định với roadmap. Sau đó tôi dựng context map, luồng event-to-incident-to-mission, state machine và ODD/assumption log. Tôi chọn cùng PO một luồng nhỏ đủ giá trị, viết API, ngoại lệ và AC để Dev/QC dùng ngay. Tôi mang kinh nghiệm Smart Safe và Smart Factory vào health, alarm và integration, còn phần điều khiển/an toàn robot tôi làm việc trực tiếp với Robotics Lead.

### 17.2. “Kinh nghiệm AI trước đây liên quan gì tới robot?”

> Tôi có kinh nghiệm ở lớp dữ liệu, nghiệp vụ và đánh giá của sản phẩm AI. AI Hub cho tôi tư duy truy vết dataset đến model và deployment; HRAI và các sản phẩm AI giúp tôi định nghĩa label, input snapshot, gold set và feedback; OCR/mChat giúp tôi xử lý output không chắc chắn và tích hợp vào workflow. Với robot, tôi áp dụng vào perception, assistant và data factory, nhưng bổ sung ODD, physical outcome, sensor freshness và hardware compatibility. Tôi không coi một model trả lời đúng là toàn hệ thống đã an toàn.

### 17.3. “Tại sao chọn anh thay vì BA thuần robotics?”

> Tôi có thể đóng góp ngay ở phần nền tảng doanh nghiệp bao quanh robot: mission/incident workflow, fleet operations, integration, data governance, quyền và release. Tôi có nền tảng developer để đọc API/log/SQL và trao đổi với engineer, đồng thời có kinh nghiệm BA/PO để làm rõ ưu tiên và hành vi người dùng. Tôi biết khoảng trống của mình ở locomotion và safety engineering, nên sẽ dùng tài liệu, simulation và phối hợp R&D để học đúng chỗ thay vì nhận mình đã làm phần đó.

### 17.4. Ba câu chuyện STAR cần hoàn thiện bằng bằng chứng thật

| Câu chuyện | Situation/Task có căn cứ | Action nên kể | Result cần điền từ thực tế |
|---|---|---|---|
| Smart Safe incident lifecycle | Nền tảng nhiều thiết bị/site, cảnh báo và trạng thái | Làm rõ heartbeat, duplicate/recovery, scope quyền, UAT | Một lỗi thực tế đã giảm/khắc phục hoặc kết quả nghiệm thu; không tự thêm % |
| AI Hub governance | Nhiều dataset/model và luồng phê duyệt | Chuẩn hóa metadata, lifecycle, permission và lineage | Evidence về flow được thống nhất/pilot/handover; nêu đúng phạm vi |
| HRAI/AI QA | Output AI cần kiểm chứng nghiệp vụ | Golden cases, sửa ground truth, phân loại nguyên nhân và regression | Một ví dụ before/after có dataset/version và report |

Nếu chưa có số liệu, dùng kết quả định tính kiểm chứng được: yêu cầu được thống nhất, luồng lỗi được bổ sung, UAT có sign-off, hoặc feature được bàn giao. Không tạo số chính xác để câu chuyện nghe mạnh hơn.

### 17.5. Đoạn tiếng Anh ngắn

> My strongest contribution is translating operational needs into testable system behavior. I have worked on IoT monitoring, factory operations, workflow and data governance, as well as AI data preparation and evaluation. For a security robot fleet, I would define the operating domain, mission states, integration contracts, failure behavior and acceptance evidence with the technical leads. I would keep mission orchestration separate from real-time robot control, and distinguish a successful AI response from a safely completed physical task.

### 17.6. Câu hỏi nên hỏi nhà tuyển dụng

1. Phạm vi Senior BA hiện tập trung fleet/mission, AI assistant, industry solutions hay toàn bộ robot platform?
2. Những capability nào đã vận hành ngoài thực địa; những capability nào đang ở nghiên cứu/demo?
3. Ai sở hữu ODD, safety requirements và quyết định cho phép mở rộng site?
4. Đội đang dùng interface/SDK nào giữa cloud, fleet và robot; có baseline contract và simulator không?
5. Dataset, evaluation và field feedback được quản lý ở đâu; BA tham gia tới mức nào?
6. Pilot đầu tiên cần chứng minh giá trị gì, ai nghiệm thu, và sai số nào không được chấp nhận?
7. Cơ chế phối hợp BA–PO–QC–Deployment–R&D và quyền quyết định change/release cụ thể ra sao?

## 18. Nguồn và sơ đồ bàn giao

Nguồn nền: [JD VinDynamics](https://vindynamics.net/vi/career/senior-business-analyst-001114.html), [CV đầy đủ](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Kim Đức CV full.pdf>), [tài liệu robot người dùng cung cấp](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/ChatGPT/Tìm hiểu Robot VinDynamics.md>), [nguồn mã mở người dùng cung cấp](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/ChatGPT/Mã nguồn robot hình người của các tập đoàn lớn.md>). Tài liệu tham khảo nền tảng: [ROS 2](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Concepts/Basic/About-Interfaces.rst), [Open-RMF](https://github.com/open-rmf/rmf), [Camunda](https://docs.camunda.io/docs/components/best-practices/best-practices-overview/), [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), [Azure IoT device twins](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins), [Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2).

Sơ đồ editable và ảnh nằm trong [Sơ đồ kiến trúc](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc>). Các hình là **thiết kế tham chiếu** cùng với hai tài liệu, không phải sơ đồ hệ thống nội bộ do công ty cũ hoặc VinDynamics công bố. Mỗi sơ đồ có file `.drawio`, PNG để đọc trong Markdown và SVG để phóng lớn.
