from flask import Flask, g, request, render_template
import sqlite3
from . import config

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    g.db = connect_db()
    g.authors = [dict(id=row[0], name=row[1]) for row in g.db.execute('SELECT id, name FROM author;')]

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    
    if request.method == 'GET':
        return render_template('form_with_template_inheritance.html', authors=g.authors, message="")
    elif request.method == 'POST':
        # Insert
        title = request.form["title"]
        isbn = request.form["isbn"]
        author = request.form["author"]
        message = ""
        
        if title == "":
            message = "Error! You must enter a title!"
        elif isbn == "":
            message = "Error! You must enter a ISBN!"
        else:
            g.db.execute("INSERT INTO book (author_id, title, isbn)" 
                "VALUES ('{author_id}', '{title}', '{isbn}')".format(
                author_id=author, title=title, isbn=isbn))
            g.db.commit()
            message = "Successfully submitted!"
            
        return render_template('form_with_template_inheritance.html', authors=g.authors, message=message)
