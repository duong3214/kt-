from utils.db_connection import get_db_connection


class Transaction:
    @staticmethod
    def add_transaction(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO transactions (member_id, book_id, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['member_id'], data['book_id'], data['status']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'message': 'Transaction added successfully'}
