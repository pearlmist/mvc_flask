from app import app
from flask import render_template, request, session
# import sqlite3
from utils import get_db_connection
from models.search_model import get_count_genre, get_count_author, get_count_publisher, get_filter_book, get_book
# borrow_book


@app.route('/search', methods=['get', 'post'])
def search():
    conn = get_db_connection()
    df_genre = get_count_genre(conn)
    df_author = get_count_author(conn)
    df_publisher = get_count_publisher(conn)
    checked_list_authors = []
    checked_list_genre = []
    checked_list_publisher = []
    df_filter_book = get_book(conn)

    if request.values.get('authors') or request.values.get('genre') or request.values.get('publisher'):
        checked_list_authors = request.form.getlist('authors')
        checked_list_publisher = request.form.getlist('publisher')
        checked_list_genre = request.form.getlist('genre')


        df_filter_book = get_filter_book(
            conn,
            checked_list_genre,
            checked_list_authors,
            checked_list_publisher
        )

    if request.values.get('reset'):
        df_filter_book = get_book(conn)
        checked_list_authors = []
        checked_list_genre = []
        checked_list_publisher = []

    html = render_template(
        'search.html',
        genre_box=df_genre,
        author_box=df_author,
        publisher_box=df_publisher,
        filter_box=df_filter_book,
        checked_list_authors=checked_list_authors,
        checked_list_genre=checked_list_genre,
        checked_list_publisher=checked_list_publisher,
        len=len
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)
