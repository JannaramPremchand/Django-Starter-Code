# Django-Starter-Code
The Django Starter Code project is a foundational template designed to kickstart Django web development projects efficiently. It provides a structured starting point equipped with essential components to accelerate the setup process and streamline the development workflow.

This guide will help you set up a Django project with proper directory structure, static files, templates, and basic configuration.

### Step 1: Install Virtual Environment
pip install virtualenv


### Step 2: Create and Activate a Virtual Environment
virtualenv venv
.\venv\Scripts\Activate



### Step 3: Install Django
pip install django


### Step 4: Create a Django Project
django-admin startproject config .


### Step 5: Create a Django App
cd config
python manage.py startapp core


### Step 6: Create Directories

Inside the main project folder (`config`), create the following directories:

- `static` (for static files)
- `templates` (for HTML templates)

Inside the `static` folder:

- `css` (for CSS files)
- `js` (for JavaScript files)
- `images` (for image files)

Inside the `templates` folder:

- `base_templates` (for base HTML files)
- `core_templates` (for core application HTML files)
- `auths_templates` (for authentication and authorization HTML files)

### Step 7: Configuration in `settings.py`

In `config/settings.py`, add the following configurations:

import os

# Add 'core' app to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'core',
]

# Add template directories
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


### Step 8: URL Configuration

In `config/urls.py`, configure the URL patterns:

python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


### Step 9: Check `urls.py` and `views.py`

Ensure that your `urls.py` and `views.py` files are properly configured according to your project requirements. These files handle URL routing and views, respectively.

### Step 10: Check Templates and Static Files

1. **Templates**:
   - Verify that your HTML templates, located in the `templates` directory, are correctly structured and named according to your project needs.
   - Ensure that templates are organized into appropriate folders (`base_templates`, `core_templates`, `auths_templates`) as per your project architecture.

2. **Static Files**:
   - Confirm that static files such as CSS, JavaScript, and images are placed in the `static` directory within your project.
   - Check that CSS files are located within the `css` folder, JavaScript files within the `js` folder, and images within the `images` folder.

### Step 11: Collect Static Files
python manage.py collectstatic


### Step 12: Database Migration
python manage.py makemigrations
python manage.py migrate


### Step 13: Run the Development Server
python manage.py runserver


Your Django project is now set up and ready for development. Ensure all configurations are correctly implemented and start building your web application!