# To-Do List Manager

This Python script is a command-line tool for managing a to-do list, utilizing the `InquirerPy` library for a user-friendly interface. The script supports basic task management features and stores tasks in a file for persistence.

## Features

- **Add Tasks**: Prompts you to enter new tasks and saves them to the list.
- **Delete Tasks**: Allows you to select and remove tasks from the list.
- **View Tasks**: Displays all the current tasks in the list.
- **Persistent Storage**: Tasks are stored in `todolist.txt`, ensuring they persist across sessions.

## How It Works

1. **Loading Tasks**: When the script starts, it reads tasks from `todolist.txt` if the file exists. If the file is not found, it initializes with an empty list.
2. **User Interaction**: The script presents a menu to the user with options to add, delete, or view tasks.
3. **Adding Tasks**: Users can input new tasks, which are appended to the list and saved to the file.
4. **Deleting Tasks**: Users can select tasks from the list to remove, and the list is updated accordingly.
5. **Viewing Tasks**: Displays a numbered list of all current tasks for easy review.

## Requirements

- Python 3.12.4
- `InquirerPy` library

## Installation

1. Install the `InquirerPy` library using pip:

   ```bash
   pip install InquirerPy
