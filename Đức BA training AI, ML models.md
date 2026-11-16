# Đức BA training AI, ML models

Tài liệu chuẩn bị phỏng vấn Senior Business Analyst tại VinDynamics · 16/11/2026.

## Mục lục

- [1. Cách sử dụng và mức độ xác nhận](#1-cách-sử-dụng-và-mức-độ-xác-nhận)
- [2. “Training AI” nghĩa là gì trong vai trò BA + QC?](#2-training-ai-nghĩa-là-gì-trong-vai-trò-ba--qc)
- [3. Hệ tri thức và AI Agent chatbot: kiến trúc tham chiếu dùng chung](#3-hệ-tri-thức-và-ai-agent-chatbot-kiến-trúc-tham-chiếu-dùng-chung)
- [4. Cổng một cửa đầu tư quốc gia](#4-cổng-một-cửa-đầu-tư-quốc-gia)
- [5. CSDL quốc gia về xử lý vi phạm hành chính](#5-csdl-quốc-gia-về-xử-lý-vi-phạm-hành-chính)
- [6. Smart Safe: AI Camera kết hợp IoT](#6-smart-safe-ai-camera-kết-hợp-iot)
- [7. HRAI One: ML trên dữ liệu nhân sự và LLM diễn giải](#7-hrai-one-ml-trên-dữ-liệu-nhân-sự-và-llm-diễn-giải)
- [8. Tori AI của Techcom Life — bài mô phỏng BA + QC](#8-tori-ai-của-techcom-life--bài-mô-phỏng-ba--qc)
- [9. mChat: Conversational AI và điều phối hội thoại](#9-mchat-conversational-ai-và-điều-phối-hội-thoại)
- [10. RPA & OCR kết hợp VLM](#10-rpa--ocr-kết-hợp-vlm)
- [11. Omnichannel CDP/CXP và CRM — một use case AI](#11-omnichannel-cdpcxp-và-crm--một-use-case-ai)
- [12. Samsung AI Data Hub: quản trị vòng đời AI](#12-samsung-ai-data-hub-quản-trị-vòng-đời-ai)
- [13. Samsung Smart Factory — hai use case Machine Learning trên Azure](#13-samsung-smart-factory--hai-use-case-machine-learning-trên-azure)
- [14. Đối chiếu JD VinDynamics và chuẩn bị bảo vệ kinh nghiệm](#14-đối-chiếu-jd-vindynamics-và-chuẩn-bị-bảo-vệ-kinh-nghiệm)

## 1. Cách sử dụng và mức độ xác nhận

Mục tiêu là trình bày Đức như một **Technical BA kiêm QC tham gia xây dựng sản phẩm AI**, có khả năng chuyển nghiệp vụ thành dữ liệu, hợp đồng tích hợp, bộ đánh giá và điều kiện phát hành. Tài liệu không lấy việc sử dụng Codex/Claude thành thạo làm bằng chứng thay thế kinh nghiệm làm sản phẩm AI.

Ba nhãn được dùng xuyên suốt:

- **[HS] Hồ sơ:** nội dung được CV hoặc tài liệu dự án mô tả; đây là kinh nghiệm tự khai trong hồ sơ, không phải kiểm chứng độc lập về triển khai production.
- **[TK] Thiết kế đề xuất:** cách triển khai cụ thể được xây dựng để giải thích kiến thức và mở rộng use case. Tên công nghệ trong phần này không có nghĩa công ty cũ đã dùng công nghệ đó.
- **[MP] Mô phỏng:** tình huống luyện phỏng vấn. Riêng **Tori AI là dự án tham khảo, Đức xác nhận chưa tham gia**; phần ngôi “tôi” ở mục 8 là bài đóng vai, không phải lịch sử làm việc.

Các ngưỡng, số lượng test và cấu hình huấn luyện mang nhãn [TK]/[MP] là mục tiêu hoặc ví dụ để thảo luận với Tech Lead, không phải kết quả đã đạt. Không có benchmark nào được chạy để tạo tài liệu này.

Một số PDF HRAI/OCR và tài liệu trong thư mục ChatGPT là nội dung hỏi đáp hoặc giáo trình. Ví dụ *1. Giới thiệu HRAI.pdf* mở đầu bằng giả định về Oracle, Python và Qwen; *AI Document Understanding End-To-End.docx* mô tả khóa học. Chúng hữu ích để thiết kế giải pháp nhưng không xác nhận Đức đã vận hành các stack đó.

### Câu giới thiệu 90 giây có thể dùng từ hồ sơ

> Tôi tham gia AI từ góc độ sản phẩm, dữ liệu và chất lượng. Với HRAI, mChat, OCR và hệ tri thức, phần việc của tôi gồm làm rõ use case, quy tắc nghiệp vụ, dữ liệu đầu vào, đầu ra cần kiểm chứng, chuẩn bị dữ liệu và đánh giá kết quả qua nhiều vòng cải tiến. Với Samsung AI Data Hub, tôi đi sâu vào vòng đời dataset–training job–model–evaluation–deployment, phân quyền, phê duyệt và truy vết phiên bản. Với Smart Safe và Smart Factory, tôi có nền tảng tích hợp thiết bị, trạng thái, cảnh báo, dữ liệu vận hành và xử lý ngoại lệ. Vì vậy, khi làm sản phẩm robot, tôi có thể nối yêu cầu khách hàng với hành vi hệ thống, dữ liệu và tiêu chí nghiệm thu; phần thuật toán chuyên sâu tôi phối hợp với AI/Robotics Engineer.

Nguồn cho phạm vi trên: [CV đầy đủ, trang 2–5 và 7](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Kim Đức CV full.pdf>). Chi tiết cá nhân cần chuẩn bị thêm để bảo vệ câu trả lời: một requirement, một bộ test, một defect có trace, một báo cáo so sánh phiên bản; chỉ dùng tài liệu được phép chia sẻ và đã ẩn dữ liệu nội bộ.

### Bản đồ 10 dự án

| Dự án | Căn cứ hồ sơ | Nội dung AI cần trình bày | Phần được bổ sung trong tài liệu |
|---|---|---|---|
| Cổng một cửa đầu tư quốc gia | CV ghi rõ Hệ tri thức & Trợ lý AI; data governance | RAG có nguồn, hiệu lực và phân quyền; hỏi đáp và tra cứu hồ sơ | Stack cụ thể, retrieval/evaluation, agent tools |
| CSDL xử lý vi phạm hành chính | CV xác nhận dự án; danh sách đầu vào nêu Copilot | Hướng dẫn theo màn hình, trạng thái, thẩm quyền | Agent có kiểm soát, workflow và rule engine |
| Smart Safe | IoT an ninh, cảnh báo, thiết bị; tài liệu nêu AI Camera | Nhận diện xâm nhập và xác minh sự cố | Detector/tracker, dataset camera, edge inference |
| HRAI One | CV xác nhận HR AI và AI Training & Evaluation ở cấp nhóm sản phẩm | Dự báo rủi ro và diễn giải có bằng chứng | Phân tách ML/LLM, feedback thành gold data, fine-tune |
| Tori AI | JD BA & QA và tài liệu tham khảo; chưa tham gia | Document ingestion, build–test–verify | Toàn bộ câu chuyện cá nhân là mô phỏng |
| mChat | Omnichannel, hội thoại, sáng kiến AI/NLP | Intent, insight, gợi ý trả lời, handover | Orchestration, dữ liệu train, chống kết quả lỗi thời |
| RPA & OCR | CV, báo cáo RPA, danh mục use case | Document AI, OCR-first/VLM fallback | Model và confidence gate, fine-tune, retry an toàn |
| Omnichannel CDP/CXP & CRM | CV xác nhận Customer 360, phân khúc, hành trình | Một use case: Next Best Action | ML propensity, decision policy, A/B test |
| Samsung AI Data Hub | CV trang 4–5, feature description, BA làm gì | Quản trị vòng đời AI, không cần tự là một AI model | Stack MLOps cụ thể và contract dataset/job/deploy |
| Samsung Smart Factory | Equipment, WMS, QMS, tích hợp ERP | Hai use case: bảo trì dự đoán; phát hiện lỗi ngoại quan | Azure architecture, ML pipeline, fleet extension |

## 2. “Training AI” nghĩa là gì trong vai trò BA + QC?

### 2.1. Phân biệt sáu loại công việc

| Loại | Có thay trọng số model? | BA/QC trực tiếp đóng góp | Bằng chứng nên có |
|---|---|---|---|
| Knowledge ingestion/RAG | Không | Chuẩn hóa nguồn, chia đoạn, metadata, quyền, bộ câu hỏi | Manifest tài liệu, chunk QA, retrieval report |
| Prompt/configuration tuning | Không | Rubric, JSON schema, prompt version, top-k, timeout | Experiment log; so sánh cùng benchmark |
| Train ML từ dữ liệu doanh nghiệp | Có | Định nghĩa nhãn, feature và thời điểm; đánh giá lỗi | Dataset manifest, label guide, experiment run |
| Fine-tune pretrained model | Có, toàn bộ hoặc adapter | Curate mẫu đúng/sai, phân tách dữ liệu, kiểm tra candidate | Base model + adapter + config + evaluation |
| Feedback/review | Chưa tự động | Chấm trường sai, sửa gold, giải quyết bất đồng | Feedback có evidence; phiên bản gold label |
| Agent/workflow configuration | Không nhất thiết | Tool contract, quyền, trạng thái, retry, human review | Sequence, state machine, API test, audit |

Nạp PDF vào vector database không phải fine-tune. Chấm PASS/FAIL chưa phải tạo dữ liệu supervised training. Dùng model mã nguồn mở không đồng nghĩa tự huấn luyện foundation model từ đầu. “Xây từ đầu” phù hợp ở đây là xây **sản phẩm, dữ liệu, quy trình và tích hợp**; ML dạng bảng có thể train từ đầu, còn LLM/VLM thường tận dụng pretrained weights.

### 2.2. Chu trình dữ liệu–training–evaluation đề xuất

[Vòng đời dữ liệu, đánh giá và cải tiến AI](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/03-ai-training-feedback.drawio.png>)

1. **Đặt bài toán:** actor, quyết định cần hỗ trợ, lỗi nào gây thiệt hại, quy trình hiện tại, quyền của AI. BA viết problem statement và output contract; PO xác định giá trị; Tech Lead kiểm tra khả thi.
2. **Tạo data contract:** schema, đơn vị đo, nguồn, thời điểm quan sát, khóa định danh, null/unknown, retention và quyền sử dụng. Dùng SQL/DataGrip, Python/pandas, Excel, dbdiagram.io.
3. **Tạo label guideline:** ví dụ đúng/sai, trường hợp mơ hồ, multi-label, evidence span, nguồn nhãn, người phê duyệt. Dùng Label Studio cho text/tabular review; CVAT cho ảnh/video nếu triển khai phần vision.
4. **Tách dữ liệu trước khi biến đổi:** theo nhân viên, khách hàng, hồ sơ, camera, lot hoặc episode tùy domain; thêm tách theo thời gian. Dedupe trước split; fitting scaler/imputer chỉ trên train. Validation để chọn cấu hình; test giữ kín để đánh giá cuối.
5. **Lập baseline:** rule-based hoặc logistic regression cho tabular; pretrained OCR/detector; prompt + RAG cho LLM. Không dùng fine-tune khi lỗi thực ra do thiếu dữ liệu hoặc retrieval sai.
6. **Train/fine-tune cùng engineer:** BA quản lý taxonomy/scope, QC xác nhận dữ liệu và run; engineer chịu trách nhiệm code, optimizer, GPU, checkpoint. BA có thể chạy notebook/job đã được bàn giao nếu thực tế đã làm; không mặc định đã tự viết trainer.
7. **Đánh giá riêng từng lớp:** dữ liệu, model, ứng dụng và vận hành. Không che lỗi tool/permission bằng điểm câu trả lời cao. Báo cáo tổng thể và từng nhóm khó.
8. **Phát hành có kiểm soát:** shadow trước, sau đó canary khi phù hợp; người có thẩm quyền duyệt. Theo dõi model/prompt/index/ruleset version. Có điều kiện rollback về bộ phiên bản tương thích.
9. **Feedback:** giữ input snapshot, prediction, model version; QA sửa trường sai; chuyên gia phân xử; mới đưa vào dataset vòng sau. Không dùng test set làm nguồn sửa model rồi vẫn gọi đó là test độc lập.

Stack [TK]: Python/pandas + Great Expectations kiểm tra dữ liệu; DVC và object storage lưu snapshot; Airflow điều phối batch; PyTorch/Transformers/PEFT/TRL hoặc XGBoost train; MLflow tracking/registry; FastAPI serving; Docker đóng gói; Prometheus/Grafana và OpenTelemetry quan sát vận hành. Không cần lắp tất cả công cụ ngay ở pilot.

LoRA cập nhật các ma trận adapter nhỏ thay vì cập nhật toàn bộ trọng số; MLflow cung cấp version/alias và liên kết experiment. Đây là năng lực của công cụ, không phải bằng chứng đã dùng ở công ty cũ. [PEFT LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora), [MLflow Registry](https://mlflow.org/docs/latest/ml/model-registry/).

### 2.3. Một gói dữ liệu huấn luyện phải bàn giao được

```json
{
  "dataset_version": "hr-risk-v3",
  "purpose": "attrition_risk_90d",
  "observation_cutoff": "2026-06-30T23:59:59+07:00",
  "label_window_days": 90,
  "split_strategy": "employee_group_and_time",
  "schema_version": "hr-feature-v2",
  "source_manifest": "sha256:example-only",
  "pii_policy": "pseudonymized-restricted",
  "label_guideline_version": "guideline-v4",
  "review_status": "approved-for-experiment"
}
```

Đây là ví dụ contract, không phải manifest thật. Với mỗi sample cần có `sample_id`, `source_ref`, `input_snapshot_id`, `label`, `label_source`, `reviewer`, `reviewed_at`, `split`. Thiếu ground truth tương lai thì chưa được gọi là nhãn nghỉ việc thực tế; nhận xét chuyên gia chỉ là một loại nhãn khác, phải ghi riêng.

### 2.4. Bộ chỉ số và cách chấm

| Lớp | Chỉ số | Cách tránh kết luận sai |
|---|---|---|
| Retrieval | Recall@k, MRR/nDCG, ACL leakage | Chấm trên nguồn gold; trường hợp không có đáp án cần tập riêng |
| LLM | Correctness, evidence support, citation validity, refusal correctness, JSON validity | Chuyên gia chấm rubric; LLM-as-judge chỉ hỗ trợ, hiệu chỉnh với người |
| Classification | Precision, recall, macro-F1, PR-AUC, confusion matrix | Lớp hiếm không đánh giá chỉ bằng accuracy; chọn threshold trên validation |
| Risk scoring | Calibration/Brier, precision@capacity, recall theo nhóm | Điểm 0,8 không mặc nhiên là 80% nếu chưa calibration |
| OCR/KIE | CER/WER, field exact match/F1, table row match | Chấm riêng tiền, ngày, mã; đo cả tỷ lệ cần review |
| Vision | mAP, event precision/recall, false alarms/camera-hour | Frame-level đẹp chưa chứng minh event-level tốt; tách site/time |
| Hệ thống | p50/p95/p99, timeout/error rate, throughput, cost/task | Ghi tải, phần cứng, độ dài input, warm/cold start và phiên bản |
| Nghiệp vụ | Thời gian xử lý, sửa tay, tỷ lệ giải quyết, conversion | Có baseline và nhóm so sánh; không tự tạo số cải thiện |

## 3. Hệ tri thức và AI Agent chatbot: kiến trúc tham chiếu dùng chung

### 3.1. Chọn một stack cụ thể để giải thích xuyên suốt [TK]

[Kiến trúc hệ tri thức và RAG có phân quyền](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/01-knowledge-rag.drawio.png>)

| Thành phần | Lựa chọn cụ thể | Trách nhiệm và trade-off |
|---|---|---|
| Web/chat | React, TypeScript, SSE | Hiện nguồn, trạng thái, xác nhận tool; SSE cho stream một chiều |
| Identity/API | Keycloak OIDC, NGINX, FastAPI/Pydantic | Xác thực; tenant/role/scope lấy từ token đã kiểm tra, không tin giá trị model tự điền |
| Kho gốc | MinIO S3-compatible; PostgreSQL metadata | Giữ bản gốc, hash, version, owner; quyền tải file kiểm tra ở backend |
| Ingestion | Apache Tika cho text; PaddleOCR/PP-Structure cho scan/layout; Airflow | Extract → normalize → review → chunk → index; retry theo document version |
| Retrieval | OpenSearch BM25 + Qdrant dense vector | Tìm exact term như mã văn bản cùng tìm ngữ nghĩa; thêm vận hành hai index |
| Embedding/rerank | BAAI/bge-m3; BAAI/bge-reranker-v2-m3 | Baseline multilingual để benchmark tiếng Việt; không mặc định tốt nhất |
| LLM | Qwen2.5-7B-Instruct qua vLLM | Baseline tự host để kiểm soát dữ liệu; chọn model/hardware sau benchmark |
| Agent | LangGraph; PostgreSQL checkpointer | State graph có bước deterministic, pause/resume, tool result và human approval |
| Workflow | Camunda 8 cho BPMN và tác vụ con người | Workflow nghiệp vụ dài hạn; không dùng thay agent reasoning hoặc motor control |
| Policy | Open Policy Agent, service-side RBAC/ABAC | Kiểm tra actor/action/resource/context, tách khỏi prompt |
| Quan sát | OpenTelemetry + Grafana/Loki; Langfuse nếu cần LLM trace | Theo `trace_id`; mask dữ liệu nhạy cảm; kiểm soát nơi lưu trace |

Đây là **một thiết kế tự host**, không đồng thời bắt buộc thêm mọi dịch vụ AWS/Azure. Ở Tori sẽ trình bày phương án managed AWS tương đương. Embedding/reranker và model được chọn làm baseline cụ thể từ [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) và [model card Qwen](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct). LangGraph hỗ trợ orchestration có trạng thái; quyền truy cập vẫn phải do ứng dụng thực thi. [Tài liệu LangGraph](https://docs.langchain.com/oss/python/langgraph/overview).

### 3.2. Ingestion không chỉ là upload PDF

1. **Inventory:** phân loại luật/quy trình/FAQ/hướng dẫn thao tác; owner xác nhận tài liệu chính thức. Lưu `document_id`, `version`, `effective_from/to`, `jurisdiction`, `audience`, `classification`, `source_url`, `checksum`.
2. **Extract:** phân biệt PDF có text với scan; xử lý trang xoay, bảng, phụ lục và chữ ký. Giữ page/bounding box để mở đúng vùng bằng chứng. Không suy ra text bị mờ bằng cách để model đoán.
3. **Normalize:** loại header/footer lặp, giữ heading path và liên kết bảng; không xóa đơn vị, số điều, phủ định, ngoại lệ. Kiểm tra bản OCR với nguồn gốc theo mẫu và các trường rủi ro cao.
4. **Chunk:** cắt theo điều/khoản/tiểu mục; baseline 400–800 token, overlap 50–100 chỉ là khởi điểm. Bảng lớn tách theo nhóm dòng kèm header. Lưu quan hệ parent–child để kéo lại đủ ngữ cảnh.
5. **Index:** embedding theo version; BM25 và vector cùng metadata filter. Chỉ công bố index snapshot khi ingestion và QA hoàn tất; rollback bằng alias/version đã duyệt.
6. **Cập nhật/hủy hiệu lực:** tombstone bản cũ, xử lý cache, index, file download; không để nguồn bị thu hồi vẫn xuất hiện trong câu trả lời cũ dưới quyền người dùng mới.

### 3.3. Luồng truy vấn online

`User → OIDC/API → resolve tenant/role/time → intent → retrieve → rerank → context builder → LLM → schema/evidence checks → answer/tool proposal → audit`.

Retrieval baseline: lấy 20 ứng viên BM25 và 20 vector sau lọc quyền/hiệu lực, hợp nhất bằng Reciprocal Rank Fusion, rerank còn khoảng 5–8 đoạn. Các số này là cấu hình thử nghiệm. Query về “hiện hành” dùng ngày yêu cầu; query về hồ sơ quá khứ phải làm rõ mốc áp dụng, không tự áp luật mới.

Output gồm câu trả lời, nguồn, ngày hiệu lực, thông tin còn thiếu, giới hạn và hành động kế tiếp. Khi các nguồn mâu thuẫn, hệ thống chỉ rõ mâu thuẫn và chuyển chuyên gia; không chọn đại nguồn có similarity cao hơn. Điểm similarity không phải xác suất câu trả lời đúng.

### 3.4. Khi nào cần Knowledge Graph/GraphRAG?

RAG thông thường đủ cho hỏi đáp một hoặc vài nguồn. Với câu hỏi nối `thủ tục → điều kiện → cơ quan → thẩm quyền → tài liệu → điều khoản`, có thể thêm **Neo4j** lưu quan hệ có `source_ref`, thời gian hiệu lực và provenance. LLM chỉ đề xuất entity/relation; chuyên gia duyệt quan hệ quan trọng. Graph retrieval bổ sung context rồi vẫn trích nguồn. Không biến graph thành nơi tự suy diễn thẩm quyền không có căn cứ.

### 3.5. Agent chatbot: dùng công cụ nhưng không vượt quyền

[Agent Copilot kết hợp quyền, workflow và xác nhận](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/02-agent-workflow.drawio.png>)

Các tools mẫu: `search_knowledge`, `get_case_status`, `get_allowed_actions`, `validate_draft`, `create_draft`, `submit_after_confirmation`. Tool đọc có thể tự thực hiện trong phạm vi quyền; tool thay đổi dữ liệu phải qua policy, preview và xác nhận theo quy tắc nghiệp vụ. Backend kiểm tra lại quyền và state version tại thời điểm commit.

State graph: `AUTHENTICATE → UNDERSTAND → RETRIEVE/READ_TOOL → VALIDATE → ANSWER` hoặc `PROPOSE_ACTION → HUMAN_CONFIRM → RECHECK → EXECUTE → VERIFY`. `NEED_CLARIFICATION`, `NO_EVIDENCE`, `TOOL_TIMEOUT`, `DENIED` là trạng thái chính thức. Retry có giới hạn; side effect dùng idempotency key, không gửi lại mù quáng sau timeout.

Memory: context hội thoại ngắn hạn theo session; long-term memory chỉ lưu dữ kiện được phép, có nguồn/TTL. Trạng thái hồ sơ, tồn kho, pin robot phải đọc từ hệ thống nguồn, không dùng “ký ức” của chatbot làm sự thật. Cache phải phân vùng theo tenant/quyền/index version; câu trả lời nhạy cảm không dùng semantic cache chung.

Prompt injection từ PDF, website hoặc tin nhắn được coi là dữ liệu không tin cậy. Không để nội dung nguồn thêm tool, đổi quyền hoặc chỉ thị tiết lộ dữ liệu. QC kiểm thử cả retrieval leak, tool injection, output HTML nguy hiểm và truy vấn chéo tenant.

## 4. Cổng một cửa đầu tư quốc gia

### Căn cứ và phạm vi

**[HS]** CV trang 2–3 nêu ba module: Trục tích hợp & Quản trị dữ liệu; Hệ tri thức & Trợ lý AI; Quản lý đầu tư nước ngoài. CV cũng mô tả đặc tả nghiệp vụ/API/dữ liệu và AI evaluation ở cấp nhóm dự án. **[TK]** Stack và quy trình chi tiết dưới đây cụ thể hóa module, chưa được xác nhận là production stack.

### Use case

| ID | Người dùng và mục tiêu | Input → output | Ngoại lệ quan trọng |
|---|---|---|---|
| INV-AI-01 | Nhà đầu tư hỏi điều kiện/thành phần hồ sơ | Câu hỏi + loại thủ tục + địa bàn + mốc thời gian → checklist có nguồn | Thiếu địa bàn/loại hình; nguồn hết hiệu lực; câu hỏi ngoài phạm vi |
| INV-AI-02 | Cán bộ tra cứu quy trình xử lý | Role + hồ sơ + bước hiện tại → các bước được phép và căn cứ | Không có quyền; hồ sơ thay đổi đồng thời; khác thẩm quyền |
| INV-AI-03 | Người nộp kiểm tra bộ hồ sơ | File → extracted fields → danh sách thiếu/mâu thuẫn | File mờ; bản scan thiếu trang; model không đủ bằng chứng |
| INV-AI-04 | Tra cứu trạng thái | Mã hồ sơ qua API được phân quyền → trạng thái và việc tiếp theo | Không tìm thấy; không thuộc người dùng; downstream timeout |

### Kiến trúc và dữ liệu

Dùng kiến trúc mục 3. Kho tri thức quản lý văn bản/quy trình; hệ thống hồ sơ giữ trạng thái và dữ liệu giao dịch. Hai miền kết nối qua API, không trộn hồ sơ cá nhân vào index công khai. Camunda quản lý luồng tiếp nhận–bổ sung–thẩm định–phê duyệt theo cấu hình đã duyệt; OPA kiểm tra phạm vi khai thác. LLM có thể diễn giải checklist nhưng **không tự ban hành kết luận pháp lý hoặc phê duyệt hồ sơ**.

Entity đề xuất: `Procedure`, `ProcedureVersion`, `Authority`, `DocumentVersion`, `RequirementItem`, `Application`, `ApplicationStep`, `KnowledgeChunk`, `AnswerCitation`. Quan hệ và hiệu lực giúp BA đặc tả được trường hợp một hồ sơ cũ cần xem hướng dẫn áp dụng tại thời điểm cũ. Rule pháp lý cụ thể phải do đầu mối chuyên môn xác nhận; tài liệu này không cung cấp tư vấn pháp luật.

### Công việc BA/QC và công cụ

| Công việc | Cách làm chi tiết | Công cụ và đầu ra |
|---|---|---|
| Discovery | Workshop với nhà đầu tư, cán bộ tiếp nhận, chuyên viên, quản trị dữ liệu; phân biệt câu hỏi hướng dẫn và quyết định nghiệp vụ | Confluence, Jira; actor/use-case map, assumption log |
| Chuẩn hóa tri thức | Lập inventory nguồn, owner, điều/khoản, phiên bản, địa bàn, ACL; định nghĩa quy trình cập nhật và thu hồi | Excel/SQL; knowledge manifest, data dictionary |
| Đặc tả hệ thống | Sequence query/RAG/tool; API hồ sơ và errors; trạng thái của câu trả lời, citation và fallback | draw.io, OpenAPI, Postman; SRS, API mapping |
| Build dữ liệu | Kiểm tra OCR, chunk, heading, metadata; tạo câu hỏi paraphrase, câu không có đáp án, câu khác mốc hiệu lực | Python/pandas, SQL, review UI; gold Q&A có nguồn |
| Đánh giá | Tách lỗi tìm nguồn/sai nguồn/diễn giải sai/tool sai; kiểm tra citation đến đúng trang | Evaluation sheet, pytest nếu tự động hóa; error taxonomy |
| UAT và release | Chạy người dùng theo role, chặn truy vấn chéo hồ sơ, kiểm tra thu hồi tài liệu và regression | Jira defect, Postman/Newman; sign-off và RTM |

**Một test có giá trị:** Given cán bộ chỉ được xem tỉnh A, When hỏi hồ sơ tỉnh B bằng mã chính xác, Then backend từ chối và chatbot không tiết lộ cả tên nhà đầu tư, snippet, URL tải file hay trạng thái hồ sơ. Không chỉ kiểm tra “bot nói không có quyền”.

**Training/fine-tune:** ưu tiên sửa ingestion/retrieval và prompt. Chỉ fine-tune khi benchmark cho thấy lỗi ổn định ở phân loại intent, format hoặc hành vi trả lời; SFT không thay thế cơ chế cập nhật văn bản có hiệu lực. BA xây Q&A gold và tool-call sample; engineer train adapter; QC so candidate và baseline trên cùng test độc lập.

**Cách kể có căn cứ:** “Ở cổng một cửa, tôi tham gia hệ tri thức và trợ lý AI gắn với nghiệp vụ và data governance. Tôi tập trung biến câu hỏi người dùng thành use case có nguồn, phạm vi quyền và tiêu chí nghiệm thu. Khi giải thích giải pháp, tôi có thể phân rã rõ kho tri thức, retrieval, agent và API hồ sơ.” Tên model chỉ bổ sung khi xác nhận thực tế.

## 5. CSDL quốc gia về xử lý vi phạm hành chính

### Căn cứ và use case

**[HS]** CV trang 2 xác nhận dự án; danh sách đầu vào của Đức nêu Copilot hướng dẫn thao tác, thẩm quyền và căn cứ. **[TK]** Các chi tiết triển khai sau là thiết kế mở rộng.

- **VPHC-AI-01:** hướng dẫn ngay trên màn hình: cán bộ ở bước kiểm tra biên bản được thấy checklist đúng role, trạng thái và phiên bản quy trình.
- **VPHC-AI-02:** hỏi “tôi được làm gì tiếp theo?”; Copilot gọi API `allowed-actions`, giải thích điều kiện chưa đạt và liên kết tới nguồn.
- **VPHC-AI-03:** tạo bản nháp nội dung từ dữ kiện đã được xác nhận; đối chiếu thiếu trường, thời hạn và tài liệu kèm theo, chờ người chịu trách nhiệm duyệt.
- **VPHC-AI-04:** hỏi căn cứ liên quan; trả đoạn trích và mốc hiệu lực, nêu khi cần chuyên gia pháp chế, không tự tính mức xử phạt theo suy đoán LLM.

### Kiến trúc cụ thể

React Copilot nhận `screen_id`, `case_id`, `workflow_instance_id`, `state_version`; backend xác minh chúng. FastAPI + LangGraph điều phối; RAG mục 3 tìm hướng dẫn; Camunda 8 chạy workflow; DMN/rule service chứa bảng quyết định đã được nghiệp vụ duyệt; PostgreSQL lưu hồ sơ, OPA/RBAC/ABAC kiểm tra thẩm quyền. `allowed-actions` do nghiệp vụ backend trả, không do model tự phát minh.

`get_case_context → get_allowed_actions → retrieve_authoritative_guidance → explain_next_step → validate_draft → user_review → commit`.

Đề xuất optimistic concurrency: gửi `expected_state_version`; nếu hồ sơ đã chuyển bước thì trả conflict, tải lại context, không áp hướng dẫn cũ. Idempotency key bảo vệ tạo nháp/gửi yêu cầu. Outbox đảm bảo event audit và cập nhật hồ sơ nhất quán khi có queue; không tuyên bố exactly-once toàn hệ thống.

### BA/QC thực hiện thế nào?

1. **BPMN và decision table:** BA lập từng bước, người chịu trách nhiệm, input/output, điều kiện chuyển, SLA, nhánh bổ sung/chuyển lại/thu hồi. Công cụ: Camunda Modeler, draw.io, Confluence. Đầu ra: workflow version, authority matrix, exception catalog.
2. **Context contract:** BA định nghĩa thông tin được gửi sang AI; field nào phải mask, field nào bắt buộc đọc lại API; tool quyền đọc/ghi. Công cụ: OpenAPI, Postman, SQL/DataGrip.
3. **Tập gold theo trạng thái:** QC lấy cùng câu hỏi tại nhiều role/state để chứng minh kết quả khác nhau đúng quy định; có câu hỏi thiếu dữ kiện và nguồn mâu thuẫn. Công cụ: Excel/JSONL, Python và review UI.
4. **Kiểm thử đồng thời:** một người chuyển hồ sơ trong khi người khác đang xem gợi ý; gửi lại request; mạng mất sau commit; ACK trễ; quyền bị thu hồi giữa lượt chat. Công cụ: Postman/Newman, browser network log, truy vấn audit.
5. **Phân tích lỗi:** lỗi do business rule, version workflow, stale context, retrieval hay model; ticket phải chứa `trace_id`, case đã ẩn danh, expected/actual, version và mức độ ảnh hưởng.

**AC mẫu:** Given bản nháp ở version 12 và người dùng còn quyền, When xác nhận nhưng hồ sơ đã sang version 13, Then không ghi thay đổi; trả `STATE_CONFLICT`; hiển thị bước hiện tại; ghi audit mà không lặp side effect.

**Kế thừa sang robot:** hồ sơ đang xử lý tương ứng mission instance; thẩm quyền tương ứng quyền điều động/teleoperation; `allowed-actions` tương ứng skill khả dụng; đổi quy trình tương ứng policy pack có version. Robot còn thêm trạng thái vật lý và an toàn, không thể hoàn tác như dữ liệu hồ sơ.

## 6. Smart Safe: AI Camera kết hợp IoT

### Căn cứ và use case

**[HS]** CV xác nhận SaaS IoT an ninh/cháy nổ, device/incident/connectivity. Tài liệu phỏng vấn mô tả gateway, cảm biến, camera, cấu hình, cảnh báo, điều khiển và UAT. **[TK]** Không có bằng chứng xác định detector hoặc framework camera; phần train vision dưới đây là mở rộng.

| Use case | Cách hoạt động | Người ra quyết định |
|---|---|---|
| SS-AI-01: xâm nhập ngoài giờ | Phát hiện người, theo dõi track đi vào polygon trong lịch giám sát | Rule engine phát cảnh báo; bảo vệ xác minh |
| SS-AI-02: xác minh báo động đa cảm biến | Kết hợp door/PIR và clip camera gần thời điểm sự kiện | Con người kết luận sự cố; AI hỗ trợ ưu tiên |
| SS-AI-03: nhận diện khói/lửa hỗ trợ | Model chuyên biệt + sensor signal, chuyển kiểm tra | Không thay hệ thống báo cháy được thiết kế/chứng nhận riêng |

[Smart Safe: vision tại edge và xử lý sự cố](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/04-smart-safe-vision.drawio.png>)

### Kiến trúc [TK]

Camera RTSP qua GStreamer → NVIDIA Jetson Orin/industrial PC → **YOLOX** detector, **ByteTrack** tracker, polygon/time-window rules → MQTT TLS qua EMQX → Spring Boot event service → RabbitMQ xử lý bất đồng bộ → PostgreSQL incident/device, TimescaleDB telemetry, MinIO clip → React dashboard và SMS/email. Chọn phần cứng sau đo FPS, nhiệt độ, điện và số camera; không mặc định một Jetson đủ mọi tải.

ONNX Runtime/TensorRT tối ưu inference sau khi kiểm tra accuracy giữa bản FP32/FP16/INT8. ONVIF dùng discovery/config khi camera hỗ trợ; RTSP vận chuyển video, MQTT gửi metadata sự kiện, không đưa video thô vào broker. Camera có AI sẵn có thể gửi sự kiện qua adapter thay vì triển khai model riêng. Detector và tracker tham chiếu từ [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) và [ByteTrack](https://github.com/FoundationVision/ByteTrack); cần kiểm tra riêng license của code, weights và dữ liệu trước khi chọn.

Event contract: `event_id`, `site_id`, `device_id`, `observed_at`, `received_at`, `event_type`, `track_id`, `zone_version`, `model_version`, `confidence`, `clip_ref`, `sequence_no`. Dedupe theo event ID; xử lý event-time và out-of-order; heartbeat độc lập với alarm. Camera mất kết nối không được diễn giải là “không có xâm nhập”.

### Training và QC vision [TK]

Thu video đủ ban ngày/đêm, mưa, chói sáng, phản xạ, bóng người, người che khuất, vật nuôi, thay góc camera. CVAT gán bounding box và track, ghi occlusion/lighting; chia train/test theo camera/site và ngày, tránh lấy hai frame liền nhau vào hai tập. Hard negatives gồm poster người, bóng đổ, màn hình TV. Train detector với PyTorch; tracker và rule được đánh giá riêng trước đánh giá toàn event.

Đo event precision/recall, false alarms trên mỗi camera-hour, thời gian từ trigger đến dashboard; báo cáo theo từng điều kiện. Đừng chỉ nêu mAP. QC test cảnh báo lặp, recovery đến trước acknowledge, inactive device, lệnh timeout, gateway reboot và replay sau offline.

### Việc Đức trình bày

**Có căn cứ ở lớp BA/IoT:** khảo sát thiết bị và đơn vị vận hành; chuẩn hóa site/device/alert; mô hình trạng thái; mapping payload, command/ACK; role/site scope; kịch bản UAT và xử lý ngoại lệ. Công cụ hồ sơ có nêu ở cấp kỹ năng: Jira, Confluence, draw.io, Figma, SQL, Postman.

**Khi mở rộng sang AI Camera:** tôi định nghĩa “xâm nhập” bằng zone, thời gian, dwell và ngoại lệ; lập bộ video nghiệm thu, rubric event, false-positive taxonomy; phối hợp engineer chỉnh model/threshold/rules; kiểm tra clip bằng chứng và trải nghiệm xác minh. CVAT, MLflow, MQTTX, Grafana là công cụ đề xuất, không mặc định đã dùng.

**Câu kể:** “Điểm mạnh của tôi ở Smart Safe là nối tín hiệu thiết bị với hành động vận hành. Một tín hiệu không chỉ cần hiển thị; nó phải đúng site, đúng loại, đúng thời điểm, không lặp và có vòng đời xử lý. Tôi mang cách phân tích đó sang AI Camera và robot.”

## 7. HRAI One: ML trên dữ liệu nhân sự và LLM diễn giải

### Căn cứ và use case

**[HS]** CV mô tả HR AI, risk prediction, talent development; phần đóng góp chung có chuẩn bị/làm sạch/gán nhãn/đánh giá dữ liệu. Các tài liệu HRAI đào sâu feature catalog, snapshot và feedback nhưng nhiều chi tiết là phương án hỏi đáp.

- **HR-AI-01:** xếp ưu tiên xem xét nguy cơ nghỉ việc trong cửa sổ thời gian, có giải thích bằng feature đã quan sát.
- **HR-AI-02:** phát hiện xu hướng giảm hiệu suất hoặc quá tải để quản lý kiểm tra, không coi đây là chẩn đoán sức khỏe.
- **HR-AI-03:** tổng hợp nhận xét và đề xuất chủ đề đào tạo từ KPI/kỹ năng/nhận xét có nguồn; không tự ra quyết định tuyển dụng, kỷ luật hoặc thăng tiến.

### Kiến trúc [TK]

Oracle/SQL Server HR source → Airflow → Python/pandas features → PostgreSQL feature snapshot → **XGBoost** risk classifier → calibrated score + evidence → **Qwen2.5-7B-Instruct** sinh diễn giải theo JSON schema → review UI → feedback/gold tables → dataset builder → MLflow candidate registry. Nội dung chính sách HR có thể lấy qua RAG; số liệu KPI phải dùng calculation service, không để LLM tự tính.

Tách `Feature Catalog` (định nghĩa) khỏi `Employee Feature Value` (giá trị tại thời điểm) và `Input Snapshot` (bộ dữ liệu thực sự đưa vào model). Ví dụ `KPI_TREND_3M` ghi rõ kỳ, công thức, source; `MANAGER_SENTIMENT` có nguồn văn bản, extractor version và độ tin cậy. Missing không mặc định bằng 0; dữ liệu synthetic chỉ dùng test hoặc nghiên cứu có đánh dấu, không biến thành kết quả nhân sự thật.

### Công việc thực tế cần mô tả và công cụ

| Bước | BA/QC làm gì | Đầu ra/công cụ |
|---|---|---|
| Định nghĩa bài toán | Chốt label, horizon, thời điểm dự đoán; phân biệt nhãn chuyên gia với kết quả tương lai | Label specification, Confluence |
| Chuẩn hóa dữ liệu | Join nguồn bằng khóa hợp lệ; xác định lịch sử, timestamp, missing, dữ liệu trùng | SQL/DataGrip, pandas; reconciliation report |
| Thiết kế feature | KPI trend, workload, tenure, training history; ghi provenance và chống leakage | Feature catalog, dbdiagram.io; không dùng trường “ngày nghỉ việc” đã biết sau cutoff |
| Tạo test có chủ đích | Nhân viên mới thiếu lịch sử; KPI giảm nhưng khối lượng tăng; dữ liệu quản lý mâu thuẫn | CSV/JSONL, Python, SQL seed trong DB test |
| Đánh giá đầu ra | Đúng label, đúng score interpretation, evidence và lời khuyên; kiểm tra nhóm dữ liệu ít mẫu | Rubric, confusion matrix, golden set |
| Feedback | PASS/PARTIAL/FAIL ở cấp trường; bắt buộc sửa nhãn và chỉ nguồn cho phần sai | Review UI; `AI_FEEDBACK`, adjudication log |
| Kiểm tra sau phát hành | Trace prediction → snapshot → model; so drift, missing rate, chất lượng theo kỳ | SQL, MLflow/Grafana đề xuất; defect triage |

**Test data không ghi vào production:** seed có `test_run_id`, khóa giả, transaction và cleanup theo ID; không dùng số định danh thật. Kiểm thử negative ở quyền truy cập HR và export cũng quan trọng như output AI.

### Feedback chuyển thành training như thế nào?

Một phản hồi “50% đúng” không tạo nhãn mới. QC phải chỉ rõ `wrong_fields`, `corrected_label`, `corrected_text`, `evidence_refs`, `error_category`; reviewer thứ hai xử lý bất đồng. Với outcome nghỉ việc, chờ cửa sổ quan sát đủ dài và xử lý mẫu chưa biết kết quả; không gán “không nghỉ” chỉ vì chưa có dữ liệu.

- XGBoost học feature và label đã phê duyệt; cân bằng lớp bằng class/sample weights được kiểm tra, không tăng tỷ trọng vô hạn cho lỗi hiếm.
- LLM SFT học diễn giải tốt từ input + evidence + corrected response, với **Transformers + TRL SFTTrainer + PEFT LoRA**. Baseline config minh họa: rank 16, alpha 32, dropout 0,05, learning rate 1e-4, 1–3 epoch; engineer điều chỉnh theo model/GPU/loss và validation. Không coi cấu hình này là tối ưu sẵn.
- DPO chỉ cân nhắc khi có cặp chosen/rejected nhất quán cho cùng input và evidence; không suy ra cặp preference từ một nút dislike đơn lẻ.

Đánh giá ML bằng PR-AUC, precision theo số ca HR có thể xem xét, calibration và subgroup error; LLM bằng groundedness, factual consistency, ngôn ngữ không quy kết. Giữ con người quyết định và có cơ chế sửa dữ liệu nguồn.

**Câu kể có thể bảo vệ:** “Tôi tham gia ở khâu định nghĩa dữ liệu, label, test scenario, golden set và đánh giá AI. Tôi phân biệt lỗi dữ liệu, feature, model và diễn giải để đưa feedback có thể hành động được cho engineer. Tôi không coi chấm output là đã tự huấn luyện foundation model.”

## 8. Tori AI của Techcom Life — bài mô phỏng BA + QC

**[MP] Đức xác nhận Tori chỉ là dự án tham khảo.** Đoạn ngôi “tôi” dưới đây là bài luyện nhập vai. Không dùng mục này như một dự án đã làm trong CV hoặc kể tên công ty như nơi đã trực tiếp triển khai.

Techcom Life công bố Tori là trợ lý hỗ trợ tư vấn viên theo thời gian thực, bên cạnh nền tảng iProtek. Nguồn công khai này không xác nhận phần việc cá nhân của Đức hoặc toàn bộ stack nội bộ. [Công bố của Techcom Life](https://www.techcomlife.com/tin-tuc/techcom-life-doat-cu-dup-giai-thuong-tai-insurance-asia-awards-2026-tiep-noi-chuoi-ghi-nhan-khu-vuc-trong-nam-dau-hoat-dong-86/).

### Use case mô phỏng bám sát JD BA & QA

| ID | Tình huống | Đầu ra cần nghiệm thu |
|---|---|---|
| TORI-01 | Tư vấn viên hỏi quyền lợi/loại trừ của một sản phẩm và phiên bản hợp đồng | Trả đúng nguồn, điều kiện, ngoại lệ, câu hỏi cần làm rõ |
| TORI-02 | So sánh hai phương án phục vụ chuẩn bị tư vấn | Bảng có nguồn; không hứa quyền lợi ngoài tài liệu |
| TORI-03 | Hỏi quy trình bổ sung hồ sơ hoặc bước xử lý | Checklist và bước tiếp theo, không tự quyết định underwriting/claim |
| TORI-04 | Kiểm tra chất lượng nội dung tư vấn | Chỉ ra câu thiếu căn cứ hoặc khác điều khoản; chuyên gia duyệt |

### Phương án AWS cụ thể [TK], chưa xác minh là stack nội bộ

S3 giữ policy wording/SOP/version → Step Functions điều phối ingestion → Textract cho loại tài liệu/ngôn ngữ được hỗ trợ, **PaddleOCR tự host làm phương án với scan tiếng Việt sau benchmark** → QA nội dung → Amazon Bedrock Knowledge Bases + Titan Text Embeddings V2 + OpenSearch Serverless vector → backend trên ECS/Fargate gọi Bedrock Converse với foundation model đang được cấp quyền tại region → policy/tool validator → UI iProtek giả định qua API được cấp phép.

Không mặc định Textract OCR tiếng Việt tốt hoặc có hỗ trợ mọi loại bảng. Danh sách ngôn ngữ tại thời điểm tra cứu không liệt kê tiếng Việt, vì vậy thiết kế phải có parser/OCR phù hợp cho corpus tiếng Việt; chọn embedding multilingual thay Titan nếu benchmark cho thấy không phù hợp. Không chốt tên model Claude hay version thực tế của Tori khi chưa có bằng chứng. [Giới hạn Textract](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html), [Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).

DynamoDB lưu session/config manifest; PostgreSQL có thể dùng cho dữ liệu evaluation quan hệ; CloudWatch/OpenTelemetry ghi trace đã mask; IAM/KMS/Secrets Manager quản lý quyền và khóa. SageMaker **chỉ là nhánh tùy chọn** cho train/fine-tune model mở hoặc pipeline ML riêng, không mặc định mỗi lần gọi Bedrock là đang train trên SageMaker. Kiro nằm ở chu trình phát triển/spec/code, không phải model trả lời khách hàng. [Kiro IDE](https://kiro.dev/docs/ide/).

### Mẫu kể ngôi “tôi” để luyện — toàn bộ là mô phỏng

> Trong tình huống này, tôi phụ trách Build và Test của trợ lý AI. Tôi nhận bộ tài liệu từ nghiệp vụ, kiểm tra phiên bản và hiệu lực, chuẩn hóa nội dung để ingest, rồi duy trì golden test set theo từng domain. Mỗi vòng tôi thay đổi có kiểm soát một cấu hình như chunking, retrieval hoặc prompt, chạy lại benchmark và phân tích lỗi. Trước UAT, tôi kiểm tra cả câu trả lời đúng nghiệp vụ, trích dẫn, ngoại lệ, quyền dữ liệu và luồng sử dụng thực tế. Sau release, tôi xác minh chất lượng trên production bằng bộ kiểm tra được duyệt và dữ liệu được phép, rồi chuyển lỗi và điểm thiếu yêu cầu vào backlog.

### Một vòng làm việc chi tiết [MP]

1. **Nhận tài liệu:** inventory và hash; SME duyệt nguồn. Tôi dùng Excel, S3 console/API và checklist để phát hiện bản trùng, bản thiếu trang, điều khoản cũ.
2. **Kiểm tra ingestion:** so text OCR và bảng quyền lợi với PDF; xác nhận `product_version`, `effective_date`, `audience`, `page_ref`. Tôi dùng review UI, SQL và Python để kiểm tra độ đầy đủ.
3. **Thiết kế golden set:** khoảng 200 câu khởi điểm gồm câu thường gặp, nhiều điều kiện, thiếu thông tin, không có đáp án và tình huống gây nhầm giữa sản phẩm. Con số là ví dụ, tăng theo coverage và độ rủi ro, không phải thành tích.
4. **Build:** cấu hình prompt, metadata filter, chunk size/top-k trong môi trường test; engineer xử lý phần cần sửa code. Lưu `config_version`, corpus snapshot, model ID, region, latency và cost.
5. **Test:** Python/boto3 gọi API được cấp; Postman kiểm tra contract; rubric chấm correctness, nguồn, loại trừ, fallback, wording. Không lấy fluency làm chất lượng nghiệp vụ.
6. **Triage:** ví dụ câu trả lời bỏ qua loại trừ do bảng bị cắt → sửa ingestion/chunk; không vội fine-tune. Jira ticket ghi query, expected answer, source, trace, config trước/sau và nhóm ảnh hưởng.
7. **UAT/production verification:** SME/tư vấn viên duyệt; QA regression; release owner quyết định; tôi kiểm tra smoke/read-only, thu feedback đã mask và theo dõi score theo version.

### Ví dụ acceptance criteria

Given câu hỏi thiếu phiên bản sản phẩm và quyền lợi thay đổi giữa các phiên bản, When tư vấn viên yêu cầu con số quyền lợi, Then Tori hỏi lại hoặc trình bày rõ phạm vi từng phiên bản; không đưa một con số duy nhất như kết luận chắc chắn. Khi không tìm được nguồn, output phải nêu chưa đủ căn cứ và cách chuyển chuyên gia.

Các đầu việc bám trực tiếp [JD_TechcomBank.pdf, trang 1–2](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Tori AI/JD_TechcomBank.pdf>): document lifecycle, iterative configuration, golden set, UAT, regression, production verification và refinement. JD không chứng minh có yêu cầu bắt buộc train model từ đầu.

## 9. mChat: Conversational AI và điều phối hội thoại

### Căn cứ, use case và phạm vi

**[HS]** CV xác nhận nền tảng đa kênh và AI hỗ trợ insight/recommendation. SRS và khảo sát thể hiện inbox, conversation, assignment, label, note, SLA và automation. Bản đăng ký sáng kiến AI là **giải pháp đề xuất**, không chứng minh mọi tính năng đã production.

- **MCHAT-AI-01:** phân loại intent, nhu cầu, sản phẩm, mức quan tâm và blocker từ chuỗi tin nhắn; trả JSON có evidence span.
- **MCHAT-AI-02:** tóm tắt để agent tiếp nhận, gợi ý câu hỏi tiếp theo/câu trả lời dựa trên KB và thông tin sản phẩm từ ERP.
- **MCHAT-AI-03:** đề xuất route tới nhóm phù hợp; low-confidence hoặc tranh chấp chuyển người. Rule routing quyết định cuối, không để LLM tự thay đổi quyền.

### Kiến trúc [TK]

Facebook/Zalo OA/website webhook → channel adapter validate signature → PostgreSQL conversation/message → RabbitMQ theo conversation → LangGraph context builder → Qwen2.5-7B-Instruct/intent classifier → Pydantic output validator → insight DB → SSE tới agent UI. Redis giữ cache ngắn hạn và trạng thái queue; ERP API cung cấp giá/tồn kho hiện tại. Có RAG cho chính sách đổi trả và bảo hành.

Định danh `channel_message_id` để dedupe; giữ thứ tự theo conversation; AI run lưu `conversation_version` và `last_message_id`. Nếu tin mới đến trước khi output xong, kết quả cũ không được ghi đè insight mới. Tách trạng thái hội thoại khỏi trạng thái phân công; kiểm soát quyền theo team/inbox. Chatbot sang người phải mang context, không tiếp tục gửi câu trả lời song song ngoài quy tắc.

### BA + QC làm gì?

| Đầu việc | Chi tiết riêng cho mChat | Công cụ/đầu ra |
|---|---|---|
| Taxonomy | Primary/secondary intent; UNKNOWN; nhu cầu khác sản phẩm; phân biệt “không mua” với “chưa quyết định” | Label guide, decision table; Excel/Confluence |
| Conversation dataset | Anonymize, cắt theo phiên, giữ multi-turn; split theo khách hàng/cuộc hội thoại | SQL/pandas, Label Studio đề xuất |
| Rule routing | Agent skill, workload, SLA, giờ làm việc, team scope và override | BPMN/state diagram, Jira stories |
| AI output contract | Enum/score/evidence/summary/next_action; score không được coi là xác suất đã calibration | JSON schema, Swagger/Postman |
| Integration test | Duplicate webhook, out-of-order, token kênh hết hạn, reconnect, queue chậm, handover | Postman/Newman, log/SQL, k6 nếu kiểm tra tải |
| AI test | Tiếng lóng, không dấu, đổi nhu cầu, nhiều sản phẩm, mỉa mai, phủ định, prompt injection | Golden conversations; field F1 và groundedness |

Fine-tune [TK]: train classifier PhoBERT/XLM-R khi có taxonomy ổn định và dataset đủ tốt; hoặc SFT LoRA cho extraction/format với input hội thoại và output gold. Tóm tắt đánh giá việc bỏ sót/đảo nghĩa, không chỉ ROUGE. RAG lấy chính sách; tool lấy giá tồn; fine-tune không giữ dữ liệu giao dịch cập nhật.

**AC:** khi khách đổi từ “mua” sang “hủy”, summary/next action phải căn cứ phiên bản hội thoại mới; output run cũ vẫn được giữ phục vụ audit nhưng không trở thành recommendation hiện hành.

**Cách kể:** “Tôi nhìn mChat như hệ thống điều phối công việc có trạng thái, người chịu trách nhiệm và SLA. Lớp AI chuyển hội thoại thành dữ liệu có cấu trúc để hỗ trợ agent; chất lượng phải đo bằng độ đúng của insight và hành động tiếp theo, không chỉ bằng câu trả lời trôi chảy.”

## 10. RPA & OCR kết hợp VLM

### Use case có căn cứ

**[HS]** CV và danh mục RPA nêu chứng từ XNK/hải quan/logistics, mua sắm và hợp đồng. Chọn ba luồng để kể sâu: (1) invoice–packing list–bill of lading → dữ liệu chuẩn; (2) đối soát contract–invoice–packing list → bảng chênh lệch; (3) hợp đồng → bản nháp và mốc thanh toán trong QLHĐ. RPA tra cứu lịch tàu là automation, không cần gán AI nếu không có bài toán nhận thức.

[Document AI và RPA có human review](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/05-document-ai-rpa.drawio.png>)

### Kiến trúc cụ thể [TK]

Upload/API/email connector → quarantine/ClamAV → MinIO raw → RabbitMQ job → OpenCV deskew/quality check → PaddleOCR + PP-Structure nhận chữ/bảng → extraction service → **Qwen2.5-VL-7B-Instruct** cho layout khó hoặc vùng cần xác minh → Pydantic schema + business validation → human review → **UiPath** robot hoặc API adapter → ERP/QLHĐ → audit/reconciliation. Không gửi cả file lại qua VLM nếu chỉ cần đọc một vùng, trừ khi cần ngữ cảnh trang.

OCR đọc ký tự; layout engine xác định vị trí/quan hệ; KIE ánh xạ thành trường; VLM hiểu ảnh và yêu cầu; RPA thực thi thao tác. **VLM không làm output thành chân lý**. Mỗi field quan trọng giữ page/bounding box, raw text, normalized value, extractor/model version và review status. Các công nghệ tham khảo: [PaddleOCR](https://www.paddleocr.ai/main/en/index.html), [Qwen2.5-VL model card](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct).

Với tiền tệ: parse theo locale và currency; kiểm tra tổng dòng, thuế, tổng chứng từ, rounding được nghiệp vụ duyệt. Số hợp đồng, mã hàng và ngày không dùng fuzzy matching tùy tiện. Gợi ý mã HS là hỗ trợ chuyên gia, không tự kê khai từ suy đoán model.

### Training và nhiệm vụ BA/QC

1. **Field dictionary:** BA chốt field bắt buộc, định dạng, đơn vị, decimal, nhiều trang, nhiều line item, quan hệ giữa chứng từ. Công cụ: Excel, SQL, OpenAPI; bàn giao mapping tới ERP/QLHĐ.
2. **Label dữ liệu:** tạo ground truth cho field/table/bounding box bằng Label Studio/CVAT; hai người review trường tiền/mã. Split theo nhà cung cấp/template và thời gian, có test template chưa từng gặp.
3. **Baseline và fine-tune:** đo PaddleOCR sẵn có; chỉ fine-tune recognizer khi lỗi ký tự có hệ thống. Cân nhắc LayoutLMv3 cho KIE nếu nhãn layout đủ tốt; LoRA VLM là nhánh riêng, không mặc định cần cả hai. BA/QC chọn coverage và adjudicate label; engineer train.
4. **Quality gate theo trường:** confidence do model tự nói không đủ; combine OCR confidence, format/rule checks và calibrated validator. Critical fields có xung đột phải review dù điểm chung cao.
5. **RPA contract:** checkpoint từng bước; API ưu tiên khi có; UI selector ổn định khi buộc dùng UI; credential qua vault; file đính kèm hash. BA đặc tả retry, timeout, human takeover.
6. **Nghiệm thu:** đo field exact match, table row alignment, tỷ lệ hồ sơ tự xử lý đúng, review rate, turnaround và duplicate posting. SQL đối soát số bản ghi/giá trị giữa extraction, review, ERP.

**AC quan trọng:** robot đã tạo hợp đồng nhưng mất mạng trước khi nhận kết quả → retry phải tra `external_reference/idempotency_key`; không tạo hợp đồng thứ hai. Nếu ứng dụng đích không hỗ trợ idempotency, cần sổ giao dịch và bước reconciliation trước retry.

**Cách kể:** “Tôi phân tích từ chứng từ đến dữ liệu đích và kiểm soát chỗ sai số có thể lan truyền. OCR/VLM là một công đoạn; đầu ra chỉ đủ điều kiện cho RPA khi qua schema, business rules và review cần thiết.”

## 11. Omnichannel CDP/CXP và CRM — một use case AI

### Next Best Action cho chăm sóc khách hàng [TK]

**[HS]** CV mô tả Customer 360, segmentation, journey, marketing và CRM. **[TK]** Use case cụ thể là gợi ý **một hành động chăm sóc phù hợp** trong tập hành động được phép: gửi hướng dẫn sử dụng, mời mua phụ kiện, nhắc dịch vụ hoặc không liên hệ. Không thêm chatbot/forecasting thành các use case riêng trong mục này.

**Input:** lịch sử mua đã hợp nhất, tương tác kênh có consent, sản phẩm đang sở hữu, ticket đang mở, tồn kho và frequency cap. **Output:** `action_id`, `channel`, `eligible`, `score`, `reason_codes`, `expires_at`; CXP chạy journey; nhân viên CRM thấy lý do và có thể bỏ qua.

### Kiến trúc và ML

Web/app/POS/CRM events → Kafka → CDP identity resolution và consent store → PostgreSQL/Data Lake → dbt feature pipeline → XGBoost propensity scoring → rule-based eligibility/ranking → CXP journey → mChat/email/SMS adapter → outcome về CDP. Model ước tính khả năng đáp ứng theo hành động; bộ policy loại hành động không được phép trước khi quyết định. Score propensity không phải causal uplift; muốn chứng minh tác động cần thí nghiệm.

Identity resolution bắt đầu bằng định danh deterministic đã xác thực; không tự merge hai khách chỉ vì giống tên. Features lấy trước thời điểm ra quyết định, tránh dùng phản hồi chiến dịch sau đó. Holdout theo customer và thời gian; sample negatives có định nghĩa; loại kết quả chưa đủ observation window.

### Công việc BA/QC

BA chốt business objective, action catalog, consent, suppression rule, attribution window, Customer 360 source-of-truth và tiêu chí doanh thu/lợi nhuận. Viết field mapping bằng SQL/dbt specification; vẽ journey bằng BPMN/draw.io; đặt backlog Jira và acceptance theo action.

QC tạo customer fixtures: opt-out, vừa mua, đang khiếu nại, trùng định danh, hết hàng, vượt cap, khách không lịch sử. Postman kiểm tra decision API; SQL đối soát audience trước/sau; dashboard Power BI kiểm tra phân phối score và kết quả. Model tốt nhưng gửi nhầm người hoặc vi phạm opt-out vẫn là lỗi chặn release.

**Thí nghiệm:** randomize theo customer đủ điều kiện, baseline rule-based vs ML policy; đo incremental conversion/profit, opt-out và complaint. Tính cỡ mẫu/độ dài theo baseline thực tế; không kết luận chỉ vì một tuần có doanh thu cao. Offline dùng PR-AUC/lift@k, online mới đánh giá tác động kinh doanh.

**Kế thừa VinDynamics:** phân quyền tenant/site, gói dịch vụ, hành trình khách hàng, ticket/SLA và adoption telemetry giúp thương mại hóa robot; không đưa danh tính người đi qua camera vào CDP marketing.

## 12. Samsung AI Data Hub: quản trị vòng đời AI

### Căn cứ và use case

**[HS]** Đây là dự án có căn cứ rõ nhất về workflow đào tạo và governance: CV trang 4–5 mô tả metadata, ownership, sensitivity, version, approval, training configuration, evaluation, promotion/rollback và lineage. [Feature description](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/AI Hub/AI Hub – System Feature Description.pdf>) và [BA làm gì](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/AI Hub/BA làm gì.docx>) bổ sung chi tiết.

AI Data Hub không nhất thiết tự có model dự đoán. Nó là **nền tảng để các đội xây và quản lý AI**. Ba use case chính: đăng ký/chia sẻ dataset; yêu cầu training và theo dõi run; đánh giá–phê duyệt–deploy model có truy vết. Không cần bịa thêm AI chatbot để gọi đây là dự án AI.

[AI Data Hub: governance và MLOps](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/07-ai-data-hub.drawio.png>)

### Kiến trúc đề xuất để giải thích implementation [TK]

React catalog → Spring Boot asset/workflow API → PostgreSQL metadata + MinIO artifacts → Camunda approval → Kubernetes Job/Argo Workflows chạy trainer → MLflow experiment/registry → evaluation runner → approval service → KServe deployment adapter → monitoring. Keycloak/OPA quản lý role/data scope. Tất cả tên công nghệ này là phương án minh họa; hồ sơ không xác nhận Samsung dùng stack này.

Tách trạng thái các entity: Dataset `Draft→Approved→Published→Deprecated`; TrainingJob `Queued→Running→Succeeded/Failed/Cancelled`; ModelVersion `Registered→Validated/Rejected`; Deployment `Pending→Active→RolledBack`. “Model đang Running” là diễn đạt mơ hồ nếu thực ra training job đang chạy. Runtime registry hiện đại dùng version/alias; business workflow có thể vẫn gọi môi trường staging/production.

### BA/QC và artifacts cụ thể

| Đầu việc | Quy tắc cần chốt | Deliverable/công cụ |
|---|---|---|
| Dataset/model templates | Required/optional field theo modality; owner/license/sensitivity/intended use | Data dictionary, JSON schema, Figma |
| Permission | Function + data scope + lifecycle; download/deploy khác quyền view | Permission matrix, negative cases; Postman/SQL |
| Approval | Conditional/parallel routing, approver động, delegate, reject/resubmit | BPMN, decision tables; Camunda Modeler |
| Training contract | Dataset/model version bất biến, code commit, image digest, seed, hyperparameters, resource quota | OpenAPI, run manifest, SRS |
| Evaluation | Benchmark version, metric slice, threshold, reviewer; không sửa kết quả cũ | Evaluation report, RTM, QC checklist |
| Promotion/rollback | Chỉ deploy artifact đã qua gate; compatibility và người duyệt | Release manifest, rollback scenario |
| Audit/lineage | Dataset source → version → run → model → evaluation → deployment | ERD/lineage diagram, SQL reconciliation |

**Test khó:** một dataset bị thu hồi quyền sau khi job đã queued. Hệ thống cần policy rõ: chặn job chưa chạy; job đang chạy xử lý theo quyết định được duyệt, artifact sinh ra không tự được publish. Không chỉ ẩn dataset khỏi catalog rồi coi là xong.

**Test race:** hai người approve cùng request; owner sửa config trong khi chờ duyệt; callback job gửi lặp; GPU hết tài nguyên; train fail giữa chừng; model đạt metric tổng nhưng fail tập ngoại lệ. QC kiểm tra trạng thái, audit, resource cleanup và kết quả hiển thị.

**Cách kể:** “Ở AI Hub, tôi chuẩn hóa quan hệ giữa dataset, model, training job, evaluation và deployment. Tôi thiết kế người nào được làm gì ở từng trạng thái, điều gì cần phê duyệt, và làm sao truy ngược một model production đến dữ liệu và kết quả đánh giá. Đó là kinh nghiệm MLOps ở góc độ BA hệ thống và governance.”

## 13. Samsung Smart Factory — hai use case Machine Learning trên Azure

### Căn cứ và phạm vi mở rộng

**[HS]** CV trang 4–5 có equipment hierarchy, monitoring/log/alarm, maintenance/OEE, WMS, QMS và ERP mapping. **[TK]** Azure, hai ML use case và AMR/fleet bên dưới là giải pháp bổ sung theo yêu cầu; chưa có bằng chứng Đức đã triển khai Azure hay fleet robot tại Samsung. Kinh nghiệm fleet tracking được CV nhắc trực tiếp ở **V-Tracking**, có thể dùng làm bằng chứng bổ trợ nhưng không tráo thành Smart Factory.

[Smart Factory trên Microsoft Azure](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Sơ đồ kiến trúc/06-smart-factory-azure.drawio.png>)

### 13.1. Kiến trúc Microsoft Cloud cụ thể [TK]

| Lớp | Công nghệ | Thiết kế và trách nhiệm |
|---|---|---|
| Máy/OT | PLC, sensor, OPC UA server; adapter Modbus khi cần | Chuẩn hóa tag, timestamp, unit, machine ID; inventory trước khi chọn connector |
| Edge | Industrial PC chạy .NET/Python OPC UA client, Docker; SQLite buffer | Làm sạch, aggregate, inference cục bộ; tách mạng OT; không đưa vòng điều khiển máy lên cloud |
| Device identity | Azure IoT Hub Standard, Device Provisioning Service, X.509 | Onboarding, credentials theo thiết bị; revoke/rotate certificate |
| State/config | IoT Hub device twins | Desired config và reported applied version; ACK không đồng nghĩa đã đạt trạng thái mong muốn |
| Ingestion | IoT Hub routing → Event Hubs → Stream Analytics | Xử lý stream, event-time/window, lateness, dedupe nghiệp vụ |
| Storage | ADLS Gen2 raw/curated; Azure Data Explorer telemetry; Azure SQL nghiệp vụ | Raw bất biến; time-series truy vấn nhanh; transactional master/work order |
| ML | Azure ML pipelines, compute, registry, managed endpoints; MLflow | Train/evaluate/register; batch scoring hoặc online theo nhu cầu |
| Application | ASP.NET Core trên Azure Container Apps; API Management; Service Bus | Equipment/maintenance/QMS API; hàng đợi công việc và DLQ |
| Observability/security | Azure Monitor, Application Insights, Log Analytics; Entra ID, Key Vault, private endpoints | Theo dõi pipeline/device/model; phân quyền OT/IT/site và audit |
| Delivery | Azure DevOps, Azure Container Registry | CI/CD image/config/model manifest; rollout theo site và rollback |
| Reporting | Power BI | OEE, downtime, alarm, chất lượng, bảo trì và hiệu quả ML |

IoT Hub device twins có desired/reported properties phục vụ đồng bộ cấu hình; chúng không phải bản mô phỏng 3D của nhà máy. Azure ML hỗ trợ pipeline/registry/lineage trong MLOps. [Device twins](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins), [Azure ML MLOps](https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2).

Thiết kế này chủ động dùng gateway container để tránh gắn toàn bộ giải pháp vào một runtime edge chưa kiểm tra vòng đời hỗ trợ. Khi lựa chọn Azure IoT Operations hoặc IoT Edge cần xác minh license, phần cứng, hỗ trợ và roadmap tại thời điểm triển khai. ADLS, ADX, SQL có thể giảm bớt ở pilot; đây là phân lớp theo nhu cầu, không bắt buộc mua đủ mọi dịch vụ.

### 13.2. Use case ML số 1: bảo trì dự đoán

**Bài toán:** dự đoán nguy cơ lỗi máy trong 7 ngày để lên lịch kiểm tra. Input gồm vibration RMS/kurtosis, nhiệt độ, dòng điện, operating hours, alarm history, load và maintenance history. Output `failure_risk`, `time_horizon`, `reason_codes`, `recommended_inspection`, `valid_until`; chưa đủ nhãn lỗi thì dùng anomaly detection và gọi đúng tên.

Pipeline: sensor → edge aggregation → IoT Hub/Event Hubs → ADX/ADLS → feature windows → Azure ML train **XGBoost** supervised nếu nhãn đủ; **IsolationForest** làm baseline phát hiện bất thường khi thiếu nhãn → endpoint/batch prediction → maintenance API → work order chờ kỹ thuật viên xác nhận. Không tự dừng máy chỉ vì score ML cao; interlock vận hành là hệ riêng.

**BA:** định nghĩa failure event, downtime planned/unplanned, cửa sổ dự báo, lead time hữu ích, năng lực đội bảo trì; làm mapping mã lỗi từ PLC sang taxonomy nghiệp vụ; phân biệt “đã bảo trì” với “đã hỏng”. Công cụ: SQL, Excel, draw.io, Jira, Power BI; đầu ra feature dictionary, label guide và maintenance workflow.

**QC/dữ liệu:** chia tập theo máy và thời gian; tránh leakage từ repair code sau sự cố; kiểm tra đơn vị °C/°F, timestamp lệch, sensor bị kẹt một giá trị, missing và overload. Đo precision/recall event, cảnh báo giả/machine-day, lead time và tỷ lệ phát hiện trước hỏng; báo cáo từng machine family. Nếu đổi loại máy phải kiểm tra domain shift, không dùng threshold cũ mặc định.

**Training contribution:** BA/QC curate lịch sử lỗi, liên kết sensor snapshot với incident/work order, adjudicate label với bảo trì; engineer chạy train; QC so baseline và candidate trên holdout theo thời gian, rồi shadow trước khi dùng để tạo đề xuất.

### 13.3. Use case ML số 2: phát hiện lỗi ngoại quan trên dây chuyền

**Bài toán:** phát hiện thiếu linh kiện, trầy xước hoặc sai lắp ráp theo SKU/công đoạn. Input ảnh camera công nghiệp + `lot_id`, `serial_no`, `station_id`, `recipe_version`; output defect class, bounding box/mask, confidence, evidence image và disposition đề xuất.

Pipeline: camera trigger → edge preprocess → **YOLOX** detection cho lỗi có đủ nhãn; **PatchCore trong anomalib** là phương án khi chủ yếu có mẫu tốt → ONNX Runtime/TensorRT inference → QMS API → người kiểm tra xác nhận rework/scrap/release → dữ liệu label đưa về ADLS/Azure ML. Recipe version và lighting setup phải đi cùng model compatibility; không phát hành một model cho mọi SKU chỉ vì cùng camera. Tham khảo thư viện [anomalib](https://github.com/open-edge-platform/anomalib) để khảo sát phương án anomaly detection; cần benchmark trên lỗi nhỏ và độ phân giải ảnh thực tế.

**BA:** định nghĩa defect taxonomy, mức độ, sampling policy, traceability lot–machine–material, quyền override và thời hạn re-inspection. **QC:** gán nhãn CVAT, dùng holdout theo lot/ca/SKU; đo false accept (lỗi lọt) và false reject (hàng tốt bị loại), latency so với takt time, ảnh thiếu/trigger lệch và lỗi ánh sáng. Python/OpenCV, SQL/ADX, CVAT, Azure ML/MLflow, Postman là bộ công cụ đề xuất.

Test khi serial scan thất bại phải đưa sản phẩm vào trạng thái chờ xử lý/luồng được phê duyệt, không gán ảnh sang sản phẩm kế tiếp. Test mất mạng: lưu local queue cùng ID/hash; đồng bộ lại không tạo duplicate inspection. Test camera hỏng: health fault phải phân biệt với “không phát hiện lỗi”.

### 13.4. Device health, cấu hình, logging và release

Health gồm connectivity, sensor freshness, data quality, CPU/GPU temperature, storage, clock skew và model runtime; online chưa chắc healthy. Heartbeat và observed telemetry tách riêng. Monitor tuổi dữ liệu theo event time; buffer giới hạn dung lượng/retention; ưu tiên alarm, kiểm soát replay và backpressure.

Configuration có `config_version`, desired/reported, actor và approved_at; deployment manifest liên kết firmware, adapter, model, feature schema và recipe. Edge chỉ nhận artifact ký/hash đúng và tương thích; rollout một máy test → một line → một site; rollback cả model và preprocessing khi cần. Thông số tần suất/timeout do measurement và vận hành chốt, không lấy số giả làm cam kết.

### 13.5. Fleet management kế thừa được gì?

Từ equipment hierarchy suy ra `site–zone–robot–component`; availability/maintenance chuyển thành ready/degraded/out-of-service; work order/SLA chuyển thành mission/incident; lot traceability chuyển thành mission evidence chain. Nếu thêm AMR, dùng fleet adapter/Open-RMF để nghiên cứu điều phối tuyến và chia sẻ tài nguyên; đây là **mở rộng**, không thuộc hai use case ML trên và không chứng minh kinh nghiệm humanoid locomotion.

**Cách kể:** “Tôi đã làm equipment, monitoring, maintenance, quality và ERP integration trong Smart Factory. Nếu mở rộng lên Azure và ML, tôi có thể thiết kế data contract từ sensor tới feature, làm rõ nhãn lỗi và quy trình nhận cảnh báo, rồi nghiệm thu cả model lẫn end-to-end. Đây cũng là nền tảng để tiếp cận device health và fleet operations.”

## 14. Đối chiếu JD VinDynamics và chuẩn bị bảo vệ kinh nghiệm

JD đặt trọng tâm vào yêu cầu rõ ràng, tích hợp, phối hợp phát triển, truy vết, UAT/field feedback và phân định trách nhiệm. Bảng dưới là mapping riêng từ hồ sơ và phương án chuẩn bị, không phải trích nguyên văn JD. [JD Senior Business Analyst](https://vindynamics.net/vi/career/senior-business-analyst-001114.html).

| Năng lực cần thể hiện | Ví dụ mạnh nhất | Artifact nên đem kể |
|---|---|---|
| Discovery, AS-IS/TO-BE, constraint | Smart Safe, một cửa, Smart Factory | Workshop note, use-case map, assumption log |
| User story/FR/NFR/AC | HRAI, mChat, Copilot | Một story có Gherkin và ngoại lệ đo được |
| API, data flow, state, fallback | Smart Safe, VPHC, OCR | Sequence + payload + state transition + error table |
| AI evaluation | HRAI, OCR, một cửa | Gold schema, rubric, confusion/error analysis |
| Agile daily collaboration | CV Viettel/Samsung | Story refinement, clarification log, demo acceptance |
| Change/traceability/baseline | AI Hub, chính phủ | Requirement → story → test → result → release |
| UAT/production verification | Smart Safe, OCR, AI products trong CV | UAT report, defect triage, re-validation |
| Cross-functional ownership | Lead BA, PO trong CV | RACI, trade-off và quyết định được ghi lại |
| SQL/logs/Jira/Confluence/English | CV skills; làm việc HQ Korea | Một query, một trace và lời giải thích tiếng Anh |
| Robotics/ROS2/HRI/robot safety | Kiến thức và case ở file thứ hai | Nêu rõ phần đang chuyển đổi ngành; không tự nhận đã vận hành humanoid |
| Edge/cloud/config/release | Smart Safe/Factory; Azure đề xuất | Online ≠ healthy, desired ≠ applied, rollback manifest |

**Điểm cần nói chính xác về số năm:** CV tự mô tả 5 năm kinh nghiệm và có vai trò BA từ 02/2023; theo mốc 16/11/2026, riêng giai đoạn ghi chức danh BA từ 02/2023 chưa tròn 4 năm. Giai đoạn 2020–2023 là developer. Nếu muốn chứng minh yêu cầu 4+ năm BA/Technical BA/System Analyst, cần chỉ ra công việc phân tích hệ thống thực tế trong giai đoạn developer; không đổi tên chức danh hoặc cộng năm không giải thích. Điều kiện 2+ năm tích hợp nên bảo vệ bằng dự án và thời gian cụ thể.

### Các câu hỏi dễ bị hỏi sâu

1. **Anh tự train gì?** Trả theo model/task đã thực làm; nếu chỉ dữ liệu/QA thì nêu đúng phạm vi, artifact và phối hợp engineer. Với model chưa xác nhận, dùng “phương án tôi đề xuất là…”.
2. **Tại sao RAG chứ không fine-tune?** Tri thức cần cập nhật, provenance, hiệu lực và ACL phù hợp retrieval; fine-tune phục vụ hành vi/format/task khi có dữ liệu và bằng chứng cần thiết.
3. **Model đúng 95% nghĩa là gì?** Hỏi metric, unit, dataset/split, thời gian, lớp hiếm, confidence interval và cost of error. Không dùng một tỷ lệ không định nghĩa.
4. **PASS có tự thành training sample?** Không; cần gold review, nguồn, dedupe, quyền sử dụng và split; tránh model tự củng cố sai sót.
5. **Tại sao AI trả đúng nhưng test vẫn fail?** Có thể sai quyền, stale state, tool ghi trùng, citation sai hoặc latency ngoài yêu cầu.
6. **Model production bị lỗi thì rollback gì?** Model/adapter, prompt, preprocessing, index, policy và API compatibility theo manifest; không chỉ đổi file weights.
7. **Anh làm khác AI Engineer thế nào?** Tôi sở hữu requirement/data semantics/evaluation và bằng chứng chất lượng; engineer sở hữu implementation/thuật toán/hạ tầng chuyên sâu; Tech Lead chốt HOW.
8. **Tori anh đã làm thật chưa?** Chưa; đây là case nghiên cứu bám JD để hệ thống hóa cách làm BA/QC. Không sử dụng bản nhập vai như lịch sử công tác.

### Danh mục nguồn nội bộ để truy ngược

| Mã | Nguồn | Cách dùng |
|---|---|---|
| S01 | [CV full](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Kim Đức CV full.pdf>) và [CV rút gọn](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Kim Đức CV rút gọn.pdf>) | Vai trò, thời gian, phạm vi và kỹ năng tự khai |
| S02 | [Danh sách 10 dự án](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án có AI tôi đã tham gia.txt>) | Phạm vi bắt buộc của tài liệu |
| S03 | [JD BA & QA](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Tori AI/JD_TechcomBank.pdf>) | Trách nhiệm công việc tham khảo; không phải bằng chứng đã tham gia |
| S04 | [Use cases TCLife](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Tori AI/0. Usecases TCLife.pdf>) | Nguồn nghiên cứu; đã phân biệt công bố và suy luận |
| S05 | [Luồng Training HRAI](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Phỏng vấn/2. Luồng Training AI HRAI.pdf>), [Cách làm BA-QA](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Phỏng vấn/Cách làm BA-QA HRAI.pdf>) | Tham khảo feature, snapshot, feedback; không coi giả định stack là thực tế |
| S06 | [AI Hub feature description](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/AI Hub/AI Hub – System Feature Description.pdf>) | Lifecycle, governance, training/evaluation workflow |
| S07 | [mChat SRS](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Projects VCM/mChat/VSS mChat SRS.docx>), [sáng kiến](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Projects VCM/mChat/mChat_Dương đăng ký sáng kiến ý tưởng.docx>) | Tách nền tảng hiện hữu với phần AI đề xuất |
| S08 | [RPA use cases](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Projects VCM/RPA usecases.docx>) | Nghiệp vụ chứng từ, logistics, hợp đồng |
| S09 | [Tổng hợp tính năng và BA](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Các dự án cũ/Dự án và tính năng/Danh_muc_tinh_nang_va_7_cong_viec_BA_Viettel_Samsung.docx>) | Nguồn tổng hợp phụ; đối chiếu với CV và tài liệu gốc |
| S10 | [Kiến trúc RPA OCR tham khảo](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/ChatGPT/Kiến trúc dự án RPA OCR.md>) | Thiết kế bổ sung, không chứng nhận triển khai |

Xem tiếp [Đức PO làm dự án VinDynamics](<C:/Users/nguye/OneDrive/Desktop/Phỏng vấn VinDynamics/Đức PO làm dự án VinDynamics.md>) để chuyển các năng lực trên sang case đội robot an ninh VinUni.
