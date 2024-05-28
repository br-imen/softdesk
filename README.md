# SoftDesk API

## Description
SoftDesk is an API designed to report and track technical issues efficiently. This repository contains the backend code necessary for managing user accounts, handling issue reports, and tracking the status of these reports.

## Features
- User authentication and management
- Project creation and management
- Issue reporting and tracking
- Comments on issues

## Technologies
- Python
- Django
- Django REST framework
- Pipenv

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/br-imen/softdesk.git
    ```
2. Navigate to the project directory:
    ```bash
    cd softdesk
    ```
3. Install the required packages using Pipenv:
    ```bash
    pipenv install
    ```

## Usage

1. Apply migrations:
    ```bash
    pipenv run python manage.py migrate
    ```
2. Create a superuser:
    ```bash
    pipenv run python manage.py createsuperuser
    ```
3. Run the server:
    ```bash
    pipenv run python manage.py runserver
    ```

## Endpoints

- **User Management**
  - `POST /signup/` - Create a new user
  - `POST /login/` - Login a user

- **Projects**
  - `GET /projects/` - List all projects
  - `POST /projects/` - Create a new project
  - `GET /projects/{id}/` - Retrieve a project

- **Issues**
  - `GET /projects/{project_id}/issues/` - List all issues for a project
  - `POST /projects/{project_id}/issues/` - Create a new issue
  - `GET /issues/{id}/` - Retrieve an issue

- **Comments**
  - `GET /issues/{issue_id}/comments/` - List all comments for an issue
  - `POST /issues/{issue_id}/comments/` - Add a comment to an issue
  - `GET /comments/{id}/` - Retrieve a comment

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues and pull requests for improvements.

## Contact
For any questions or support, please contact the repository owner through GitHub.

## Authors and acknowledgments
Special Thanks to my mentor Amine SGHIR and OpenClassrooms.
