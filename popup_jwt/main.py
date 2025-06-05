from flask import Flask, render_template, request, jsonify
import jwt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import uuid  # to generate unique guest IDs

SECRET_KEY = 'super-secret-key'

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY

CORS(app) # 👈 This enables CORS for all routes
jwt = JWTManager(app)

def is_valid_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

@app.route('/')
def index():
    return render_template('index.html')
    # token = request.cookies.get('token')
    # show_popup = not token or not is_valid_jwt(token)
    # #print(show_popup)
    # #show_popup = False
    # if show_popup:
    #     return render_template('index.html', show_popup=show_popup)
    # else:
    #     return "<h1>No Popup</h1>"
    
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
    app.run(host='0.0.0.0', port=5005, debug=True)