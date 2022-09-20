import json
import pprint
from datetime import datetime

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://192.168.253.12:27017')

db = client.test_database
# db = client['test_database']

collection = db.test_collection

# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.utcnow()}

posts = db.posts
# post_id = posts.insert_one(post).inserted_id
print(db.list_collection_names())

# pprint.pprint(posts.find_one())
# pprint.pprint(posts.find_one({"author": "Mike"}))

# new_posts = [{"author": "Mike",
#               "text": "Another post!",
#               "tags": ["bulk", "insert"],
#               "date": datetime(2009, 11, 12, 11, 14)},
#              {"author": "Eliot",
#               "title": "MongoDB is fun",
#               "text": "and pretty easy too!",
#               "date": datetime(2009, 11, 10, 10, 45)}]
# result = posts.insert_many(new_posts)
# print(result.inserted_ids)

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))

print(posts.count_documents({"author": "Mike"}))

d = datetime(2009, 11, 13)
for post in posts.find({"date": {"$lt": d}}).sort("date"):
    pprint.pprint(post)

# create index
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
pprint.pprint(sorted(list(db.profiles.index_information())))

# user_profiles = [
#     {'user_id': 211, 'name': 'Luke'},
#     {'user_id': 212, 'name': 'Ziltoid'}]
# result = db.profiles.insert_many(user_profiles)

# DuplicateKeyError
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# result = db.profiles.insert_one(new_profile)  # This is fine.
# result = db.profiles.insert_one(duplicate_profile)

