import argparse
import json
import datetime

class Task_Manager:
    def __init__(self):
        self.tasks = dict()
        self.ids = int(1)
        self.date = datetime.datetime.now()

    def json_converter(self):
        with open("tasks.json", encoding="UTF-8", errors="ignore", mode="w") as file:
            json.dump(self.tasks, file, indent=4)

        with open("tasks.json", errors="ignore", mode="r") as file:
            print(file.read())
    
    def json_atualizer(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

        except FileNotFoundError:
            self.tasks = dict()
            self.ids = int(1) 

    def add_task(self, task_name):
        while str(self.ids) in self.tasks.keys():
            self.ids += 1
        
        self.tasks.update({int(self.ids): {
            "name": str(task_name),
            "status": "off",
            "description": str(),
            "date_create": str(self.date),
            "date_update": str(self.date)}})

    def update_task(self, task_id, task_description):
        self.tasks[str(task_id)].update({
            "description": str(task_description),
            "date_update": str(self.date)})

    def delete_task(self, task_id):
        del self.tasks[str(task_id)]

    def mark_progress_task(self, task_id):
        self.tasks[str(task_id)].update({
            "status": "in-progress"})

    def mark_done_task(self, task_id):
        self.tasks[str(task_id)].update({
            "status": "done"})

    def task_list(self, task_filter):
        if task_filter == "all":
            print(json.dumps(self.tasks, indent=4))
            return

        found = False
        for task_id, task_info in self.tasks.items():
            if task_info["status"] == task_filter:
                print(json.dumps({task_id: task_info}, indent=4))
                found = True

        if not found:
            print(f"Don't exist any task with status '{task_filter}'")


def main():
    parser = argparse.ArgumentParser(description="args for tasks")
    
    parser.add_argument("-add", type=str, help="\tAdd task")
    parser.add_argument("-update", nargs=2, metavar=("ID", "DESCRIPTION"), help="\tUpdate description")
    parser.add_argument("-delete", type=int, help="\tDelete task")
    parser.add_argument("-mark-in-progress", type=int, help="\tMark task in progress")
    parser.add_argument("-mark-done", type=int, help="\tMark task as done")
    parser.add_argument("-list", choices=["all", "done", "off", "in-progress"], help="\tList the tasks" )

    args = parser.parse_args()
    task_manager = Task_Manager()

    while True:
        task_manager.json_atualizer()
        
        if args.add:
            task_manager.add_task(args.add)

        if args.update:
            task_id, description = args.update
            task_manager.update_task(task_id, description)

        if args.delete:
            task_manager.delete_task(args.delete)

        if args.mark_in_progress:
            task_manager.mark_progress_task(args.mark_in_progress)

        if args.mark_done:
            task_manager.mark_done_task(args.mark_done)
        
        if args.list:
            value = args.list
            task_manager.task_list(value)
            break

        task_manager.json_converter()
        break

if __name__ == "__main__":
    main()
