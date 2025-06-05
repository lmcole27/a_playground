from flask import Flask, request, make_response, session, jsonify
import uuid
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'top_secret_key'
CORS(app)

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
    session['ID'] = f"{uuid.uuid4()}"
    return f"{session['ID']}"

@app.route('/get_session')
def get_session():
    id = session.get('ID', None)
    if id is None:
        return jsonify({"error": "No session found"}), 404
    return f"<H1>Hello World! {id} </H1>"


#RUN THE WEBAPP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)