import sqlite3
import pandas as pd


class RecognitionHistory:

    def __init__(self):
        self.conn = sqlite3.connect("database/attendance.db")

    def get_recent(self, limit=10):

        query = f"""
        SELECT *
        FROM attendance
        ORDER BY id DESC
        LIMIT {limit}
        """

        return pd.read_sql_query(query, self.conn)

    def close(self):
        self.conn.close()