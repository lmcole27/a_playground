# Store data server side using: Redis, Memcached, Filesystem, or SQLAlchemy DB

from flask import Flask, request, make_response, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    id = session.get('ID', None)
    if id is None:
        #return f"Hello Worlds"
        return set_session()
    else:
        return f"<H1>Hello World! {session['ID']} </H1>"

@app.route('/set_session')
def set_session():
    session['ID'] = '987654321'
    return session['ID']

#RUN THE WEBAPP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)