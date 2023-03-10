from DataApi import DataApi
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(DataApi, '/data')

if __name__ == '__main__':
    app.run(debug=True)
