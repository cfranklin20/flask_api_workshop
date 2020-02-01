from flask import Flask
from flask_restplus import Api, Resource, fields


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='1.0',
                       title='Sample Book API',
                       description='A simple Book API',
                       doc='/books/docs'
                       )
        self.app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    def run(self):
        self.app.run(
            debug=True,
            port=5000
        )


server = Server()
