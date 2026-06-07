CREATE DATABASE IF NOT EXISTS monitor_db;
USE monitor_db;

CREATE TABLE IF NOT EXISTS realtime_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_name VARCHAR(50),
    value FLOAT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tạo sẵn một dòng để Node-RED cập nhật và API đọc
INSERT INTO realtime_data (data_name, value) VALUES ('gold_price', 0.0);