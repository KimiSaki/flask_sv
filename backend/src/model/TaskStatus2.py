import datetime
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Time
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.sqltypes import Boolean

from model.common import strftime
from model.common import strptime

from model.db import engine
from model.db import Base


class TaskStatus2(Base):
    __tablename__ = 'task_status2'

    id = Column(Integer, primary_key=True)
    status_name = Column(String(), nullable=False)
    background_color = Column(String(), nullable=True)
    is_valid = Column(Boolean, nullable=False)
    created_by = Column(Integer, nullable=True)
    created_at = Column(Timestamp, nullable=True)
    updated_by = Column(Integer, nullable=True)
    updated_at = Column(Timestamp, nullable=True)

    # get Dict data
    def toDict(self):
        """
        ディクショナリ形式でクラスの全メンバを返却する

        Parameters
        ----------
        self : 自クラス

        Returns
        -------
        クラスの全メンバのディクショナリ
        """
        return {
            'id': int(self.id),
            'status_name': str(self.status_name),
            'background_color': str(self.background_color),
            'created_by': int(self.created_by),
            'created_at': strptime(self.created_at),
            'updated_by': int(self.updated_by),
            'updated_at': strptime(self.updated_at)
        }

    def toJson(self):
        return {
            "name": "task_status2",
            "id": str(self.id),
            "status_name": self.status_name,
            "background_color": self.background_color,
            "created_by": int(self.created_by),
            "created_at": strftime(self.created_at),
            "updated_by": int(self.updated_by),
            "updated_at": strftime(self.updated_at)
        }


# get List data
def getByList(arr):
    res = []
    for item in arr:
        res.append(item.toJson())
    return res


# get all mydata record
def getAll():
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(TaskStatus2).all()
    ses.close()
    return res


def getById(status_id):
    """
    タスクステータスidでtask_status2テーブルを検索をし、該当したオブジェクト群を取得する

    Parameters
    ----------
    task_status_id : 検索対象のタスクステータスid

    Returns
    -------
    TaskStatus2オブジェクトのリスト
    """
    Session = sessionmaker(bind=engine)
    ses = Session()
    res = ses.query(TaskStatus2).get(status_id)
    ses.close()
    return res


def create(task_status_dict):
    task_status = TaskStatus2()
    task_status.status_name = task_status_dict['status_name']
    task_status.background_color = task_status_dict['background_color']
    task_status.created_by = task_status_dict['created_by']
    task_status.created_at = task_status_dict['created_at']
    task_status.updated_by = task_status_dict['updated_by']
    task_status.updated_at = task_status_dict['updated_at']
    Session = sessionmaker(bind=engine)
    ses = Session()
    ses.begin()
    try:
        ses.add(task_status)
        ses.commit()
        res = True
    except:
        ses.rollback()
        res = False
    finally:
        ses.close()
    return res


def update(task_status2_dict):
    status_id = task_status2_dict.get('id')
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    res = False
    ses = Session()
    task_status = ses.query(TaskStatus2).with_for_update().get(status_id)
    print(f"TaskStatus2#update record={task_status}")
    message = ""
    try:
        v = task_status2_dict.get('status_name')
        if v is not None:
            task_status.status_name = v
        v = task_status2_dict.get('background_color')
        if v is not None:
            task_status.background_color = v
        task_status.updated_by = task_status2_dict.get('updated_by')
        task_status.updated_at = task_status2_dict.get('updated_at')

        ses.add(task_status)
        ses.commit()
        res = True
    except Exception as e:
        message = str(e)
        print(f"TaskStatus2#update error:{message}")
        ses.rollback()
        res = False
    finally:
        ses.close()
    return (res, message)


def delete(status_id, operation_account_id):
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False))
    ses = Session()
    task_status = ses.query(TaskStatus2).with_for_update().get(status_id)
    try:
        task_status.is_valid = False
        task_status.updated_by = operation_account_id
        task_status.updated_at = datetime.datetime.now()
        ses.add(task_status)
        ses.commit()
        message = ""
        res = True
    except Exception as e:
        message = str(e)
        print(f"TaskStatus#delete error:{message}")
        ses.rollback()
        res = False
    finally:
        ses.close()
    return (res, message)
