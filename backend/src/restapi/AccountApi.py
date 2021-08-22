from model import Account
from model import Status
#from __future__ import absolute_import, unicode_literals 
import json
import datetime
from model.common import strftime
from model.common import strptime

#import requests

def getById(account_id, operation_account_id):
    """
    /account/get/<id>で呼び出されたAPIの検索処理

    Parameters
    ----------
    account_id : int
        検索するアカウントのアカウントID
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    ret
        json形式のアカウント詳細
    {
      "body": {
        "name": "account",
        "id": <account_id>,
        "account_name": <account_name>,
        "start_on": "2021-01-01 10:00:00",
        "end_on": "2025-12-31 21:00:00"
    },
      "status": {
        "code" : "I0001",
        "message" : "",
        "detail" : ""
      }
    }
    """
    
    result = Account.getById(account_id, operation_account_id)
    # TODO モデルの検索結果(正常・異常)によってレスポンスの出力内容を変える
    result_json = {
        "body": {
            "name": "account",
            "id": account_id,
            "account_name": result.account_name,
            "start_on": result.start_on.strftime("%Y-%m-%d %H:%M:%S"),
            "end_on": result.end_on.strftime("%Y-%m-%d %H:%M:%S")
        },
        "status": {
            "code" : "I0001",
            "message" : "",
            "detail" : ""
        }
    }
    return result_json

def create(account_request, operation_account_id):
    """
    /account/createで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        作成するアカウント詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    account = {
        'account_name' : str(account_request['account_name']),
        'start_on' : str(account_request['start_on']),
        'end_on' : str(account_request['end_on']),
        'created_by' : operation_account_id,
        'created_at' : datetime.datetime.now(),
        'updated_by' : operation_account_id,
        'updated_at' : datetime.datetime.now(),
        'status' :  Status.getStatusKey("NEW")
    }

    try:
        if Account.create(account, operation_account_id) == True:
            code="I0001"
            message="Created Account Succesfuly."
        else:
            code="E0001"
            message=""
        
    except:
        code="E0009"
        message="Created failed"
    

    result_json = {
        "body": "",
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    return result_json


def search(request, user_id):
    """
    /account/searchで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        アカウント検索項目
    user_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    account_request = convertdict(request)
    try:
        results = Account.search(account_request, user_id)
        code="I0001"
        message=f"Found ({len(results)}) records."
        
    except Exception as e:
        code="E0009"
        message="Search failed: " + str(e)

    result_json = {
        "body": list(map(lambda s: s.toJson(), results)),
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    return result_json

def update(account_request, operation_account_id):
    """
    /account/updateで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_request : json
        作成するアカウント詳細
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    account = convertdict(account_request)
    try:
        res = Account.update(account, operation_account_id)
        print(f"AccountApi#update res={res[0]},{res[1]}")
        if res[0] == True:
            code="I0001"
            message="Updated Account Succesfuly."
        else:
            code="E0001"
            message=res[1]
        
    except Exception as e:
        code="E0009"
        message=f"Updated failed {e}"
    
    result_json = {
        "body": "",
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    return result_json

def delete(account_id, operation_account_id):
    """
    /account/deleteで呼び出されたAPIの検索処理

    Parameters
    ----------
    account_id : int
        削除するアカウントID
    operation_account_id : int
        Webアプリケーション操作アカウントのID

    Returns
    -------
    JSON形式の処理結果
        正常
        異常
    """

    try:
        res = Account.delete(account_id, operation_account_id)
        if res[0] == True:
            code="I0001"
            message="deleted Account Succesfuly."
        else:
            code="E0001"
            message=res[1]
        
    except Exception as e:
        code="E0009"
        message=f"Deleted failed:{str(e)}"
    
    result_json = {
        "body": "",
        "status": {
            "code" : code,
            "message" : message,
            "detail" : ""
        }
    }
    return result_json

def convertdict(from_dict):
    print(f"convertdict from_dict={from_dict}")
    target_dict = {}
    if not (from_dict is None):
        if ('id' in from_dict):
            target_dict['id'] = int(from_dict['id'])
        if ('account_name' in from_dict):
            target_dict['account_name'] = str(from_dict['account_name'])
        if ('start_on' in from_dict):
            target_dict['start_on'] = strptime(from_dict['start_on'])
        if ('end_on' in from_dict):
            target_dict['end_on'] = strptime(from_dict['end_on'])
        if ('created_by' in from_dict):
            target_dict['created_by'] = int(from_dict['created_by'])
        if ('created_at' in from_dict):
            target_dict['created_at'] = strptime(from_dict['created_at'])
        if ('updated_by' in from_dict):
            target_dict['updated_by'] = int(from_dict['updated_by'])
        if ('updated_at' in from_dict):
            target_dict['updated_at'] = strptime(from_dict['updated_at'])
        if ('status' in from_dict):
            target_dict['status'] = int(from_dict['status'])
    return target_dict

        
#    (lambda label_func: target_dict[(label_func[0])]=(label_func[1](from_dict[label_func[0]])) if label_func[0] in from_dict,labels_funcs)
#    labels_funcs = [('account_name', str), ('start_on', strptime), ('end_on',strptime), ('created_by', int), ('created_at', strptime), ('updated_by', int), ('updated_at', strptime), ('status', int)]
