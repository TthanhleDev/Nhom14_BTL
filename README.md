# Spotify Backend Project

This is a Django-based backend project for a Spotify-like application, utilizing Django REST Framework, JWT authentication, WebSockets with Channels, and MySQL as the database.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.8+
- MySQL (via XAMPP or standalone installation)
- Redis (for WebSocket channel layers)
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Setup Instructions

### 1. Clone the Repository
Clone the project repository to your local machine:
```bash
git clone <repository-url>
cd backend
```

### 2. Create a Virtual Environment
Create and activate a Python virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```
**Note**: If `requirements.txt` is not provided, install the following core packages:
```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers channels daphne channels-redis mysqlclient
```

### 4. Set Up MySQL Database
1. Start your MySQL server (e.g., via XAMPP control panel).
2. Create a database named `spotify`:
   ```sql
   CREATE DATABASE spotify;
   ```
3. Verify the database settings in `backend/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'spotify',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
   Update `USER`, `PASSWORD`, `HOST`, or `PORT` if your MySQL configuration differs.

### 5. Set Up Redis
1. Install and start Redis on your machine:
   - **Windows**: Download Redis from [redis.io](https://redis.io/download) or use a Redis Docker container.
   - **Mac/Linux**: Install via package manager (e.g., `brew install redis` or `sudo apt install redis-server`).
2. Ensure Redis is running on `localhost:6379` (default). Update `CHANNEL_LAYERS` in `backend/settings.py` if using a different host/port:
   ```python
   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               "hosts": [('127.0.0.1', 6379)],
           },
       },
   }
   ```

### 6. Apply Migrations
Run Django migrations to set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Optional)
Create an admin user to access the Django admin panel:
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
The server will be available at `http://localhost:8000`.

### 9. Test the Application
- Access the Django admin panel at `http://localhost:8000/admin` (login with superuser credentials).
- Test API endpoints using tools like Postman or cURL, ensuring CORS settings allow your frontend (e.g., `http://localhost:3000`).
- Verify WebSocket functionality if implemented in the `api` app.

## Project Structure
- `backend/`: Main Django project directory.
- `api/`: Custom app for API logic (ensure it’s created and registered in `INSTALLED_APPS`).
- `media/`: Directory for uploaded media files.
- `backend/settings.py`: Configuration for Django, REST Framework, JWT, CORS, and Channels.
- `backend/urls.py`: Root URL configurations.
- `backend/asgi.py`: ASGI configuration for WebSocket support.

## Configuration Notes
- **CORS**: The project allows connections from `http://localhost:3000`, `http://localhost:5173`, etc. Update `CORS_ALLOWED_ORIGINS` in `settings.py` for additional frontend URLs.
- **JWT**: Access tokens expire after 60 minutes, and refresh tokens after 7 days. Adjust `SIMPLE_JWT` settings as needed.
- **Media Files**: Uploaded files are stored in the `media/` directory. Ensure proper permissions.
- **Debug Mode**: `DEBUG = True` is set for development. Set to `False` in production and configure `ALLOWED_HOSTS`.

## Troubleshooting
- **MySQL Errors**: Ensure MySQL is running and the `mysqlclient` package is installed (`pip install mysqlclient`).
- **Redis Errors**: Verify Redis is running and accessible at `127.0.0.1:6379`.
- **CORS Issues**: Check `CORS_ALLOWED_ORIGINS` in `settings.py` matches your frontend’s URL.
- **Dependency Issues**: Ensure all required packages are installed and compatible with your Python version.

## Additional Notes
- For production, secure the `SECRET_KEY`, disable `DEBUG`, and configure a production-grade ASGI server (e.g., Daphne or Uvicorn).
- Consider using environment variables (e.g., via `python-decouple`) for sensitive settings like `SECRET_KEY` and database credentials.
- Refer to the [Django documentation](https://docs.djangoproject.com/en/5.1/) and [Channels documentation](https://channels.readthedocs.io/) for advanced configurations.
