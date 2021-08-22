from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from restapi import AccountApi

system_account_id=999

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/account/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = AccountApi.getById(id, system_account_id)
    res = make_response(jsonify(account_json))
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080/"
    res.headers['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE"
    return res

@api_bp.route('/account/create', methods=['POST'])
def createAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.create(payload, system_account_id)
    return jsonify(response_json)

@api_bp.route('/account/search', methods=['POST'])
def searchAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.search(payload, system_account_id)
    res = make_response(jsonify(response_json))
    res.headers['Access-Control-Allow-Origin'] = "http://localhost:8080"
    res.headers['Access-Control-Allow-Methods'] = "POST,GET,PUT,DELETE,OPTIONS"
    res.headers['Access-Control-Max-Age'] = 17280000
    res.headers['Access-Control-Allow-Headers'] = "*"
    res.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    res.headers['Access-Control-Allow-Credentials'] = "true"
    return res

@api_bp.route('/account/update', methods=['POST'])
def updateAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.update(payload, system_account_id)
    return jsonify(response_json)

@api_bp.route('/account/delete/<id>', methods=['GET'])
def deleteAccount(id):
    account_json = AccountApi.delete(id, system_account_id)
    return jsonify(account_json)

class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}

api = Api(api_bp)
api.add_resource(Spam, '/spam')

