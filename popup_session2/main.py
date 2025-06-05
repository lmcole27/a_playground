from flask import Flask, session, request, jsonify, render_template

app = Flask(__name__)
app.secret_key = 'super-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/profile')
def profile():
    username = session.get('username')
    if username:
        return jsonify(username=username)
    return jsonify(username=None), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    if username:
        session['username'] = username
        return jsonify(success=True)
    return jsonify(success=False), 400

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)