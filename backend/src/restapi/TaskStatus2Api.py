import datetime
from model import TaskStatus2


def getList():
    """/task_status2/listで呼び出された一覧の取得処理

    Returns
    -------
    dict
        json形式のタスクステータスの一覧
    """
    list = TaskStatus2.getByList(TaskStatus2.getAll())
    return {
        "body": list,
        "status": {
            "code": "I0001",
            "message": "",
            "detail": ""
        }
    }


def getById(status_id):
    """
    /task_status2/get/<id>で呼び出されたAPIの検索処理

    Parameters
    ----------
    status_id : int
        検索するタスクステータスのID

    Returns
    -------
    ret
        json形式のタスクステータス詳細
    {
      "body": {
        "name": "task_status2",
        "id": <status_id>,
        "status_name": <status_name>,
        "background_color": <background_color>
    },
      "status": {
        "code" : "I0001",
        "message" : "",
        "detail" : ""
      }
    }
    """

    result = TaskStatus2.getById(status_id)
    # TODO モデルの検索結果(正常・異常)によってレスポンスの出力内容を変える
    result_json = {
        "body": {
            "name": "task_status2",
            "id": status_id,
            "status_name": result.status_name,
            "background_color": result.background_color,
        },
        "status": {
            "code": "I0001",
            "message": "",
            "detail": ""
        }
    }
    return result_json


def create(request, operation_account_id):
    """
    /task_status2/createで呼び出されたAPIの検索処理

    Parameters
    ----------
    request : json
        作成するタスクステータス詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
    """
    task_status = {
        'status_name': request['status_name'],
        'background_color': request['background_color'],
        'created_by': operation_account_id,
        'created_at': datetime.datetime.now(),
        'updated_by': operation_account_id,
        'updated_at': datetime.datetime.now(),
    }

    try:
        if TaskStatus2.create(task_status):
            code = "I0001"
            message = "Created TaskStatus Succesfuly."
        else:
            code = "E0001"
            message = ""

    except Exception as e:
        code = "E0009"
        message = "Created failed"
        print(e)

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json


def update(request, operation_account_id):
    task_status = {
        'id': request['id'],
        'status_name': request['status_name'],
        'background_color': request['background_color'],
        'updated_by': operation_account_id,
        'updated_at': datetime.datetime.now(),
    }

    try:
        if TaskStatus2.update(task_status):
            code = "I0001"
            message = "Updated TaskStatus Succesfuly."
        else:
            code = "E0001"
            message = ""

    except Exception as e:
        code = "E0009"
        message = "Updated failed"
        print(e)

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json


def delete(status_id, operation_account_id):
    try:
        if TaskStatus2.delete(status_id, operation_account_id):
            code = "I0001"
            message = "Deleted TaskStatus Succesfuly."
        else:
            code = "E0001"
            message = ""

    except Exception as e:
        code = "E0009"
        message = "Deleted failed"
        print(e)

    result_json = {
        "body": "",
        "status": {
            "code": code,
            "message": message,
            "detail": ""
        }
    }
    return result_json
