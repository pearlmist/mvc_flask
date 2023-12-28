from app import app
from flask import render_template, request, session
# import sqlite3
from utils import get_db_connection
from models.index_model import get_reader, get_book_reader, get_new_reader 
#borrow_book


@app.route('/new_reader', methods=['get'])
def new_reader():
    html = render_template(
        'new_reader.html',
        len=len
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)
