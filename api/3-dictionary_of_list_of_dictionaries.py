#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    usernames = {}
    all_tasks = {}
    for user in users:
        usernames[user.get("id")] = user.get("username")
        all_tasks[str(user.get("id"))] = []

    for task in todos:
        user_id = task.get("userId")
        all_tasks[str(user_id)].append({
            "username": usernames.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
