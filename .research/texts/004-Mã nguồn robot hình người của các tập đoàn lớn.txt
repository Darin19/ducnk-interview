**You:**

NVIDIA hay Microsoft hay một bên nào đó có mã nguồn mở về Robot hình người không?

* * *

**ChatGPT:**

**Có. Đặc biệt, NVIDIA đã công bố mã nguồn mở cho nền tảng phát triển robot hình người (Humanoid Robotics), bao gồm mô hình AI, công cụ mô phỏng, huấn luyện và điều khiển robot.**

Không chỉ NVIDIA, các tổ chức như Stanford, UC Berkeley, Hugging Face và cộng đồng ROS cũng có những dự án rất đáng nghiên cứu.

Điểm thú vị là **bạn hoàn toàn có thể lấy các nền tảng này làm cơ sở để phát triển robot bảo vệ, robot phục vụ, robot nhà máy**, thay vì tự xây dựng mọi thứ từ đầu.

Tuy nhiên, cần phân biệt ba mức độ mở:

- **Open-source Hardware:** Bản thiết kế cơ khí, linh kiện, mạch điện và cấu tạo robot.
- **Open-source Robotics Software:** Phần mềm điều khiển vận động, cảm biến, di chuyển, thao tác tay và phối hợp các thành phần.
- **Open-source Robot AI:** Mô hình AI giúp robot hiểu hình ảnh, ngôn ngữ, học kỹ năng và tạo ra hành động vật lý.

Một dự án mở cả phần cứng lẫn phần mềm sẽ khác rất nhiều so với dự án chỉ công bố mô hình AI.

## 1. NVIDIA — Isaac GR00T

![NVIDIA Isaac GR00T Reference Humanoid Robot for Frontier Research | Amit Goel posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/_b7ByLJxmQJJgkDcOBFCXSASbp0uzD4Hj1bMWSNsqf2iLkhMvlGseHUsgJKCyKYIDxZQ89A68IufOn1gX0BhZYmqPHXGrk95QNpk_kJ6ImOhSSuIfWuJWws6nxpsOie90koNExnHFK9sMVZ_2DCEEb3mNbqT1YaNzFIyexPmn4Y?purpose=inline) · NVIDIA Isaac GR00T

(Có mã nguồn công khai)

Đây là một trong những lựa chọn đáng nghiên cứu nhất nếu bạn muốn xây dựng phần mềm và AI cho robot hình người.

NVIDIA công bố nền tảng phát triển GR00T và một thiết kế robot tham chiếu trong năm 2026. 

[NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design?utm_source=chatgpt.com) · [NVIDIA Technical Blog](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/?utm_source=chatgpt.com)

NVIDIA cung cấp những thành phần chính:

| Công nghệ | Chức năng |
| --- | --- |
| **Isaac GR00T** | Mô hình Vision-Language-Action (VLA), biến quan sát và chỉ dẫn thành hành động robot |
| **Isaac Sim** | Mô phỏng robot, cảm biến và môi trường 3D |
| **Isaac Lab** | Huấn luyện kỹ năng bằng Reinforcement Learning, Imitation Learning |
| **Isaac ROS** | Các thành phần xử lý cảm biến, nhận thức và tăng tốc AI trong hệ ROS |
| **Jetson Thor** | Phần cứng tính toán AI đặt trực tiếp trên robot |

Đáng chú ý, GR00T có mã nguồn theo Apache 2.0 và trọng số mô hình theo NVIDIA Open Model License. Hai loại giấy phép này không giống nhau. 

