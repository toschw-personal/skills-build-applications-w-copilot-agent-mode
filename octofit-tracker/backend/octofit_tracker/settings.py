# Add MongoDB database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Explicitly define INSTALLED_APPS and MIDDLEWARE if they are not already defined
if 'INSTALLED_APPS' not in globals():
    INSTALLED_APPS = [
        'corsheaders',
        'octofit_tracker',
    ]

if 'MIDDLEWARE' not in globals():
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    ]

# Ensure INSTALLED_APPS and MIDDLEWARE are defined before appending or modifying them
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djongo',
    'corsheaders',
    'octofit_tracker',
]

MIDDLEWARE = [
    # Default Django middleware can be added here
] + MIDDLEWARE if 'MIDDLEWARE' in globals() else [
    'corsheaders.middleware.CorsMiddleware',
]

# Enable CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']