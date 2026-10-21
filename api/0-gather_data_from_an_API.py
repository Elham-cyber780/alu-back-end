#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for title in done_tasks:
        print("\t {}".format(title))
