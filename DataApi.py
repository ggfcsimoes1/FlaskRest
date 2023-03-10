from flask_restful import Resource
from flask import request
import requests
from dotenv import load_dotenv

ADDRESS = load_dotenv("DATABASE_ADDRESS")

class DataApi(Resource):
    def get(self):
        r = requests.get(ADDRESS)
        return r.json()

    def post(self):
        #key = request.form['key']
        #value = request.form['value']
        #r = requests.post(ADDRESS, data={key: value})
        #return r.status_code
        pass