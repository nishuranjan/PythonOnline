import datetime
import redis
from pymongo import MongoClient


redis_client = redis.Redis(
        host='localhost',
        port=6397,
        password='if any'
    )

def test_redis():
    post = {
        "author": "Mike",
	    "text": "My first blog post!",
	    "tags": ["mongodb", "python", "pymongo"],
	    "date": datetime.datetime.utcnow()
    }

    redis_client.set('key-post', post)
    # redis_client.set('trainees', 'Mohita')
    redis_value = redis_client.get('key-post')
    
    # mongodb connect and store redis value in document
    client = MongoClient()
    db = client.test_database
    posts = db.posts
    post_id = posts.insert_one(redis_value).inserted_id

    print(redis_value)
    print(f"records from mongodb {post_id}")


# calling the redis
test_redis()
