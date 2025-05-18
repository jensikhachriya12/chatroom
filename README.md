chatroom:

A chat room is an online platform where multiple users can communicate with each other in real-time. 
In a Python-based real-time chat application, messages are sent and received instantly, allowing seamless interaction between users.

WORK:

User Logs In → Authenticated users can access chatrooms.
Chatroom Selection → Users choose a chatroom or start a private conversation.
Real-Time Messaging → Messages are instantly sent and displayed.
Database Storage → Messages are saved for record-keeping.
Live Updates → New messages appear in real time without refreshing the page.

FRAMEWORK:

Use web frameworks like Django to create a web-based chat application.
These frameworks allow you to build web applications where users can interact through a web interface.

LIBRARIES: 
1.	Django Authentication(django.contrib.auth): Manages user authentication (login, logout, user registration). 

2.	 Messages Framework( django.contrib.messages): Provides a way to display temporary messages to users.

3.	Admin Interface(django.contrib.admin):   Django’s built-in admin panel to manage database models.

    Allows developers to create an admin dashboard without writing extra code.

    Provides CRUD (Create, Read, Update, Delete) operations for models.

4.	URL Dispatcher(django.urls.path): Handles routing of URLs to views in Django.

5.	Settings Configuration(django.conf.settings): Provides access to Django’s global settings (e.g., database settings, static files, middleware).


6.	Django ORM for Databases(django.db.models): Used to define database models in Django.

FEATURES:

o	User authentication: User authentication is a crucial part of a chatroom application to ensure that only registered users can join and participate in conversations.

o	Real-Time Messaging: Users can send and receive messages instantly due to the real-time capabilities provided by Django Channels.

o	Multiple Rooms: Users can join different chat rooms, each with its own set of participants and messages.

o	User Management: Users can be authenticated and managed within the chat application, allowing for features like private messaging and moderation.

   
•	Django installation Steps: 

Step 1: Install Python:
•	python –version

Step 2: Create a Virtual Environment:
	
•	python/py -m venv myenv
•	myenv\Scripts\activate

Step 3: Install Django:
•	pip install django  

Step 4: Verify Django Installation:
•	django-admin --version  

Step 5: Create a Django Project:
•	django-admin startproject myproject  

Step 6: Run the Development Server:
•	python/py manage.py runserver

Setp 7: Succesfull Django install:
•	Open a web browser and go to http://127.0.0.1:8000/ to see your Django project running


  


