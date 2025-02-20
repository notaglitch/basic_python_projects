import argparse
import os
import json

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)
    
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "description": description
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"{task['id']}: {task['title']} - {task['description']}")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(updated_tasks) == len(tasks):
        print(f"No task found with ID {task_id}.")
        return
    
    save_tasks(updated_tasks)
    print(f"Task with ID {task_id} has been deleted.")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('title', help="Title of the task")
    add_parser.add_argument('description', help="Description of the task")

    subparsers.add_parser('view', help="View all tasks")

    delete_parser = subparsers.add_parser('delete', help="Delete a task by its ID")
    delete_parser.add_argument('task_id', type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.title, args.description)
    elif args.command == 'view':
        view_tasks()
    elif args.command == 'delete':
        delete_task(args.task_id)
    else:
        print("Invalid command. Use 'add', 'view', or 'delete'.")

if __name__ == '__main__':
    main()
