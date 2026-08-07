import sqlite3
import os
from openpyxl import Workbook


class AttendanceExporter:

    def __init__(self):

        os.makedirs("exports", exist_ok=True)

    def export(self):

        conn = sqlite3.connect("database/attendance.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM attendance")

        records = cursor.fetchall()

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Attendance"

        sheet.append(["ID", "Name", "Date", "Time"])

        for row in records:
            sheet.append(row)

        workbook.save("exports/attendance.xlsx")

        conn.close()

        print("Attendance exported successfully.")