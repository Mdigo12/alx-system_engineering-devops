#!/usr/bin/python3
"""
Using `https://jsonplaceholder.typicode.com/` REST API
Use urllib or requests module

Script to export data in the CSV format
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",\
        "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},\
            {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,\
                  "username": "USERNAME"}, ... ]}

File name must be: USER_ID.json
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    """
    Sample URLs
    To users`https://jsonplaceholder.typicode.com/users/`
    To a user `https://jsonplaceholder.typicode.com/users/2/`
    To a user's todos `https://jsonplaceholder.typicode.com/users/2/todos`
    """
    user_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = base_url + 'users/'
    user_todos_url = users_url + user_id + '/todos'
    user = requests.get(users_url + user_id).json()
    user_todos = requests.get(user_todos_url).json()
    file_name = user_id + '.json'

    with open(file_name, 'w') as f:
        tasks_list = []
        for todo in user_todos:
            task_dict = {"Task": todo.get('title'),
                         "completed": todo.get('completed'),
                         "username": user.get('username')}
            tasks_list.append(task_dict)
        # print(tasks_list)
        user_dict = {user_id: tasks_list}
        # print(user_dict)
        json.dump(user_dict, f)
