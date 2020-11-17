import datetime
import redis
from pymongo import MongoClient


redis_client = redis.Redis(
        host='redis-18767.c17.us-east-1-4.ec2.cloud.redislabs.com',
        port=18767,
        password='pRPbp9UXd4bkPvOKvrNKJJxgSPSLqNIS'
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
    client = MongoClient('mongodb+srv://testmongouser:test123@cluster0.use8p.mongodb.net/testmongodb?retryWrites=true&w=majority')
    db = client.test_database
    posts = db.posts
    post_id = posts.insert_one(redis_value).inserted_id

    print(redis_value)
    print(f"records from mongodb {post_id}")


# calling the redis
test_redis()
