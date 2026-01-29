from flask import Flask, render_template, url_for, jsonify, session, request
import uuid
from flask_cors import CORS
#from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
# from pymongo import MongoClient, server_api
from pymongo import AsyncMongoClient
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from datetime import datetime, timezone
from bson import ObjectId
load_dotenv()

# CREATE DATABASE CONNECTION
uri=os.environ['MONGODB_URI']
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    database = client["flashCards"]
    collection = database["frenchExpressions"]
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)


#CREATE WEBAPP
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.environ['FLASK_SECRET_KEY']
#app.config['SESSION_COOKIE_SECURE'] = True  # Set to True in production
#app.config['SESSION_COOKIE_HTTPONLY'] = True
#app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


#INFO REQUIRED TO LOAD .env in pythonanywhere
# project_folder = os.path.expanduser('~/mysite')
# load_dotenv(os.path.join(project_folder, '.env'))

def check_session():
    if session.get('token', None) is None:
        session['token'] = ("g:" + str(uuid.uuid4()))
        print("New session created with token:", session['token'])
    else:
        print("Existing session with token:", session['token'])

#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    check_session()
    return render_template("index.html")
    
#API ENDPOINT
@app.route('/api/nextCard', methods=['GET', 'POST'])
def api():
    doc = list(database.collection.aggregate([
    {"$sample": {"size": 1}}
    ]))[0]
    cardID = str(doc['_id'])
    phrase = doc['phrase']
    translation = doc['translation']
    output = {
        "cardID": cardID,
        "Phrase": phrase,
        "Translation": translation
        }
    json_string = json.dumps(output, indent=4)
    print("cardID:", cardID)
    return json_string

@app.route('/api/hideCard', methods=['GET', 'POST'])
def userCard():
    check_session()
    payload = request.get_json()
    currentCardID = payload.get("currentCardID")
    status = payload.get("status")
    guest_user_token = session['token']
    now = datetime.now(timezone.utc)
    # user_cards = list(database.userCards.find({"userKey": user_token}))
    # for card in user_cards:
    #     card['_id'] = str(card['_id'])  # Convert ObjectId to string for JSON serialization
    print(f"Guest User Token: {guest_user_token}, Current Card: {currentCardID}, Status: {status}, Time: {now}")

    userCards = database["userCards"]
    result = userCards.update_one(
        {"userID": guest_user_token, "cardId": currentCardID},
        {
            "$set": {
                "status": status,
                "updatedAt": now
            },
        },
        upsert=True
    )
    print(result.raw_result)
    # result.matched_count tells you if it found an existing doc
    # result.upserted_id is set if it inserted a new one
    return jsonify({"message": "This is a placeholder for userCards endpoint."})

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

client.close()