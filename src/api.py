import sys
sys.path.append('.')
from flask import Flask, request
from flask_restful import Api
from src.resources.publish_resource import PublishResource


app = Flask(__name__)

api = Api(app)

api.add_resource(PublishResource, '/api/publish', endpoint='publish')
api.add_resource(PublishResource, '/api/publish/<int:id>', endpoint='published')

@app.route('/')
def index():
    return 'Hello my friend'


app.run(debug=True)
