from robot.api.deco import keyword
from pymongo import  MongoClient

client = MongoClient('mongodb+srv://qax:xperience@cluster0.alcch.mongodb.net/markX?retryWrites=true&w=majority&appName=Cluster0')

db = client['markX']

@keyword('Removendo task from database')
def remove_task_by_name(task_name):
    colletion = db['tasks']
    colletion.delete_many({'text': task_name})
    print('Removendo a tarefa ' +task_name)