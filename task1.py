from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base1.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')    
