Yo, I see you're adding the logic to handle task creation and management. Let's update the README and task flow accordingly. Here's your updated **README.md** with the new logic, and I'll include the current `TaskViewSet` and `run_task` structure for clarity:

---

# UNIX Task Manager

Welcome to the **UNIX Task Manager**! 🚀 This is a simple, responsive, and powerful task manager app where you can register, log in, create tasks, view task details, and more. Powered by Django REST API on the backend and a smooth, minimal front-end interface.

## Features

- **User Authentication**: Register, log in, and access your personal tasks.
- **Task Management**: Create, view, and manage tasks in a clean UI.
- **Task Details**: View detailed task info including name, status, description, and timestamps.
- **Token-Based Authentication**: Secure login with token storage in the browser.
- **Task Execution**: Run background tasks asynchronously (like `sleep` for now) upon creation.
  
---

## Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/unix-task-manager.git
cd unix-task-manager
```

### 2. Backend Setup (Django)

- Create a **virtual environment**:
  ```bash
  python -m venv venv
  ```

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Apply migrations:
  ```bash
  python manage.py migrate
  ```

- Run the Django development server:
  ```bash
  python manage.py runserver
  ```

---

### 3. Frontend Setup

- Open `index.html` in any browser to see the frontend in action. (No additional setup required for the front end)

The frontend will automatically interact with the backend running at `http://localhost:8000`.

---

## API Endpoints

### **User Registration**

- **POST** `/userapi/register/`
  - Request body:
    ```json
    {
      "username": "yourusername",
      "email": "youremail@example.com",
      "password": "password123",
    }
    ```

### **User Login**

- **POST** `/userapi/login/`
  - Request body:
    ```json
    {
      "username": "yourusername",
      "password": "password123"
    }
    ```

- Response:
    ```json
    {
      "token": "your_token_here"
    }
    ```

### **Get Tasks**

- **GET** `/taskapi/tasks/`
  - Headers: `Authorization: Token your_token_here`
  - Response:
    ```json
    [
      {
        "id": 1,
        "name": "Task 1",
        "status": "pending"
      },
      {
        "id": 2,
        "name": "Task 2",
        "status": "completed"
      },
      {
        "id": 3,
        "name": "Task 3",
        "status": "running"
      }
    ]
    ```

### **Create Task**

- **POST** `/taskapi/tasks/`
  - Request body:
    ```json
    {
      "name": "New Task",
      "description": "Task description goes here."
    }
    ```

### **Get Task Detail**

- **GET** `/taskapi/tasks/{task_id}/`
  - Response:
    ```json
    {
      "id": 1,
      "name": "Task 1",
      "status": "Pending",
      "description": "Task description",
      "created_at": "2025-04-01T12:00:00Z",
      "updated_at": "2025-04-01T12:30:00Z",
      "completed_at": null
    }
    ```

---

## Task Flow

Tasks can be created and processed asynchronously. Here's how the process works:

1. **Task Creation**: 
   When a task is created, it is saved with a `PENDING` status.

2. **Asynchronous Execution**:
   After the task is created, it enters the background, and a worker starts executing the task asynchronously. For now, we simulate a task operation like `sleep` as an example.

3. **Task Update**:
   - During execution, the task status is updated to `RUNNING`.
   - After completion, the status is set to `COMPLETED`, and the completion timestamp is added.

4. **Failure Handling**:
   If any errors occur during task execution, the task's status will be set to `FAILED`.


---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Authentication**: Token-based authentication
- **Database**: SQLite (Django default, easy to swap for PostgreSQL or MySQL)
- **Async**: `asyncio` and `threading` for asynchronous task handling



---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Credits

Created with ❤️ by [jztchl](https://github.com/jztchl)

---

Now you have the README reflecting your updated task flow with the background processing of tasks. Each part of the code ties into the task handling process, so any task, for now, can be added for asynchronous execution like a simple `sleep`.