[GitHub](https://github.com/NVIDIA/Isaac-GR00T?utm_source=chatgpt.com)

Các kho mã nguồn:

[NVIDIA Isaac GR00T – GitHub](https://github.com/NVIDIA/Isaac-GR00T?utm_source=chatgpt.com)

[NVIDIA Isaac Lab – GitHub](https://github.com/isaac-sim/IsaacLab?utm_source=chatgpt.com)

[NVIDIA Isaac Sim – GitHub](https://github.com/isaac-sim/IsaacSim?utm_source=chatgpt.com)

Đối với bài toán VinUni, NVIDIA đặc biệt hữu ích ở phần **AI Vision, học kỹ năng vận động, thao tác tay, mô phỏng tình huống và điều khiển robot**, nhưng chưa tự động cung cấp một hệ thống quản lý đội robot bảo vệ hoàn chỉnh.

## 2. Stanford — ToddlerBot: Robot hình người mã nguồn mở

![ToddlerBot Bundle Kit - ROBOTIS](https://images.openai.com/static-rsc-4/pThVrNFaGHAAAnR2ZxQjrlufvOfEsUNoAkxH2Ml-QC6LKPOE4lb8ehoy8SVmRdemWbHLBbv9ffD-MpdjT3m2AIKDzyxmmAtVJRcsM-J7obJiWih_iUmeZbDcQImaTB3_1DgIz9a-FBmLccAWh3923ur7FOMLvvZgPCBf-SNvGBk?purpose=inline) · **

ToddlerBot

**

Đây là dự án rất phù hợp nếu muốn hiểu cách chế tạo và lập trình một robot hình người từ những thành phần cơ bản.

[Mã nguồn ToddlerBot](https://github.com/hshi74/toddlerbot?utm_source=chatgpt.com)

[Demo, tài liệu và video](https://toddlerbot.github.io/?utm_source=chatgpt.com)

Stanford công bố cả thiết kế phần cứng, phần mềm điều khiển và mã huấn luyện, phục vụ nghiên cứu robot đi bằng hai chân và thao tác đồ vật. 

[toddlerbot.github.io](https://toddlerbot.github.io/?utm_source=chatgpt.com) · [hshi74.github.io](https://hshi74.github.io/?utm_source=chatgpt.com)

Bạn có thể nghiên cứu cách robot giữ thăng bằng, điều khiển khớp, phối hợp hai tay, học động tác bằng mô phỏng rồi triển khai trên robot thật.

**Lưu ý:** Phần mềm và bản thiết kế phần cứng có giấy phép khác nhau; thiết kế ToddlerBot có hạn chế sử dụng thương mại. 

[GitHub](https://github.com/stephane-caron/awesome-open-source-robots/blob/main/README.md?utm_source=chatgpt.com)

## 3. Các dự án mã nguồn mở đáng chú ý khác

![New Model Every Four Months: China's Humanoid Robot Speed Race - Seoul Economic Daily](https://images.openai.com/static-rsc-4/Nxi-nqgImYnpNsUEvEauOG4oXWf1jNFMtbJTUgo8xsUQAT6w9GFAwLUIbCr9eKGPOVRk_mko2Uvxh_pg_-xhjGhUnTYgOfS5DIOchf3y6igy4JCB9cBZ3svF8WD5YiwDQRdbfdxse-avmU7p0-kYnmy80Rj7Ykio7nCcO67ohMs?purpose=inline) · **OpenLoong — Trung Quốc**

Có thiết kế phần cứng và mã điều khiển động lực học toàn thân, sử dụng MPC và Whole-Body Control. Phù hợp nghiên cứu robot đi bộ, giữ cân bằng, vượt vật cản. 

[GitHub](https://github.com/loongOpen/openloong-dyn-control?utm_source=chatgpt.com)

[OpenLoong GitHub](https://github.com/loongOpen?utm_source=chatgpt.com)

---

![Unitree G1 Humanoid Robot | Roboworks AU (Reserved)](https://images.openai.com/static-rsc-4/Xnfai_-FzmDHfX01QIScGL6cDNHjRGOSwPOjovUq46RTdBKo0la4rHpppes8rZqfMmBrSNRcYVBH9XvfyKE3ygX-nQheINn9ZpFdmXFbHshsYhvJvSWnDM114R5kheeVdmaIvvWtDXUW7ehoPX0VnnlIyVo3fV3Zw6w81jP2LAU?purpose=inline) · **Unitree G1 — Robot thương mại có SDK công khai**

Unitree công khai SDK, giúp nhà phát triển kết nối robot và xây dựng ứng dụng. Tuy nhiên, **có SDK không đồng nghĩa toàn bộ firmware, bộ điều khiển và thiết kế phần cứng đều mở**.

[Unitree SDK2](https://github.com/unitreerobotics/unitree_sdk2?utm_source=chatgpt.com) 

[GitHub](https://github.com/unitreerobotics/unitree_sdk2?utm_source=chatgpt.com)

---

![ROBOTIS OP3](https://images.openai.com/static-rsc-4/18OlroL5Ww_RW4NBOAz-X5uyJsD55ZWQLH3U83VvLPwEvqzchzqN7S7d1p5sxxpVuJTP0IBqm1sUlNl2DsV17Hgo1ulzX04g8ZzIT1DAeolQGmltooGMe3wWA_LyX2AQoR3ynsRUGTn4uZ_ECqVb1dmKnA_rtDNPLQMnv3AE6Ps?purpose=inline) · **ROBOTIS — OP3 / AI Sapiens**

Có các gói ROS phục vụ mô tả robot, bộ điều khiển, giao tiếp phần cứng và mô phỏng. Phù hợp học kiến trúc robot dựa trên ROS. 

[GitHub](https://github.com/ROBOTIS-GIT/ai_sapiens?utm_source=chatgpt.com)

[ROBOTIS OP3](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3?utm_source=chatgpt.com)

[AI Sapiens ROS 2](https://github.com/ROBOTIS-GIT/ai_sapiens?utm_source=chatgpt.com)

---

![🤖 Poppy Humanoid・Free STL File for ・Cults](https://images.openai.com/static-rsc-4/THwEH87ugD_f1ShgPaImt-3uUuRvk0_lXJhxNTlB2BUbMRDoIzEni6FqZ822r2GWqaWy2ev1x6Fhr0ul8Wf08ONw1YPgEGVDiu6N1JF6ypoOlOi3aDchVq_iEUMnMW0KfAcpdy6rd67zT9_u83oRV-ZhVdQ-XouIRX6aqv4Ax0Y?purpose=inline) · **HOPEJr — TheRobotStudio**

Dự án robot hình người DIY có mô hình URDF, thiết kế cơ khí, bàn tay linh hoạt và tích hợp hệ thống thu thập dữ liệu/teleoperation với LeRobot. 

[GitHub](https://github.com/TheRobotStudio/HOPEJr?utm_source=chatgpt.com)

[HOPEJr GitHub](https://github.com/TheRobotStudio/HOPEJr?utm_source=chatgpt.com)

## 4. Hugging Face và Microsoft thì sao?

**Hugging Face — LeRobot**

Đây là bộ công cụ AI Robotics mã nguồn mở rất đáng tìm hiểu. LeRobot cung cấp giao diện để kết nối nhiều loại robot, thu thập dữ liệu, huấn luyện chính sách hành động và đánh giá mô hình. Kho mã hiện hỗ trợ cả Unitree G1, HOPEJr và nhiều nền tảng khác. 

[GitHub](https://github.com/huggingface/lerobot?utm_source=chatgpt.com)

[Hugging Face LeRobot](https://github.com/huggingface/lerobot?utm_source=chatgpt.com)

**Microsoft — Có dự án Robotics mở, nhưng không phải lựa chọn hàng đầu cho humanoid full-stack**

Microsoft có [Applied Robotics Research Library](https://github.com/microsoft/AppliedRoboticsResearchLibrary?utm_source=chatgpt.com) về service robotics, HRI, navigation và các thiết kế tham chiếu. Ngoài ra còn [AirSim](https://github.com/microsoft/AirSim?utm_source=chatgpt.com), tập trung chủ yếu vào mô phỏng drone và xe tự hành. 

[GitHub](https://github.com/microsoft/AppliedRoboticsResearchLibrary?utm_source=chatgpt.com) · [GitHub](https://github.com/Microsoft/AirSim?utm_source=chatgpt.com)

Tôi chưa tìm thấy ở Microsoft một nền tảng humanoid mã nguồn mở có phạm vi tương đương NVIDIA Isaac GR00T. Nếu mục tiêu là phát triển robot hình người, nên ưu tiên NVIDIA, ROS2 và các dự án chuyên biệt hơn.

## 5. Nếu xây dựng đội robot bảo vệ VinUni thì nên dùng gì?

Tôi đề xuất một kiến trúc kết hợp mã nguồn mở, thay vì chọn duy nhất một hãng.

**Security Business Application**

Tuần tra · Xác minh sự cố · Hội thoại · Xử lý incident

Phát triển theo nghiệp vụ VinUni

↓

**Open-RMF + Mission Engine**

Điều phối robot · Phân nhiệm vụ · Quản lý đội robot

↓

**NVIDIA GR00T / LeRobot**

AI, thị giác, học và tạo hành động

**ROS2 + Robot Controllers**

Điều khiển khớp, cảm biến, di chuyển, kỹ năng

↓

**Robot Hardware**

Robot hình người, camera, LiDAR, microphone, động cơ

Kiến trúc đề xuất, không phải giải pháp đã được tích hợp sẵn hoặc kiến trúc được xác nhận của VinDynamics.

Trong đó, [Open-RMF](https://github.com/open-rmf/rmf?utm_source=chatgpt.com) là một dự án mã nguồn mở chuyên về quản lý nhiều đội robot. 

[GitHub](https://github.com/open-rmf/rmf?utm_source=chatgpt.com)

 Phần lớn quy trình an ninh, kết nối Camera AI và xử lý sự cố vẫn phải phát triển thêm.

### Bảng lựa chọn theo mục tiêu

| Muốn nghiên cứu | Nên bắt đầu |
| --- | --- |
| AI điều khiển robot hình người | **NVIDIA GR00T** |
| Mô phỏng và huấn luyện robot | NVIDIA Isaac Sim + Isaac Lab |
| Thiết kế cơ khí, nguyên lý điều khiển | Stanford ToddlerBot / OpenLoong |
| Thu thập dữ liệu, học hành động | Hugging Face LeRobot |
| Kết nối phần mềm với robot thật | ROS2 + Unitree SDK hoặc SDK nhà sản xuất |
| Quản lý, điều phối nhiều robot | Open-RMF |
| Xây dựng nghiệp vụ an ninh | Custom Mission Engine + Security Pack |

**Điều quan trọng nhất:** Chưa có một kho mã nguồn mở nào trong những dự án trên mà chỉ cần tải về là có ngay đội robot bảo vệ VinUni hoạt động hoàn chỉnh. AI điều khiển cơ thể, quản lý đội robot và nghiệp vụ bảo vệ vẫn là những lớp riêng cần tích hợp, kiểm thử an toàn và tùy biến.

Với góc nhìn Senior BA, tôi khuyên bạn tìm hiểu **NVIDIA Isaac GR00T + ROS2 + Open-RMF** trước. Bộ ba này giúp bạn hình dung rõ sự khác biệt giữa *robot biết hành động*, *robot thực thi hành động* và *nền tảng giao nhiệm vụ cho nhiều robot* — nền tảng để xây dựng một hệ thống Robotics phục vụ đa ngành.