# cosmodrome

# Introduction
Welcome to our Django-based application. This project is designed to manage tasks with a streamlined user interface, providing features such as task creation, user management, and pagination. The application aims to simplify the process of task tracking and user management within an organization or personal projects.

# Key Features
1) Task Management
- Create, View, and Edit Tasks: Users can create new tasks, view task details, and edit existing tasks with ease.
- Pagination: Efficiently browse through tasks using pagination on the task list page for better navigation and performance.
  
2) User Management
- User Creation: Admins can create new users through a dedicated form, simplifying user onboarding.
- User Information: View and update user details to manage profiles effectively.

3) Tags Management
- Tag Creation and Management: Add and manage tags associated with tasks, enhancing organization and searchability.

4) Admin Panel
- Admin Interface: A comprehensive admin panel for managing the application’s data and configurations, providing robust control and oversight.

# Installation Instructions
- git clone https://github.com/Timur5050/cosmodrome.git
- cd cosmodrome
- python -m venv env
- env\Scripts\activate or source env/bin/activate on mac
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- go to http://127.0.0.1:8000/

# Usage Guide
- Main Page, URL: /, View: index. This is the main landing page of the application.
- User Registration, URL: /registration/, View: user_creation_view. Allows users to register a new account.
- User Profile, URL: /profile/<int:pk>/, View: user_profile_view. Displays information about a specific user.
- Racket List, URL: /rackets/, View: racket_list_view. Displays a list of rackets, with pagination.
- Racket Creation, URL: /rackets/create/, View: racket_create_view. Allows users to create a new racket.
- Racket Details, URL: /rackets/<int:pk>/details/, View: racket_details. Displays the details of a specific racket.
- Astronaut List, URL: /astronauts/, View: astronaut_list_view. Displays a list of astronauts, with pagination.
- Astronaut Creation, URL: /astronauts/create/, View: astronaut_create_view. Allows users to create a new astronaut.
- Astronaut Details, URL: /astronauts/<int:pk>/details/, View: astronaut_details. Displays the details of a specific astronaut.
- Flight List, URL: /flights/, View: flight_list_view. Displays a list of flights, with pagination.
- Flight Creation, URL: /flights/create/, View: flight_list_create. Allows users to create a new flight.
- Flight Details, URL: /flights/<int:pk>/details/, View: flight_details. Displays the details of a specific flight.


# demo
![Website Interface](demo.png)

