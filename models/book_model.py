from utils.db_connection import get_db_connection


class Book:
    @staticmethod
    def add_book(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO books (title, author) VALUES (%s, %s)"
        cursor.execute(query, (data['title'], data['author']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'message': 'Book added successfully'}

    @staticmethod
    def get_all_books():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books
