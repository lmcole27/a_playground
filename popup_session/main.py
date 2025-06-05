from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import uuid #to generate unique guest IDs


SECRET_KEY = 'super-secret-key'

app = Flask(__name__)
app.secret_key = 'top_secret_key'

CORS(app) # This enables CORS for all routes


@app.route('/', methods=['GET', 'POST'])
def index():
    id = session.get('ID', None)
    if id is None:
        #return f"Hello Worlds"
        return render_template("index.html")
    else:
        return f"<H1>Welcome Back! {id} </H1>"

@app.route('/token', methods=['GET'])
def token():
    token = session.get('token')
    if token is None:
        return jsonify({"error": "No token found"}), 404
    return jsonify({"token": token})

# Create guest session
@app.route('/guest', methods=['GET'])
def guest_session():
    guest_id = f"guest-{uuid.uuid4()}"  # unique guest ID
    access_token = {"guest": guest_id}
    session['token'] = access_token  # Store the token in session
    return jsonify(access_token=access_token)

@app.route('/verify_token', methods=['POST'])
def verify_token():
    data = request.get_json()
    if not data or 'token' not in data:
        return jsonify({"error": "No token provided"}), 400
    
    client_token = data['token']
    # You can add additional token verification logic here
    return jsonify({
        "message": "Token received",
        "token": client_token,
        "is_valid": True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)