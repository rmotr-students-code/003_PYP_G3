import os

from flask import Flask

app = Flask("This is my first app")

@app.route("/")
def hello_world():
    """Simplest template string rendering"""
    order_total = 10
    html = """
        <html>
            <b>Your order: ${order}</b>
        </html>
    """.format(order=order_total)
    return html


if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)