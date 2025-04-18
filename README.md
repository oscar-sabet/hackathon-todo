# Django To-Do List Application

## Links

[Project Board](https://github.com/users/oscar-sabet/projects/5)

[Github Repo](https://github.com/oscar-sabet/hackathon-todo)

[Deployed App](https://todo-hack-b58aed29fc9d.herokuapp.com/)

## Description

This is a Django-based web application designed to help users manage their tasks effectively. The app allows users to create, read, update, and delete tasks, with additional functionality for filtering tasks by user, setting the priority of the task, and updating the individual task's status, e.g., marking tasks as completed.

## Features

- **User Authentication:** Secure login/logout functionality.
- **CRUD Operations:** Users can create, view, edit, and delete tasks.
- **Task Filtering:** Display the priority and status of tasks for better organisation.
- **Status Updates:** Mark tasks as completed or in progress.
- **Responsive Design:** A user-friendly interface that works seamlessly across devices.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** Heroku
- **Version Control:** Git and Github

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/oscar-sabet/hackathon-todo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo-name
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your browser and go to `http://127.0.0.1:8000/`.
2. Register or log in to manage your tasks.
3. Create, edit, or delete tasks as needed.
4. Filter tasks by due date or update their status.

## Project Structure

## Acknowledgements

This project was created using the Django framework with assistance from Microsoft CoPilot. 

*Resources Used*

[Doodle CSS Pack](https://chr15m.github.io/DoodleCSS/)

[Images](https://cdn.lapa.ninja/assets/images/backer-news.webp )

## Screenshots

Landing Page

![Landing Page](readme/todo-hack-b58aed29fc9d.herokuapp.com_.png)

Task List

![Task List](readme/todo-hack-b58aed29fc9d.herokuapp.com_task_list_.png)

Project Board

![Project Board](readme/todo-hack-b58aed29fc9d.herokuapp.com_board_.png)
