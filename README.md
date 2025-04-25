# Task-Tracker
This was a mini project of a task manager made in python 3. Its syntax is relatively simple and can be run on any distro.

What it does is create a JSON file and modify it according to the commands passed; adding, modifying and deleting tasks according to the user's wishes.

---

### Install

The command below can be used to easily install the tool.

```
git clone https://www.github.com/kenshin-kuntarou/Task-Tracker/ 
```

### Commands

You can add tasks.

```
python3 task-cli.py -add 'My Task'

```

You can delete tasks from `id`.

```
python3 task-cli.py -delete 1 
```

You can update description

```
python3 task-cli.py -update 1 'My new task to do'
```

You can change the status (`mark-in-progress` \ `-mark-done`)

```
python3 task-cli.py -mark-done 1
```

You can list all the tasks (`done` \ `not-done` \ `in-progress`)

```
python3 task-cli -list all
```

---
