import sqlite3
from datetime import datetime
import os


class AttendanceDatabase:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.conn = sqlite3.connect("database/attendance.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                date TEXT,
                time TEXT
            )
        """)

        self.conn.commit()

    def mark_attendance(self, name):

        today = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        self.cursor.execute(
            "SELECT * FROM attendance WHERE name=? AND date=?",
            (name, today)
        )

        record = self.cursor.fetchone()

        if record is None:

            self.cursor.execute(
                "INSERT INTO attendance(name,date,time) VALUES(?,?,?)",
                (name, today, current_time)
            )

            self.conn.commit()

            print(f"Attendance Marked -> {name}")

        else:

            print(f"{name} already marked today.")

    def close(self):
        self.conn.close()