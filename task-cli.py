import argparse
import json

class Task_Manager:
    def __init__(self):
        self.tasks = dict()
        self.ids = 1

    def json_converter(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)
        with open("tasks.json", "r") as file:
            print(file.read())
    
    def task_atualizer(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

        except FileNotFoundError:
            self.tasks = dict()
            self.ids = 0

    def add_task(self, task_name):
        self.task_atualizer()
        
        while str(self.ids) in self.tasks.keys():
            self.ids += 1
        
        self.tasks.update({int(self.ids): {
            "name": str(task_name),
            "progress": str(),
            "description": str()}})
        self.json_converter()

    def update_task(self, task_update):
        self.task_atualizer()
        self.tasks[task_update].update({
            "description": str(task_update)})
        self.json_converter()

    def delete_task(self, task_id):
        self.task_atualizer()
        del self.tasks[str(task_id)]
        self.json_converter()

    def mark_progress_task(self, task_id):
        self.task_atualizer()
        self.tasks[str(task_id)].update({
            "progress": "in progress"})
        self.json_converter()

    def mark_done_task(self, task_id):
        self.task_atualizer()
        self.tasks[str(task_id)].update({
            "progress": "done"})
        self.json_converter()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="args for tasks")

    parser.add_argument("-add", type=str, help="Add task")
    parser.add_argument("-update", type=str and int, help="Update task")
    parser.add_argument("-delete", type=int, help="Delete task")
    parser.add_argument("-mark-in-progress", type=int, help="Mark task in progress")
    parser.add_argument("-mark-done", type=int, help="Mark task as done")

    args = parser.parse_args()
    task_manager = Task_Manager()


    if args.add:
        task_manager.add_task(args.add)

    if args.update:
        task_manager.update_task(args.update)

    if args.delete:
        task_manager.delete_task(args.delete)

    if args.mark_in_progress:
        task_manager.mark_progress_task(args.mark_in_progress)

    if args.mark_done:
        task_manager.mark_done_task(args.mark_done)
