from utils.db_connection import get_db_connection


class ReportGenerator:
    @staticmethod
    def generate_report():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM transactions"
        cursor.execute(query)
        report = cursor.fetchall()
        cursor.close()
        conn.close()
        return report
