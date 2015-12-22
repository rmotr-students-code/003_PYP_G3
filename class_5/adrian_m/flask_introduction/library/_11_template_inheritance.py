import sqlite3
from flask import Flask, request, render_template, g
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    if request.method == 'GET':
        return render_template('form_with_template_inheritance.html',
            authors=authors)
    elif request.method == 'POST':
        error = False
        success = False
        author_id = int(request.form.get('author'))
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        if not author_id or not isbn or not title:
            error = True
        else:
            cursor = g.db.cursor()
            cursor.execute(
                'INSERT INTO book (author_id, isbn, title) VALUES ("{}", "{}", "{}")'.format(
                author_id, isbn, title))
            g.db.commit()
            success = True
        
        return render_template('form_with_template_inheritance.html',
            authors=authors, error=error, success=success, author_id=author_id, title=title)


@app.route('/results', methods=['POST', 'GET'])
def results():
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    print authors
    cursor.close()
    if request.method == 'GET':
        return render_template('results.html',
            authors=authors)
    if request.method == 'POST':
        author_id = request.form.get('author')
        cursor = g.db.cursor()
        cursor.execute(
            'SELECT author_id, isbn, title FROM book where author_id=?', author_id)
        books = [dict(id=row[0], isbn=row[1], title=row[2]) for row in cursor.fetchall()]
        cursor.close()
        for author in authors:
            if author['id'] == int(author_id):
                author_name = author['name']
        print(books)
        return render_template('results.html', authors=authors, books=books, author_name=author_name)

        
        

    
    
    
