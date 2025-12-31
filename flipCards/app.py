from flask import Flask, render_template, url_for
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

#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template("index.html")

#API ENDPOINT
@app.route('/api', methods=['GET', 'POST'])
def api():
    doc = list(database.collection.aggregate([
    {"$sample": {"size": 1}}
    ]))[0]

    phrase = doc['Phrase']
    translation = doc['Translation']
    output = {
        "Phrase": phrase,
        "Translation": translation
        }

    # for doc in database.collection.find().limit(1):
    #     phrase = doc['Phrase']
    #     translation = doc['Translation']
    #     output = {
    #         "Phrase": phrase,
    #         "Translation": translation
    #     }

    json_string = json.dumps(output, indent=4)
    return json_string

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

client.close()