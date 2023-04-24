#!/usr/bin/python3
"""
Using `https://jsonplaceholder.typicode.com/` REST API
Use urllib or requests module

Script to export data in the CSV format
    Records all tasks that are owned by each employee
    Format must be: { "USER_ID": [{"username": "USERNAME",\
        "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},\
            {"username": "USERNAME", "task": "TASK_TITLE",\
                 "completed": TASK_COMPLETED_STATUS,\
                  }, ... ]}

File name must be: todo_all_employees.json
"""
import json
import requests

if __name__ == '__main__':

    """
    Sample URLs
    To users`https://jsonplaceholder.typicode.com/users/`
    To a user `https://jsonplaceholder.typicode.com/users/2/`
    To a user's todos `https://jsonplaceholder.typicode.com/users/2/todos`
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = base_url + 'users/'
    file_name = 'todo_all_employees.json'

    with open(file_name, 'w') as f:
        users_dict = {}
        for user in requests.get(users_url).json():
            user_id = str(user.get('id'))
            tasks_list = []
            user_todos_url = users_url + user_id + '/todos'
            user_todos = requests.get(user_todos_url).json()
            for todo in user_todos:
                task_dict = {"username": user.get('username'),
                             "task": todo.get('title'),
                             "completed": todo.get('completed')}
                tasks_list.append(task_dict)
            user_dict = {user_id: tasks_list}
            users_dict.update(user_dict)
        json.dump(users_dict, f)
