# CRM-in-django

## Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Nandhukriss/CRM-in-django.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd crm
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install project dependencies using the requirements file:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Create a superuser (if needed):**

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the Django development server.

## Without Customer Data
![home](https://github.com/Nandhukriss/CRM-in-django/assets/103727372/63f84067-831a-4cb8-a488-1843bbcb3307)

## With Customer Data

![allusers](https://github.com/Nandhukriss/CRM-in-django/assets/103727372/197cb039-cced-40a9-b7fe-66fc3cf7543f)

## Delete Action

![Delete](https://github.com/Nandhukriss/CRM-in-django/assets/103727372/c280a239-2184-437d-8c97-348a46658329)
