from flask import Flask, jsonify, render_template, request

from models.book_model import Book
from models.member_model import Member
from models.transaction_model import Transaction
from utils.db_connection import get_db_connection

app = Flask(__name__)

# Route chính, hiển thị trang index
@app.route('/')
def index():
    return render_template('index.html')

# API thêm sách
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    result = Book.add_book(data)
    return jsonify(result)

# API lấy danh sách sách
@app.route('/api/books', methods=['GET'])
def get_books():
    books = Book.get_all_books()
    return jsonify(books)

# API thêm thành viên
@app.route('/api/members', methods=['POST'])
def add_member():
    data = request.json
    result = Member.add_member(data)
    return jsonify(result)

# API lấy danh sách thành viên
@app.route('/api/members', methods=['GET'])
def get_members():
    members = Member.get_all_members()
    return jsonify(members)

# API thêm giao dịch
@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    result = Transaction.add_transaction(data)
    return jsonify(result)

# Khởi động server
if __name__ == '__main__':
    app.run(debug=True)
