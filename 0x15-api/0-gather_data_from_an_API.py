#!/usr/bin/python3
"""
Using `https://jsonplaceholder.typicode.com/` REST API
Use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output
the employee TODO list progress in this exact format:
    First line: Employee EMPLOYEE_NAME is done\
    with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks,\
            which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""


from sys import argv
import requests

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
    user = requests.get(users_url + user_id).json()
    user_todos_url = users_url + user_id + '/todos'
    user_todos = requests.get(user_todos_url).json()
    completed_todos = 0
    completed_todos_titles = []

    for todo in user_todos:
        if todo.get("completed") is True:
            completed_todos += 1
            completed_todos_titles.append(todo.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), completed_todos, len(user_todos)
    ))
    for todo_titles in completed_todos_titles:
        print('\t {}'.format(todo))
