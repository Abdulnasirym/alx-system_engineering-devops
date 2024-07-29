#!/usr/bin/env python3
"""returns information about his/her TODO list progress"""

import request
import sys

if __name__ == "__main__":
    completed = []
    url = https://jsonplaceholder.typicode.com/
    user = request.get("url + user/{}".format(sys.argv[1])).json()
    todos = request.get("url + todos/", params={"userId": sys.argv[1]}).json()

    for task in todos:
        if task.get('completed') is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
