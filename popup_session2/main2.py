from flask import Flask, session, request, jsonify, render_template
import uuid #to generate unique guest IDs

app = Flask(__name__)
app.secret_key = 'super-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/profile')
def profile():
    token = session.get('token')
    if token:
        return jsonify(token=token)
    return jsonify(username=None), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    token = uuid.uuid4()  # unique guest ID
    token_str = str(token)
    session['token'] = token_str  # Store the token in session
    return jsonify(success=True)
    # if username:
    #     session['username'] = username
    #     return jsonify(success=True)
    # return jsonify(success=False), 400

@app.route('/api/guest', methods=['POST'])
def guest():
    token = uuid.uuid4()  # unique guest ID
    token_str = str(token)
    session['token'] = token_str  # Store the token in session
    return jsonify(success=True)

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)