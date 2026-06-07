
# 📊 Hệ thống Giám sát Real-time (Bài tập 5)

**Sinh viên:** Đặng Đình Đạt

---

## 🛠 Kiến trúc hệ thống
Hệ thống sử dụng **Docker Compose** để quản lý 6 dịch vụ hoạt động song song:
1. **Node-RED:** Điều phối, thu thập và xử lý luồng dữ liệu.
2. **MariaDB:** Lưu trữ giá trị tức thời (`realtime_data`).
3. **InfluxDB:** Lưu trữ chuỗi thời gian (`history_db`).
4. **Grafana:** Trực quan hóa dữ liệu lịch sử.
5. **Backend API (Flask):** Cung cấp dữ liệu cho Web qua RESTful API.
6. **Frontend (Nginx/HTML/JS):** Hiển thị dashboard.



[Image of system architecture diagram]


---

## 📋 Quy trình triển khai (Các bước thực hiện)

### Bước 1: Thiết lập môi trường (Docker)
- Định nghĩa file `docker-compose.yml` liên kết toàn bộ các container và mạng nội bộ (`network`).
- Tạo `Dockerfile` và `requirements.txt` để đóng gói Backend API.

### Bước 2: Xử lý dữ liệu (Node-RED)
- Tạo flow thu thập dữ liệu từ Binance API mỗi 5 giây.
- Phân luồng dữ liệu:
  - Cập nhật vào MariaDB.
  - Ghi lịch sử vào InfluxDB.
  - Gửi cảnh báo Telegram nếu giá vượt ngưỡng an toàn.

### Bước 3: Trực quan hóa (Grafana)
- Kết nối InfluxDB làm Data Source.
- Xây dựng biểu đồ Time-series giám sát biến động giá theo thời gian thực.

### Bước 4: Xây dựng Bot Telegram
- Cấu hình Bot qua `@BotFather`.
- Lập trình logic kiểm tra ngưỡng giá trong Node-RED để gửi thông báo khẩn cấp đến Group Chat.

### Bước 5: Phát triển Web Dashboard
- **Backend:** Python Flask API lấy dữ liệu từ MariaDB.
- **Frontend:** HTML/JavaScript sử dụng `fetch()` để cập nhật con số tức thời.
- **Tích hợp:** Nhúng biểu đồ Grafana tràn viền vào Web bằng `iframe`.

### Bước 6: Triển khai
- Chạy lệnh: `docker-compose up -d --build` để khởi động toàn bộ hệ thống.

---

## 💡 Lý thuyết Docker
- **Docker là gì?** Là nền tảng đóng gói ứng dụng vào **Container**, đảm bảo phần mềm chạy ổn định trên mọi môi trường.
- **Ưu điểm:** Nhất quán môi trường, tiết kiệm tài nguyên, triển khai tự động.
- **Triển khai máy chủ Offline:**
  1. `docker save`: Lưu image thành file `.tar`.
  2. Copy file `.tar` và mã nguồn sang máy chủ.
  3. `docker load`: Tải image từ file nén.
  4. `docker-compose up -d`: Khởi chạy hệ thống.

---

## 📸 Kết quả
* Hệ thống đã hoạt động hoàn hảo, hiển thị số liệu tức thời và cảnh báo Telegram ổn định.
* Mã nguồn và cấu hình đã được kiểm tra trên môi trường Docker.
