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

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>  
    </head>
<body>
    <!-- {{ variable_name }} -->
    {% if books %}
         {% for book in books %}                                                   
             <h1>{{book.title}} by {{book.author}}.</h1>
             <p>Published: {{book.publication_date}}. Page Count: {{book.page_count}}.</p>
         {% empty %}
            <p>No books found.</p>
         {% endfor %}
    {% else %}
        <p>There was an error retrieving the books.</p>
    {% endif %}                   
</body>
</html>
```

    URL Patterns -> Defines how URLs map to functions in your application.

    To make our view accessible through the web we need to define it in urlpatterns list inside urls.py file located at /books    
    To make our view available through the web we need to link it to a url pattern.
    In order to do this we have to define a new urlpattern inside the "urlpatterns" list in the main urls.py file

