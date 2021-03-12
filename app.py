from flask import Flask
import asyncio
from posts import send_posts
from config import configure_db
from werkzeug import Response
import json
from db_reader import read

app = Flask(__name__)
loop = asyncio.get_event_loop()

db = configure_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/createPosts', methods=['POST'])
def create_posts():
    result = loop.run_until_complete(send_posts(10, db))
    if result is None:
        return Response(status=400, mimetype='application/json')
    else:
        return Response(status=200, mimetype='application/json')


@app.route('/getPosts', methods=['GET'])
def get_posts():
    result = read(db, 7)
    if result is None:
        return Response(status=400, mimetype='application/json')
    else:
        return Response(result, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
