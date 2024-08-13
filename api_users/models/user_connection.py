import psycopg

class UserConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=postgres host=localhost port=5432")
        except psycopg.OperationalError as e:
            print(e)
            self.conn.close()
    def getUsers(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "tblUsers"
            """)
            return cur.fetchall()
            
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "tblUsers"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
        self.conn.commit()


    def __def__(self):
        self.conn.close()

