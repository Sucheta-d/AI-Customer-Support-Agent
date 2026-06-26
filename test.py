from Backend.database import get_connection

conn = get_connection()
print(conn)
conn.close()