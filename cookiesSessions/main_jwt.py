from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
import uuid  # to generate unique guest IDs

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
CORS(app) # 👈 This enables CORS for all routes
jwt = JWTManager(app)


@app.route('/')
def home():
    return render_template('index.html')

# 👉 Create guest session
@app.route('/guest', methods=['GET'])
def guest_session():
    guest_id = f"guest-{uuid.uuid4()}"  # unique guest ID
    access_token = create_access_token(identity=guest_id)
    return jsonify(access_token=access_token)


# 👉 Use token to access protected route
@app.route('/whoami', methods=['GET'])
@jwt_required()
def whoami():
    user_id = get_jwt_identity()
    return jsonify(identity=user_id)


# 👉 Protected area that only guests can use
@app.route('/guest-zone', methods=['GET'])
@jwt_required()
def guest_zone():
    user_id = get_jwt_identity()
    if user_id.startswith("guest-"):
        return jsonify(msg=f"Welcome, {user_id}!")
    else:
        return jsonify(msg="Access denied."), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)