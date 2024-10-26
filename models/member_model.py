from utils.db_connection import get_db_connection


class Member:
    @staticmethod
    def add_member(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO members (name, birth_date, address) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['name'], data['birth_date'], data['address']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'message': 'Member added successfully'}

    @staticmethod
    def get_all_members():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        cursor.close()
        conn.close()
        return members
