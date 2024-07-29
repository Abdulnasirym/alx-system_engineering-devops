#!/usr/bin/env python3
"""returns information about his/her TODO list progress"""

import request
import sys

if __name__ == "__main__":
    completed = []
    url = https://jsonplaceholder.typicode.com/
    user = request.get("url + user/{}".format(sys.argv[1])).json()
    todos = request.get("url + todos/", params={"userId": sys.argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
