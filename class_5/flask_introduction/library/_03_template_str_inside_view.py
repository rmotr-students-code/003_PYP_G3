import os

from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Poe"
    html = """
        <html>
            <h1>Welcome to {{library_name}} library!</h1>
        </html>
    """
    context = {
        'library_name': library_name
    }
    rendered_html = render_template_string(html, **context)
    print(rendered_html)
    return rendered_html
