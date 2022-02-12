from crypt import methods
from flask import Flask, jsonify, request

from data import Blog, all_authors, all_blogs, get_author, get_blog, update_blog

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello, REST-API!'


@app.route('/blogs', methods=['GET'])
def fetch_blogs():
    return jsonify(all_blogs())


@app.route('/blogs/<int:id>', methods=['GET'])
def fetch_blog(id: int):
    return jsonify(get_blog(id))


@app.route('/authors', methods=['GET'])
def fetch_authors():
    return jsonify(all_authors())


@app.route('/authors/<int:id>', methods=['GET'])
def fetch_author(id: int):
    return jsonify(get_author(id))


@app.route('/blogs/<int:id>', methods=['POST'])
def post_blog(id: int) -> Blog:
    payload = request.get_json()
    return jsonify(update_blog(id, payload))

