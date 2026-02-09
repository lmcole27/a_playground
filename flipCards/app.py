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
    database = client["flashCards"]
    cards = database["cards"]
    userCards = database["userCards"]
    print("Pinged your deployment. You successfully connected to MongoDB!")
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
    return session['token']

#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    check_session()
    return render_template("index.html")
    
#API ENDPOINTS
@app.route("/api/nextCard", methods=["GET"])
def api():
    user_id = check_session()
    #cards = database["cards"]
    #userCards = database["userCards"]

    # 1) Get hidden cardIds for this user
    hidden_cursor = userCards.find(
        {"userID": user_id, "status": "hide"},
        {"_id": 0, "cardId": 1}
    )
    hidden_ids = [d["cardId"] for d in hidden_cursor]  # these should already be ObjectId

    # 2) Build pipeline to exclude hidden, then sample
    pipeline = []
    if hidden_ids:
        pipeline.append({"$match": {"_id": {"$nin": hidden_ids}}})
    pipeline.append({"$sample": {"size": 1}})

    docs = list(cards.aggregate(pipeline))
    if not docs:
        print("ERROR: No cards left (all hidden?)")
        return jsonify(error="No cards left (all hidden?)"), 404

    doc = docs[0]
    print("Selected card for user", user_id, ":", doc["_id"])
    return jsonify(
        cardID=str(doc["_id"]),
        Phrase=doc.get("phrase", ""),
        Translation=doc.get("translation", "")
    )

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
        {"userID": guest_user_token, "cardId": ObjectId(currentCardID)},
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

@app.route('/api/showAll', methods=['GET', 'POST'])
def showAll():
    check_session()
    guest_user_token = session['token']
    userCards = database["userCards"]
    status = "show"
    now = datetime.now(timezone.utc)
    result = userCards.update_many(
        {},
        {
            "$set": {
                "status": status,
                "updatedAt": now
            },
        },
        upsert=True
    )
    for doc in database.userCards.find().limit(3):
        print(doc)
    print(f"Show All Cards for Guest User Token: {guest_user_token}")
    return jsonify({"message": "This is a placeholder for Show All Cards endpoint."})

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

client.close()