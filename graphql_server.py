from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, jsonify, request

from schema.create import create_schema


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello, GraphQL-API!'


@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()

    schema = create_schema()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    
    status_code = 200 if success else 400
    return jsonify(result), status_code
