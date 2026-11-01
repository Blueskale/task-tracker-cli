# Task Tracker CLI

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white) ![Dependencies](https://img.shields.io/badge/dependencies-none-7aa2f7) ![Storage](https://img.shields.io/badge/storage-JSON-bb9af7)

A simple command-line task tracker built with Python.

The application allows users to create, update, delete, and manage tasks directly from the terminal. Tasks are stored locally in a JSON file.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as done
* Mark tasks as in-progress
* List all tasks
* Filter tasks by status
* Automatically generate task IDs
* Store task data using JSON

## Technologies

* Python
* JSON
* Command-line arguments (`sys.argv`)
* File handling
* Git

## Installation

Requires Python 3.6 or newer. Clone the repository:

```bash
git clone https://github.com/Blueskale/task-tracker-cli.git
```

Navigate into the project:

```bash
cd task-tracker-cli
```

No external Python packages are required.

## Usage

### Add a Task

```bash
python tracker.py add "Learn Python"
```

### Update a Task

```bash
python tracker.py update 1 "Learn advanced Python"
```

### Delete a Task

```bash
python tracker.py delete 1
```

### Mark a Task as Done

```bash
python tracker.py mark-done 1
```

### Mark a Task as In-Progress

```bash
python tracker.py mark-in-progress 1
```

### List All Tasks

```bash
python tracker.py list
```

### List Tasks by Status

List tasks that are still to do:

```bash
python tracker.py list todo
```

List completed tasks:

```bash
python tracker.py list done
```

List tasks currently in progress:

```bash
python tracker.py list in-progress
```

## Data Storage

Tasks are stored locally in a `tasks.json` file.

Each task contains an ID, description, and status.

Example:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "todo"
}
```

The `tasks.json` file is excluded from Git using `.gitignore` because it contains local task data.

If the file does not exist, the application automatically creates it.

## How It Works

The application uses Python's `sys.argv` to receive commands and arguments from the terminal.

For example:

```bash
python tracker.py add "Learn Python"
```

The arguments are received by Python as:

```text
sys.argv[0] → tracker.py
sys.argv[1] → add
sys.argv[2] → Learn Python
```

The program then passes the appropriate arguments to functions such as `add_task()`, `delete_task()`, and `update_task()`.

The tasks are represented in Python as a list of dictionaries and are converted to JSON when saved to `tasks.json`.

## What I Learned

This project helped me practice:

* Python functions
* Function parameters and arguments
* Lists and dictionaries
* Loops and conditionals
* Command-line arguments using `sys.argv`
* Converting command-line strings to integers
* Reading and writing JSON
* File handling
* Checking whether files exist
* CRUD operations
* Persistent data storage
* Git and GitHub

## Future Improvements

* Add automated tests
* Improve command-line validation
* Refactor repeated code
* Add better error handling
* Use `argparse` for command-line argument parsing
* Improve the user interface and command output
