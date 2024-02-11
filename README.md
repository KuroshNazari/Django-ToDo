#  Django Todo List App
This is a simple Django web application for managing todo lists and tasks. Users can create, view, and delete projects (todo lists) and tasks associated with each project. The tasks have attributes such as name, due time, priority, and status.

## Features

- Create and manage todo lists (projects).
- Add tasks to todo lists with details like name, due time, priority, and status.
- Change the status of tasks between Pending, In Progress, and Done.
- Delete tasks and projects.

- ## Setup

1. Make sure you have Python and Django installed on your system.
2. Clone this repository to your local machine.
   ```
   git clone https://github.com/KuroshNazari/Django-ToDo.git
   ```
3. Navigate to the project directory.
   ```
   cd todo-app
   ```
4. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```
5. Apply the database migrations.
   ```
   python manage.py migrate
   ```
6. Run the development server.
   ```
   python manage.py runserver
   ```
7. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage

- Visit the home page to view and manage your todo lists.
- Click on a specific project to view and manage its tasks.
- Use the "Add Task" button to create new tasks within a project.
- Edit or delete tasks as needed.
- Change the status of a task by clicking the "Next State" button.

## Project Structure

- **`todo/`**: Django app directory containing models, views, forms, and templates.
- **`static/`**: Static files (CSS, JavaScript) for styling the application.
- **`templates/`**: HTML templates for rendering views.

## Contributing

Feel free to contribute to this project by opening issues or creating pull requests. Follow the standard Git workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push your branch to your fork.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
