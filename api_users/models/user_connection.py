import psycopg

class UserConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=postgres host=localhost port=5432")
        except psycopg.OperationalError as e:
            print(e)
            self.conn.close()

    def __def__(self):
        self.conn.close()

    #def write(self, data):
    #    with self.conn.cursor() as cur:
    #        cur.execute("""
    #                    INSERT INTO tblUsers)
