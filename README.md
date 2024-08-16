# Django Restricted Access Project

This project is a Django-based web application that implements restricted access to certain pages. Users must log in to view these pages. If they do not have the necessary permissions, they will be denied access.

## Features

- **User Authentication**: Users can log in to access restricted pages.
- **Permission Checks**: Specific pages are restricted based on user permissions.
- **Bootstrap Styling**: The project uses Bootstrap for a responsive and modern user interface.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/django-restricted-access.git
    cd django-restricted-access
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (optional):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Login**: Visit `/login/` to log in with your credentials.
   
2. **Restricted Page**: After logging in, you can visit the `/restricted/` page. If your user account has the necessary permissions, you will be granted access. Otherwise, you will see a message indicating that access is denied.

## File Structure

- **`restricted/templates/restricted/check_permission.html`**: Template to check and display user permissions for accessing a restricted page.
- **`restricted/templates/registration/login.html`**: Login page template.
- **`restricted/templates/restricted/restricted_page.html`**: Restricted content page that displays content only to users with the appropriate permissions.
- **`urls.py`**: Defines the URL routes for login and restricted pages.
- **`views.py`**: Contains the logic for handling user authentication and permission checks.
- **`models.py`**: Defines the models for managing restricted content (if applicable).

## Customization

- **Styling**: The project uses Bootstrap for UI styling. You can customize the look and feel by modifying the HTML templates or adding your own CSS.
- **Permissions**: Modify the permission logic in `views.py` to change which users have access to restricted pages.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

