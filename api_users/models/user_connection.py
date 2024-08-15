import psycopg

class UserConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=postgres host=localhost port=5432")
        except psycopg.OperationalError as e:
            print(e)
            self.conn.close()
    
    def get_users(self):
        print("get_users")
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "tblUsers"
            """)
            data=cur.fetchall()
            print(data)
            return cur.fetchall()
    
    def add_user(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "tblUsers"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
        self.conn.commit()

    def update_user(self, data, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "tblUsers" SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s
            """, data, id)
        self.conn.commit()

    def delete_user(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "tblUsers" WHERE id = %(id)s
            """, id)
        self.conn.commit()


    def __def__(self):
        self.conn.close()

