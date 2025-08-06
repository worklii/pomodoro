import psycopg2

try:
    conn = psycopg2.connect(
        dbname="pomodoro",
        user="postgres",
        password="password",
        host="localhost",
        port="5433"
    )
    print("Подключение успешно")
    conn.close()
except Exception as e:
    print("Ошибка подключения:", e)