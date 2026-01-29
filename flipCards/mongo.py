import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from documentLists import document_list, document_list2, document_list3

load_dotenv()

# CREATE DATABASE CONNECTION
uri=os.environ['MONGODB_URI']
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    database = client["flashCards"]
    # collection = database["frenchExpressions"]
    collection = database["userCards"]
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

# Current frechExpressions Collection Keys: phrase, translation, categories 

# Insert documents into collection
#database.collection.insert_many(document_list3)

# database.collection.update_many(
#     {"cardID": {"$exists": False}},
#     {"$set": {"cardID": "$_id"}}
# )

# database.collection.update_many(
#     {},
#     {
#         "$rename": {
#             "Phrase": "phrase",
#             "Translation": "translation"
#         }
#     }
# )
# Create unique index on userID and cardId - RUN ONCE ONLY
# database.userCards.create_index(
#     [("userID", 1), ("cardId", 1)], 
#     unique=True)

# Verify index creation
# print(database.userCards.index_information()
# )

database.userCards.update_many(
    {"userID": {"$regex": r"^g:g:"}},
    [
        {"$set": {"userID": {"$replaceOne": {"input": "$userID", "find": "g:g:", "replacement": "g:"}}}}
    ]
)

num = database.userCards.count_documents({})
print(f"Number of documents in collection: {num}")
# print(collection)

for doc in database.userCards.find().limit(3):
    print(doc)
    

# database.collection.drop()