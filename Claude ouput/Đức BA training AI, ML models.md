# Đức BA training AI, ML models

> Tài liệu chuẩn bị phỏng vấn **Senior Business Analyst — VinDynamics**. Trình bày kinh nghiệm của tôi (Nguyễn Kim Đức) ở vai trò **Technical BA kiêm QC** trong 10 dự án có AI/ML: use case, kiến trúc và công nghệ cụ thể, việc tôi làm trong vòng đời dữ liệu → training/fine-tune → đánh giá → phát hành, cùng công cụ đã dùng.
>
> Sơ đồ: thư mục [`Sơ đồ kiến trúc/`](<Sơ đồ kiến trúc/>) có 18 file `.drawio` (mở bằng draw.io, chỉnh được) và ảnh PNG từng sheet. File tiếp theo: [Đức PO làm dự án VinDynamics](<Đức PO làm dự án VinDynamics.md>).

## Mục lục

1. [Định vị bản thân với JD VinDynamics](#1-định-vị-bản-thân-với-jd-vindynamics)
2. [Khung làm việc chung: BA + QC trong training AI/ML](#2-khung-làm-việc-chung-ba--qc-trong-training-aiml)
3. [Hệ tri thức & AI Agent chatbot — kiến trúc tham chiếu chi tiết](#3-hệ-tri-thức--ai-agent-chatbot--kiến-trúc-tham-chiếu-chi-tiết)
4. [Cổng một cửa đầu tư quốc gia — Hệ tri thức & Trợ lý AI](#4-cổng-một-cửa-đầu-tư-quốc-gia--hệ-tri-thức--trợ-lý-ai)
5. [CSDL quốc gia về xử lý vi phạm hành chính — AI Copilot](#5-csdl-quốc-gia-về-xử-lý-vi-phạm-hành-chính--ai-copilot)
6. [Smart Safe — Camera AI](#6-smart-safe--camera-ai)
7. [HRAI One — AI cho nhân sự](#7-hrai-one--ai-cho-nhân-sự)
8. [Tori AI — Techcom Life](#8-tori-ai--techcom-life)
9. [mChat — AI Agent Assist cho chăm sóc khách hàng đa kênh](#9-mchat--ai-agent-assist-cho-chăm-sóc-khách-hàng-đa-kênh)
10. [RPA & OCR kết hợp VLM](#10-rpa--ocr-kết-hợp-vlm)
11. [Omnichannel CDP/CXP & CRM — use case Next Best Action](#11-omnichannel-cdpcxp--crm--use-case-next-best-action)
12. [Samsung AI Data Hub — quản trị vòng đời AI](#12-samsung-ai-data-hub--quản-trị-vòng-đời-ai)
13. [Samsung Smart Factory — 2 use case Machine Learning trên Azure](#13-samsung-smart-factory--2-use-case-machine-learning-trên-azure)
14. [Câu hỏi đào sâu và cách trả lời](#14-câu-hỏi-đào-sâu-và-cách-trả-lời)
15. [Phụ lục A — Bảng tự ôn trước buổi phỏng vấn](#phụ-lục-a--bảng-tự-ôn-trước-buổi-phỏng-vấn)
16. [Phụ lục B — Danh mục sơ đồ](#phụ-lục-b--danh-mục-sơ-đồ)

---

## 1. Định vị bản thân với JD VinDynamics

### 1.1. Giới thiệu 90 giây

> Tôi là BA có nền developer 3 năm (Viettel, FPT), sau đó làm BA Lead / PO ở Samsung R&D, Viettel Commerce và hiện là Lead BA ở VTX Group – Synodus. Mảng tôi mạnh nhất là **hệ thống có thiết bị, dữ liệu và AI cùng chạy trong một quy trình nghiệp vụ**: IoT an ninh Smart Safe với hơn 5.000 thiết bị ở khoảng 400 cửa hàng, Smart Factory của Samsung, và các sản phẩm AI như HRAI, mChat, OCR/VLM, hệ tri thức cho Cổng một cửa đầu tư.
>
> Trong sản phẩm AI tôi làm ở vị trí **BA kiêm QC**: định nghĩa use case và output contract, chuẩn bị và gán nhãn dữ liệu, dựng golden set, chấm và phân loại lỗi, biến feedback thành gold label cho vòng huấn luyện sau, và nghiệm thu trước – sau khi phát hành. Ở Samsung AI Data Hub tôi thiết kế toàn bộ vòng đời Dataset → Training Job → Model → Evaluation → Deployment.
>
> Với robot, tôi mang sang ba thứ: tư duy **thiết bị – sự kiện – trạng thái – ngoại lệ** từ IoT, tư duy **điều phối có thẩm quyền và policy** từ dự án chính phủ, và kỷ luật **đánh giá AI bằng dữ liệu** từ các sản phẩm AI.

**Bản tiếng Anh (30 giây):**

> I'm a technical BA with a developer background. I've worked on IoT security monitoring, smart factory, government workflow platforms and several AI products, where I acted as BA and QC: defining use cases and output contracts, preparing and labeling data, building golden sets, evaluating and triaging AI errors, and turning reviewed feedback into training data. For robotics I bring device-event-state thinking, policy-driven orchestration, and data-driven AI evaluation.

### 1.2. JD nói gì và tôi chứng minh bằng dự án nào

| Nhóm việc trong JD | Bằng chứng mạnh nhất | Artifact tôi mang đi kể |
|---|---|---|
| Requirement discovery: use case, điều kiện vận hành, gap, risk, ảnh hưởng tới hành vi robot và tích hợp | Smart Safe, Smart Factory, Cổng một cửa | Bản đồ use case, AS-IS/TO-BE, assumption & dependency log |
| Specification: user story, FR/NFR, AC đo được; API, data flow, state, error, fallback (mất mạng, lỗi cảm biến, AI trả sai) | Smart Safe (heartbeat, ACK, recovery), XLVPHC Copilot (STATE_CONFLICT), RPA/OCR (idempotency) | Sequence + payload + state machine + bảng lỗi/fallback |
| Tiêu chí đánh giá AI (accuracy, latency, behavior boundaries) cùng Tech Lead | HRAI, OCR/VLM, Tori, mChat | Rubric, metric theo slice, quality gate, error taxonomy |
| Làm việc hằng ngày với dev trong Scrum | Toàn bộ dự án Viettel, Samsung | Backlog Jira, refinement, clarification log, review demo theo AC |
| Change management & traceability | AI Data Hub, dự án chính phủ | RTM requirement → story → test → result, baseline |
| UAT, onsite, commissioning, field feedback | Smart Safe (300–400 UAT case), Tori (production verification), OCR | UAT pack, defect triage, phân loại defect / gap / AI limitation / deployment issue |
| Preferred: ROS2, VLM/LLM/Agentic AI, HRI, edge/cloud, logging, monitoring, config, release, robot safety | Smart Safe, Smart Factory (Azure IoT), Agent/RAG, AI Hub | File thứ hai: case đội robot an ninh VinUni |

Bảng phủ đầy đủ từng gạch đầu dòng của JD nằm ở file [Đức PO làm dự án VinDynamics](<Đức PO làm dự án VinDynamics.md>), mục 9.

---

## 2. Khung làm việc chung: BA + QC trong training AI/ML

### 2.1. "Training AI" gồm sáu loại việc khác nhau

Khi phỏng vấn, tôi tách rõ sáu loại để không nhầm "nạp tài liệu vào vector DB" với "fine-tune model":

| Loại việc | Có đổi trọng số model? | BA làm | QC làm | Artifact |
|---|---|---|---|---|
| **Knowledge ingestion / RAG** | Không | Inventory nguồn, owner, hiệu lực, quyền; quy tắc chunk theo cấu trúc văn bản | Kiểm tra chunk, metadata, retrieval Recall@k trên golden | Knowledge manifest, retrieval report |
| **Prompt / cấu hình** (top-k, filter, temperature, schema) | Không | Output contract (JSON), quy tắc trả lời, từ chối | Chạy lại golden sau mỗi thay đổi một biến | Config version, experiment log |
| **Train ML cổ điển** (XGBoost, LightGBM, IsolationForest) | Có, từ đầu | Định nghĩa nhãn, thời điểm quan sát, cửa sổ dự báo, feature | Chống leakage, split theo thực thể/thời gian, metric theo lớp | Feature catalog, label spec, dataset manifest |
| **Fine-tune model pretrained** (SFT LoRA/QLoRA, DPO; PhoBERT, YOLO, Qwen-VL) | Có, adapter hoặc toàn bộ | Chọn hành vi cần học, phạm vi nhãn | Curate mẫu đúng/sai, adjudication, so candidate với baseline | Dataset SFT/DPO, model card, gate report |
| **Feedback → gold label** | Chưa, là nguyên liệu | Định nghĩa verdict, issue code | Sửa từng trường, phân xử bất đồng, chỉ đưa VERIFIED vào dataset | AI_FEEDBACK, AI_GOLD_LABEL |
| **Agent / workflow** (tool, quyền, state, HITL) | Không | Tool contract, allowed actions, trạng thái, ngoại lệ | Test tool sai tham số, timeout, quyền, gửi lặp | Sequence, state machine, API test |

Nguyên tắc tôi áp dụng: **sửa dữ liệu và retrieval trước, rồi prompt, cuối cùng mới fine-tune**. Fine-tune chỉ khi lỗi ổn định, lặp lại theo mẫu và đã có dữ liệu đúng để học (ví dụ phân loại intent, format JSON, văn phong). Fine-tune không thay được cơ chế cập nhật văn bản có hiệu lực.

### 2.2. Vòng đời 10 bước và ai làm gì

![Vòng đời dữ liệu – training – đánh giá – phát hành](<Sơ đồ kiến trúc/02-vong-doi-training-ai-1.png>)

*Nguồn chỉnh sửa: [02-vong-doi-training-ai.drawio](<Sơ đồ kiến trúc/02-vong-doi-training-ai.drawio>) (2 sheet).*

| # | Bước | Tôi làm gì cụ thể | Công cụ |
|---|---|---|---|
| 1 | Bài toán & output contract | Viết problem statement: ai dùng, quyết định nào được hỗ trợ, lỗi nào gây thiệt hại (false negative hay false positive đắt hơn), AI được làm gì và không được làm gì. Chốt output schema JSON | Confluence, draw.io, Figma (màn hiển thị kết quả AI) |
| 2 | Data contract & label guideline | Nguồn, khóa định danh, mốc thời gian quan sát, NULL/UNKNOWN, PII; guideline có ví dụ đúng/sai, ca mơ hồ, multi-label, evidence span | Excel decision table, dbdiagram.io, Confluence |
| 3 | Thu thập, làm sạch, gán nhãn | SQL kiểm tra NULL, trùng, ngày vô lý, mâu thuẫn; gán nhãn hai người độc lập, SME phân xử | DataGrip, Oracle SQL Developer, pandas, Label Studio, CVAT |
| 4 | Split & golden set | Chia theo thực thể (nhân viên, khách, cửa hàng, nhà cung cấp) **và** theo thời gian; golden set khóa version, không bao giờ dùng để train | pandas, DVC, manifest JSON |
| 5 | Baseline | Cùng AI Engineer chạy rule / prompt / model có sẵn để biết khoảng cách thật | Notebook, Postman |
| 6 | Train / fine-tune | Engineer chạy job; tôi kiểm tra dataset đầu vào, config và tách nhãn đúng phiên bản | MLflow UI, Unsloth/TRL (đọc config), Azure ML / SageMaker console |
| 7 | Đánh giá offline | Metric theo từng slice (lớp hiếm, nhóm khó), confusion matrix, error taxonomy, so với production | pytest, Python, Excel pivot, promptfoo / DeepEval / Ragas |
| 8 | UAT nghiệp vụ | SME chấm rubric trên kịch bản thật, ký nghiệm thu | Jira Xray / TestRail, Excel |
| 9 | Release có kiểm soát | Shadow → canary; manifest gồm model + prompt + index + rule; kế hoạch rollback | Registry, Release note, Confluence |
| 10 | Production verification & feedback | Smoke read-only, lấy mẫu output đã mask, so điểm theo version; PASS / PARTIAL / FAIL + sửa từng trường → gold label | Review UI, SQL, Langfuse, Power BI / Grafana |

### 2.3. Data contract và dataset manifest

Mỗi dataset tôi bàn giao đều có manifest để truy vết được model nào học từ dữ liệu nào:

```json
{
  "dataset_id": "HRAI_GOLD_V12",
  "purpose": "risk_alert_classification + explanation_sft",
  "schema_version": "HRAI_OUTPUT_SCHEMA_V4",
  "feature_version": "HRAI_FEATURE_V5",
  "observation_cutoff": "2026-06-30T23:59:59+07:00",
  "split_strategy": { "by": ["employee_id", "time"], "train": "<2026-04", "val": "2026-04..05", "test": "2026-06" },
  "label_guideline_version": "LG-HRAI-v4",
  "sources": ["APP_AI.CAREER", "KPI_PERIOD", "MANAGER_COMMENT", "AI_GOLD_LABEL(VERIFIED)"],
  "pii_policy": "pseudonymized; tên người trong test dùng mã TST_",
  "counts": { "total": 12500, "pass": 8100, "partial_corrected": 2900, "fail_corrected": 1500 },
  "checksum": "sha256:…",
  "approved_by": ["AI Lead", "HR Expert"]
}
```

Mỗi mẫu có `sample_id`, `input_snapshot_id`, `label`, `label_source` (AI_ACCEPTED_BY_QA / AI_CORRECTED_BY_QA / REPLACED_BY_QA / ADJUDICATED_BY_EXPERT), `reviewer_id`, `verifier_id`, `split`.

**Label guideline** tôi viết theo khung: định nghĩa nhãn → tiêu chí đủ để gán → ví dụ dương / âm / mơ hồ → nhãn không được gán khi thiếu dữ liệu → evidence bắt buộc → người phân xử.

### 2.4. Fine-tune cụ thể tôi tham gia ở mức nào

Tôi không viết trainer, nhưng tôi **chuẩn bị dữ liệu, đọc và rà config, chạy notebook/job đã được bàn giao, và nghiệm thu candidate**. Cấu hình baseline team dùng cho model 7–9B:

| Hạng mục | Giá trị khởi điểm | Ghi chú tôi kiểm tra |
|---|---|---|
| Phương pháp | QLoRA 4-bit (Unsloth) hoặc LoRA bf16 | QLoRA chạy được trên 1 GPU 24–48GB cho 7–9B |
| `r` / `lora_alpha` / dropout | 16 / 32 / 0,05 | Tăng r khi task khó, theo dõi overfit |
| Target modules | q, k, v, o, gate, up, down proj | |
| Learning rate | 2e-4 (QLoRA) · 1e-4 (LoRA) | Cosine, warmup 3–5% |
| Epoch | 2–3 | Dừng sớm theo validation loss **và** metric nghiệp vụ |
| `max_seq_length` | 4.096 | Đủ cho snapshot + evidence |
| Định dạng | JSONL `messages` (system / user / assistant) | Output assistant phải đúng schema 100% |
| DPO (khi có cặp chosen/rejected) | `beta` 0,1 | Chỉ dùng cặp cùng input, cùng evidence |

Sau fine-tune luôn so **base + prompt tốt nhất** với **candidate** trên cùng golden set, kiểm thêm một tập kiến thức chung nhỏ để phát hiện "quên" (catastrophic forgetting) và kiểm JSON hợp lệ 100%.

### 2.5. Metric theo loại bài toán

| Loại | Metric chính | Bẫy cần tránh |
|---|---|---|
| Retrieval | Recall@k, MRR, nDCG; tỷ lệ rò quyền = 0 | Chấm trên nguồn gold; câu không có đáp án phải có tập riêng |
| RAG / LLM | Faithfulness, answer relevancy, context precision/recall (Ragas), citation đúng trang, từ chối đúng, JSON hợp lệ | LLM-as-judge phải hiệu chỉnh với người chấm (Cohen's kappa ≥ 0,7 trên mẫu 100 câu) |
| Phân loại | Precision, recall, macro-F1, PR-AUC, confusion matrix | Lớp hiếm không dùng accuracy; chọn ngưỡng trên validation |
| Risk score | Calibration (Brier, reliability curve), precision@capacity | Score 0,8 chưa phải xác suất 80% nếu chưa calibrate |
| OCR / KIE | CER, WER, field exact match, TEDS (bảng), STP rate, **false accept** | Sai 2 ký tự trong số hóa đơn = sai cả trường |
| Vision | mAP@0.5, event precision/recall, cảnh báo giả / camera-ngày | mAP frame đẹp chưa chắc event tốt; split theo site và ngày |
| Hệ thống | p50 / p95 latency, timeout rate, cost / request | Ghi tải, phần cứng, độ dài input, version |
| Nghiệp vụ | Thời gian xử lý, tỷ lệ sửa tay, tỷ lệ chấp nhận gợi ý, conversion | Cần baseline và nhóm đối chứng |

### 2.6. Quality gate phát hành

![Quality gate](<Sơ đồ kiến trúc/02-vong-doi-training-ai-2.png>)

Gate tôi đề xuất và giữ: candidate không thấp hơn production ở metric chính; recall nhóm rủi ro trọng yếu ≥ ngưỡng đã ký; false positive / false accept không tăng; không slice nào giảm quá mức cho phép; hallucination = 0 trên tập critical; p95 latency và cost trong ngân sách; có model card, dataset manifest và người duyệt.

### 2.7. Bộ công cụ BA + QC tôi dùng

| Nhóm | Công cụ |
|---|---|
| Quản lý yêu cầu & test | Jira (+ Xray), Confluence, Smartsheet, Excel/Google Sheets |
| Mô hình hóa | draw.io, Camunda Modeler (BPMN/DMN), dbdiagram.io, Figma, Visily |
| Dữ liệu | SQL (Oracle, PostgreSQL, SQL Server), DataGrip, Oracle SQL Developer, Python pandas, Power BI |
| Sinh dữ liệu test | Python (pandas, Faker, allpairspy), Excel decision table |
| API & tích hợp | Postman/Newman, Swagger/OpenAPI, MQTTX (IoT) |
| Gán nhãn | Label Studio (văn bản, form), CVAT (ảnh, video, tracking) |
| Đánh giá AI | pytest, promptfoo, DeepEval, Ragas, Langfuse / LangSmith, MLflow UI |
| AI hỗ trợ công việc BA | Codex, Claude Code với skills/MCP, Kiro (spec-driven) để viết spec, sinh test case, prototype |

---

## 3. Hệ tri thức & AI Agent chatbot — kiến trúc tham chiếu chi tiết

Đây là kiến trúc tôi dùng lại cho Cổng một cửa đầu tư, Copilot XLVPHC, Tori AI và lớp AI của mChat. Mỗi dự án thay nguồn tri thức, tool và yêu cầu triển khai (on-prem hay cloud), nhưng khung giữ nguyên.

![Kiến trúc tổng thể hệ tri thức và AI Agent](<Sơ đồ kiến trúc/01-he-tri-thuc-va-ai-agent-1.png>)

*Nguồn chỉnh sửa: [01-he-tri-thuc-va-ai-agent.drawio](<Sơ đồ kiến trúc/01-he-tri-thuc-va-ai-agent.drawio>) (3 sheet: tổng thể, luồng xử lý, ingestion).*

### 3.1. Bảy lớp và công nghệ

| Lớp | Công nghệ | Vai trò | Điều BA/QC phải đặc tả |
|---|---|---|---|
| 1. Kênh | React + Next.js (SSE streaming), mobile app, Zalo OA/Messenger webhook, Copilot sidebar nhúng phần mềm nghiệp vụ, Open API | Nhận câu hỏi, hiển thị nguồn, nút xác nhận | Trạng thái loading / không có nguồn / đang chuyển người; hiển thị trích dẫn |
| 2. Cổng & bảo mật | Kong API Gateway, Keycloak (OIDC, SSO, VNeID với dịch vụ công), Presidio (mask PII), Llama Guard / bộ lọc injection | Xác thực, rate limit, lọc đầu vào | Role, đơn vị, phạm vi dữ liệu lấy từ token, **không** từ lời người dùng |
| 3. Điều phối Agent | LangGraph StateGraph, checkpoint PostgreSQL, Redis cho session | Router → planner → tool → compose; pause/resume; HITL | Danh sách intent, trạng thái lỗi hợp lệ, giới hạn số vòng tool |
| 4. Tools qua MCP | MCP servers: `search_knowledge`, `get_case_status`, `get_allowed_actions` (Camunda 8), `check_rule` (DMN), `draft_document`, `create_ticket` | Truy cập dữ liệu và hành động có kiểm soát | Tool contract: input, output, quyền, timeout, idempotency |
| 5. RAG & model | OpenSearch (BM25) + Qdrant (vector), BAAI/bge-m3, bge-reranker-v2-m3, vLLM phục vụ Qwen2.5-72B-Instruct (on-prem) hoặc Claude / GPT-4o cho dữ liệu công khai | Tìm, xếp hạng, sinh câu trả lời có trích dẫn | Top-k, ngưỡng, quy tắc mâu thuẫn nguồn |
| 6. Kho tri thức | Airflow, Apache Tika, PaddleOCR / PP-Structure, MinIO, PostgreSQL, Neo4j | Ingestion, version, hiệu lực, ACL | Metadata bắt buộc, quy trình duyệt, thu hồi |
| 7. LLMOps | Langfuse, Ragas, DeepEval, promptfoo, MLflow, Prometheus/Grafana | Trace, eval, registry, giám sát | Golden set, rubric, gate, dashboard chất lượng |

### 3.2. Ingestion: từ văn bản đến index có thể xuất bản

![Ingestion tri thức](<Sơ đồ kiến trúc/01-he-tri-thuc-va-ai-agent-3.png>)

1. **Thu thập** từ email, upload, crawl cổng văn bản pháp luật; mỗi file có `document_id`, owner xác nhận là bản chính thức.
2. **Kiểm tra**: ClamAV, SHA-256 chống trùng, số trang, có mật khẩu hay không.
3. **Trích xuất**: PDF có text dùng Apache Tika; bản scan dùng PaddleOCR; bảng dùng PP-Structure. Giữ số trang và bounding box để mở đúng vùng bằng chứng.
4. **Chuẩn hóa**: dựng `heading_path` (Chương › Điều › Khoản › Điểm), bỏ header/footer lặp, giữ nguyên phủ định, đơn vị, ngoại lệ.
5. **BA/SME duyệt** hiệu lực (`effective_from/to`), phạm vi áp dụng, đối tượng (công khai / cán bộ / nội bộ).
6. **Chunk**: văn bản pháp luật cắt theo Điều/Khoản, 400–800 token, overlap 50–100; bảng lớn cắt theo nhóm dòng kèm tiêu đề cột; lưu quan hệ parent–child để lấy lại đủ ngữ cảnh.
7. **Embed & index**: bge-m3 (1.024 chiều, hỗ trợ đến 8.192 token, đa ngôn ngữ) → Qdrant HNSW; song song BM25 trên OpenSearch với analyzer tiếng Việt (ICU tokenizer) để tìm đúng mã thủ tục, số hiệu văn bản.
8. **Publish snapshot**: chỉ chuyển alias `kb_current` sang `kb_vN` khi golden retrieval đạt; rollback bằng cách trả alias về bản trước.
9. **Hết hiệu lực / bị thay thế**: tombstone khỏi index, xóa cache, giữ lịch sử để trả lời câu hỏi "tại thời điểm hồ sơ nộp áp dụng văn bản nào".

### 3.3. Retrieval và sinh câu trả lời

- **Tiền xử lý câu hỏi**: chuẩn hóa tiếng Việt không dấu, mở rộng từ viết tắt (TTHC, IRC, ĐKDN), tách câu hỏi nhiều ý.
- **Lọc trước khi tìm**: theo quyền, đối tượng, ngày hiệu lực tại thời điểm hỏi (hoặc thời điểm hồ sơ), cấp áp dụng.
- **Hybrid**: lấy 20 kết quả BM25 + 20 kết quả vector, hợp nhất bằng Reciprocal Rank Fusion (k = 60), rerank còn 5–8 đoạn.
- **Context builder**: kéo parent chunk khi đoạn con quá ngắn; gắn mã `[S1]…[Sn]` cho từng nguồn.
- **Prompt**: quy tắc chỉ trả lời từ context, mỗi ý gắn mã nguồn, thiếu căn cứ thì nói rõ; output theo schema:

```json
{ "answer": "...", "citations": [{"source_id": "S2", "doc": "NĐ …/2021", "article": "Điều 5 khoản 2", "page": 3}],
  "missing_info": ["quy mô vốn", "tỷ lệ sở hữu nước ngoài"], "confidence": "medium",
  "next_actions": ["Hỏi lại quy mô vốn", "Chuyển chuyên viên Sở"] }
```

- **Output guardrail**: kiểm citation tồn tại và đúng đoạn, câu trả lời không chứa thông tin ngoài context (grounding check), JSON hợp lệ; nguồn mâu thuẫn thì nêu mâu thuẫn và chuyển chuyên viên, không tự chọn.

### 3.4. AI Agent: dùng công cụ nhưng không vượt quyền

![Luồng Agent xử lý một câu hỏi](<Sơ đồ kiến trúc/01-he-tri-thuc-va-ai-agent-2.png>)

- **State graph (LangGraph)**: `AUTHENTICATE → GUARD_INPUT → CLASSIFY_INTENT →` một trong ba nhánh: hỏi đáp (`RETRIEVE → RERANK → CHECK_EVIDENCE → GENERATE → GUARD_OUTPUT`), tra cứu (`READ_TOOL → GENERATE`), thao tác (`PLAN → POLICY_CHECK → HUMAN_CONFIRM → EXECUTE → VERIFY`). Các trạng thái `NEED_CLARIFICATION`, `NO_EVIDENCE`, `DENIED`, `TOOL_TIMEOUT`, `STATE_CONFLICT` là kết quả hợp lệ, có thông điệp và test riêng.
- **Tool qua MCP**: tool đọc chạy với quyền của người hỏi; tool ghi luôn đi qua OPA policy, xem trước, xác nhận và **backend kiểm tra lại quyền + `state_version` tại thời điểm ghi**. Tool ghi có `idempotency_key`; sau timeout không gửi lại mù quáng mà tra trạng thái.
- **Giới hạn**: tối đa 6 lần gọi tool / lượt, tổng thời gian 30 giây, ngân sách token theo kênh.
- **Memory**: ngắn hạn là cửa sổ hội thoại + tóm tắt; dài hạn chỉ lưu sở thích được phép, có TTL. Trạng thái hồ sơ, tồn kho, pin robot **luôn đọc lại từ hệ thống nguồn**, không dùng "trí nhớ" của chatbot.
- **Cache**: semantic cache phân vùng theo tenant, quyền và version index; câu hỏi có dữ liệu cá nhân không cache.

### 3.5. GraphRAG khi nào cần

RAG thường đủ cho câu hỏi một – hai nguồn. Khi câu hỏi phải nối nhiều quan hệ (ngành nghề → điều kiện → thủ tục → cơ quan → hồ sơ → ưu đãi theo địa bàn), tôi thêm **Neo4j**: LLM đề xuất thực thể/quan hệ khi ingest, chuyên viên duyệt quan hệ trọng yếu, mỗi cạnh mang `source_ref` và thời gian hiệu lực. Agent truy vấn graph qua **tool có Cypher template được duyệt**, không cho LLM tự viết Cypher tự do với dữ liệu quan trọng. Ontology mẫu ở mục 4.

### 3.6. Triển khai model và sizing

| Phương án | Khi dùng | Cấu hình tham khảo |
|---|---|---|
| On-prem (dữ liệu nhà nước, nhân sự) | Dữ liệu không được ra Internet | vLLM + Qwen2.5-72B-Instruct-AWQ trên 2 × L40S 48GB hoặc 1 × H100 80GB; Qwen2.5-32B cho tải lớn hơn; tensor parallel khi cần |
| Cloud managed | Dữ liệu được phép, cần nhanh | Amazon Bedrock (Claude Sonnet/Haiku), Azure OpenAI |
| Model nhỏ cho tác vụ phụ | Phân loại intent, rewrite câu hỏi | PhoBERT fine-tune, Qwen2.5-7B, Claude Haiku |

### 3.7. Đánh giá và vận hành chất lượng (LLMOps)

- **Golden set khởi điểm ~300 câu** chia: 50% câu thường gặp, 20% nhiều bước, 15% không có đáp án, 10% phụ thuộc thời điểm hiệu lực, 5% đối kháng (prompt injection, hỏi vượt quyền). Mỗi câu có đáp án gold, nguồn gold (doc/điều/trang), mức rủi ro.
- **Chấm hai lớp**: retrieval (Recall@5, MRR) và câu trả lời (Ragas faithfulness, answer relevancy, context precision/recall + rubric SME: đúng, đủ, có nguồn, đúng phạm vi).
- **LLM-as-judge** chỉ dùng sau khi đo độ đồng thuận với người chấm trên 100 câu; câu critical luôn có người chấm.
- **Regression** chạy tự động (promptfoo/DeepEval trong CI) mỗi khi đổi prompt, model, chunking hoặc index.
- **Trace** bằng Langfuse: input/output đã mask, tool args/result, latency, token, version prompt/model/index; dashboard tỷ lệ NO_EVIDENCE, 👍👎, lỗi tool.
- **Feedback**: 👍👎 + lý do vào hàng đợi review; BA/QC chấm, sửa đáp án → bổ sung golden và dữ liệu fine-tune (intent classifier, embedding) khi đủ mẫu.

### 3.8. Fine-tune trong hệ tri thức: làm ở đâu

| Thành phần | Có fine-tune không | Dữ liệu tôi chuẩn bị |
|---|---|---|
| Intent classifier (PhoBERT / XLM-R) | Có, khi taxonomy ổn định | Câu hỏi thật đã gán intent, cân bằng lớp, câu UNKNOWN |
| Embedding (bge-m3) | Có khi Recall@5 thấp ở thuật ngữ chuyên ngành | Cặp (câu hỏi, đoạn đúng) + hard negative (đoạn giống nhưng sai điều khoản), huấn luyện MultipleNegativesRankingLoss bằng sentence-transformers |
| Reranker | Có khi rerank đảo sai thứ tự | Bộ ba (câu hỏi, đoạn đúng, đoạn sai) |
| LLM trả lời | Hiếm, chỉ cho văn phong / format | Cặp input + câu trả lời chuẩn đã duyệt (SFT LoRA) |
| Tri thức pháp lý | **Không** fine-tune vào trọng số | Cập nhật qua ingestion để còn hiệu lực, nguồn, quyền |

### 3.9. Checklist BA/QC cho mọi dự án hệ tri thức + agent

1. Inventory nguồn: owner, phiên bản, hiệu lực, đối tượng, quyền.
2. Taxonomy intent và danh sách câu hỏi ngoài phạm vi.
3. Output contract và thông điệp cho từng trạng thái lỗi.
4. Tool contract: quyền, timeout, idempotency, xác nhận.
5. Golden set có nguồn gold và câu không có đáp án.
6. Test rò quyền: cùng câu hỏi, người dùng khác quyền phải nhận kết quả khác; không lộ snippet, URL tải file.
7. Test thời gian: văn bản hết hiệu lực, hồ sơ cũ áp dụng văn bản cũ.
8. Test đối kháng: prompt injection trong tài liệu và trong câu hỏi.
9. Gate phát hành và kế hoạch rollback snapshot index.
10. Dashboard chất lượng sau phát hành và quy trình feedback → golden.

---

## 4. Cổng một cửa đầu tư quốc gia — Hệ tri thức & Trợ lý AI

**Bối cảnh.** Nền tảng quốc gia của Bộ Tài chính, kết nối nhà đầu tư với cơ quan ở bộ, ngành, địa phương trong suốt vòng đời đầu tư; 17 module. Tôi phụ trách 3 module: **Trục tích hợp & Quản trị dữ liệu**, **Hệ tri thức & Trợ lý AI**, **Quản lý đầu tư nước ngoài**. Bắt đầu khi còn ở Viettel Commerce (dự án chiến lược), tiếp tục ở VTX Group – Synodus với vai trò Lead BA, kiêm PO cho phần AI.

### 4.1. Use case AI

| ID | Use case | Input → Output | Người dùng | Ranh giới |
|---|---|---|---|---|
| INV-AI-01 | Hỏi đáp thủ tục, điều kiện đầu tư, đa ngôn ngữ (VI, EN, ZH, KO, JA) | Câu hỏi + loại dự án + địa bàn → câu trả lời có điều/khoản, ngày hiệu lực | Nhà đầu tư | Không tư vấn pháp lý thay cơ quan; thiếu dữ kiện thì hỏi lại |
| INV-AI-02 | Checklist hồ sơ cá nhân hóa | Ngành nghề, quy mô vốn, tỷ lệ sở hữu nước ngoài, địa bàn → danh sách thủ tục, thành phần hồ sơ, cơ quan, thời hạn | Nhà đầu tư | Checklist là hướng dẫn, không phải kết quả thẩm định |
| INV-AI-03 | Tra cứu trạng thái hồ sơ bằng ngôn ngữ tự nhiên | Mã hồ sơ (đã xác thực chủ sở hữu) → bước hiện tại, việc cần bổ sung | Nhà đầu tư | Chỉ hồ sơ của chính người hỏi |
| INV-AI-04 | Copilot cán bộ thẩm định | Hồ sơ → tóm tắt, đối chiếu điều kiện, gợi ý căn cứ, cảnh báo thiếu thành phần | Cán bộ Sở, BQL KCN | Cán bộ quyết định; AI không phê duyệt |
| INV-AI-05 | Hỏi đáp số liệu đầu tư (intelligent analytics) | Câu hỏi → truy vấn trên data mart đã duyệt (NL2SQL qua view whitelist) → bảng + biểu đồ | Lãnh đạo, phân tích chính sách | Chỉ view tổng hợp, không truy vấn dữ liệu định danh |

### 4.2. Kiến trúc

![Cổng một cửa đầu tư — kiến trúc](<Sơ đồ kiến trúc/03-cong-mot-cua-dau-tu-1.png>)

| Khối | Công nghệ | Ghi chú |
|---|---|---|
| Trợ lý AI | LangGraph agent, RAG hybrid (OpenSearch + Qdrant, bge-m3), GraphRAG Neo4j, vLLM Qwen2.5-72B-Instruct on-prem | Theo kiến trúc mục 3; đa ngôn ngữ trả lời theo ngôn ngữ câu hỏi, trích dẫn bản tiếng Việt gốc |
| KB CMS | Web biên tập, workflow duyệt 2 cấp, version, hiệu lực | Chuyên viên pháp chế là owner nội dung |
| Trục tích hợp | WSO2 API Manager, Kafka, chuẩn bản tin, kết nối NDXP/LGSP | Kết nối Cổng DVCQG, CSDL quốc gia về đầu tư, đăng ký doanh nghiệp, dân cư/VNeID, hệ thống bộ ngành địa phương |
| Quản trị dữ liệu | OpenMetadata (catalog, lineage, owner), MDM danh mục dùng chung (ngành nghề VSIC, địa bàn, cơ quan), Great Expectations | Danh mục dùng chung là "xương sống" cho cả AI lẫn báo cáo |
| Phân tích | Lakehouse MinIO + Apache Iceberg, Trino, Superset | NL2SQL chỉ chạy trên view đã duyệt |
| Bảo mật | Keycloak, ABAC theo cơ quan và địa bàn, audit bất biến | |

**Ontology cho GraphRAG:**

![Ontology GraphRAG](<Sơ đồ kiến trúc/03-cong-mot-cua-dau-tu-2.png>)

### 4.3. Training và đánh giá

- **Golden Q&A ~400 câu** theo 6 nhóm (thủ tục, điều kiện ngành nghề, ưu đãi, nhà đầu tư nước ngoài, trạng thái hồ sơ, câu ngoài phạm vi), mỗi câu có nguồn gold đến điều/khoản; 20% câu dịch sang 4 ngôn ngữ để đo độ nhất quán giữa các ngôn ngữ.
- **Fine-tune embedding bge-m3** khi Recall@5 thấp với thuật ngữ đầu tư: tôi dựng cặp (câu hỏi, đoạn đúng) từ log đã duyệt và hard negative là đoạn cùng chủ đề nhưng khác điều khoản; engineer train bằng sentence-transformers. So sánh Recall@5, MRR trước/sau trên golden khóa.
- **Fine-tune intent classifier** (PhoBERT) cho 12 intent + UNKNOWN để định tuyến sang RAG, GraphRAG, tool tra hồ sơ hay NL2SQL.
- **NL2SQL**: bộ 150 câu hỏi số liệu có SQL gold và kết quả gold; chấm execution accuracy, không chấm chuỗi SQL.
- **Rò quyền**: cùng một câu hỏi về hồ sơ, tài khoản tỉnh A không được thấy tên nhà đầu tư, snippet hay trạng thái hồ sơ tỉnh B.

### 4.4. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ / đầu ra |
|---|---|---|
| PO | Business case, vision, roadmap 3 module; ưu tiên backlog theo giá trị và mức sẵn sàng dữ liệu | Confluence, Jira, Smartsheet |
| Discovery | Workshop với nhà đầu tư (qua hiệp hội), cán bộ tiếp nhận, chuyên viên pháp chế, quản trị dữ liệu; phân biệt câu hỏi hướng dẫn với quyết định nghiệp vụ | Actor map, use case map, assumption log |
| Chuẩn hóa tri thức | Inventory văn bản và thủ tục; owner; hiệu lực; quy trình cập nhật và thu hồi | Excel, SQL; knowledge manifest |
| Đặc tả | Sequence RAG/tool, API tra hồ sơ và mã lỗi, trạng thái câu trả lời, fallback | draw.io, OpenAPI, Postman; SRS, API mapping |
| Data governance | Data dictionary, owner, mức nhạy cảm, quy tắc chất lượng, lineage | OpenMetadata, dbdiagram.io |
| Build dữ liệu | Kiểm OCR, chunk, metadata; tạo câu paraphrase, câu không có đáp án, câu phụ thuộc mốc hiệu lực | Python pandas, review UI |
| Đánh giá & UAT | Tách lỗi tìm nguồn / sai nguồn / diễn giải sai / tool sai; kiểm citation đúng trang; UAT theo vai trò | Ragas, pytest, Jira; error taxonomy, sign-off |

**Câu chuyện kể.** Trong UAT, trợ lý trả lời ưu đãi thuế theo một nghị định đã bị thay thế. Truy vết cho thấy văn bản cũ thiếu `effective_to` khi ingest. Tôi bổ sung rule bắt buộc trường hiệu lực, tạo 30 câu test "phụ thuộc thời điểm", và đưa kiểm tra này vào gate trước khi publish snapshot. Từ đó lỗi loại này không lặp lại ở các vòng sau.

**Mang sang VinDynamics:** Industry Solution Pack về bản chất là "bộ tri thức + quy tắc + quy trình có hiệu lực theo phiên bản" giống kho thủ tục; kinh nghiệm quản trị nguồn, hiệu lực và quyền dùng được ngay cho SOP an ninh và Knowledge Service (M15) của robot.

---

## 5. CSDL quốc gia về xử lý vi phạm hành chính — AI Copilot

**Bối cảnh.** Hệ thống quản lý CSDL quốc gia về xử lý vi phạm hành chính (Bộ Công an), tại VTX Group – Synodus, vai trò Lead BA. Phần mềm có nhiều luồng nghiệp vụ dài (lập biên bản, ra quyết định, thi hành, khiếu nại), mỗi bước phụ thuộc vai trò, thẩm quyền và thời hạn. Copilot giúp cán bộ thao tác đúng từng bước và hiểu căn cứ.

### 5.1. Use case AI

| ID | Use case | Input → Output | Ranh giới |
|---|---|---|---|
| VP-AI-01 | Hướng dẫn thao tác theo màn hình (guided tour) | `screen_id` + bước + vai trò → các bước cần làm, highlight từng trường | Chỉ hướng dẫn, không tự điền |
| VP-AI-02 | "Tôi làm gì tiếp?" | `case_id` + `state_version` → hành động hợp lệ, điều kiện chưa đạt, thời hạn còn lại | Hành động hợp lệ do workflow trả, không do LLM nghĩ ra |
| VP-AI-03 | Thẩm quyền & căn cứ | Hành vi, mức phạt, chức danh → cấp có thẩm quyền + điều/khoản, hiệu lực | Không tự tính mức phạt bằng LLM; quy tắc thẩm quyền chạy trong DMN |
| VP-AI-04 | Kiểm tra hồ sơ trước khi trình | Bản nháp → trường thiếu, thời hạn sắp quá, tài liệu đính kèm thiếu | Cán bộ sửa và chịu trách nhiệm |
| VP-AI-05 | Hỏi đáp nghiệp vụ chung | Câu hỏi → trả lời từ hướng dẫn nghiệp vụ và văn bản | Có trích dẫn; không có căn cứ thì đề nghị hỏi pháp chế |

### 5.2. Kiến trúc

![XLVPHC AI Copilot — kiến trúc](<Sơ đồ kiến trúc/04-xlvphc-ai-copilot-1.png>)

- **Front-end** React gửi `screen_id`, `case_id`, bước quy trình, vai trò, đơn vị, `state_version` cho Copilot; backend xác minh lại tất cả từ token và DB.
- **Copilot service on-prem**: FastAPI + LangGraph; LLM Qwen2.5-32B-Instruct qua vLLM trên GPU nội bộ, không ra Internet; Langfuse self-host cho trace.
- **4 skill** gắn tool: screen & field catalog (dựng từ SRS và hướng dẫn sử dụng), `get_allowed_actions` từ Camunda 8, RAG văn bản + bảng thẩm quyền DMN, `validate_draft`.
- **Guided tour** bằng driver.js: Copilot trả danh sách bước `{selector, message}` để highlight đúng trường.
- **Đồng thời**: mọi thao tác ghi gửi `expected_state_version`; hồ sơ đã chuyển bước thì trả `STATE_CONFLICT` và tải lại context.

![Luồng "việc tiếp theo"](<Sơ đồ kiến trúc/04-xlvphc-ai-copilot-2.png>)

### 5.3. Training và đánh giá

- **Screen & field catalog** (toàn bộ màn hình và popup) chuyển từ SRS thành tri thức có cấu trúc: màn, trường, bắt buộc, điều kiện hiển thị, lỗi thường gặp. Đây là nguồn cho skill 1; tôi kiểm tra bằng bộ câu hỏi "trường X ở đâu, nhập gì".
- **Golden set theo vai trò × trạng thái**: cùng câu hỏi "tôi làm gì tiếp?" ở nhiều vai trò và trạng thái để chứng minh câu trả lời khác nhau **đúng quy định**. Tỷ lệ "hành động gợi ý ∈ allowed actions" phải đạt 100%.
- **Tập critical về thẩm quyền**: 100% đúng hoặc từ chối; sai một câu là chặn release.
- **Intent classifier** fine-tune để tách 4 skill + câu ngoài phạm vi.
- **Tool-call samples**: cặp (câu hỏi, tool đúng, tham số đúng) dùng để test và khi cần SFT LoRA cho model nhỏ chọn tool.

### 5.4. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| BPMN & decision table | Từng bước, người chịu trách nhiệm, input/output, điều kiện chuyển, thời hạn, nhánh trả lại/thu hồi; bảng thẩm quyền | Camunda Modeler, draw.io, Confluence |
| Context contract | Trường nào gửi sang AI, trường nào phải mask, trường nào backend phải đọc lại | OpenAPI, Postman, DataGrip |
| Catalog màn hình | Chuyển SRS/HDSD thành catalog có cấu trúc | Excel, script Python, Figma |
| Gold theo trạng thái | Câu hỏi × vai trò × trạng thái, câu thiếu dữ kiện, nguồn mâu thuẫn | Excel/JSONL, Python |
| Kiểm thử đồng thời | Người khác chuyển hồ sơ khi đang xem gợi ý; gửi lặp; mất mạng sau commit; quyền bị thu hồi giữa phiên | Postman/Newman, browser network log, truy vấn audit |
| Phân tích lỗi | Lỗi do rule, version workflow, context cũ, retrieval hay model; ticket có `trace_id` | Jira, Langfuse |

**AC mẫu:**

```gherkin
Given bản nháp quyết định đang ở state_version 12 và cán bộ còn thẩm quyền
When cán bộ bấm xác nhận nhưng hồ sơ đã chuyển sang state_version 13
Then hệ thống không ghi thay đổi và trả STATE_CONFLICT
And Copilot hiển thị bước hiện tại mới
And audit ghi nhận lần thử mà không lặp side effect
```

**Mang sang VinDynamics:** vụ việc ↔ mission, thẩm quyền ↔ quyền điều động/teleoperation, `allowed-actions` ↔ skill khả dụng theo trạng thái robot, quy trình có version ↔ policy pack có version. Khác biệt: hành động robot là vật lý, không hoàn tác được như dữ liệu hồ sơ.

---

## 6. Smart Safe — Camera AI

**Bối cảnh.** SaaS IoT giám sát cháy, nổ, xâm nhập cho chuỗi bán lẻ Viettel Commerce: khoảng **400 cửa hàng, hơn 5.000 thiết bị** (gateway, khói, nhiệt, gas, cửa từ, PIR, vỡ kính, AI camera), giá trị ước tính khoảng 30 tỷ đồng/năm nhờ giảm nhu cầu bảo vệ tại chỗ. Tôi là PO kiêm BA duy nhất, UI/UX và tester; viết 300–400 UAT test case. Dự án nằm trong nhóm được ghi nhận giải Viettel Innovation & Breakthrough Ideas (07/2026).

### 6.1. Use case AI

| ID | Use case | Cách hoạt động | Người quyết định |
|---|---|---|---|
| SS-AI-01 | Xác minh cảnh báo cảm biến bằng camera | Cửa từ/PIR báo → edge lấy clip ±10 giây → detector người → gắn mức tin cậy cao / thấp / không xác nhận | Trung tâm giám sát |
| SS-AI-02 | Phát hiện người ngoài giờ trong vùng cấm | YOLOv8 + ByteTrack, polygon vùng, lịch giám sát, dwell ≥ 5 giây | Rule engine sinh cảnh báo; người xác minh |
| SS-AI-03 | Khói/lửa bằng hình ảnh hỗ trợ cảm biến | Model khói/lửa + tín hiệu cảm biến nhiệt/khói | Không thay hệ thống báo cháy chuẩn |
| SS-AI-04 | Dự báo thiết bị sắp lỗi | Chuỗi heartbeat, pin, RSSI, số lần mất kết nối → XGBoost dự báo lỗi trong 7 ngày | Đội kỹ thuật lên lịch bảo trì |

### 6.2. Kiến trúc

![Smart Safe — edge-cloud và AI camera](<Sơ đồ kiến trúc/05-smart-safe-ai-camera-1.png>)

| Lớp | Công nghệ | Ghi chú |
|---|---|---|
| Thiết bị | Cảm biến Zigbee/RF, IoT Gateway 4G/Ethernet, camera IP RTSP/ONVIF | Gateway gửi heartbeat, nhận lệnh bật/tắt sensor |
| Edge AI | NVIDIA Jetson Orin NX, DeepStream, YOLOv8 (TensorRT INT8), ByteTrack, rule vùng & lịch | Gửi metadata + snapshot; clip kéo khi cần; buffer SQLite khi mất mạng |
| Kết nối | MQTT TLS qua EMQX, ACL theo thiết bị | Topic theo site/device; QoS 1; sequence_no chống sai thứ tự |
| Cloud | Spring Boot microservices (ingestion, device, incident, command, notification), RabbitMQ (event, command, DLQ), Redis (trạng thái, lock) | Tư vấn kiến trúc microservice, Redis, RabbitMQ để xử lý bất đồng bộ và mở rộng |
| Lưu trữ | PostgreSQL (site, device, incident), TimescaleDB (telemetry, heartbeat), MinIO (snapshot, clip) | |
| Thông báo | SMS, email, app push (FCM), Zalo ZNS, gọi điện | Template, kênh, mức độ, lịch, retry, lưu kết quả gửi |
| Tích hợp | ERP (user, cửa hàng, chức danh), Google Maps, camera | |
| MLOps camera | CVAT, PyTorch/Ultralytics, TensorRT, model registry, OTA qua Device service | Canary theo cửa hàng |

Lưu ý license: Ultralytics YOLOv8 là AGPL-3.0, dùng thương mại cần license doanh nghiệp; phương án thay thế giấy phép Apache-2.0 là YOLOX hoặc RT-DETR. Đây là một điểm tôi đưa vào danh sách rủi ro khi chọn model.

![Vòng đời cảnh báo](<Sơ đồ kiến trúc/05-smart-safe-ai-camera-2.png>)

### 6.3. Training và đánh giá camera AI

- **Dữ liệu**: clip từ các cửa hàng pilot, đủ ban ngày / đêm hồng ngoại / chói / mưa; hard negative: poster người, ma-nơ-canh, bóng phản chiếu kính, vật nuôi, màn hình TV.
- **Gán nhãn**: CVAT, bounding box + track ID; guideline ghi rõ che khuất, người một phần ngoài khung, đứng sau kính.
- **Split** theo cửa hàng và ngày, không để hai frame liền nhau ở hai tập.
- **Fine-tune** YOLOv8s ảnh 640, khoảng 100 epoch từ pretrained COCO; engineer chạy, tôi kiểm dataset và kết quả.
- **Metric**: mAP@0.5 cấp frame; **event precision/recall** và **cảnh báo giả / camera-ngày** cấp sự kiện; thời gian từ trigger đến dashboard. So sánh FP16 với INT8 trước khi phát hành.
- **Phát hành**: OTA canary 5 cửa hàng → 50 → toàn chuỗi; rollback về model trước nếu cảnh báo giả tăng.

### 6.4. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Khảo sát | Đơn vị vận hành, đội lắp đặt, quản lý cửa hàng; luồng cảnh báo hiện tại | Phỏng vấn, shadowing, URD |
| Master data | Tòa nhà, cửa hàng, thiết bị (IMEI, loại, vị trí, lịch giám sát), cảnh báo, người dùng | Excel, dbdiagram.io, ERD |
| Chuẩn bản tin IoT | Payload telemetry, mã lệnh điều khiển, ACK, tần suất gửi/quét, heartbeat | Swagger, MQTTX, Postman |
| State machine | Incident, kết nối thiết bị, lệnh điều khiển | draw.io, BPMN, Camunda |
| Định nghĩa AI | "Xâm nhập" = vùng + giờ + dwell + ngoại lệ; taxonomy cảnh báo sai; bộ video nghiệm thu | Confluence, CVAT |
| Kiểm thử | Functional, API, integration, regression, smoke, performance, UAT (300–400 case) | Jira, Postman, DataGrip, ChatGPT hỗ trợ sinh case |
| Go-live | Hướng dẫn sử dụng, đào tạo, hỗ trợ sau go-live | Visily, Figma, video |

**Test case đáng kể:** bản tin trùng và sai thứ tự; phục hồi đến trước thao tác xác nhận; nhiều cảm biến cùng một sự cố → 1 incident; thiết bị inactive (`STATUS = 0`) không sinh cảnh báo mất kết nối; tạm dừng giám sát khi bảo trì; người mất quyền site giữa phiên không xem và không điều khiển được; xuất tối đa 50.000 cảnh báo.

**Câu chuyện kể.** Một số cửa hàng báo xâm nhập ban đêm liên tục do PIR nhạy với luồng gió điều hòa. Tôi đề xuất bước xác minh bằng camera tại edge: chỉ cảnh báo mức cao khi detector thấy người trong vùng; còn lại vẫn hiện nhưng gắn nhãn "chưa xác nhận bằng hình ảnh". Tôi viết lại AC cho từng mức tin cậy và thêm test "camera mất kết nối không được hiểu là không có xâm nhập".

**Mang sang VinDynamics:** robot an ninh chính là "camera AI có chân": cùng chuỗi sự kiện → xác minh → điều động → đóng sự cố, cùng bài toán cảnh báo giả, heartbeat, OTA, phân quyền theo site.

---

## 7. HRAI One — AI cho nhân sự

**Bối cảnh.** Hệ thống HR có AI ở Viettel Commerce: tổng hợp dữ liệu nhân sự hiện tại và lịch sử để AI phân loại nhân viên, dự báo rủi ro, nhận diện tiềm năng và sinh nhận xét giải thích cho quản lý. Tôi làm BA kiêm AI QA: dữ liệu, feature, nhãn, bộ kiểm thử, chấm và phản hồi cho vòng huấn luyện. Dự án được ghi nhận trong giải Viettel Innovation 07/2026.

### 7.1. Use case AI

| ID | Use case | Input → Output |
|---|---|---|
| HR-AI-01 | Phân loại nhân viên | Snapshot nhân viên → OUTSTANDING / POSITIVE / NORMAL / NEGATIVE_SIGNAL |
| HR-AI-02 | Dự báo 8 nhóm rủi ro | → nghỉ việc, suy giảm hiệu suất, giảm gắn kết, burnout/quá tải, vi phạm kỷ luật, rủi ro tài chính/tuân thủ, không phù hợp vị trí, chậm phát triển; mỗi rủi ro có mức và độ tin cậy |
| HR-AI-03 | Nhận diện tiềm năng | → nhân sự nguồn, sẵn sàng thăng tiến, ưu tiên đào tạo |
| HR-AI-04 | Nhận xét & khuyến nghị | → nhận xét tổng quan, yếu tố tích cực, tín hiệu rủi ro, lập luận có bằng chứng, khuyến nghị hành động cho quản lý |

Ràng buộc: AI không tự đề xuất kỷ luật hay chấm dứt hợp đồng; khuyến nghị nhạy cảm cần người duyệt.

### 7.2. Kiến trúc

![HRAI One — kiến trúc](<Sơ đồ kiến trúc/06-hrai-one-1.png>)

| Khối | Công nghệ |
|---|---|
| Nguồn | Oracle (schema `APP_AI`: hồ sơ, `APP_AI.CAREER`, KPI theo kỳ, nhận xét quản lý, khen thưởng/kỷ luật, đào tạo, lương & bậc) |
| Pipeline | Apache Airflow DAG: `extract_employee_data → validate_source_data → build_features → create_input_snapshot → call_ai_inference → save_prediction → publish_to_ui` |
| Feature | pandas; `kpi_trend` bằng `np.polyfit`; Feature Catalog 3 tầng `HR_FEATURE_CATALOG`, `EMPLOYEE_FEATURE_VALUE` (FEATURE_STATUS: PRESENT, MISSING, UNKNOWN, NOT_APPLICABLE, CALCULATION_ERROR…), `MODEL_FEATURE_SET` (ví dụ `FS_BURNOUT_V2`) |
| Model | **RoBERTa (PhoBERT)** phân loại sắc thái nhận xét → feature `MANAGER_SENTIMENT`; **XGBoost** xếp loại + 8 rủi ro, score đã calibration; **Qwen3.5-9B + LoRA (Unsloth)** sinh nhận xét/lập luận/khuyến nghị theo JSON |
| Kiểm soát | Validator schema, enum, evidence phải tồn tại trong snapshot, mâu thuẫn class ↔ reasoning; style linter (cụm từ cấm, mẫu câu) |
| Lưu trữ | `AI_PREDICTION` (model / prompt / feature version), `AI_FEEDBACK`, `AI_GOLD_LABEL`, dataset Parquet/JSONL + manifest sha256 |
| UI | HRAI One UI cho quản lý/HR; QA Review UI; Adjudication queue |

### 7.3. Luồng training — từ feedback đến model mới

1. Mỗi prediction gắn **input snapshot bất biến**; không bao giờ query lại dữ liệu hiện tại để dựng dataset (dữ liệu đã đổi sau vài tuần).
2. QA chấm hai lớp: **verdict** (PASS / PARTIAL_PASS / FAIL) và **ground truth đã sửa** (cảnh báo đúng, điểm đúng, evidence đúng, lập luận đúng, issue code). Tách thêm `business_verdict` và `language_verdict` vì một output có thể đúng nghiệp vụ nhưng sai văn phong.
3. Issue code chuẩn: `WRONG_ALERT_TYPE`, `MISSED_ALERT`, `FALSE_POSITIVE`, `WRONG_RISK_SCORE`, `MISSING_EVIDENCE`, `UNSUPPORTED_REASONING`, `STALE_INPUT_DATA`, `FEATURE_CALCULATION_ERROR`, `PROMPT_ERROR`, `BUSINESS_RULE_ERROR`.
4. Quy tắc thành gold: PASS → gold = output AI (không có nút PASS hàng loạt); PARTIAL → gold = merge(AI, sửa của QA), **không có nhãn 0,5**; FAIL → gold = output QA viết lại, output cũ thành `rejected_output`; FAIL chỉ có comment → không vào training.
5. Hai QA chấm khác nhau → Adjudication queue cho HR Expert / QA Lead, ghi `verifier_id` và lý do.
6. DAG `hraI_feedback_to_dataset` (14 task): lấy feedback VERIFIED → dựng gold → kiểm taxonomy, evidence → dedupe → phát hiện xung đột → mask PII → split (theo `employee_id` 70/15/15 + test theo thời gian) → xuất artifact → manifest → đăng ký version.
7. Từ dataset sinh 3 loại dữ liệu: bảng cho XGBoost; `messages` cho SFT; `prompt/chosen/rejected` cho DPO (TRL, PEFT).
8. Thứ tự cải thiện: (A) sửa rule, prompt, feature — nhanh, ít rủi ro; (B) SFT; (C) DPO. Văn phong đi qua 3 cấp: lỗi đơn lẻ → lưu mẫu; lặp lại ~30 lần → thành policy `STYLE-0xx`; đủ dữ liệu → SFT/DPO.
9. Candidate (ví dụ `hraiv1.9-rc1`) so với production: macro-F1 không thấp hơn, recall cảnh báo quan trọng đạt ngưỡng, FP không tăng, không loại nào giảm mạnh; shadow → canary 5% → 20% → 100%, luôn giữ bản cũ để rollback.

### 7.4. Bộ kiểm thử AI hai bước

![Bộ kiểm thử HRAI](<Sơ đồ kiến trúc/06-hrai-one-2.png>)

- **Bước A (làm trước) — `FEATURE_READY`**: feature đã có sẵn, hệ thống không tính lại → đánh giá thuần AI. Excel 3 sheet (TestCase, FeatureInput, ExpectedAIResult) → Python validate & insert vào staging `QA_*` (mã `TST_AI_000001`, không dùng mã thật) → kích hoạt qua `EMPLOYEE_RELOAD` (STATUS=1, IS_TRIGGERED=1) hoặc Postman `POST /api/hr-ai/analyze` → `QA_ACTUAL_AI_RESULT` → **pytest** kiểm `score ∈ [min, max]`, `required_reasons ⊆ actual_reason_codes`, `must_not_predict` → QA chấm reasoning thủ công.
- **Bước B (làm sau) — `RAW_DATA`**: dữ liệu thô → feature job → so `QA_ACTUAL_FEATURE` với `QA_EXPECTED_FEATURE` (ví dụ lương 18 triệu so ngạch 24 triệu → `SALARY_GAP_PERCENT = 25`; điểm 90/80/65 → `PERFORMANCE_DECLINE_RATE = 27,78`). Feature PASS mới chạy end-to-end.
- **Thiết kế tổ hợp**: 6 mức hiệu suất × 5 loại nhận xét × 4 kỷ luật × 4 thâm niên × 4 nghề nghiệp = 1.920 tổ hợp → pairwise (allpairspy) còn vài chục ca; cộng Decision Table, BVA, Equivalence Partitioning, risk-based. Tổng cộng 1.500–2.000 test case qua các vòng.
- **Quy mô mỗi lần chạy**: smoke 10–20, functional 100–300, golden regression 200, edge case 50–100, data quality 50.

Test case mẫu (burnout):

```json
{ "test_id": "HRAI_BURNOUT_003",
  "input": { "kpi_history": [94, 91, 85, 76], "task_count": 185, "overdue_task_rate": 0.23, "overtime_hours": 62 },
  "expected": { "employee_class": "NEGATIVE_SIGNAL",
                "risks": [{"type": "BURNOUT", "level": "HIGH"}, {"type": "LOW_PERFORMANCE", "level": "MEDIUM"}],
                "must_not_predict": ["DISCIPLINE_RISK"],
                "required_reasons": ["KPI_DECLINE_3_PERIODS", "HIGH_OVERTIME"] } }
```

### 7.5. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Data quality | SQL bắt NULL, trùng `(EMPLOYEE_CODE, POSITION, START_DATE)`, `END_DATE < START_DATE`, nhiều vị trí hiện hành, nghỉ việc mà còn KPI kỳ hiện tại, KPI xuất sắc nhưng nhận xét toàn tiêu cực | DataGrip, Oracle SQL |
| Feature & nhãn | Feature catalog, công thức, nguồn, trạng thái thiếu; rule gán nhãn sơ bộ để HR expert xác nhận | Excel, pandas, Confluence |
| Sinh dữ liệu test | Generator có kiểm soát (không random thuần), ví dụ `generate_declining_kpi(start=95, periods=4, step=6)` | Python, Faker, allpairspy |
| Kiểm thử | Bước A/B, regression so phiên bản, phân loại lỗi theo đội xử lý | pytest, Postman, DataGrip |
| Đánh giá | Precision/recall theo từng rủi ro, macro-F1, calibration, tỷ lệ evidence đúng, tỷ lệ sinh thông tin không tồn tại | Python, Excel |
| Feedback & dataset | Thiết kế bảng `AI_FEEDBACK`, `AI_GOLD_LABEL`, quy tắc adjudication, DAG feedback → dataset | dbdiagram.io, Airflow (spec) |
| Production verification | Chọn tập nhân viên có kiểm soát, chạy lại qua `EMPLOYEE_RELOAD`, so với UAT, kiểm quyền xem dữ liệu nhân sự, rollback khi lỗi nghiêm trọng | SQL, log |

**Câu chuyện kể (hallucination do dấu).** AI viết "hiệu suất giảm 3 kỳ liên tiếp" cho một nhân viên có KPI 92 → 93 → 94. Tôi lập checklist reasoning (nhầm dấu tăng/giảm, kết luận quá mức, mâu thuẫn với phân loại cuối, lẫn dữ liệu nhân viên khác), viết rule tự động bắt mâu thuẫn `employee_class = OUTSTANDING` mà reasoning nói "hiệu suất thấp", và đưa 40 ca "xu hướng tăng / ngang / giảm" vào golden regression. Lỗi được phân loại là `UNSUPPORTED_REASONING`, xử lý bằng prompt + validator trước, rồi mới bổ sung mẫu SFT.

**Mang sang VinDynamics:** snapshot đầu vào bất biến ↔ episode robot; issue code & adjudication ↔ phân loại field feedback; quy tắc "chỉ VERIFIED mới thành gold" ↔ không đưa log robot chưa duyệt vào dataset huấn luyện.

---

## 8. Tori AI — Techcom Life

**Bối cảnh.** Techcom Life định hướng AI-first; **Tori** là trợ lý AI in-house cho tư vấn viên tài chính, gợi ý theo thời gian thực tại điểm chạm khách hàng, được khoảng 85% trong 1.500 tư vấn viên sử dụng (theo Insurance Asia). Tôi ở vị trí **Business Analyst & QA**, sở hữu pha **Build** và **Test** trong chuỗi Research → Requirement → Build → UAT → Production Verification, đồng thời hỗ trợ Requirement và quản trị knowledge base nhiều domain.

### 8.1. Use case

| ID | Use case | Đầu ra cần nghiệm thu |
|---|---|---|
| TORI-01 | Tra cứu sản phẩm, quyền lợi, điều khoản loại trừ theo phiên bản sản phẩm | Đúng nguồn, đúng phiên bản, nêu điều kiện và loại trừ; thiếu phiên bản thì hỏi lại |
| TORI-02 | So sánh hai sản phẩm / phương án khi chuẩn bị tư vấn | Bảng so sánh có nguồn; không hứa quyền lợi ngoài tài liệu |
| TORI-03 | Hướng dẫn quy trình (thẩm định, bồi thường, bổ sung hồ sơ) | Checklist và bước tiếp theo; không tự quyết định underwriting/claim |
| TORI-04 | Gợi ý trong lúc tư vấn | Câu hỏi khai thác nhu cầu (bảo vệ sức khỏe, thu nhập, tích lũy, hưu trí, giáo dục) |
| TORI-05 | Chuẩn bị trước buổi gặp | Tóm tắt thông tin khách đã đồng ý chia sẻ + sản phẩm phù hợp để cân nhắc |
| TORI-06 | Kiểm tra nội dung tư vấn | Chỉ ra câu thiếu căn cứ hoặc khác điều khoản; chuyên gia duyệt |

### 8.2. Kiến trúc trên AWS

![Tori AI trên Amazon Bedrock](<Sơ đồ kiến trúc/07-tori-ai-aws-bedrock-1.png>)

| Lớp | Dịch vụ AWS / công cụ | Ghi chú |
|---|---|---|
| Edge & bảo mật | CloudFront + AWS WAF, API Gateway (REST + WebSocket), Cognito (SSO), KMS, Secrets Manager, PrivateLink | Lưu lượng tới Bedrock qua VPC endpoint |
| Ứng dụng | Tori Orchestrator chạy LangGraph trên ECS Fargate; session trên DynamoDB; Lambda | Streaming câu trả lời |
| Agent & tool | **Amazon Bedrock Agents** với action groups (Lambda) gọi Core insurance API (sản phẩm, quyền lợi, hợp đồng, read-only), CRM | Tool chỉ đọc |
| Tri thức | **Bedrock Knowledge Bases** (hybrid search, metadata filter theo sản phẩm, phiên bản, hiệu lực), **OpenSearch Serverless** vector, **Titan Text Embeddings V2** hoặc Cohere Embed Multilingual | |
| Model | **Anthropic Claude Sonnet** trên Bedrock cho trả lời; **Claude Haiku** cho phân loại ý định | Chọn theo benchmark nội bộ, chi phí, latency |
| Kiểm soát | **Bedrock Guardrails**: denied topics (tư vấn ngoài sản phẩm, cam kết lợi nhuận), PII filter, contextual grounding check | |
| Cấu hình | Bedrock Prompt Management, AWS AppConfig | Mỗi thay đổi có version |
| Ingestion | S3 raw → Step Functions → Textract / Bedrock Data Automation (PDF, bảng quyền lợi) → Lambda chuẩn hóa metadata → QA nội dung → S3 curated → KB sync | |
| Đánh giá | **Bedrock Evaluations** (RAG evaluation, LLM-as-judge), golden set trên S3 + kết quả trên DynamoDB, regression runner pytest + boto3, QuickSight dashboard | |
| Quan sát | CloudWatch, model invocation logging, X-Ray | Log đã mask |
| Phát triển | **Kiro** (spec-driven): `requirements.md` viết theo EARS, `design.md`, `tasks.md`, agent hooks chạy regression khi đổi prompt/config, steering file chứa thuật ngữ bảo hiểm; GitHub + CodePipeline + AWS CDK | |

Lưu ý kỹ thuật khi chọn OCR: Textract không hỗ trợ tốt mọi tài liệu tiếng Việt; bảng quyền lợi dạng scan cần kiểm riêng, có thể dùng Bedrock Data Automation hoặc model VLM để parse bảng, rồi QA đối chiếu với PDF gốc.

### 8.3. Chu trình Build → Test → Verify tôi vận hành

![Build–Test–Verify](<Sơ đồ kiến trúc/07-tori-ai-aws-bedrock-2.png>)

1. **Nhận & kiểm kê tài liệu**: hash, trùng, thiếu trang, bản cũ; SME xác nhận bản chính thức. Excel inventory + S3 console.
2. **Ingest & kiểm tra**: đối chiếu bảng quyền lợi sau parse với PDF; gắn `product_code`, `product_version`, `effective_date`, `domain`, `audience`, `page_ref`.
3. **Đổi một biến cấu hình mỗi vòng**: chunk size, top-k, metadata filter, prompt, model. Mỗi thay đổi có lý do và config version.
4. **Chạy golden set** theo domain (sản phẩm, quy trình, underwriting, claim): khởi điểm ~200 câu, mở rộng theo độ phủ và rủi ro; gồm câu thường gặp, nhiều điều kiện, thiếu thông tin, không có đáp án, dễ nhầm giữa hai sản phẩm.
5. **Phân tích lỗi**: ingestion, chunk cắt ngang bảng, retrieval, prompt, tri thức thiếu. Ví dụ câu trả lời bỏ qua điều khoản loại trừ vì bảng bị cắt → sửa chunk, không vội fine-tune.
6. **UAT** với tư vấn viên và SME: kịch bản tư vấn thật, severity theo tác động tới khách hàng.
7. **Release** snapshot KB + config version.
8. **Production verification**: smoke read-only, lấy mẫu hội thoại đã mask, so điểm theo version, theo dõi trend.
9. **Feedback & backlog**: 👍👎 + lý do; lỗi mới → test case mới; yêu cầu thiếu → BA.

**Mẫu ghi một vòng tối ưu (decision log):**

| Vòng | Thay đổi | Giả thuyết | Kết quả trên golden | Quyết định |
|---|---|---|---|---|
| R-07 | Chunk bảng quyền lợi theo nhóm dòng + giữ tiêu đề cột | Lỗi bỏ sót loại trừ do bảng bị cắt | Ghi điểm correctness, citation, tỷ lệ bỏ sót loại trừ trước/sau theo domain | Giữ / hoàn tác, người duyệt, bài học |

### 8.4. Việc tôi làm và công cụ

| Mảng JD | Việc cụ thể | Công cụ |
|---|---|---|
| Build — document lifecycle | Thu thập, xử lý, QA, ingest; quản lý version và hiệu lực | S3, Step Functions console, Excel, Python |
| Build — cấu hình & tối ưu | Vòng build–test–evaluate–adjust; ghi quyết định cấu hình thành tri thức dùng lại | Bedrock console, Prompt Management, Kiro, Confluence |
| Golden set & chỉ số | Duy trì golden set theo domain; theo dõi điểm qua các vòng; chặn regression | S3, DynamoDB, pytest + boto3, Bedrock Evaluations, QuickSight |
| Test plan & UAT | Kế hoạch test luồng chức năng, edge case, kịch bản thực; UAT có severity | Jira, Excel |
| Validate output | Đối chiếu câu trả lời với business rule và độ chính xác domain | Rubric, SME review |
| Regression & production verification | Không suy giảm sau thay đổi/triển khai; báo trend, bất thường | Regression runner, CloudWatch |
| Requirement support | Phát hiện gap, mơ hồ, edge case qua test; chuyển AC thành test case & checklist | Jira, Confluence |
| Knowledge base | Curate nội dung nhiều domain, sẵn sàng cho AI | KB console, Excel |

**AC mẫu:**

```gherkin
Given câu hỏi không nêu phiên bản sản phẩm và quyền lợi khác nhau giữa các phiên bản
When tư vấn viên hỏi số tiền quyền lợi
Then Tori hỏi lại phiên bản hoặc trình bày rõ từng phiên bản kèm nguồn
And không đưa ra một con số duy nhất như kết luận chắc chắn
```

**Mang sang VinDynamics:** JD VinDynamics yêu cầu "define evaluation criteria for AI features" và "re-validation after fixes" — đó chính là chu trình build–test–verify và golden set theo domain; với robot, domain đổi thành kịch bản (tuần tra, xác minh, hỏi đường) và thêm tiêu chí an toàn, latency, hành vi biên.

---

## 9. mChat — AI Agent Assist cho chăm sóc khách hàng đa kênh

**Bối cảnh.** Nền tảng omnichannel của Viettel Commerce gom hội thoại từ Facebook Page, Zalo OA, website widget, livestream comment (và connector email, Telegram, WhatsApp); có routing, SLA, automation, báo cáo. Tôi làm PO/BA cho lớp **AI Agent Assist**, theo sáng kiến chuyển AI từ "trả lời khách" sang "**hiểu khách**". Dự án nằm trong nhóm được ghi nhận giải Viettel Innovation 07/2026.

Nguyên tắc tôi chốt với team: **Rule quyết định hội thoại đi đâu; AI giúp người nhận hiểu nhanh; con người chịu trách nhiệm phản hồi.** AI không tự gửi tin, không tự cam kết giá, không tự chuyển agent, không đổi trạng thái hội thoại.

### 9.1. Use case AI

| ID | Use case | Input → Output |
|---|---|---|
| MC-AI-01 | Nhận diện intent | Chuỗi tin nhắn → primary + secondary intent (PRODUCT_CONSULTING, PRICE_INQUIRY, STOCK_CHECK, ORDER_TRACKING, COMPLAINT, PROMOTION_INQUIRY, INSTALLMENT_INQUIRY, COMPARE_PRODUCT, PURCHASE_PRODUCT, WARRANTY_SUPPORT, UNKNOWN) |
| MC-AI-02 | Tóm tắt hội thoại | → nhu cầu chính, sản phẩm, vấn đề chưa giải quyết; dùng khi bàn giao agent (handover summary) |
| MC-AI-03 | Chấm lead | → HOT / WARM / COLD / UNQUALIFIED / UNKNOWN + lý do; ưu tiên queue, tạo task gọi lại |
| MC-AI-04 | Trích entity & nhu cầu | → model, màu, ngân sách, địa điểm, SĐT, mã đơn, hình thức thanh toán, thời điểm mua |
| MC-AI-05 | Sentiment & blocker | → tiêu cực / tức giận, xu hướng; blocker (PRICE_CONCERN…) kèm `evidence_message_id` |
| MC-AI-06 | Next best action & draft reply | Chat + snapshot ERP → câu hỏi khơi gợi, gợi ý chốt đơn, bản nháp trả lời, product card (SKU, giá, khuyến mại, tồn theo cửa hàng, bảo hành, timestamp) — chỉ chèn vào ô soạn |

### 9.2. Kiến trúc

![mChat — kiến trúc 3 lớp](<Sơ đồ kiến trúc/08-mchat-ai-agent-assist-1.png>)

| Lớp | Công nghệ | Trách nhiệm |
|---|---|---|
| Kênh & adapter | Webhook Facebook/Zalo OA, widget; verify signature, dedup `channel_message_id` | Không mất, không trùng tin |
| Deterministic | Conversation service (PostgreSQL), Routing engine (giờ làm việc, ưu tiên VIP/B2B, chiến lược ít hội thoại mở / trả lời nhanh / cân bằng, capacity), SLA 3 chặng, tự phân phối lại khi agent không phản hồi 60 phút hoặc offline 30 phút | Hội thoại luôn chạy kể cả khi AI lỗi |
| AI Understanding | AI Trigger service (Redis debounce, lock), RabbitMQ (priority, retry, DLQ), AI Analysis worker LangGraph; **PhoBERT** fine-tune cho intent/NER; **Qwen2.5-14B-Instruct** qua vLLM (JSON mode) cho tóm tắt, lead, next action; Product matching qua ERP API | Phân tích bất đồng bộ, có version |
| Human | Agent workspace (SSE/WebSocket): insight panel, draft reply, product card; Supervisor dashboard | Agent quyết định và gửi |
| Dữ liệu | `AI_ANALYSIS`, `AI_EXTRACTED_ATTRIBUTE`, `AI_RECOMMENDED_ACTION`, `AI_FEEDBACK` (bản gốc + bản agent sửa), đồng bộ lead/intent sang CRM Customer 360 | Truy vết `model_version`, `prompt_version`, `from/to_message_id` |

![Trạng thái AI job](<Sơ đồ kiến trúc/08-mchat-ai-agent-assist-2.png>)

- **Trigger**: P1 MANUAL (nút "AI gợi ý") > P2 SPEAKER_CHANGED > P3 CUSTOMER_IDLE (5 phút từ tin cuối, reset mỗi tin); thêm agent nhận/chuyển nhóm (handover summary), tạm dừng, đóng (final analysis).
- **Chống trigger thừa**: debounce 5–10 giây, gom tin thành "turn", 1 job active / hội thoại, cooldown 30 giây, bỏ "ok/vâng/sticker", idempotency key `convId-msgId-type`.
- **Trạng thái job**: PENDING, PROCESSING, COMPLETED, FAILED, RETRYING, CANCELLED, STALE, DEAD_LETTER. Kết quả cũ hơn hội thoại hiện tại → STALE, không ghi đè insight mới.

### 9.3. Training và đánh giá

- **Taxonomy** (intent, need, entity, sentiment, interest LOW…VERY_HIGH, lead, blocker, outcome) + label guideline + decision table; hai người gán nhãn độc lập trên **Label Studio**, bất đồng thì SME quyết.
- **Dataset**: hội thoại đã ẩn danh (mask SĐT, email), cắt theo phiên, giữ multi-turn; tách Training / Validation / Test / Regression / Adversarial; không để hội thoại gần giống nhau ở cả train và test.
- **Fine-tune PhoBERT** cho intent đa nhãn và NER; LLM dùng prompt + JSON schema, chỉ cân nhắc SFT LoRA cho trích xuất khi lỗi format/nhãn ổn định.
- **Synthetic data** cho ca hiếm bằng LLM **khác** model đang test (tránh tự củng cố), người duyệt trước khi dùng.
- **Golden test set** phủ: có dấu/không dấu, viết tắt, Việt pha Anh, emoji, mỉa mai, spam, đổi nhu cầu giữa chừng, lead nóng nói gián tiếp, dữ liệu cá nhân.
- **Feature matrix** kênh × intent × lead × sentiment × blocker × trạng thái sản phẩm = 9.600 tổ hợp → pairwise còn vài trăm.
- **Metric**: intent macro-F1 + confusion matrix; sentiment recall lớp tiêu cực; entity P/R; lead macro-F1; tóm tắt và chiến lược chấm rubric 10 điểm (nhu cầu, sản phẩm, blocker, việc còn chờ, không bịa — mỗi mục 0–2); product fact phải khớp ERP, sai một giá trị quan trọng là fail; tỷ lệ agent chấp nhận / sửa / từ chối gợi ý.
- **Đối soát 3 lớp**: API trả HOT thì DB phải lưu HOT, UI phải hiện HOT; null không được thành chuỗi "null".

### 9.4. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Ranh giới Rule–AI–Human | As-is/To-be, BPMN, event map, scope/non-scope | draw.io, Miro |
| Taxonomy & guideline | Intent, lead, blocker, rule điểm lead (80–100 HOT, 50–79 WARM, < 50 COLD, kèm điều kiện ngoại lệ) | Excel (Taxonomy, Feature_Matrix, Test_Conversation, Expected_Result, Test_Result), Confluence |
| Dữ liệu & mapping | ERD, data dictionary, mapping API/DB/UI/AI; webhook trùng, merge contact, tin hệ thống lọt vào input | dbdiagram.io, DataGrip, pgAdmin |
| Routing/SLA | Conflict matrix giữa các rule ưu tiên, capacity, fallback | Decision table |
| AI trigger & job | Trigger catalog, state machine, job contract | draw.io, OpenAPI |
| ERP grounding | Mapping SKU/giá/tồn/khuyến mại, rule "không nói còn hàng nếu ERP không trả tồn" | Postman |
| UI Agent Assist | Trạng thái loading / empty / low-confidence / ERP unavailable / stale | Figma |
| Kiểm thử | Hallucination, ambiguity, adversarial, noisy text, idempotency/retry, AI down mà chat vẫn chạy; E2E 13 bước | Postman/Newman, Playwright, pytest, promptfoo, DeepEval, Langfuse, k6 |

**Câu chuyện kể.** Khi rà spec routing, tôi phát hiện thứ tự ưu tiên giữa "agent tiếp nhận cuối", "khách VIP" và "nhóm phòng ban" chưa được chốt — hai rule có thể chọn hai agent khác nhau. Tôi lập conflict matrix, đưa PO quyết định thứ tự và bổ sung AC. Cũng từ đó tôi đề xuất AI **không** tham gia quyết định routing để giữ hành vi xác định và dễ kiểm thử.

**Mang sang VinDynamics:** routing hội thoại ↔ phân công nhiệm vụ cho robot; SLA và tự phân phối lại ↔ timeout mission và tái giao; handover summary ↔ chuyển nhiệm vụ giữa robot hoặc robot → bảo vệ kèm ngữ cảnh.

---

## 10. RPA & OCR kết hợp VLM

**Bối cảnh.** Đề án tự động hóa chứng từ của Phòng CNTT Công ty Thương mại & XNK Viettel: khảo sát 3 đơn vị (Trung tâm XNK, Phòng Pháp chế & Đầu tư, Trung tâm Phân phối), 17 kịch bản. Hiện trạng: copy–paste giữa email/PDF/Excel/hệ thống, rà mắt, tra HS theo kinh nghiệm (rủi ro áp sai mã, sửa tờ khai, bị phạt), hồ sơ lưu không chuẩn. Tôi làm BA kiêm QC: use case, field catalog, annotation guideline, business rule, output schema, confidence workflow, test dataset, AC.

### 10.1. Use case tiêu biểu

| Đơn vị | Use case | Input → Output | Hệ thống đích |
|---|---|---|---|
| XNK | Bản nháp tờ khai hải quan | Invoice, Packing List, B/L, C/O, hợp đồng → tờ khai nháp + checklist thiếu chứng từ | VNACCS (qua phần mềm khai báo), Google Sheet theo dõi |
| XNK | Đối soát bộ chứng từ | HĐ, Invoice, PL, tờ khai nháp → bảng chênh lệch theo mức độ, highlight chỗ lệch | Ticket |
| XNK | Gợi ý HS code | Mô tả hàng → top gợi ý + lý do; **người xác nhận trước khi bot điền** | Tờ khai |
| XNK | Số hóa biểu thuế | PDF/scan → danh mục tra cứu có version theo ngày hiệu lực | Danh mục nội bộ |
| Pháp chế & Đầu tư | Nhập hợp đồng | HĐ/phụ lục → số HĐ, ngày ký, các bên (tên, MST, địa chỉ, đại diện), giá trị trước thuế/VAT/tổng, thời hạn, mốc thanh toán (tổng % = 100%) | **QLHĐ qua API** |
| Pháp chế & Đầu tư | Bảng so sánh báo giá/hồ sơ thầu | Báo giá → bảng so sánh, kiểm "đơn giá × số lượng = thành tiền" | Excel/Sheet |
| Pháp chế & Đầu tư | Đối soát thanh toán | Nghiệm thu, hóa đơn, kế hoạch thanh toán → danh sách đủ điều kiện; paid/partial/late/unmatched | QLHĐ |
| Phân phối | Chứng từ kho, POD, đối soát 4 nguồn | Phiếu giao/xuất, biên bản giao nhận → WMS/ERP; serial/lô confidence thấp thì cảnh báo trùng serial | WMS/ERP |

### 10.2. Kiến trúc: OCR-first, VLM-fallback

![RPA & OCR + VLM](<Sơ đồ kiến trúc/09-rpa-ocr-vlm-1.png>)

| Tầng | Công nghệ | Ghi chú |
|---|---|---|
| Ingestion | Email/Upload/SFTP/API, ClamAV, MinIO (SHA-256, bất biến), OpenCV (deskew, 300 DPI, tách trang), phân loại chứng từ | Spring Boot ingestion API, PostgreSQL, RabbitMQ, Airflow |
| Luồng A — OCR modular | **PaddleOCR 3.x (PP-OCRv5)** detection + recognition → **PP-StructureV3** (layout, bảng, reading order) → **LayoutLMv3** KIE (BIO, key–value), serve bằng Triton → rule chuẩn hóa | Mặc định cho template quen; rẻ, có confidence từng tầng |
| Luồng B — VLM | **Qwen2.5-VL-7B-Instruct + LoRA** (fine-tune bằng Unsloth QLoRA), serve **vLLM**; output JSON schema + evidence (bbox, trang) | Khi confidence thấp, thiếu trường, layout lạ, bảng merge cell |
| Kiểm soát | Business validation, cross-document match, confidence gate, human review UI (ảnh trái – form phải, highlight bbox, phím tắt) | |
| Đầu ra | API → QLHĐ (`POST /api/v1/ocr/jobs` + signed URL + `schema_code` + callback HMAC + idempotency key), **UiPath** robot cho hệ thống không có API (tờ khai nháp, ERP, WMS), Google Sheets API | API trước, RPA UI sau |

**Confidence gate:** ≥ 0,95 tự nhập; 0,80–0,95 review; < 0,80 chạy VLM hoặc nhập tay. Với QLHĐ: ≥ 0,98 xanh, 0,85–0,98 vàng, < 0,85 đỏ. Ngưỡng theo trường: số tài khoản ≥ 0,995 hoặc luôn review; MST ≥ 0,99; giá trị hợp đồng **luôn chạy rule** dù confidence cao. Confidence tổng = 20% detection + 35% recognition + 35% entity + 10% validation. Confidence của VLM tính từ nhiều tín hiệu: khớp OCR, nhất quán qua nhiều lần chạy, rule pass, có bbox bằng chứng.

![Vòng đời chứng từ](<Sơ đồ kiến trúc/09-rpa-ocr-vlm-2.png>)

### 10.3. Training, gán nhãn và đánh giá

- **Thứ tự**: chạy pretrained → đo gap theo tầng → chỉ fine-tune tầng không đạt. Với VLM: prompt chuẩn → JSON schema → few-shot → rule → golden → rồi mới LoRA/QLoRA.
- **Nhãn**: layout bbox, polygon detection, crop + transcript recognition, token BIO (`B-INVOICE_NO`, `B-TAX_CODE`…), quan hệ key–value, bảng (cell, rowspan, colspan); mẫu VLM `{image, messages}`.
- **Quy trình gán nhãn**: Annotator A → Annotator B → Reviewer nghiệp vụ phân xử → tool kiểm format → duyệt dataset. Tôi xử lý ca mơ hồ và cập nhật guideline.
- **Split**: train / val / test / **Golden-UAT khóa**; cả một hợp đồng chỉ nằm trong một tập; giữ lại một số nhà cung cấp/template chưa từng thấy để đo khả năng tổng quát. Dataset công khai SROIE, FUNSD, CORD chỉ để benchmark; dữ liệu tiếng Việt nội bộ quyết định chất lượng thật.
- **Metric theo tầng**: layout P/R/mAP; detection H-mean; recognition **CER/WER**; entity P/R/F1; bảng **TEDS**; end-to-end **field exact match**; VLM: JSON validity, hallucination rate, missing field, evidence accuracy; vận hành: **STP rate, false accept**, số trường sửa / tài liệu, latency, cost / trang.
- **Calibration**: bảng confidence so với accuracy thực; nếu confidence > 0,98 mà accuracy thật 90% thì không dùng làm ngưỡng tự nhận.
- **Regression**: mỗi model version chạy lại golden, bộ lỗi cũ, template hiếm, ảnh xấu; một version tăng MST nhưng giảm line-item là regression dù điểm tổng tăng.
- **Feedback**: correction → Data Reviewer xác nhận → golden/training → retrain → regression → deploy; không đưa thẳng mọi correction vào training.

### 10.4. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Khảo sát & chọn kịch bản | Document inventory, as-is/to-be, scope matrix, risk matrix; ưu tiên kịch bản tần suất cao, dữ liệu ổn định | Excel, BPMN, draw.io |
| Chuỗi artifact BA | Field catalog → annotation guideline → business rules → output schema → confidence workflow → test dataset → AC | Confluence, Excel, JSON Schema |
| RPA spec | PDD/SDD, data mapping, exception matrix (business vs system exception), checkpoint, retry, human takeover, credential qua vault | UiPath Studio (đọc/duyệt flow), Visio/draw.io |
| Ingestion spec | 12 tiêu chí nghiệm thu: 100% file có `document_id`, file gốc không ghi đè, retry không tạo trùng, phụ lục lưu version mới, audit log… | SRS |
| Gán nhãn & QC nhãn | Label Studio (form, KIE), CVAT (layout), kiểm đồng thuận | Label Studio, CVAT, Python |
| Đánh giá | Field exact match, CER, TEDS, STP, false accept; regression giữa version | Python pandas, pytest |
| Đối soát | SQL so số bản ghi/giá trị giữa extraction, review, ERP/QLHĐ | SQL, DataGrip |
| UAT | Test matrix: chất lượng ảnh, nguồn, ngôn ngữ, template mới, số trang, bảng, dấu/chữ ký, dấu chấm/phẩy, timeout/retry, bảo mật | Jira, Excel |

**Câu chuyện kể.**
- *Sai 2 ký tự vẫn là sai cả trường*: số hóa đơn `…OO1` thay vì `…001` có CER rất thấp nhưng làm hỏng đối soát. Tôi đề xuất dùng **field exact match** cho trường định danh và đo **false accept** làm chỉ số chính, vì tự nhận sai nguy hiểm hơn đẩy sang review.
- *Idempotency*: bot tạo hợp đồng trên QLHĐ xong thì mất mạng; retry không được tạo hợp đồng thứ hai. AC yêu cầu tra `external_reference/idempotency_key` trước khi retry, ứng dụng đích không hỗ trợ thì có sổ giao dịch và bước reconciliation.

**Mang sang VinDynamics:** OCR/VLM ↔ perception/VLM của robot (cùng bài toán "model tự tin nhưng sai", calibration, human review); RPA idempotency ↔ command idempotent cho robot; chuỗi annotation guideline → golden → regression dùng nguyên cho Data Factory.

---

## 11. Omnichannel CDP/CXP & CRM — use case Next Best Action

**Bối cảnh.** Viettel Store CRM: Customer 360, phân khúc, omnichannel, call center, marketing, ticket; khoảng 420 yêu cầu trong 9 nhóm nghiệp vụ; tích hợp ERP, website/Excel, BankPlus, ticket, mChat, call center Hoa Sao, VT++, Facebook, Google, TikTok, SMS, email. Nền tảng Omnichannel & CDP/CXP hợp nhất hành trình online – offline. Tôi làm PO/BA: capability map, RTM, Customer 360 canonical, mapping nguồn – đích, ticket state machine/SLA, permission matrix, migration, UAT, go-live. Use case AI tôi chọn trình bày: **Next Best Action (NBA)**.

### 11.1. Use case

Với mỗi khách hàng đủ điều kiện, chọn **một** hành động trong tập được phép: gửi hướng dẫn sử dụng, mời phụ kiện phù hợp, nhắc bảo dưỡng/gia hạn bảo hành, mời quay lại sau khiếu nại đã đóng, hoặc **không liên hệ**. Output kèm lý do để nhân viên CRM hiểu và có thể bỏ qua.

### 11.2. Kiến trúc

![CDP/CXP — Next Best Action](<Sơ đồ kiến trúc/10-cdp-cxp-next-best-action-1.png>)

| Khối | Công nghệ | Ghi chú |
|---|---|---|
| Thu thập | Snowplow (web/app event schema), POS/OMS, CRM, mChat (intent, lead, sentiment), call center, consent store → **Kafka** + schema registry | Event có `user_id`/`anonymous_id`, timestamp, kênh |
| Identity resolution | Deterministic theo SĐT/email đã xác thực; không merge theo tên | Quy tắc merge do BA chốt |
| Customer 360 | ClickHouse (hành vi), PostgreSQL (hồ sơ) | Completeness, duplicate rate là KPI |
| Segment | Rule builder, preview, sync audience sang Facebook/Google/TikTok | |
| Feature | **dbt**; feature lấy **trước** thời điểm quyết định để chống leakage | |
| Model | **XGBoost/LightGBM** propensity theo từng action; product affinity (co-purchase, implicit ALS); churn 90 ngày | Offline: PR-AUC, lift@k |
| Decision | NBA engine: eligibility (consent, frequency cap, đang khiếu nại, tồn kho) → score → contact policy → chọn 1 action + reason codes | Policy loại trước, model xếp sau |
| CXP | Journey orchestrator (trigger, wait, branch), adapter ZNS/SMS/email/push, gợi ý trong mChat, task CRM | |
| Đo lường | Experiment service: holdout và A/B theo khách hàng; outcome (mở, click, mua, opt-out, khiếu nại) quay về Kafka | Online: incremental conversion, profit, opt-out |

Output decision API: `{customer_id, action_id, channel, eligible, score, reason_codes[], expires_at, experiment_arm}`.

### 11.3. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Mục tiêu & action catalog | Business objective, danh sách action, kênh, điều kiện, frequency cap, suppression rule, attribution window | Confluence, Jira |
| Dữ liệu | Customer 360 source-of-truth, mapping nguồn → đích, quy tắc match/merge/dedup, reconciliation | dbdiagram.io, SQL, dbt spec |
| Nhãn | Định nghĩa "phản hồi tích cực" theo action và cửa sổ quan sát; loại mẫu chưa đủ thời gian quan sát | Excel |
| Journey | BPMN hành trình, nhánh, thời gian chờ | draw.io |
| QC | Customer fixture: opt-out, vừa mua, đang khiếu nại, trùng định danh, hết hàng, vượt cap, khách không lịch sử; Postman cho decision API; SQL đối soát audience | Postman, SQL, Power BI |
| Thí nghiệm | Random theo khách, baseline rule-based vs ML policy; cỡ mẫu và thời lượng tính từ baseline | Excel/Python |

**Quy tắc chặn release:** gửi cho khách opt-out, vượt frequency cap, gửi cho khách đang khiếu nại, gợi ý hàng hết tồn — chặn dù model có PR-AUC cao.

**Mang sang VinDynamics:** thương mại hóa robot (Robot-as-a-Service): khách hàng – site – gói capability – SLA – ticket hỗ trợ – usage; telemetry adoption của bảo vệ; không đưa dữ liệu người đi qua camera robot vào marketing.

---

## 12. Samsung AI Data Hub — quản trị vòng đời AI

**Bối cảnh.** Nền tảng nội bộ thuộc Samsung AI Platform, quản trị vòng đời tài sản AI giữa các phòng ban. Tôi là **Lead BA khoảng 8 tháng**, từ ý tưởng đến handover và pilot; yêu cầu đến từ chuyên gia Samsung HQ Korea (Data Governance, MDM, vận hành AI platform) sang Việt Nam 3–4 tháng một lần, giữa các đợt PM và BA họp 1–2 lần mỗi tuần qua chat và Confluence để mọi quyết định có dấu vết.

AI Data Hub **không phải ứng dụng AI**, mà là nền tảng để các đội **xây và quản lý AI**: dataset, model, training job, evaluation, deployment, phê duyệt, phân quyền và truy vết.

### 12.1. Use case

| Use case | Mô tả |
|---|---|
| Đăng ký & xuất bản dataset | Tạo từ template → metadata, nguồn, schema, sensitivity, ownership, license → validate → phê duyệt → publish → catalog |
| Tìm & xin quyền dùng | Catalog/search, visibility, request access, recommended datasets theo domain, task, model liên quan |
| Training job | Chọn dataset version, base model, tham số, tài nguyên compute; chạy, theo dõi log, lưu artifact |
| Evaluation & benchmark | Accuracy, precision, recall, F1, latency, throughput, robustness, fairness; so sánh version |
| Promote & deploy | Staging → Production có phê duyệt; rollback |
| Label & annotation | Class, phân bố nhãn, class weight, chất lượng nhãn (ví dụ ảnh normal/defect/blurred/unknown) |
| Governance | Audit, lineage, dashboard tuân thủ, SLA phê duyệt |

### 12.2. Kiến trúc

![AI Data Hub — kiến trúc](<Sơ đồ kiến trúc/11-ai-data-hub-1.png>)

| Khối | Thiết kế | Công nghệ triển khai |
|---|---|---|
| Portal | Catalog & search, dataset/model card, approval inbox, governance dashboard | React |
| Asset service | Dataset, Model, Data Source, Template; card theo template động | Spring Boot, PostgreSQL |
| Workflow engine | Mẫu phê duyệt tái sử dụng: tuần tự, song song, điều kiện, auto-routing theo department/owner/sensitivity/asset type/action, delegation, reassign, SLA, reminder, escalation | Engine cấu hình (BPMN) |
| Permission | Function-level + data-level (role, phòng ban, owner/sponsor/contributor, sensitivity, usage scope, **trạng thái tài sản**) | ABAC |
| Training orchestration | Job spec, quota GPU, log, artifact | Kubernetes + Kubeflow Pipelines |
| Registry & deployment | Model version, Staging/Production, rollback | MLflow Model Registry, KServe |
| Lưu trữ | Metadata DB, object storage (S3-compatible), lineage graph | PostgreSQL, MinIO, OpenLineage |

Vai trò: Global Admin, Local Admin, Data Owner, Data Steward, Model Owner, AI Engineer/Data Scientist, Reviewer/Approver, Contributor, Viewer, Auditor — tách trách nhiệm owner / steward / auditor.

![Vòng đời & truy vết](<Sơ đồ kiến trúc/11-ai-data-hub-2.png>)

**Quy tắc chặn:** không Publish khi thiếu phê duyệt, metadata bắt buộc hoặc license; không Train khi dataset chưa Approved hoặc không truy cập được; không Deploy Production khi Evaluation chưa Validated; Approved/Published chỉ sửa qua change request; mọi thay đổi state, quyền, version đều audit.

### 12.3. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Asset model | Dataset/Model card, metadata schema, template, ownership, sensitivity, usage scope, version, label, nguồn, validation rule, lifecycle status | Excel field dictionary, dbdiagram.io, Figma |
| Workflow phê duyệt | Gom các luồng mua/đăng ký/chia sẻ/sửa/xóa/đổi nguồn/training/deploy thành **mẫu phê duyệt cấu hình được** thay vì nhiều flow riêng | BPMN, draw.io |
| Phân quyền | Ma trận function × data × trạng thái; thao tác rủi ro (download raw, chia sẻ, xóa, deploy production) có kiểm soát riêng | Permission matrix, state-action matrix |
| Training/Eval/Deploy | Đặc tả cách chọn version, cấu hình tham số và tài nguyên, theo dõi job, so sánh model, promote, rollback, phê duyệt | SRS, sequence diagram |
| Truy vết | Dataset → Training Job → Model → Evaluation → Deployment | Lineage diagram, ERD |
| API | Mapping từ Swagger: request/response, mã lỗi, gap giữa API hiện có và yêu cầu | Swagger, Postman |
| Kiểm thử | Negative permission, state transition, race condition (hai người duyệt cùng lúc, sửa config khi đang chờ duyệt, callback lặp, GPU hết tài nguyên, job fail giữa chừng) | Jira, Postman, SQL |
| Bàn giao | Walkthrough, handover, đào tạo, pilot | Confluence |

**Câu chuyện kể.** Ban đầu yêu cầu là "phân quyền theo vai trò". Tôi chỉ ra rằng cùng một Data Owner có thể sửa trực tiếp dataset ở Draft nhưng phải gửi change request khi đã Published — tức quyền phụ thuộc **trạng thái**, không chỉ vai trò. Tôi đề xuất mô hình permission ba chiều (function × data × state) và tách metadata (sửa được) khỏi hành động rủi ro (cần duyệt). HQ chấp nhận và đó trở thành nền cho toàn bộ workflow.

**Mang sang VinDynamics:** đây là nền tảng gần nhất với Data Factory và MLOps robot: dataset episode, model perception/VLA, evaluation gate, deployment theo robot/site, rollback — chỉ cần thêm chiều tương thích phần cứng, firmware, map.

---

## 13. Samsung Smart Factory — 2 use case Machine Learning trên Azure

**Bối cảnh.** Samsung R&D Vietnam (2023–2024): nền tảng nhà máy gồm **Production Equipment Management** (trọng tâm), **WMS**, **QMS** và tích hợp ERP. Tôi là Lead BA mảng Equipment, BA cho WMS/QMS, phụ trách đặc tả tích hợp ERP và dashboard/báo cáo; có tên trong đơn đăng ký sáng chế của Samsung cho một giải pháp Digital Factory (09/2024).

Nghiệp vụ tôi đã phân tích: line – station – equipment hierarchy, quy tắc mã thiết bị, tham số vận hành, machine log, tín hiệu, alarm/event, mapping trạng thái; bảo trì (kiểm tra, báo lỗi, sửa chữa, bảo trì định kỳ, bảo hành), phân loại downtime, OEE; WMS (nhập, xuất, vị trí, lô, WIP, truy vết vật tư); QMS (công đoạn kiểm tra, lấy mẫu, phân loại lỗi, SPC, NCR); tích hợp ERP (endpoint, mapping, tần suất đồng bộ, full/incremental, đối soát, xử lý lỗi).

### 13.1. Kiến trúc trên Microsoft Azure

![Smart Factory trên Azure](<Sơ đồ kiến trúc/12-smart-factory-azure-ml-1.png>)

| Lớp | Dịch vụ / công nghệ | Thiết kế |
|---|---|---|
| OT | PLC Siemens S7 / Mitsubishi, cảm biến rung–nhiệt–dòng điện, máy SMT, camera AOI, SCADA/HMI, MES | Vòng điều khiển máy ở lại OT |
| Edge | **Azure IoT Operations** (Arc-enabled Kubernetes), OPC UA connector (asset model, tag mapping), MQTT broker, ONNX Runtime inference, store & forward | Chuẩn hóa tag, đơn vị, timestamp; replay có thứ tự khi mất mạng |
| Định danh & cấu hình | **IoT Hub / Event Grid MQTT**, Device Provisioning Service, X.509, **device twin** desired/reported | Desired ≠ applied cho tới khi máy báo reported |
| Streaming | **Event Hubs**, **Stream Analytics** (window, dedup, alarm, lateness) | Event-time, xử lý trễ |
| Lưu trữ | **Azure Data Explorer** (time-series, KQL), **ADLS Gen2** (bronze/silver/gold Delta), **Azure SQL** (master data, work order, inspection) | |
| Data & ML | **Azure Databricks** (feature), **Azure Machine Learning** (pipeline, registry, managed endpoint, MLflow), **Azure Digital Twins** (nhà máy – line – station – máy) | |
| Ứng dụng | Equipment/Maintenance API trên AKS, WMS/QMS services, **Service Bus** (work order, DLQ), **API Management** + **Logic Apps** (đồng bộ ERP SAP, reconciliation) | |
| Báo cáo | **Power BI**: OEE, downtime, SPC, hiệu quả ML | |
| Vận hành & bảo mật | **Azure Monitor** (App Insights, Log Analytics), **Entra ID** (RBAC theo site, tách quyền OT/IT), **Key Vault**, private endpoint, **Defender for IoT**, **Azure DevOps + ACR** (CI/CD, manifest model + config) | Rollout một máy → một line → một site; rollback model và preprocessing cùng lúc |

### 13.2. Hai use case ML

![Hai use case ML](<Sơ đồ kiến trúc/12-smart-factory-azure-ml-2.png>)

**Use case 1 — Bảo trì dự đoán (rủi ro hỏng máy trong 7 ngày).**
- Input: RMS/kurtosis rung theo phút, nhiệt, dòng điện, giờ chạy, tải, lịch sử alarm, lịch sử bảo trì. Output: `failure_risk`, `time_horizon`, `reason_codes`, `recommended_inspection`, `valid_until`.
- Pipeline: sensor → edge aggregation → IoT Hub/Event Hubs → ADX/ADLS → feature window 24 giờ/7 ngày → nhãn từ work order + mã lỗi PLC → **XGBoost** trên Azure ML (khi đủ nhãn) hoặc **IsolationForest** phát hiện bất thường (khi thiếu nhãn, gọi đúng tên là anomaly) → batch scoring mỗi giờ → Service Bus → work order đề xuất → kỹ thuật viên xác nhận → kết quả kiểm tra thành nhãn mới.
- BA/QC: định nghĩa failure khác planned downtime; lead time hữu ích; mapping mã lỗi PLC → taxonomy nghiệp vụ; phân biệt "đã bảo trì" với "đã hỏng"; split theo máy + thời gian; chống leakage từ mã sửa chữa sau sự cố; đo precision/recall theo sự kiện, cảnh báo giả / máy-ngày, lead time, báo cáo theo họ máy. Không tự dừng máy theo score; interlock là hệ riêng.

**Use case 2 — Phát hiện lỗi ngoại quan trên dây chuyền.**
- Input: ảnh AOI/camera + `lot_id`, `serial_no`, `station_id`, `recipe_version`. Output: defect class, bbox/mask, confidence, ảnh bằng chứng, disposition đề xuất.
- Pipeline: trigger → crop ROI, chuẩn hóa sáng → **YOLOv8** cho lỗi có đủ nhãn; **PatchCore (anomalib)** cho lỗi hiếm khi chủ yếu có mẫu tốt → **ONNX Runtime/TensorRT** tại edge, latency ≤ takt time → QMS (OK/NG, Quality Hold lot) → QC xác nhận rework/scrap/release → nhãn về ADLS → retrain trên Azure ML.
- BA/QC: defect taxonomy và mức độ, sampling policy, quyền override, truy vết lot – máy – vật tư; gán nhãn CVAT; holdout theo lot/ca/SKU; đo **false accept** (lọt lỗi) và **false reject** (loại nhầm hàng tốt); test camera hỏng ≠ "không có lỗi", serial scan lỗi không gán ảnh sang sản phẩm kế tiếp, mất mạng không tạo kiểm tra trùng. Model gắn với recipe và điều kiện chiếu sáng; đổi SKU phải đánh giá lại.

### 13.3. Việc tôi làm và công cụ

| Hạng mục | Chi tiết | Công cụ |
|---|---|---|
| Khảo sát Gemba | Production, Maintenance, Automation; layout line, hierarchy | Phỏng vấn, quan sát, ghi chú hiện trường |
| Equipment master | Equipment dictionary, tag list, state-transition matrix, alarm matrix, event catalog | Excel, draw.io |
| Bảo trì & OEE | BPMN bảo trì; KPI dictionary, công thức OEE = Availability × Performance × Quality; MTBF, MTTR; sample calculation làm **UAT oracle** | Excel, Power BI |
| WMS/QMS | Luồng nhập – xuất – lô – WIP; kiểm tra IQC/IPQC/FQC/OQC, NCR, CAPA, SPC (Cp/Cpk) | BPMN, ERD |
| Tích hợp ERP | Endpoint, mapping, phụ thuộc master/transaction, tần suất, full/incremental, reconciliation, xử lý lỗi | Swagger, Postman, SQL |
| UAT | Telemetry simulation với out-of-order, duplicate, lost event, reconnect, ranh giới ca, downtime chồng nhau, counter reset, recipe mismatch | Script giả lập, SQL, Excel |
| ML (2 use case) | Feature dictionary, label guide, quy trình nhận cảnh báo; nghiệm thu model và end-to-end | Azure ML studio, MLflow, CVAT, Python |

**Câu chuyện kể.** OEE trên dashboard lệch với số tổ trưởng tính tay. Nguyên nhân là downtime chồng nhau giữa hai alarm và một ca cắt ngang sự cố. Tôi viết bảng quy tắc split/merge downtime theo ranh giới ca, dựng file tính tay làm **UAT oracle**, và thêm 12 kịch bản telemetry giả lập vào regression.

**Mang sang VinDynamics:** equipment hierarchy ↔ site – zone – robot – component; availability/maintenance ↔ robot READY/DEGRADED/MAINTENANCE; device twin desired/reported ↔ cấu hình robot đã gửi vs đã áp dụng; OTA theo vòng ↔ release robot; dashboard OEE ↔ fleet availability.

---

## 14. Câu hỏi đào sâu và cách trả lời

**1. Anh tự train model nào?**
Tôi không viết trainer. Tôi sở hữu phần dữ liệu và chất lượng: định nghĩa nhãn, chuẩn bị và gán nhãn, chia tập, golden set, đọc và rà config, chạy notebook/job đã bàn giao khi cần, nghiệm thu candidate so với production. Ví dụ HRAI: tôi dựng quy tắc feedback → gold label và DAG feedback → dataset; engineer fine-tune Qwen3.5-9B bằng Unsloth LoRA và train lại XGBoost trên dataset đó; tôi chạy bộ regression và đề xuất go/no-go theo gate.

**2. Khi nào RAG, khi nào fine-tune?**
Tri thức thay đổi, cần nguồn, hiệu lực, quyền → RAG. Hành vi lặp lại có mẫu (phân loại intent, format JSON, văn phong, chọn tool) và đã có dữ liệu đúng → fine-tune. Thứ tự: sửa dữ liệu/retrieval → prompt → fine-tune. Fine-tune không thay được việc cập nhật văn bản có hiệu lực.

**3. Golden set xây thế nào, bao nhiêu là đủ?**
Bắt đầu 200–400 mẫu phủ theo rủi ro chứ không theo tỷ lệ tự nhiên: câu thường gặp, nhiều bước, không có đáp án, phụ thuộc thời gian, đối kháng. Mỗi mẫu có đáp án gold, nguồn gold, mức rủi ro, người duyệt. Golden khóa version, không dùng để train; lỗi mới từ production được thêm vào bộ regression chứ không sửa golden cũ để candidate qua.

**4. LLM-as-judge có tin được không?**
Chỉ sau khi đo đồng thuận với người chấm trên khoảng 100 mẫu (kappa ≥ 0,7). Câu critical luôn có người chấm. Judge dùng model khác model đang được đánh giá và có rubric cụ thể.

**5. PASS/PARTIAL/FAIL có phải nhãn training không?**
Không. Đó là trạng thái QA. Chỉ output đã được sửa thành bản đúng hoàn chỉnh và được xác minh mới thành gold. "50% đúng" không phải nhãn 0,5.

**6. "Model đúng 95%" nghĩa là gì?**
Tôi hỏi lại: metric nào, trên tập nào, chia theo cách nào, lớp hiếm ra sao, chi phí sai ở mỗi chiều. Với cảnh báo rủi ro, 95% accuracy có thể vô nghĩa nếu lớp dương chỉ 3%.

**7. Ví dụ data leakage anh từng chặn?**
HRAI: dùng trường "ngày nghỉ việc" sau mốc quan sát để dự báo nghỉ việc. Smart Factory: dùng mã sửa chữa sau sự cố làm feature dự báo hỏng. OCR: hai trang của cùng hợp đồng nằm ở train và test. Cách chặn: mốc `observation_cutoff`, split theo thực thể + thời gian, dedupe trước khi split.

**8. Đánh giá hallucination thế nào?**
Validator kiểm evidence có tồn tại trong input/snapshot; grounding check với context; rule mâu thuẫn (class ↔ reasoning, risk LOW mà khuyến nghị khẩn cấp); tập ca "thiếu dữ liệu" mà model phải hạ confidence. Tỷ lệ hallucination trên tập critical phải bằng 0.

**9. Chọn ngưỡng confidence thế nào?**
Không chọn cảm tính. Vẽ bảng confidence so với accuracy thật (calibration) trên validation, chọn theo rủi ro từng trường: trường tiền/MST ngưỡng cao hoặc luôn review; giá trị hợp đồng luôn chạy business rule dù confidence cao. Theo dõi false accept sau phát hành.

**10. Rollback cái gì?**
Cả bộ tương thích theo manifest: model/adapter, prompt, preprocessing, index snapshot, ruleset, đôi khi cả schema. Đổi lại file trọng số một mình thường không đủ.

**11. Phân biệt lỗi dữ liệu, feature, retrieval, prompt, model, rule?**
Theo thứ tự loại trừ: input snapshot có đúng không → feature tính đúng không (test bước B) → retrieval có lấy đúng nguồn không → prompt có ép đúng hành vi không → model hiểu sai → rule nghiệp vụ sai. Mỗi ticket có `trace_id`, version, expected/actual và issue code để chuyển đúng đội.

**12. Anh khác AI Engineer ở đâu?**
Tôi sở hữu ý nghĩa nghiệp vụ của dữ liệu, tiêu chí đánh giá, bằng chứng chất lượng và quyết định nghiệm thu đề xuất. Engineer sở hữu thuật toán, code, hạ tầng. Tech Lead chốt HOW.

**13. Làm sao để agent không vượt quyền?**
Quyền lấy từ token, không từ lời người dùng; tool có quyền riêng; tool ghi qua policy + xác nhận + backend kiểm lại quyền và `state_version`; giới hạn số vòng tool; prompt injection trong tài liệu được coi là dữ liệu. Test: cùng câu hỏi với người dùng khác quyền.

**14. Vision: frame-level với event-level khác gì?**
mAP frame cao nhưng event vẫn có thể báo giả nhiều (một người đi qua tạo 30 frame). Nghiệm thu bằng event precision/recall, cảnh báo giả / camera-ngày, thời gian tới dashboard, theo từng điều kiện ánh sáng và từng site.

**15. Đánh giá agent chọn tool đúng thế nào?**
Bộ mẫu (câu hỏi, tool đúng, tham số đúng, kết quả mong đợi); chấm tool selection accuracy, argument accuracy, task success, số bước thừa; thêm ca tool timeout, trả lỗi, trả dữ liệu cũ.

**16. Đánh giá AI cho robot khác phần mềm thường ở đâu?**
Thêm điều kiện vận hành (ODD), kết quả vật lý, độ tươi dữ liệu cảm biến, tương thích phần cứng/firmware/map; đánh giá qua nhiều cổng offline → mô phỏng → phần cứng → thực địa; và một câu trả lời đúng của model không đồng nghĩa nhiệm vụ vật lý đã hoàn thành an toàn.

---

## Phụ lục A — Bảng tự ôn trước buổi phỏng vấn

Bảng này để tôi tự biết phần nào nằm trong CV và tài liệu dự án gốc, phần nào là kiến trúc và chi tiết được dựng thêm trong tài liệu này — phần sau cần học kỹ để trả lời được khi bị hỏi sâu.

| Dự án | Có trong CV / tài liệu dự án | Dựng thêm trong tài liệu này — cần học kỹ | Câu dễ bị hỏi vặn |
|---|---|---|---|
| Cổng một cửa | 3/17 module, vai trò PO/BA, AI Training & Evaluation, data governance | Stack (LangGraph, Qdrant, Qwen2.5-72B, WSO2, OpenMetadata, Trino), số lượng golden/NL2SQL/intent, câu chuyện văn bản hết hiệu lực | "Embedding nào, vì sao? Chunk văn bản pháp luật thế nào?" |
| XLVPHC Copilot | Tên dự án trong CV; Copilot hướng dẫn thao tác, thẩm quyền, căn cứ (ghi chú dự án) | Kiến trúc on-prem, 4 skill, guided tour, gold theo vai trò × trạng thái | "Copilot biết màn hình hiện tại bằng cách nào?" |
| Smart Safe | Phạm vi, ~400 cửa hàng, >5.000 thiết bị, loại thiết bị có AI camera, 300–400 UAT case, Redis/RabbitMQ | Jetson/DeepStream/YOLOv8/EMQX/TimescaleDB, 4 use case AI, quy trình train camera, câu chuyện PIR | "Đo cảnh báo giả thế nào? Model chạy ở đâu?" |
| HRAI One | Use case, Airflow, RoBERTa, XGBoost, Qwen3.5-9B, Unsloth, allpairspy, luồng feedback, bộ test 2 bước | Một số tên bảng/con số lấy từ ghi chú hỏi đáp; câu chuyện hallucination dấu | "Fine-tune Qwen bằng dữ liệu gì, bao nhiêu mẫu?" |
| Tori AI | Không có trong CV; JD BA & QA của Techcombank; thông tin công khai về Tori | Toàn bộ vai trò, kiến trúc AWS, Kiro, chu trình build–test–verify | "Làm ở đơn vị nào, thời gian nào, ai quản lý?" — cần thống nhất với CV trước khi kể |
| mChat | Tính năng, routing/SLA, sáng kiến AI, taxonomy, logic trigger (thiết kế) | PhoBERT, Qwen2.5-14B, LangGraph; lớp AI là thiết kế/sáng kiến | "AI đã chạy production chưa, kết quả ra sao?" |
| RPA & OCR | 17 kịch bản, 3 đơn vị, use case và bất cập (tài liệu đề án) | PaddleOCR, Qwen2.5-VL, UiPath, ngưỡng confidence (từ thiết kế tham chiếu); chưa có số đo thực | "Đã đo field accuracy thực tế bao nhiêu?" |
| CDP/CXP & CRM | CRM ~420 yêu cầu, Customer 360, tích hợp, segment sync | Toàn bộ use case NBA và stack | "Chứng minh tác động bằng gì?" |
| AI Data Hub | Phạm vi, Lead BA ~8 tháng, HQ Korea, asset model, workflow, permission, lifecycle, lineage | Tên công nghệ triển khai (Spring Boot, Kubeflow, MLflow, KServe) | "Hệ thống chạy trên hạ tầng gì?" |
| Smart Factory | Equipment/WMS/QMS/ERP, OEE, bảo trì, patent application 09/2024 | Kiến trúc Azure, 2 use case ML, câu chuyện OEE oracle | "Azure IoT Operations khác IoT Edge thế nào?" |

Hai điểm cần chuẩn bị câu trả lời trung thực:
- **Số năm BA**: JD yêu cầu 4+ năm BA/Technical BA/System Analyst; CV có chức danh BA từ 02/2023 và 3 năm developer trước đó. Chuẩn bị ví dụ về phần phân tích hệ thống đã làm trong giai đoạn developer (RBAC/ABAC, approval engine, tối ưu truy vấn ngân hàng) để chứng minh kinh nghiệm system analysis.
- **Số liệu kết quả**: các con số trong mẫu decision log, golden set và câu chuyện là để minh họa cách làm; khi kể, chỉ nêu số liệu mình chắc chắn.

---

## Phụ lục B — Danh mục sơ đồ

Tất cả trong [`Sơ đồ kiến trúc/`](<Sơ đồ kiến trúc/>); mỗi file `.drawio` mở được bằng draw.io desktop hoặc app.diagrams.net; PNG xuất theo từng sheet (`-1`, `-2`, `-3`).

| File | Sheet | Nội dung |
|---|---|---|
| `01-he-tri-thuc-va-ai-agent.drawio` | 3 | Kiến trúc tổng thể · luồng agent · ingestion |
| `02-vong-doi-training-ai.drawio` | 2 | Vòng đời BA–QC · quality gate |
| `03-cong-mot-cua-dau-tu.drawio` | 2 | Kiến trúc · ontology GraphRAG |
| `04-xlvphc-ai-copilot.drawio` | 2 | Kiến trúc Copilot · luồng "việc tiếp theo" |
| `05-smart-safe-ai-camera.drawio` | 2 | Edge–cloud & AI camera · vòng đời cảnh báo |
| `06-hrai-one.drawio` | 2 | Kiến trúc & pipeline · bộ kiểm thử 2 bước |
| `07-tori-ai-aws-bedrock.drawio` | 2 | Kiến trúc AWS · chu trình build–test–verify |
| `08-mchat-ai-agent-assist.drawio` | 2 | Kiến trúc 3 lớp · trạng thái AI job |
| `09-rpa-ocr-vlm.drawio` | 2 | OCR-first, VLM-fallback · vòng đời chứng từ |
| `10-cdp-cxp-next-best-action.drawio` | 1 | Next Best Action |
| `11-ai-data-hub.drawio` | 2 | Kiến trúc · vòng đời & truy vết |
| `12-smart-factory-azure-ml.drawio` | 2 | Kiến trúc Azure · 2 use case ML |
| `13`–`18` | | Dùng ở file [Đức PO làm dự án VinDynamics](<Đức PO làm dự án VinDynamics.md>) |
