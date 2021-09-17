# 君塚
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from restapi import TaskStatus2Api

system_account_id = 999

task_status2_bp = Blueprint(
    'task_status2_app', __name__, url_prefix='/api/task_status2')


@task_status2_bp.route('/list', methods=['GET'])
def listTaskStatus2():
    response_json = TaskStatus2Api.getList()
    return jsonify(response_json)


@task_status2_bp.route('/get/<id>', methods=['GET'])
def getTaskStatus(id):
    account_json = TaskStatus2Api.getById(id)
    return jsonify(account_json)


@task_status2_bp.route('/create', methods=['POST'])
def createTaskStatus2():
    payload = request.json
    response_json = TaskStatus2Api.create(payload, system_account_id)
    return jsonify(response_json)


@task_status2_bp.route('/update', methods=['POST'])
def updateTaskStatus2():
    payload = request.json
    response_json = TaskStatus2Api.update(payload, system_account_id)
    return jsonify(response_json)


@task_status2_bp.route('/delete', methods=['POST'])
def deleteTaskStatus2():
    payload = request.json
    response_json = TaskStatus2Api.delete(payload['id'], system_account_id)
    return jsonify(response_json)
