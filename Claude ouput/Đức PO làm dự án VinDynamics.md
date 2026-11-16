# Đức PO làm dự án VinDynamics

> Một PO/BA mới vào VinDynamics sẽ tiếp cận hệ thống thế nào, dựng overview ra sao, và làm những việc BA + QC cụ thể nào theo JD Senior Business Analyst — minh họa bằng dự án giả định **"Đội robot an ninh bảo vệ Vin University"**. Phần cuối chỉ rõ tôi dùng lại kinh nghiệm từ các dự án cũ như thế nào.
>
> Nền tảng kinh nghiệm: [Đức BA training AI, ML models](<Đức BA training AI, ML models.md>). Sơ đồ chỉnh sửa được: [`Sơ đồ kiến trúc/`](<Sơ đồ kiến trúc/>) (file 13–18 cho tài liệu này, file 01 và 02 dùng chung).

## Mục lục

1. [VinDynamics, vị trí và ranh giới vai trò](#1-vindynamics-vị-trí-và-ranh-giới-vai-trò)
2. [Tiếp cận hệ thống mới và dựng overview](#2-tiếp-cận-hệ-thống-mới-và-dựng-overview)
3. [Case: Đội robot an ninh VinUni — định nghĩa sản phẩm](#3-case-đội-robot-an-ninh-vinuni--định-nghĩa-sản-phẩm)
4. [Kiến trúc giải pháp](#4-kiến-trúc-giải-pháp)
5. [Luồng chính và luồng ngoại lệ](#5-luồng-chính-và-luồng-ngoại-lệ)
6. [State machine](#6-state-machine)
7. [Hệ tri thức & AI Agent cho robot (HRI)](#7-hệ-tri-thức--ai-agent-cho-robot-hri)
8. [AI training, fine-tune và dữ liệu robot](#8-ai-training-fine-tune-và-dữ-liệu-robot)
9. [Công việc BA + QC theo từng nhóm trong JD](#9-công-việc-ba--qc-theo-từng-nhóm-trong-jd)
10. [Kế thừa kinh nghiệm từ dự án cũ](#10-kế-thừa-kinh-nghiệm-từ-dự-án-cũ)
11. [Industry Solution Packs](#11-industry-solution-packs)
12. [Thương mại hóa robot](#12-thương-mại-hóa-robot)
13. [Câu trả lời phỏng vấn mẫu và câu hỏi hỏi lại](#13-câu-trả-lời-phỏng-vấn-mẫu-và-câu-hỏi-hỏi-lại)

---

## 1. VinDynamics, vị trí và ranh giới vai trò

### 1.1. Những gì tôi đã tìm hiểu

- VinDynamics thuộc hệ sinh thái Vingroup, phát triển robot hình người và giải pháp robot cho doanh nghiệp. Tháng 06/2026 Vingroup giới thiệu robot hình người **Dyno**, định hướng cho an ninh và giám sát ở khu đô thị, trường học, tổ hợp dịch vụ; robot xuất hiện tại lễ tốt nghiệp VinUni ngày 27/06/2026.
- Website có hai mảng: **Giải pháp Robot** và **Data Factory** (nhận yêu cầu xây bộ dữ liệu robot, ví dụ "bộ dữ liệu robot tay gắp trong kho hàng"). Data Factory cho thấy công ty coi dữ liệu huấn luyện robot là một sản phẩm — nơi kinh nghiệm dataset/annotation/evaluation của tôi dùng trực tiếp.
- JD nhấn mạnh: tích hợp phần cứng – phần mềm, edge/cloud, AI Vision/VLM, LLM/Agentic AI, Conversational AI, HRI, an toàn robot thành NFR, UAT/commissioning thực địa và phân loại field feedback.

### 1.2. Ranh giới vai trò theo JD

| Ai | Sở hữu |
|---|---|
| Market Development | Cơ hội kinh doanh, quan hệ khách hàng |
| Product Owner | Ưu tiên và quyết định phát hành |
| **Senior BA (tôi)** | **Độ rõ ràng và chất lượng yêu cầu**, baseline chung, truy vết, phân tích tác động |
| Tech Lead / R&D | HOW: kiến trúc, giải pháp kỹ thuật |
| QC | Kế hoạch và thực thi kiểm thử; tôi review test case theo yêu cầu và làm rõ hành vi mong đợi |
| Deployment / Robot Ops / PMO | Triển khai, vận hành, tiến độ — cùng dùng một baseline yêu cầu |

Tên tài liệu dùng "PO" vì tôi có kinh nghiệm PO; ở vị trí Senior BA, tôi đề xuất ưu tiên bằng dữ liệu và để PO quyết định. Kiến trúc trong tài liệu là đề xuất để trao đổi với Tech Lead.

---

## 2. Tiếp cận hệ thống mới và dựng overview

### 2.1. Bức tranh 5 tầng tôi dựng trong tuần đầu

![Bức tranh hệ thống robot dịch vụ](<Sơ đồ kiến trúc/13-vindynamics-tong-quan-1.png>)

*Nguồn chỉnh sửa: [13-vindynamics-tong-quan.drawio](<Sơ đồ kiến trúc/13-vindynamics-tong-quan.drawio>).*

| Tầng | Câu hỏi tôi cần trả lời | Người tôi hỏi |
|---|---|---|
| 5. Industry Solution Packs | Ngành nào đang có khách? Quy trình, quy tắc, sự kiện, mẫu nhiệm vụ của từng ngành ở đâu? | PO, Market Development |
| 4. Mission & Fleet | Mission được tạo, phân công, theo dõi, hủy thế nào? Ai điều phối thang máy, cửa, hành lang? | Tech Lead backend |
| 3. AI & Shared Services | Model vision/VLM/LLM/speech nào đang dùng, chạy ở edge hay cloud, đánh giá bằng gì? | AI Lead |
| 2. Robot Runtime / Edge | ROS 2 interface, skill nào ổn định, navigation/locomotion của hãng làm được gì, safety cục bộ ra sao? | Robotics Lead |
| 1. Hardware | Cảm biến, pin, tải, giới hạn môi trường (dốc, nước, ánh sáng) | Hardware/Robotics |
| Xuyên suốt | Safety, security & privacy, observability, device management & OTA, configuration & release | Safety, DevOps, Robot Ops |

### 2.2. Bốn thứ thay đổi độc lập và 18 module

![Core · Pack · Site · Adapter](<Sơ đồ kiến trúc/13-vindynamics-tong-quan-2.png>)

- **Core Platform** ổn định, dùng chung; **Industry Pack** đổi theo ngành; **Site Configuration** đổi theo địa điểm; **Robot Adapter** đổi theo phần cứng. Khi khách yêu cầu điều gì, việc đầu tiên tôi làm là xác định nó rơi vào ô nào — vì ô quyết định ai sửa, test gì và rủi ro tới đâu. Không phải mọi khác biệt đều giải bằng cấu hình: capability mới (ví dụ thao tác tay) phải phát triển và kiểm định riêng.
- **Capability ≠ Skill ≠ Mission ≠ Workflow**: di chuyển / `navigate_to` / "giao thuốc từ kho đến khoa Nội" / toàn bộ quy trình nghiệp vụ. Skill tái sử dụng; quy trình đổi theo ngành.
- **Skill contract** tôi đặc tả: input · preconditions · permissions · feedback · timeout · failure handling · postconditions.

### 2.3. Lộ trình 30 – 60 – 90 ngày

| Giai đoạn | Việc | Đầu ra |
|---|---|---|
| Ngày 1–10 | Đọc tài liệu sản phẩm, SDK, interface; xem demo robot thật; đi thực địa VinUni (ngày và đêm, nếu được phép); phỏng vấn stakeholder; lập danh sách điều chưa biết | System Overview v0.1, glossary, capability baseline (đã ổn định / demo / roadmap), ODD nháp, assumption log |
| Ngày 11–30 | Phân tích 3 luồng ưu tiên (tuần tra, xác minh sự kiện, hỏi đường); mapping API/event; prototype màn điều hành; chốt test basis với QC | BPMN, state machine, API/event contract, backlog "ready" cho 2 sprint, RTM khung |
| Ngày 31–60 | Refinement, daily clarification; review demo theo AC; dựng golden scenario; hỗ trợ SIL/HIL và integration test | Test report, defect taxonomy, checklist commissioning, decision log |
| Ngày 61–90 | Pilot có giám sát; UAT tại hiện trường; thu telemetry và feedback; điều chỉnh backlog | Pilot report, KPI, re-validation, SOP và tài liệu đào tạo, đề xuất mở rộng có điều kiện |

### 2.4. Stakeholder và câu hỏi khảo sát

| Đối tượng | Câu hỏi cần chốt | Bằng chứng thu thập |
|---|---|---|
| Trưởng an ninh VinUni | Mục tiêu, khu vực ưu tiên, ai nhận cảnh báo, ai đóng sự cố, SLA hiện tại | SOP, lịch ca trực, nhật ký sự cố |
| Bảo vệ ca đêm | Điểm hay bỏ sót, sự kiện thường gặp, khi nào cần robot, khi nào không | Đi theo ca (shadowing), task analysis |
| Sinh viên, giảng viên, khách | Robot gây cản trở hay lo ngại gì? Cần hỗ trợ gì ngoài giờ? | Phỏng vấn ngắn, kịch bản usability |
| IT / quản lý tòa nhà | Camera/VMS, access control, thang máy, cửa, Wi-Fi/5G có API gì? | Inventory hệ thống, sơ đồ mạng, ràng buộc |
| Robotics / R&D | Capability đã ổn định, ODD, SDK, map/localization, chế độ an toàn | Demo thật, interface docs, danh sách hạn chế |
| AI Lead | Model nào có sẵn, benchmark, điều kiện suy giảm | Model card, evaluation report |
| Safety / Privacy / Pháp chế VinUni | Ai phê duyệt vận hành, lưu video, quyền truy cập, khẩn cấp | Risk register, chính sách dữ liệu |
| PO / Market Development / PMO | Pilot cần chứng minh gì, ngân sách, thời gian, tiêu chí nghiệm thu | Product goal, success criteria |

---

## 3. Case: Đội robot an ninh VinUni — định nghĩa sản phẩm

### 3.1. Bài toán và vì sao là robot chứ không chỉ camera AI

Mục tiêu: **tăng độ phủ tuần tra và rút ngắn thời gian có bằng chứng cho bảo vệ**, đồng thời giữ tương tác an toàn và con người kiểm soát. Robot quan sát, báo cáo, hỗ trợ chỉ dẫn và tạo bằng chứng; bảo vệ quyết định xử lý.

| Camera AI cố định làm tốt | Robot làm tốt hơn |
|---|---|
| Quan sát liên tục một điểm, chi phí và bảo trì thấp | Di chuyển tới sự cố, đổi góc nhìn, tới điểm mù |
| Phát hiện sự kiện trong khung hình | Tiếp cận xác minh, hội thoại, răn đe bằng sự hiện diện |
| | Hộ tống, dẫn đường, hỗ trợ người cần giúp ngoài giờ |

Nếu robot chỉ gửi thông báo thì khó chứng minh giá trị so với camera AI — vì vậy use case phải có **hành động vật lý tạo khác biệt**.

### 3.2. ODD — Operational Design Domain

Tôi ghi rõ điều kiện vận hành và cách nhận biết khi ra ngoài ODD; ngưỡng vật lý do Robotics/Safety xác nhận bằng thử nghiệm.

| Chiều | Pilot (giả định để thảo luận) |
|---|---|
| Khu vực | 1–2 tòa nhà, sảnh, hành lang, khu để xe trong nhà; tuyến đã khảo sát |
| Mặt sàn | Bằng phẳng, không cầu thang, dốc trong giới hạn robot |
| Thời gian | 18:00–06:00 và cuối tuần; tránh giờ cao điểm |
| Mật độ người | Thấp – trung bình; quá ngưỡng thì chuyển chế độ quan sát từ xa |
| Môi trường | Trong nhà; không mưa, không nước đọng |
| Mạng | Wi-Fi 6 / 5G riêng; có vùng mất sóng đã đánh dấu trên bản đồ |
| Số robot | 3 robot, 1 dock sạc mỗi tòa |

### 3.3. Use case theo nhóm và giai đoạn

| Nhóm | ID | Use case | Giai đoạn |
|---|---|---|---|
| **UC1 · Tuần tra & răn đe chủ động** | SEC-01 | Tuần tra theo lịch, checkpoint, báo cáo | MVP |
| | SEC-02 | Cửa khu hạn chế mở ngoài giờ: dừng quan sát, truyền hình, chờ bảo vệ | MVP |
| | SEC-03 | Hành vi cấm (hút thuốc nơi cấm): phát loa nhắc, gửi sự kiện, không kết luận vi phạm | Pilot |
| | SEC-04 | Xe đỗ chắn lối thoát hiểm: đọc biển số, nhắc, quan sát lại, chuyển bảo vệ | Pilot |
| | SEC-05 | Kiểm tra điểm mù ngoài tầm camera cố định | MVP |
| **UC2 · Tương tác & xác minh truy cập** | SEC-06 | Người ở khu hạn chế: robot đề nghị xác thực thẻ, kết nối bảo vệ từ xa; không hợp tác thì lùi về vị trí an toàn và gọi bảo vệ | Pilot |
| | SEC-07 | Khách cần hỗ trợ ngoài giờ: hỏi đường tiếng Việt/Anh, dẫn tới quầy | Pilot |
| | SEC-08 | Hộ tống sinh viên về ký túc xá ban đêm | Mở rộng (rủi ro cao) |
| **UC3 · Phản ứng sự cố & can thiệp từ xa** | SEC-09 | Camera cố định báo sự kiện → robot tới xác minh (Integrated Alarm Response) | MVP |
| | SEC-10 | Hai robot phối hợp quan sát từ hai vị trí | Mở rộng |
| | SEC-11 | Vật thể khả nghi (túi bỏ quên): dừng xa, gửi ảnh và vị trí, chờ người có thẩm quyền | Pilot |
| | SEC-12 | Y tế khẩn cấp: kết nối hình ảnh/âm thanh, hướng dẫn gọi cấp cứu; không tự chẩn đoán | Pilot |
| **Vận hành** | OPS-01 | Pin thấp → bàn giao nhiệm vụ → về dock | MVP |
| | OPS-02 | Thiết bị suy giảm → hạ capability / ticket bảo trì | MVP |
| | OPS-03 | Teleoperation / telepresence có phiên độc quyền | MVP |
| | OPS-04 | Báo cáo ca trực tự động có kiểm tra | Pilot |

### 3.4. Thang hành động L1–L5 và ranh giới

| Cấp | Tên | Ví dụ | Tự động / cần duyệt / cấm |
|---|---|---|---|
| L1 | Observe & Alert | Phát hiện, gửi cảnh báo + ảnh | Tự động |
| L2 | Navigate & Investigate | Tới điểm quan sát an toàn | Tự động trong ODD |
| L3 | Communicate & Deter | Phát loa theo câu mẫu đã duyệt, đề nghị xác thực | Tự động với câu mẫu; câu tự do cần bảo vệ qua telepresence |
| L4 | Assist & Coordinate | Dẫn đường, gọi bảo vệ, điều phối robot khác | Tự động; hộ tống cần duyệt |
| L5 | Physical Task Execution | Thao tác vật lý | Ngoài phạm vi pilot |
| — | Truy đuổi, khống chế, dùng lực, nhận diện khuôn mặt sinh viên, tự mở khóa cửa | | **Cấm** — thuộc lực lượng có thẩm quyền hoặc ngoài chính sách |

Mỗi use case tôi đặc tả theo chu trình **Detect → Assess → Decide → Act → Verify → Escalate/Close**, và ở bước Decide/Act ghi rõ hành động nào tự động, hành động nào cần bảo vệ duyệt, hành động nào bị cấm.

### 3.5. KPI và nguồn đo

| Mục tiêu | Metric | Nguồn |
|---|---|---|
| Độ phủ tuần tra | Checkpoint hoàn tất hợp lệ / checkpoint đến hạn trong ODD | Mission events (lý do bỏ lỡ tách riêng) |
| Hữu ích cho bảo vệ | Thời gian event → bảo vệ có bằng chứng dùng được (median, p95) | Trace event / evidence / view |
| Chất lượng cảnh báo | Xác minh đúng / cảnh báo đã review; cảnh báo giả / robot-giờ | Incident adjudication |
| Hoàn thành nhiệm vụ | Mission thành công / mission nhận trong ODD; phân loại abort | Mission state ledger |
| Mức can thiệp | Lần con người can thiệp / mission, phân loại | Teleop & handover log |
| Khả dụng | Thời gian đủ capability / thời gian theo lịch | Health + schedule + maintenance |
| HRI | Hiểu đúng ý định, gọi trợ giúp thành công, điểm usability | Transcript test, khảo sát |
| Giá trị tăng thêm | Chi phí / robot-giờ hữu ích so với camera AI và bảo vệ truyền thống | Billing, vận hành |

Target đặt sau khi đo baseline; mỗi số liệu pilot ghi rõ cỡ mẫu, tuyến, điều kiện và phiên bản.

### 3.6. Lộ trình

1. **PoC/MVP**: tuần tra, phát hiện bất thường, phát loa, điều khiển từ xa, xác minh sự kiện camera.
2. **Pilot nâng cao**: tiếp cận, hội thoại, xác minh truy cập, tích hợp access control.
3. **Multi-robot**: phối hợp nhiều robot, bàn giao, traffic.
4. **Platform**: đóng gói Security Pack, mở sang ngành khác. Nguyên tắc **vertical-first, platform-ready**: modular backend, không tách 18 microservice từ đầu.

---

## 4. Kiến trúc giải pháp

![Robot · site edge · cloud](<Sơ đồ kiến trúc/14-vinuni-kien-truc-1.png>)

*Nguồn chỉnh sửa: [14-vinuni-kien-truc.drawio](<Sơ đồ kiến trúc/14-vinuni-kien-truc.drawio>) (2 sheet).*

### 4.1. Chia việc giữa robot, site edge và cloud

| Nơi chạy | Thành phần | Lý do |
|---|---|---|
| **Robot** (NVIDIA Jetson Thor/Orin) | Cảm biến, perception (YOLO + tracking, VLM nhỏ), ROS 2 Jazzy, skill executor (BehaviorTree.CPP), Nav2 + bộ điều khiển đi bộ của hãng, **local safety** (E-stop, safety controller), HRI (VAD, STT, TTS), robot agent (MQTT client, buffer, OTA agent) | Độ trễ thấp; an toàn không phụ thuộc mạng |
| **Site edge** (phòng máy VinUni) | Site gateway (K3s, VPN, buffer), EMQX, **Open-RMF fleet adapter** (traffic, thang máy, cửa), adapter VMS/camera AI, adapter access control, local mission cache | Gần thiết bị tòa nhà; giữ một tập nhiệm vụ đã duyệt khi mất cloud |
| **Cloud** (Azure) | Fleet & mission platform, workflow & incident (Camunda 8 + Security Pack), event engine, AI services (VLM, LLM agent, RAG, speech), data platform (rosbag2/MCAP), MLOps & release, observability (OpenTelemetry, Grafana, Azure Monitor), IAM (Entra ID) | Quản lý nhiều site, lịch dài hạn, model lớn, dữ liệu huấn luyện |

Nguyên tắc truyền dữ liệu: telemetry metadata liên tục; ảnh/clip theo sự kiện và theo quyền; **video đi kênh riêng (WebRTC/RTSP)**, lệnh và sự kiện đi MQTT/HTTPS; không mở ROS graph ra Internet.

### 4.2. Bốn tầng "điều phối" không được trộn

| Tầng | Ví dụ | Cơ chế |
|---|---|---|
| Nghiệp vụ | Incident cần bảo vệ xác minh rồi đóng | BPMN / Camunda, human task, SLA |
| Fleet | Robot nào nhận mission, ai giữ dock, hành lang | Scheduler + reservation (Open-RMF) |
| Skill | Đi tới điểm, quan sát, phát lời nhắc, về dock | Behavior tree + ROS 2 Action |
| Motion / control | Giữ thăng bằng, điều khiển khớp | Bộ điều khiển thời gian thực của hãng, safety |

LLM/agent có thể **đề xuất** nhiệm vụ mức cao; không thay bốn tầng này và không bao giờ có tool điều khiển khớp hay tốc độ.

### 4.3. Bản đồ tích hợp

![Context map tích hợp](<Sơ đồ kiến trúc/14-vinuni-kien-truc-2.png>)

| Hệ thống | Chiều | Dữ liệu | Giao thức | Hành vi khi lỗi |
|---|---|---|---|---|
| CCTV / VMS | VMS → nền tảng | Clip theo sự kiện, luồng xem trực tiếp | RTSP, ONVIF, API VMS | Không có clip → incident ghi "thiếu bằng chứng", không lấy clip khác |
| Camera AI analytics | → nền tảng | Sự kiện xâm nhập, đám đông, vật bỏ quên | Webhook JSON | Dedupe theo `event_id`; trễ thì xử lý theo event time |
| Access control | Hai chiều | Trạng thái cửa, log quẹt thẻ; yêu cầu mở | API của hãng | Robot chỉ gửi `request_door_access`; hệ thống cửa quyết định |
| Thang máy, cửa tự động | Hai chiều | Gọi thang, giữ cửa | Open-RMF door/lift adapter | Không phản hồi → chờ / đổi tuyến / báo bảo vệ; ACK không có nghĩa cửa đã mở |
| SOC VinUni | Hai chiều | Incident, video, teleop | Web console, WebRTC | Mất kết nối teleop → hành vi an toàn đã duyệt |
| Bảo vệ | Hai chiều | Điều động, xác nhận | Mobile app (push), bộ đàm | Không xác nhận trong SLA → escalate |
| Lịch hoạt động khu vực | → nền tảng | Sự kiện, giờ mở cửa | API read-only | Thiếu lịch → dùng lịch mặc định đã duyệt |
| Bản đồ / BIM | → nền tảng | Map, semantic zone, lối thoát hiểm | File map có version | Map version lệch → chặn mission |
| Hotline khẩn cấp, y tế trường | Nền tảng → | Chuyển cuộc gọi, vị trí | SIP / app | |
| IT VinUni | Hai chiều | SSO, chính sách mạng | Entra ID, VPN | |

---

## 5. Luồng chính và luồng ngoại lệ

![Camera báo → robot xác minh → bảo vệ xử lý](<Sơ đồ kiến trúc/15-vinuni-luong-su-kien-1.png>)

| Bước | Module | Việc | Dữ liệu chính |
|---|---|---|---|
| 1 | Integration Gateway | Nhận sự kiện từ camera AI | `event_id`, camera, zone, `observed_at`, confidence, model_version |
| 2 | Event Engine | Kiểm tra vùng, khung giờ, access control vừa quẹt thẻ hợp lệ chưa, dedupe | Business event `UNVERIFIED_PRESENCE_IN_RESTRICTED_AREA` (cần xác minh, **chưa kết luận xâm nhập**) |
| 3 | Incident | Tạo incident OPEN | `incident_id`, mức độ |
| 4 | Mission Engine | Tạo mission `VERIFY_SECURITY_EVENT` với điểm quan sát an toàn, deadline | `mission_id`, `observation_point_id` |
| 5 | Fleet Orchestrator | Lọc ràng buộc cứng (capability, pin cho nhiệm vụ + dự phòng + về dock, map version, ODD, không bị teleop giữ) rồi chấm điểm | `Score = w1·ETA + w2·EnergyCost + w3·Workload + w4·CoverageGap` |
| 6 | Robot | ACK, recheck health, đi tới điểm quan sát | `command_id`, TTL, `assignment_epoch` |
| 7 | Perception / VLM / HRI | Quan sát, ảnh/clip, VLM mô tả vùng ảnh; phát câu mẫu nếu được phép | Evidence, mô tả, không nhận diện danh tính |
| 8 | Human Ops | Bảo vệ xem bằng chứng, phân loại, điều động | false alarm / cần xử lý / xác nhận sự cố |
| 9 | Incident | Ghi kết quả; đóng hoặc escalate | Người đóng, lý do |
| 10 | Mission / Fleet | Mission kết thúc khi có bằng chứng quan sát; robot quay lại tuyến | Mission xong **không** tự đóng incident |

**Ngoại lệ đã đặc tả:** không có robot đủ điều kiện → chuyển bảo vệ ngay, dashboard nói rõ lý do; không nhận ACK → kiểm tra assignment rồi mới retry; robot mất mạng sau khi nhận → `EXECUTION_UNKNOWN`, áp lease/fencing, không tái giao chỉ vì timeout; hành lang bị khóa hoặc đông người → điểm quan sát thay thế, robot khác, hoặc bảo vệ trực tiếp; người tại chỗ không hợp tác → robot lùi về vị trí an toàn, không truy đuổi; camera báo nhiều khung hình hoặc hai robot cùng thấy → 1 incident, gom quan sát.

---

## 6. State machine

![Mission state machine](<Sơ đồ kiến trúc/16-vinuni-state-machine-1.png>)

![Robot · kết nối · incident](<Sơ đồ kiến trúc/16-vinuni-state-machine-2.png>)

| Entity | Trạng thái | Quy tắc quan trọng |
|---|---|---|
| Kết nối robot | ONLINE / STALE / OFFLINE | Theo độ tươi heartbeat; **online chưa chắc sẵn sàng** |
| Vận hành robot | READY / BUSY / DEGRADED / CHARGING / MAINTENANCE / SAFETY_STOP / TELEOP | Capability khả dụng = health + mode + policy + pin; SAFETY_STOP cần người có thẩm quyền reset kèm checklist |
| Mission | DRAFT → VALIDATING → QUEUED → ASSIGNED → ACKNOWLEDGED → EXECUTING → SUCCEEDED; nhánh REJECTED, ESCALATED_TO_HUMAN, PAUSED, HANDED_OVER, EXECUTION_UNKNOWN, FAILED, CANCELLING → CANCELLED | SUCCEEDED cần result + evidence; CANCELLED chỉ khi robot xác nhận dừng; không tự resume sau reconnect nếu đang SAFETY_STOP |
| Incident | OPEN → TRIAGED → INVESTIGATING → RESOLVED → CLOSED; FALSE_ALARM | Người có thẩm quyền đóng; false alarm bắt buộc lý do và đi vào dữ liệu huấn luyện |
| Command | CREATED → SENT → ACCEPTED → RUNNING → SUCCEEDED/FAILED | ACCEPTED ≠ hoàn tất; gửi lặp giữ cùng `command_id` |

---

## 7. Hệ tri thức & AI Agent cho robot (HRI)

Robot an ninh cần trả lời người trong campus (hỏi đường, giờ mở cửa, gọi trợ giúp) và hỗ trợ bảo vệ (SOP, tình trạng robot, bối cảnh sự cố). Tôi dùng lại kiến trúc hệ tri thức & agent ở [file 1, mục 3](<Đức BA training AI, ML models.md#3-hệ-tri-thức--ai-agent-chatbot--kiến-trúc-tham-chiếu-chi-tiết>) và thêm ngữ cảnh site – zone – map – mission – ODD.

![Kiến trúc hệ tri thức & AI Agent dùng lại](<Sơ đồ kiến trúc/01-he-tri-thuc-va-ai-agent-1.png>)

### 7.1. Ba nhóm tri thức, ba cách truy cập

| Nhóm | Nguồn | Cách truy cập |
|---|---|---|
| Công khai | Bản đồ hướng dẫn, giờ hoạt động, điểm dịch vụ, FAQ campus | RAG theo site/version; trả lời mọi người |
| Nội bộ vận hành | SOP an ninh, escalation, bảo trì, giới hạn skill | RAG có role/scope; chỉ bảo vệ, operator |
| Thời gian thực | Mission, pin, health, vị trí robot, incident, trạng thái cửa | **Tool/API có quyền**; không bao giờ lấy từ vector index |

### 7.2. Pipeline hội thoại bằng giọng nói

`Mic array → Silero VAD → STT (faster-whisper large-v3 trên edge, hoặc Azure AI Speech) → chuẩn hóa → intent + slot → LangGraph agent → câu trả lời đã duyệt → TTS (Azure AI Speech giọng tiếng Việt, hoặc engine edge đã benchmark) → loa + màn hình`.

- STT confidence thấp hoặc ồn → hỏi lại, hiện chữ trên màn hình để xác nhận.
- Không xác thực quyền bằng giọng nói tự nhận; xác thực bằng thẻ hoặc bảo vệ qua telepresence.
- Người dùng luôn biết đang nói với AI hay với bảo vệ (đèn/biểu tượng trạng thái).

### 7.3. Agent graph cho robot

`Receive → Xác định chế độ người dùng (khách / sinh viên / bảo vệ) → Resolve site & context (zone, map version, mission hiện tại) → Classify intent → Public KB | Operator KB | Read tool | Propose mission → Policy check → Trả lời / Xác nhận → Thực thi API được phép → Xác minh → Báo cáo`.

Giới hạn số vòng tool, tổng thời gian và chi phí; trace lưu quyết định có cấu trúc, nguồn, kết quả tool đã mask. Không đưa lịch tuần tra hoặc nội dung camera vào câu trả lời công khai.

### 7.4. Tool catalog

| Tool | Ai dùng | Input → Output | Chính sách |
|---|---|---|---|
| `lookup_public_location` | Khách, sinh viên | Tên nơi → chỉ dẫn đã duyệt | Read-only, chỉ vùng công khai |
| `search_security_sop` | Bảo vệ, operator | Tình huống → đoạn SOP có nguồn/version | Lọc role/site ở backend |
| `get_robot_health` | Operator | Robot ID → health + độ tươi dữ liệu | Dữ liệu cũ phải nói là cũ |
| `get_incident_context` | Bảo vệ có scope | Incident ID → timeline, token bằng chứng | URL bằng chứng ngắn hạn, kiểm quyền khi tải |
| `propose_patrol_mission` | Operator | Zone, giờ → bản nháp + ràng buộc khả thi | Chỉ tạo nháp |
| `submit_mission` | Dispatcher | Draft ID + expected version → mission ID | Xác nhận + OPA + kiểm ODD/state |
| `request_guard_help` | Người cần giúp | Vị trí + mô tả ngắn → ticket + ACK | Chống spam; không hỏi thông tin cá nhân không cần |
| ~~`set_joint_torque`, `set_speed`~~ | — | — | **Không bao giờ cấp cho LLM** |

Ví dụ: "đi theo người áo đỏ" → agent kiểm tra use case được phép, không suy ra quyền theo dõi người; chuyển bảo vệ quyết định. "Dẫn tôi tới phòng máy chủ" → không tạo mission dẫn vào vùng hạn chế.

### 7.5. Golden set và metric cho HRI

- **Golden**: hai phòng trùng tên khác tòa; lối đi thay đổi sau sửa chữa; khách yêu cầu vào vùng cấm; hỏi lịch tuần tra; văn bản SOP hết hiệu lực; tiếng Việt không dấu, tiếng Anh, mã phòng; tiếng ồn, câu bị cắt; tool timeout; bị chen ngang; nguồn chứa prompt injection.
- **Chấm từng lớp**: STT (WER), intent/slot (F1), retrieval (Recall@k), câu trả lời (đúng, có nguồn), tool selection & arguments, permission, task success, HRI (hiểu đúng ý, thời gian phản hồi, điểm hài lòng).
- **Fail rõ ràng**: nói đúng tên phòng nhưng dẫn qua vùng cấm; trả lời theo bản đồ cũ; báo "đã gửi robot" khi mới tạo nháp.

---

## 8. AI training, fine-tune và dữ liệu robot

### 8.1. Bốn loại model, bốn quy trình

| Loại | Dataset | Tôi (BA/QC) đóng góp | AI/Robotics Engineer sở hữu |
|---|---|---|---|
| Vision detector / event model | Ảnh/video theo camera robot và site; nhãn object/event | Event taxonomy, annotation guide, hard negatives, coverage theo điều kiện | Training code, augmentation, tối ưu inference |
| LLM / VLM assistant | Q&A có nguồn, hội thoại, cặp ảnh–câu hỏi, mẫu tool-call | Ground truth, rubric, ca từ chối/quyền, phân xử lỗi | Chọn base model, LoRA/SFT, serving |
| Tabular ML (health, ETA, pin) | Telemetry window, incident, bảo trì, kết quả mission | Định nghĩa target/horizon, quy tắc chống leakage | Feature, model, calibration |
| Robot skill / VLA / policy | Episode: observation, action, proprioception, nhãn thành công/an toàn | Định nghĩa task, tiêu chí thành công/thất bại, độ phủ dataset, protocol test | Teleop capture, imitation/RL, sim-to-real |

Không gọi mọi feedback về robot là "fine-tune LLM": cập nhật vision, cấu hình navigation, policy workflow và huấn luyện VLA là các thay đổi khác nhau, có gate khác nhau.

### 8.2. Mã nguồn mở dùng ở đâu

| Dự án | Dùng để | Không được hiểu nhầm |
|---|---|---|
| ROS 2 / Nav2 / BehaviorTree.CPP | Middleware, navigation, task execution | Không có sẵn bộ giữ thăng bằng hai chân |
| Open-RMF | Fleet adapter, traffic, thang máy, cửa (có demo khuôn viên trường) | Không thay bộ điều khiển robot |
| NVIDIA Isaac GR00T | Mô hình VLA cho humanoid; mã Apache 2.0, trọng số theo NVIDIA Open Model License | Không phải sản phẩm an ninh hoàn chỉnh; kiểm license riêng code/weights |
| Isaac Sim / Isaac Lab | Mô phỏng, huấn luyện RL/imitation | Thành công trong mô phỏng ≠ thành công thực tế |
| Hugging Face LeRobot | Thu thập dữ liệu, huấn luyện, đánh giá policy | Không đảm bảo chạy ngay trên phần cứng VinDynamics |
| VDA 5050 | Chuẩn giao diện nhiệm vụ/trạng thái robot di động | Chuẩn giao tiếp, không phải thuật toán |

Điều cần nhớ: không có kho mã nguồn mở nào tải về là có ngay đội robot bảo vệ — AI điều khiển cơ thể, quản lý đội robot và nghiệp vụ an ninh là các lớp riêng, phải tích hợp, kiểm thử an toàn và tùy biến.

### 8.3. Dữ liệu → huấn luyện → các cổng đánh giá → phát hành

![Data flywheel và gate](<Sơ đồ kiến trúc/17-robot-ai-data-release-1.png>)

1. **Kịch bản & ODD** (BA): precondition, success, failure, abort, human takeover; QC lập coverage matrix (site/zone, sáng–tối, mật độ người, pin, mạng, version).
2. **Thu thập**: rosbag2/MCAP, teleop demo, đồng bộ timestamp; đúng quyền và giới hạn dữ liệu (mặt người làm mờ khi không cần).
3. **Data Factory**: kiểm timestamp, calibration, frame rơi, ranh giới episode, version bản đồ/robot; nhãn perception ≠ nhãn hành động ≠ nhãn thành công nhiệm vụ.
4. **Split** theo site, ca/ngày, người biểu diễn, episode, robot; không để frame liền nhau của một episode ở hai tập.
5. **Huấn luyện**: YOLO/VLM LoRA, VLA fine-tune (GR00T), RL trong Isaac Lab — engineer chọn; tôi quản lý ngữ nghĩa, độ phủ, golden scenario. Reward RL phải phản ánh cả thành công và vi phạm; chặn reward hacking bằng kiểm tra độc lập.
6. **Gate 1 Offline**: metric theo slice, hard negatives, chạy model đã lượng tử hóa trên phần cứng đích.
7. **Gate 2 SIL** (Isaac Sim/Gazebo): người, vật cản, mất mạng, lỗi cảm biến.
8. **Gate 3 HIL**: phần cứng thật trong khu thử có kiểm soát.
9. **Gate 4 Test site**: tuyến thật ngoài giờ, có người giám sát.
10. **Gate 5 Pilot shadow**: chạy song song, không tác động điều khiển.
11. **Release manifest → OTA canary** (1 robot → 1 zone → toàn site, ngoài giờ cao điểm) → giám sát drift, field failure → rollback cả bộ nếu vượt ngưỡng. Không auto-retrain rồi tự rollout.

**Release manifest** (kế thừa tư duy AI Data Hub):

```json
{
  "release_id": "sec-vinuni-2026.12.1",
  "robot_type": "Dyno", "hardware_revision": "rev-C",
  "firmware": "fw-3.4.2", "ros_distro": "jazzy", "driver_version": "drv-1.9.0",
  "perception_model": {"id": "yolo-sec-v7", "sha256": "…", "precision": "int8"},
  "vlm_model": {"id": "vlm-edge-v2", "adapter": "lora-sec-v3"},
  "skill_versions": {"navigate_to": "2.1.0", "inspect_area": "1.4.0", "return_to_dock": "1.2.3"},
  "map_version": "vinuni-bldA-map-v12", "policy_pack_version": "security-pack-1.3.0",
  "evaluation_run_ids": ["offline-118", "sil-77", "hil-31", "site-12"],
  "approved_by": ["Robotics Lead", "AI Lead", "Safety Officer", "PO"],
  "rollback_bundle": "sec-vinuni-2026.11.3"
}
```

---

## 9. Công việc BA + QC theo từng nhóm trong JD

Mỗi gạch đầu dòng của JD → việc tôi làm trong dự án VinUni → artifact → công cụ.

### 9.1. Requirement Discovery & Analysis

| JD | Việc tôi làm | Artifact | Công cụ |
|---|---|---|---|
| Hiểu bài toán, use case, điều kiện vận hành, kết quả mong đợi cùng PO, Market Development, khách hàng | Workshop với an ninh VinUni; đi ca đêm; quan sát điểm mù; xem demo robot; khảo sát người dùng | Use case catalog, ODD, success criteria | Confluence, Miro, ghi chú hiện trường |
| Elicit, làm rõ, ghi nhận; AS-IS / TO-BE | Quy trình tuần tra và xử lý sự cố hiện tại → quy trình có robot | BPMN AS-IS/TO-BE | Camunda Modeler, draw.io |
| Gap, risk, ảnh hưởng tới hành vi robot và tích hợp | Mỗi yêu cầu mới: chạm Core, Pack, Site hay Adapter? Ảnh hưởng ODD, skill, safety, tích hợp nào? | Gap & impact analysis | Excel, Jira |
| Assumption, dependency, constraint, known limitation | Sổ ghi có owner và hạn xác nhận | Assumption / dependency / limitation log | Confluence, Jira |

Ví dụ sổ ghi:

| Loại | Nội dung | Owner | Hạn xác nhận |
|---|---|---|---|
| Assumption | Wi-Fi phủ đủ tuyến tuần tra tòa A | IT VinUni | Trước khảo sát mạng |
| Dependency | API trạng thái cửa của hãng access control | Vendor | Sprint 3 |
| Constraint | Không lưu video có mặt sinh viên quá 30 ngày | Pháp chế VinUni | Đã ký |
| Known limitation | Robot không đi cầu thang; tầng 2 dùng thang máy qua Open-RMF | Robotics | Baseline |

### 9.2. Requirement Specification for Development

**User story mẫu — phân công robot:**

> Là **điều phối viên**, tôi muốn hệ thống chỉ giao mission cho robot đủ điều kiện, để nhiệm vụ chạy trong phạm vi đã duyệt và tôi thấy rõ khi nào cần người can thiệp.

```gherkin
Given robot R1 có dữ liệu health quá ngưỡng freshness đã cấu hình
When scheduler chọn robot cho mission VERIFY_SECURITY_EVENT
Then R1 không thuộc danh sách đủ điều kiện
And reason_code là HEALTH_STALE và quyết định được ghi audit

Given request tạo mission đã thành công với Idempotency-Key K
When client gửi lại cùng payload với cùng K sau timeout
Then server trả cùng mission_id
And không tạo thêm assignment hay lệnh di chuyển

Given không có robot đủ điều kiện
When hết thời gian chờ theo policy
Then mission chuyển ESCALATED_TO_HUMAN
And dashboard nêu rõ nguyên nhân và không hiển thị "đang xác minh"
```

**Ba tình huống JD nêu đích danh — mất mạng, lỗi cảm biến, AI trả sai:**

```gherkin
Scenario: Mất kết nối cloud khi robot đang di chuyển
  Given robot đang EXECUTING mission tuần tra
  When mất kết nối cloud quá T_cloud
  Then robot duy trì safety cục bộ và hoàn thành checkpoint hiện tại nếu mission nằm trong tập offline đã duyệt
  And nếu không, robot dừng an toàn tại vị trí cho phép và chờ
  And khi có mạng lại, robot đồng bộ sự kiện tồn đọng theo thứ tự và không thực thi lại lệnh đã hết TTL

Scenario: Camera chính của robot hỏng giữa nhiệm vụ
  Given robot đang quan sát điểm A
  When health báo camera chính lỗi
  Then trạng thái robot chuyển DEGRADED và capability capture_evidence không khả dụng
  And mission chuyển sang robot khác hoặc bảo vệ, kèm lý do SENSOR_FAILURE

Scenario: VLM mô tả sai cảnh
  Given VLM mô tả "có người mang vật dụng khả nghi" với độ tin cậy dưới ngưỡng
  When kết quả được gửi tới SOC
  Then mô tả được gắn nhãn "chưa xác minh" kèm ảnh gốc
  And hệ thống không tự nâng mức sự cố và không phát loa cảnh báo
```

**FR / NFR, trong đó an toàn là NFR đo được:**

| ID | Yêu cầu | Cách kiểm chứng |
|---|---|---|
| FR-FLT-01 | Chỉ robot thỏa ràng buộc cứng mới được giao mission | Unit + integration test với bộ fixture health/pin/map |
| FR-INC-03 | Incident chỉ đóng bởi người có thẩm quyền, có lý do | UAT, audit query |
| NFR-SAF-01 | Cơ chế an toàn cục bộ hoạt động độc lập với cloud | Fault injection cắt mạng trong khu thử; quan sát vật lý + telemetry |
| NFR-SAF-02 | Lệnh hết TTL không khởi động hành động mới | Contract test với đồng hồ và hàng đợi trễ |
| NFR-SAF-03 | Tốc độ, khoảng cách tới người, quãng dừng theo giá trị Robotics/Safety đã ký (tham chiếu tiêu chuẩn phù hợp loại robot, ví dụ ISO 13482, ISO 3691-4) | Protocol test do Safety duyệt |
| NFR-SEC-01 | Lệnh không có quyền bị từ chối ở backend và tại robot | Negative test theo role/site/capability |
| NFR-OBS-01 | 100% mission/command có `trace_id`, version, actor | Query độ phủ trace trên toàn bộ test run |
| NFR-PERF-01 | p95 sự kiện tới dashboard ≤ 2 giây trong tải pilot đã định nghĩa | Load test, ghi rõ tải và mạng |
| NFR-PRV-01 | Video có mặt người lưu ≤ 30 ngày, quyền xem theo vai trò | Kiểm cấu hình retention, audit truy cập |

**API contract — tạo mission:**

```http
POST /v1/sites/VINUNI/missions
Authorization: Bearer <operator-token>
Idempotency-Key: 6f1c…
Content-Type: application/json
```

```json
{
  "mission_type": "VERIFY_SECURITY_EVENT",
  "incident_id": "INC-20261116-0042",
  "zone_id": "BLD-A-LOBBY",
  "observation_point_id": "SAFE-POINT-02",
  "required_capabilities": ["navigate", "capture_evidence"],
  "priority": "P2",
  "expires_at": "2026-11-16T16:30:00Z",
  "map_version": "vinuni-bldA-map-v12",
  "policy_pack_version": "security-pack-1.3.0"
}
```

`202 Accepted` chỉ xác nhận đã nhận, trả `mission_id` và `state = VALIDATING`. Lỗi: `400 INVALID_REQUEST`, `403 FORBIDDEN`, `409 STATE_CONFLICT / IDEMPOTENCY_CONFLICT`, `422 OUTSIDE_ODD / INCOMPATIBLE_CAPABILITY`, `503 NO_ELIGIBLE_ROBOT`. Cùng Idempotency-Key với payload khác → từ chối.

**Event contract — tiến độ mission:**

```json
{ "event_id": "evt-…", "schema_version": "1.0", "event_type": "mission.progress",
  "robot_id": "R02", "site_id": "VINUNI", "mission_id": "M-…", "command_id": "C-…",
  "assignment_epoch": 7, "boot_id": "b-…", "sequence_no": 14,
  "observed_at": "2026-11-16T15:00:04Z", "received_at": "2026-11-16T15:00:05Z",
  "state": "NAVIGATING", "pose": {"frame": "map", "x": 12.4, "y": 3.1, "cov": 0.2},
  "map_version": "vinuni-bldA-map-v12", "trace_id": "…" }
```

Phân biệt `observed_at` / `received_at`; lưu UTC, hiển thị Asia/Ho_Chi_Minh; `boot_id` để hiểu khi sequence reset; vị trí luôn kèm frame và sai số.

**ROS 2 ở mức BA:**

| Interface | Ví dụ | Tôi đặc tả |
|---|---|---|
| Topic | `/battery_state`, `/robot_health`, `/pose` | Schema, đơn vị, frame, tần suất, độ tươi, QoS, hành vi khi dữ liệu cũ |
| Service | `get_capabilities`, `validate_goal` | Request/response, timeout, lỗi |
| Action | `navigate_to_observation_point`, `dock` | Goal, feedback, result, reject, cancel/preempt, timeout |

**Error / fallback matrix:**

| Sự cố | Phát hiện | Hành vi phải có | Bằng chứng QC |
|---|---|---|---|
| Mất cloud | Heartbeat / API timeout | Safety cục bộ; chỉ tiếp tục tập offline đã duyệt hoặc dừng an toàn | Cắt mạng, timeline sự kiện, quan sát vật lý |
| Mất localization | Chất lượng pose, độ tươi | Không đi tiếp "mù"; hành vi an toàn của hãng; gọi hỗ trợ | Replay/fault injection có kiểm soát |
| Cảm biến lỗi/che khuất | Self-test, dữ liệu bất thường | Hạ capability, dừng nhiệm vụ phụ thuộc cảm biến | Che camera, dropout, giá trị kẹt |
| Pin không đủ | Ước lượng năng lượng + dự phòng + đường về dock | Không nhận mission mới; bàn giao; về dock | Ca biên; dock bị chiếm/hỏng |
| AI sai/không chắc | Validator, ngưỡng, không có nguồn | Không hành động vượt ranh giới; hỏi lại/chuyển người | Yêu cầu mơ hồ, cảnh không hỗ trợ |
| Cửa/thang máy không phản hồi | Timeout adapter + trạng thái vật lý | ACK ≠ cửa đã mở; chờ / đổi tuyến / báo bảo vệ | ACK giả, sự kiện trễ |
| Hàng đợi gửi trùng/sai thứ tự | ID, sequence, epoch | Dedupe, guard chuyển trạng thái, ghi bất thường | Payload trùng/đảo thứ tự |
| Mất link teleop | Heartbeat phiên, deadman | Hành vi an toàn đã duyệt; lệnh cũ không chạy tiếp | Thử mất link có kiểm soát |
| Map/policy sai version | Manifest không khớp | Từ chối hoặc migrate theo quy trình | Compatibility test |
| E-stop | Trạng thái controller | Ngắt nhiệm vụ; điều kiện khôi phục rõ ràng | Protocol của Safety, không chỉ UI mock |

**Tiêu chí đánh giá AI cùng Tech Lead (accuracy, latency, behavior boundaries):**

| Tính năng AI | Accuracy | Latency | Ranh giới hành vi |
|---|---|---|---|
| Phát hiện người tại khu hạn chế (camera robot) | Event recall ≥ ngưỡng ký, cảnh báo giả / robot-giờ ≤ ngưỡng, theo sáng/tối | Phát hiện → dashboard p95 ≤ 2 s | Không nhận diện danh tính; chỉ "cần xác minh" |
| VLM mô tả cảnh | Rubric 0–2 trên 200 ảnh golden; hallucination = 0 trên tập critical | ≤ 3 s trên edge | Không kết luận vi phạm; gắn "chưa xác minh" |
| Trợ lý hỏi đường | Task success ≥ ngưỡng; WER STT trong tiếng ồn sảnh | Câu trả lời p95 ≤ 3 s | Không dẫn vào vùng cấm; không tiết lộ lịch tuần tra |
| Chọn robot (scoring) | Đúng ràng buộc cứng 100%; ETA lệch ≤ ngưỡng | Quyết định ≤ 500 ms | Không giao robot đang SAFETY_STOP/TELEOP |

Ngưỡng cụ thể chốt cùng Tech Lead sau khi đo baseline; tôi giữ bảng này trong baseline và RTM.

### 9.3. Day-to-day Collaboration với Dev

- **Refinement / planning / daily / review**: giữ backlog "ready" trước sprint 1–2 sprint; trả lời câu hỏi dev trong ngày; câu chưa trả lời được thì ghi owner và hạn.
- **Definition of Ready**: actor và giá trị; ODD/precondition; luồng chính/thay thế/ngoại lệ; schema/API phụ thuộc; state/lỗi/fallback; AC đo được; dữ liệu test; người quyết định. Không đưa story "AI hiểu mọi tình huống" vào sprint khi chưa có coverage và ranh giới.
- **Definition of Done**: code review và test đạt; AC có bằng chứng; RTM cập nhật; known limitation ghi rõ; telemetry/log đủ truy vết; tài liệu/config/version đồng bộ; với field release có gate và người duyệt. "Demo chạy được một lần" chưa phải Done.
- **Review demo/build theo AC**: tôi kiểm cả luồng thất bại (cắt mạng, che camera) chứ không chỉ happy path; lệch thì báo sớm bằng ticket có trace.
- **Hỗ trợ QC**: review test case với yêu cầu, làm rõ expected behavior, bổ sung ca biên từ khảo sát thực địa.

### 9.4. Change Management & Traceability

**Change request mẫu:** "Cho robot tuần tra cả khu ngoài trời." Tôi phân tích tác động tới ODD (mưa, nắng, mặt đường), độ bám, bản đồ, localization ngoài trời, mạng, chuẩn chống nước của phần cứng, dataset vision (ánh sáng ngoài trời), pin, SOP, quyền riêng tư, test plan, hỗ trợ vận hành. PO/PMO quyết định phạm vi/thời gian; Tech Lead chốt khả thi; Safety/Operations duyệt điều kiện vận hành. Không sửa polygon trên UI rồi coi là xong.

Quy trình: `change request → impact assessment → quyết định → cập nhật baseline → implement → re-validate → release`. Workflow đang chạy phải pin version hoặc có quy tắc migrate; không áp workflow mới cho mission giữa chừng.

**RTM mẫu:**

| Requirement | Story | Test | Bằng chứng | Gate |
|---|---|---|---|---|
| FR-FLT-01 chỉ robot đủ điều kiện | SEC-09-03 | TC-FLT-001..008 | Reason code, health snapshot, trace phân công | Tất cả ca critical pass |
| FR-CMD-02 command idempotent | SEC-09-04 | TC-CMD-011 | Cùng `command_id`, không thực thi trùng | Contract + integration |
| FR-AI-03 không lộ SOP nội bộ | SEC-07-02 | TC-AI-021..030 | Từ chối quyền, không lộ snippet | Security/data gate |
| FR-INC-03 incident đóng có người chịu trách nhiệm | SEC-09-05 | TC-INC-041 | Audit actor/lý do | UAT |
| NFR-SAF-01 an toàn khi mất cloud | OPS-05 | TC-HIL-051 | Phản ứng cục bộ theo protocol | Robotics/Safety ký |

Baseline chung cho Dev, QC, Deployment, PMO gồm: BRD/SRS version, story/AC, API/schema, workflow/policy pack, test suite, deployment manifest.

### 9.5. UAT, Deployment Support & Field Feedback

**Checklist commissioning tại VinUni:**
1. Site, zone, tuyến, map, dock, mạng, biển báo, nhân sự phụ trách.
2. Định danh robot (certificate), health, calibration cảm biến, tương thích firmware/model/policy.
3. Preflight và phản ứng mất mạng / dừng / khôi phục theo protocol an toàn.
4. Demo tuần tra – sự kiện – bằng chứng – bảo vệ xác minh, **kể cả luồng thất bại**.
5. Quyền operator, quyền tải clip, audit, retention, phân vùng dữ liệu.
6. Diễn tập bàn giao, ticket bảo trì, rollback, đổi ca.
7. Chốt lỗi tồn đọng và known limitation với owner, điều kiện chấp nhận, thời hạn; lỗi blocker không được che bằng waiver sai thẩm quyền.
8. Bàn giao baseline, ký nghiệm thu theo quy trình khách hàng.

**Phân loại field feedback đúng 4 nhóm JD:**

| Quan sát | Loại | Hướng xử lý |
|---|---|---|
| Một sự kiện tạo hai mission dù spec cấm | **Defect** | Dev sửa, QC replay + regression |
| Bảo vệ cần hoãn mission trong lúc đổi ca nhưng chưa có yêu cầu | **Requirement gap** | BA khảo sát, PO ưu tiên, thêm AC |
| Vision kém khi camera bị chói ở sảnh kính dù trong ODD | **AI limitation** | Phân tích dữ liệu/model, thu thêm dữ liệu, tạm thu hẹp phạm vi |
| Bản đồ sai tầng, camera lắp lệch khi commissioning | **Deployment issue** | Deployment sửa cấu hình/calibration, re-validate |
| Nhiều nguyên nhân cùng lúc | Nguyên nhân chính + phụ | Không ép mọi sự cố thành "AI lỗi" |

**Defect template:** hành vi quan sát · yêu cầu mong đợi · site/robot/mission · điều kiện ODD · versions · `trace_id` · bằng chứng · khả năng tái hiện · tác động nghiệp vụ/an toàn · biện pháp tạm · owner · kết quả retest. Severity theo hậu quả; priority do PO cân đối; owner Safety đặt gate khi liên quan.

**SQL điều tra (read-only):**

```sql
-- Command nào bị bắt đầu thực thi nhiều lần?
SELECT command_id, COUNT(DISTINCT execution_id) AS starts
FROM command_execution_event
WHERE event_type = 'STARTED' AND site_id = :site AND observed_at >= :from
GROUP BY command_id HAVING COUNT(DISTINCT execution_id) > 1;

-- Mission quá hạn mà chưa có trạng thái kết thúc
SELECT mission_id, robot_id, state, deadline_at
FROM mission
WHERE site_id = :site AND deadline_at < CURRENT_TIMESTAMP
  AND state NOT IN ('SUCCEEDED','FAILED','CANCELLED','REJECTED');

-- p95 độ trễ sự kiện (chỉ bản ghi có đồng hồ đã đồng bộ)
SELECT percentile_cont(0.95) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM received_at - observed_at)) AS p95_s
FROM robot_event
WHERE site_id = :site AND observed_at >= :from AND clock_sync_valid AND received_at >= observed_at;
```

**Đọc log có phương pháp:** từ incident/mission lấy `trace_id` → API validation → policy decision → scheduler → queue → edge ACK → ROS action feedback/result → upload bằng chứng. Cloud chỉ có SENT mà không có ACK thì chưa kết luận robot không nhận; có ACK mà không RUNNING thì kiểm precondition/controller; RUNNING mà result trễ thì kiểm buffer edge và mạng trước khi kết luận lỗi model.

### 9.6. Cross-functional Collaboration — RACI

| Hoạt động | Chịu trách nhiệm cuối | Tôi làm |
|---|---|---|
| Cơ hội, quan hệ khách hàng | Market Development | Hỗ trợ discovery, đánh giá phạm vi |
| Mục tiêu, ưu tiên, phạm vi phát hành | PO | Đề xuất bằng dữ liệu và bằng chứng |
| Độ rõ ràng & baseline yêu cầu | **Senior BA** | Spec, truy vết, làm rõ, phân tích tác động |
| Kiến trúc, thuật toán, triển khai | Tech Lead / R&D | Đưa ràng buộc, cùng đánh giá trade-off |
| Thực thi kiểm thử, bằng chứng chất lượng | QC Lead | Review expected behavior, test trực tiếp phần được giao |
| Sẵn sàng vận hành & an toàn robot | Robotics / Safety / Robot Ops | Chuyển rủi ro thành yêu cầu và tiêu chí nghiệm thu |
| Commissioning tại site | Deployment Lead | Hỗ trợ yêu cầu/UAT, ghi nhận gap |
| Nghiệm thu khách hàng | Đại diện khách được ủy quyền | Chuẩn bị bộ hồ sơ nghiệm thu |
| Tiến độ, phụ thuộc, escalation | PMO | Báo tác động, giữ liên kết phạm vi – phụ thuộc – sẵn sàng |

---

## 10. Kế thừa kinh nghiệm từ dự án cũ

![Bản đồ kế thừa kinh nghiệm](<Sơ đồ kiến trúc/18-ke-thua-kinh-nghiem-1.png>)

*Nguồn chỉnh sửa: [18-ke-thua-kinh-nghiem.drawio](<Sơ đồ kiến trúc/18-ke-thua-kinh-nghiem.drawio>).*

### 10.1. Smart Safe → hệ thống an ninh và AI camera cho robot

Smart Safe đã là hệ thống an ninh có dàn thiết bị và AI camera. Tôi dùng lại gần như nguyên vẹn:
- **Chuỗi sự kiện**: thiết bị báo → validate/dedupe → tương quan → incident → thông báo → xác nhận → xử lý → đóng/tự đóng. Robot chỉ thêm bước "điều robot tới xác minh".
- **Cảnh báo giả là chỉ số sống còn**: kinh nghiệm xác minh cảm biến bằng camera chuyển thành xác minh camera cố định bằng robot; cùng cách đo cảnh báo giả / thiết bị-giờ và event precision/recall.
- **Heartbeat và trạng thái kết nối tách khỏi trạng thái nghiệp vụ**: camera/robot mất kết nối ≠ "không có sự cố".
- **Lệnh điều khiển có ACK, timeout, retry, idempotency**: lệnh bật/tắt sensor → command cho robot.
- **Phân quyền theo site, phê duyệt nhiều cấp cho thao tác nhạy cảm**: điều khiển còi → teleoperation robot.
- **UAT 300–400 case và đào tạo vận hành**: kinh nghiệm commissioning nhiều điểm và hỗ trợ sau go-live.

### 10.2. mChat và điều phối thủ tục hành chính → điều phối đội robot

| Hành chính công / mChat | Robot |
|---|---|
| Hồ sơ / hội thoại cần xử lý | Mission |
| Cơ quan có thẩm quyền / agent đủ kỹ năng | Robot có capability phù hợp |
| Điều phối liên thông / routing | Fleet orchestration |
| Quy trình xử lý hồ sơ | Mission workflow |
| Trạng thái, kết quả | Task status, execution result |
| Cán bộ giám sát, xử lý ngoại lệ / supervisor | Human operator, SOC |
| SLA, tự phân phối lại khi agent không phản hồi | Timeout mission, tái giao có kiểm tra |
| Handover summary khi chuyển agent | Bàn giao nhiệm vụ giữa robot, hoặc robot → bảo vệ kèm ngữ cảnh |

Khác biệt tôi luôn nhấn mạnh: tái giao một hội thoại không có hậu quả vật lý; tái giao một mission khi robot cũ chưa xác nhận dừng có thể khiến hai robot cùng tới một điểm hoặc tranh hành lang — vì vậy cần lease, epoch, fencing.

### 10.3. Samsung Smart Factory → fleet management và device health

- **Equipment hierarchy** nhà máy – line – station – máy – linh kiện → site – zone – robot – linh kiện.
- **Trạng thái thiết bị** Running/Idle/Setup/Planned Down/Unplanned Down/Maintenance/Offline → READY/BUSY/CHARGING/DEGRADED/MAINTENANCE/SAFETY_STOP/OFFLINE.
- **Alarm lifecycle, debounce, suppression, correlation** chống alarm storm → health alert của đội robot.
- **Bảo trì định kỳ / theo điều kiện, MTBF, MTTR, OEE** → fleet availability, mission completion, MTBF robot.
- **Recipe có version, gửi xuống máy, nhận ACK, cảnh báo mismatch, rollback** → cấu hình/skill/policy gửi xuống robot.
- **Kiến trúc Azure IoT** (DPS, X.509, device twin desired/reported, OTA theo vòng, Azure Monitor) → device management, configuration & release management của robot. Desired ≠ applied cho tới khi robot báo reported.
- **Error handling** đã làm: out-of-order, duplicate, lost event, reconnect, counter reset → cùng bộ test cho telemetry robot.

### 10.4. Dự án chính phủ → policy, Industry Solution Packs, data governance, workflow động

- **Tuân thủ chặt**: quen làm việc với văn bản có hiệu lực, thẩm quyền, mẫu biểu, thời hạn, audit. Industry Solution Pack về bản chất là "bộ quy trình + bộ quy tắc + sự kiện + mẫu nhiệm vụ" có phiên bản — giống kho thủ tục hành chính.
- **Data governance** (Cổng một cửa): owner, data dictionary, mức nhạy cảm, lineage, MDM danh mục dùng chung → dữ liệu video/telemetry/bản đồ của robot cần owner, retention, quyền truy cập.
- **Workflow động kiểu Camunda**: quy trình cấu hình BPMN + bảng quyết định DMN, version, instance gắn version → mission template và rule theo ngành; một mission đang chạy giữ version cũ.
- **Segregation of duties, phê duyệt nhiều cấp** → ai được tạo mission, ai được teleop, ai được đóng incident, ai được phát hành bản cập nhật.

### 10.5. IoT, edge/cloud, logging, monitoring, configuration, release

Từ Smart Safe, Smart Factory và giai đoạn developer (SafeOne cảnh báo cháy realtime, V-Tracking theo dõi đội xe GPS):
- Phân chia việc edge/cloud theo độ trễ, tự chủ, dữ liệu.
- Buffer offline, replay có thứ tự, chống trùng sau reconnect.
- Logging có `trace_id`; monitoring theo độ tươi dữ liệu; cảnh báo vận hành.
- Configuration có version, desired/reported, người duyệt.
- Release theo vòng (một thiết bị → một nhóm → toàn bộ), rollback cả bộ tương thích.

### 10.6. Các sản phẩm AI → training, fine-tune, nghiệm thu output

HRAI, mChat, Cổng một cửa, XLVPHC Copilot, Tori AI, RPA & OCR/VLM cho tôi kỷ luật BA/QC cho AI: định nghĩa use case và output contract, label guideline, golden set khóa version, metric theo slice, error taxonomy, adjudication, feedback → gold label, quality gate, shadow/canary, production verification. Với robot, tôi giữ nguyên quy trình và thêm các chiều ODD, kết quả vật lý, tương thích phần cứng.

### 10.7. Harness & AI Agents → skill, orchestration cho robot

Kinh nghiệm cấu hình AI coding agent (Codex, Claude Code): MCP server, skill tái sử dụng, subagent, hook, rule, context engineering, multi-agent orchestration. Tư tưởng áp dụng được cho robot:

| Agent phần mềm | Robot |
|---|---|
| Skill có mô tả, input, output, phạm vi | Skill contract: input, precondition, permission, feedback, timeout, failure, postcondition |
| Tool permission / sandbox | Policy enforcement tại runtime (M09), không dựa vào prompt |
| Hook trước/sau khi gọi tool | Pre-check (health, ODD) và post-check (xác minh kết quả) quanh mỗi skill |
| Orchestrator + subagent | Mission engine + fleet orchestrator + skill executor |
| Context engineering | Context site – zone – map – mission cho agent HRI |
| Checkpoint để resume | Checkpoint logic; **nhưng không "undo" được vị trí robot** — resume phải đối chiếu thế giới hiện tại |

### 10.8. Samsung AI Data Hub → luồng training và dataset

AI Data Hub là kinh nghiệm gần nhất với **Data Factory** và MLOps robot: asset card, template, sensitivity, license, phê duyệt, phân quyền theo trạng thái, training job, evaluation, promote/rollback, lineage Dataset → Job → Model → Evaluation → Deployment. Với robot, thêm chiều episode, robot type/hardware revision, firmware, map version vào card và manifest (xem mục 8.3).

### 10.9. Omnichannel, CDP/CXP, CRM → thương mại hóa robot

Customer 360, hành trình khách hàng, ticket/SLA, phân khúc, đo hiệu quả bằng thí nghiệm → onboarding khách hàng/site, gói dịch vụ, SLA hỗ trợ, usage metering, customer success (mục 12).

### 10.10. BA vững + tech vững → use case AI và ngoại lệ chính xác

Nền developer (Android banking, back-office ngân hàng với approval engine, RBAC/ABAC, tối ưu truy vấn, hàng đợi bất đồng bộ) giúp tôi đọc API, log, SQL, hiểu at-least-once, idempotency, race condition — nên khi viết use case AI tôi viết được cả **ngoại lệ hệ thống** (timeout, gửi trùng, dữ liệu cũ, mất mạng) chứ không chỉ happy path, và trao đổi trade-off ngang hàng với Tech Lead.

### 10.11. RPA & OCR + VLM → tự động hóa, VLM, LLM

- OCR-first, VLM-fallback ↔ perception chuyên dụng trước, VLM cho tình huống mở; cùng bài toán model tự tin nhưng sai, calibration, review của người.
- Annotation guideline → golden → regression → dùng nguyên cho dữ liệu camera robot.
- RPA checkpoint, exception matrix, idempotency, human takeover ↔ skill có checkpoint, ngoại lệ và teleop.

---

## 11. Industry Solution Packs

### 11.1. Cách tôi phân tích một ngành (mượn từ dự án chính phủ)

1. **Quy định & chính sách** của khách hàng/ngành (SOP an ninh, quy định riêng tư, nội quy bệnh viện…) → danh sách quy tắc có nguồn và hiệu lực.
2. **Quy trình** AS-IS/TO-BE → BPMN; điểm có con người, SLA, bằng chứng.
3. **Sự kiện** → event catalog (nguồn, schema, mức độ, tương quan).
4. **Quy tắc** → bảng quyết định (DMN): khi nào tạo mission, mức escalate, ai được duyệt.
5. **Mẫu nhiệm vụ** → mission template dùng skill sẵn có; capability còn thiếu → backlog R&D.
6. **Vai trò & quyền**, **tích hợp**, **dialogue playbook**, **KPI**.

### 11.2. Cấu trúc một Pack

`Event Catalog · Task/Mission Templates · Workflow Definitions · Navigation Policies · Dialogue Playbooks · Integrations · Authorization Policies · KPIs` — tất cả có version, validator, chữ ký và test trước khi đưa vào runtime; Pack không được nới giới hạn an toàn cốt lõi ngoài quy trình phê duyệt.

### 11.3. Security Pack mẫu

**Event catalog (trích):**

| Event | Nguồn | Điều kiện tạo incident | Mức |
|---|---|---|---|
| `UNVERIFIED_PRESENCE_IN_RESTRICTED_AREA` | Camera AI, robot | Ngoài giờ, không có quẹt thẻ hợp lệ trong 2 phút | P2 |
| `DOOR_HELD_OPEN_AFTER_HOURS` | Access control | Cửa mở > 60 giây ngoài giờ | P3 |
| `UNATTENDED_OBJECT` | Camera AI | Vật đứng yên > 10 phút ở khu đông người | P2 |
| `FIRE_LANE_BLOCKED` | Robot (đọc biển số) | Xe đỗ ở lối thoát hiểm > 5 phút | P3 |
| `HELP_REQUESTED` | HRI robot | Người bấm/nói yêu cầu trợ giúp | P1–P3 theo nội dung |

**Mission template:**

```yaml
pack_id: security
pack_version: 1.3.0
mission_type: VERIFY_SECURITY_EVENT
required_capabilities: [navigate, capture_evidence]
allowed_roles: [security_dispatcher, event_engine]
preconditions: [robot_health_fresh, localization_valid, route_inside_odd, energy_reserve_ok]
steps:
  - skill: navigate_to_observation_point
    timeout_s: 300
    on_failure: request_alternative_point_or_guard
  - skill: capture_evidence
    on_failure: report_missing_evidence
  - skill: speak_template            # chỉ câu mẫu đã duyệt
    when: policy.allow_deterrence_message
  - skill: await_guard_decision
completion: { requires: [observation_result, evidence_status] }
incident_closure: { actor: authorized_guard }
```

### 11.4. So sánh nhanh các Pack

| Pack | Quy trình đặc thù | Quy tắc / tích hợp riêng | Kinh nghiệm cũ dùng được |
|---|---|---|---|
| Security | Tuần tra → phát hiện → xác minh → xử lý | VMS, access control, quyền xem clip, escalation ca trực | Smart Safe, mChat routing, chính phủ |
| Hospital | Giao thuốc/vật tư → bàn giao có xác nhận | Chain of custody, ngăn khóa theo quyền, khu hạn chế, HIS | Workflow thẩm quyền, OCR truy vết |
| Hotel | Yêu cầu khách → giao đồ → xác nhận | PMS, thang máy, giờ yên tĩnh, riêng tư | CRM, CXP, ticket |
| Restaurant | `ORDER_READY` → nhận → giao → thu khay | POS/KDS, số bàn, tải trọng | Omnichannel fulfillment, WMS |
| Residential | Tuần tra, hướng dẫn → sự cố → ban quản lý | Intercom, kiểm soát ra vào, tách cư dân/site | Smart Safe SaaS đa site |
| Industrial | Kiểm tra → bất thường → bảo trì | MES/SCADA/ERP, vùng nguy hiểm, camera nhiệt | Smart Factory |

---

## 12. Thương mại hóa robot

Từ kinh nghiệm CRM/CDP/Omnichannel, tôi nhìn robot an ninh như một **dịch vụ (Robot-as-a-Service)**:

- **Đối tượng**: khách hàng → site → gói capability → SLA → kênh hỗ trợ.
- **Onboarding site**: khảo sát, bản đồ, ODD, tích hợp, đào tạo bảo vệ, commissioning, nghiệm thu.
- **Gói dịch vụ**: Basic (tuần tra + cảnh báo), Pro (xác minh sự kiện camera, HRI), Enterprise (đa robot, tích hợp access control, báo cáo tùy biến). Gói không được tự mở capability an toàn chưa nghiệm thu.
- **Đo lường & tính phí**: usage metering (robot-giờ hữu ích, số mission, số xác minh), chi phí vận hành/bảo trì; giả thuyết giá dựa trên giá trị nghiệp vụ so với camera AI và bảo vệ truyền thống.
- **Customer success**: ticket/SLA hỗ trợ, adoption của bảo vệ (tỷ lệ dùng tính năng, thời gian phản hồi), báo cáo định kỳ; vòng phản hồi về backlog.
- **Dữ liệu**: không đưa hình ảnh người đi qua camera robot vào marketing; dữ liệu khách hàng tách theo tenant.

---

## 13. Câu trả lời phỏng vấn mẫu và câu hỏi hỏi lại

### 13.1. "Anh mới vào thì tháng đầu làm gì?"

> Tôi làm rõ ba thứ: bài toán vận hành của khách hàng, capability thật của robot và ranh giới tích hợp. Với VinUni, tôi đi theo một ca bảo vệ để hiểu tuần tra và xử lý sự cố hiện tại, xem demo cùng R&D để tách tính năng đã ổn định khỏi roadmap. Sau đó tôi dựng context map, luồng event → incident → mission, state machine, ODD và sổ giả định. Tôi cùng PO chọn một luồng nhỏ đủ giá trị — camera báo sự kiện, robot tới xác minh — viết API, ngoại lệ và AC để Dev/QC dùng ngay trong sprint kế tiếp.

### 13.2. "Kinh nghiệm AI trước đây liên quan gì tới robot?"

> AI Data Hub cho tôi tư duy truy vết dataset → model → deployment; HRAI và các sản phẩm AI cho tôi cách định nghĩa nhãn, snapshot đầu vào, golden set, feedback thành gold label; OCR/VLM và mChat cho tôi cách xử lý output không chắc chắn và đưa nó vào quy trình có con người. Với robot tôi áp dụng vào perception, trợ lý HRI và Data Factory, và bổ sung ODD, kết quả vật lý, độ tươi cảm biến, tương thích phần cứng. Tôi không coi một câu trả lời đúng của model là nhiệm vụ đã hoàn thành an toàn.

### 13.3. "Vì sao chọn anh thay vì một BA thuần robotics?"

> Tôi đóng góp ngay ở phần nền tảng bao quanh robot: mission/incident workflow, fleet operations, tích hợp, data governance, phân quyền và release — những thứ tôi đã làm ở IoT, nhà máy và chính phủ. Nền developer giúp tôi đọc API, log, SQL và trao đổi trade-off với engineer. Khoảng trống của tôi là locomotion và safety engineering; tôi học qua tài liệu, mô phỏng và làm việc sát Robotics Lead, không nhận mình đã làm phần đó.

### 13.4. Tình huống: "Khách muốn robot hiểu lệnh giọng nói, tự tìm và mang vật tới"

> Tôi tách yêu cầu thành các capability: hiểu lệnh (STT + intent + slot), tìm vật (perception + bản đồ semantic + tìm kiếm có giới hạn vùng), lấy và mang (manipulation + navigation có tải), bàn giao (xác nhận người nhận). Với mỗi capability tôi hỏi R&D: đã ổn định, demo hay roadmap? Tôi định nghĩa ODD (loại vật, kích thước, trọng lượng, vị trí, mật độ người), tiêu chí thành công/thất bại/abort, hành vi khi không tìm thấy hoặc lệnh mơ hồ, ranh giới an toàn (không lấy vật trong vùng cấm, không đưa vật nguy hiểm), và kế hoạch đánh giá qua mô phỏng → khu thử → thực địa. Phần nào chưa có capability ổn định thì đưa vào backlog R&D, không hứa trong pilot.

### 13.5. Tiếng Anh

> My strongest contribution is translating operational needs into testable system behavior. I've worked on IoT security monitoring, factory operations, government workflow and data governance, and on AI products where I owned data preparation, golden sets and evaluation. For a security robot fleet I would define the operating domain, mission and incident states, integration contracts, failure behavior and acceptance evidence together with the tech leads, keep mission orchestration separate from real-time control, and never treat a correct AI answer as proof that a physical task was completed safely.

### 13.6. Câu hỏi tôi hỏi lại nhà tuyển dụng

1. Phạm vi Senior BA hiện tập trung vào fleet/mission, AI assistant, Industry Packs hay toàn bộ nền tảng robot?
2. Những capability nào của Dyno đã vận hành ngoài thực địa, những gì đang ở R&D/demo?
3. Ai sở hữu ODD, yêu cầu an toàn và quyết định mở rộng site?
4. Giữa cloud, fleet và robot đang dùng interface/SDK nào; đã có simulator và contract baseline chưa?
5. Dataset, evaluation và field feedback đang quản lý ở đâu (Data Factory)? BA tham gia tới mức nào?
6. Pilot đầu tiên cần chứng minh giá trị gì, ai nghiệm thu, sai số nào không được chấp nhận?
7. Cơ chế phối hợp BA – PO – QC – Deployment – R&D và quyền quyết định change/release hiện ra sao?
