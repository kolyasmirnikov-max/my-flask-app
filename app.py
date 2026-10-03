from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.environ.get('APP_ENV', 'unknown')
    try:
        conn = psycopg2.connect(
            host="db",
            port="5432",
            user="user",
            password="pass",
            dbname="kolyauzumaki"
        )
        conn.close()
        return f"Hello, Docker! База подключена! Режим: {env}"
    except Exception as e:
        return f"Ошибка подключения: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)