# from flask import Flask, session, request, jsonify, render_template
# import uuid

# # app = Flask(__name__)
# # app.secret_key = 'super-secret-key'

# # @app.route('/')
# # def index():
# #     return "Hello World"   

# guest_id = f"guest-{uuid.uuid4()}"  # unique guest ID
# print(guest_id)
# access_token = {"guest": guest_id}
# session['token'] = access_token 
# print(access_token)

age = 15
message = "You can vote." if age >= 18 else "You're too young."
print(message)  # You can vote.

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5003, debug=True)