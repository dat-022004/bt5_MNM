from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='mariadb', # Tên service trong docker-compose
        user='root',
        password='rootpassword',
        database='monitor_db',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/current-data', methods=['GET'])
def get_current_data():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            # Lấy giá trị tức thời của gold_price
            cursor.execute("SELECT value FROM realtime_data WHERE data_name='gold_price'")
            result = cursor.fetchone()
        conn.close()
        
        # BỌC LÓT AN TOÀN: Kiểm tra xem DB đã có dữ liệu chưa
        if result is not None:
            val = result['value']
        else:
            val = 0 # Nếu rỗng thì tạm trả về 0 để web không chết
            
        # Cho phép CORS đơn giản để Nginx có thể gọi được bằng AJAX
        response = jsonify({'value': val})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    except Exception as e:
        # Quan trọng: Gắn cả CORS vào thông báo lỗi để Cốc Cốc đọc được
        err_response = jsonify({'error': str(e)})
        err_response.headers.add('Access-Control-Allow-Origin', '*')
        return err_response, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)