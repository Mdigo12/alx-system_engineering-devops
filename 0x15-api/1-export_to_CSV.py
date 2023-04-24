#!/usr/bin/python3
"""
Using `https://jsonplaceholder.typicode.com/` REST API
Use urllib or requests module

Script to export data in the CSV format
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME",\
        "TASK_COMPLETED_STATUS","TASK_TITLE"
        `"2","Antonette","False","suscipit repellat esse"`
File name must be: USER_ID.csv
"""

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
    file_name = user_id + '.csv'

    with open(file_name, 'w') as f:
        for todo in user_todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                user_id,
                user.get('username'),
                todo.get('completed'),
                todo.get('title')
                ))
