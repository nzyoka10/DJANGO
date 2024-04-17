# Python - DJANGO FRAMEWORK

<!-- 
    1. Create virtual environment
       1. py -m venv venv
   
    2. Activate the virtual environment
       1. source venv/Scripts/activate
   
    3. Install Django in the virtual environment
       1. py -m install Django
   
    4. Start a new project using django-admin startproject projectName
       1. django-admin startproject appName .
   
    5. Change directory to the project folder 
       1. cd projectName
   
    6. Run python manage.py runserver to start the server
       1. py manage.py runserver
   
    7.  Open http://localhost:8000 on your browser, you should see "Welcome to Django" if everything is set up correctly.
   
    8.  Press [CTRL + C] to Stop the server.
   
 #  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ******************************** ******************************** ********************************

    Django Create App
      - An App is a web application that has a specific meaning in a project, like, a home page, or a contact form, or memebers database. 

    # create app
    django-admin startapp appName
    # add 'appName' to INSTALLED_APPS of project settings file (settings.py)


    Django Views
        - Django views are python functions that take http request and returns http response, like HTML documents.
        - A web page that uses DJANGO is full of views with different tasks and missions, 
        - VIEWS are usually put in a file called vies.py LOCATED on apps folder.

    Django URLs
       - #create file name urls.py in same folder as the views.py file,

    Django Templates
       - 
-->

### Course Outline

## Module 1: Introduction to Django
- Overview of Django framework
- History and evolution of Django
- Setting up Django environment
- Creating a sample project

## Module 2: Django Models
- Introduction to Django Models
- Defining models
- Django ORM (Object-Relational Mapping)
- Working with database migrations

## Module 3: Django Views
- Understanding Django views
- Class-based views vs Function-based views
- URL routing and view functions
- Request and response handling

## Module 4: Django Templates
- Introduction to Django templates
- Template language basics
- Template inheritance and inclusion
- Building dynamic templates

## Module 5: Django Forms
- Handling forms in Django
- Using Django forms for user input
- Form validation and error handling
- Customizing form behavior

## Module 6: Django Admin
- Exploring Django Admin interface
- Customizing Django Admin
- Registering models with Django Admin
- Adding actions and filters to Django Admin

## Module 7: Django Security
- Common security threats in web applications
- Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF)
- Authentication and authorization in Django
- Securing Django applications

## Module 8: Django REST Framework
- Introduction to Django REST Framework (DRF)
- Building RESTful APIs with DRF
- Serializers and views in DRF
- Authentication and permissions in DRF

## Module 9: Testing in Django
- Writing unit tests for Django applications
- Test-driven development (TDD) approach
- Testing Django views, models, and forms
- Using Django testing utilities

## Module 10: Deployment and Scaling
- Preparing Django application for deployment
- Deploying Django application on popular hosting platforms
- Scaling Django applications
- Best practices for Django deployment

## Module 11: Advanced Django Topics (Optional)
- Caching in Django
- Asynchronous tasks with Celery
- Integrating Django with frontend frameworks
- Building real-time applications with Django Channels

## Module 12: Project Work
- Working on a real-world Django project
- Applying concepts learned throughout the course
- Collaboration and code reviews
- Presentation of the project

## Conclusion
- Recap of key concepts learned
- Next steps in Django development
- Resources for further learning

