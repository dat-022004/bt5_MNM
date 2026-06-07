function fetchRealtimeData() {
    // Gọi API từ Flask backend (đang chạy ở port 5000)
    fetch('http://localhost:5000/api/current-data')
        .then(response => response.json())
        .then(data => {
            if (data.value !== undefined) {
                // Cập nhật số liệu mới lên web
                document.getElementById('realtime-value').innerText = data.value;
            } else {
                document.getElementById('realtime-value').innerText = 'Lỗi dữ liệu';
            }
        })
        .catch(error => {
            console.error('Lỗi khi lấy dữ liệu API:', error);
            document.getElementById('realtime-value').innerText = 'Chờ API kết nối...';
        });
}

// Lấy dữ liệu ngay lần đầu tiên mở web
fetchRealtimeData();

// Thiết lập tự động gọi lại hàm trên mỗi 2 giây (2000 ms)
setInterval(fetchRealtimeData, 2000);