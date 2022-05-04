# RememberTheCoders

Welcome to your final project of the JTC course! This one is called "The Dream Project"

## Mission Staement 


## The Dream Project Wireframe

Each member collaborated on the wireframe, which is a visual guide representing what our site will look like, and what features it will have and how the user will interact with the app.

## 1-page written proposal

-   **Paragraph(s) 1-2:** A summary of your app's MVP functionality. The overall functionality employs **CRUD** (Create, Read, Update, Delete) operations:
    -   **Create** - The app allows a user to create items in the database. E.g. when a user adds a todo item in the todo app, the todo item is added to the database.
    -   **Read** - The app read items from a database. E.g. Displaying one or more todo items on a page in the todo app, the todo items are read from the database.
    -   **Update** - The app must allow a user to update items in the database, E.g. when a user edits a todo item in the todo app and saves it, the todo item is updated in the database.
    -   **Delete** - The app allows a user to delete items in the database. E.g. when a user removes a todo item in the todo app, the todo item is deleted from the database.

## Proposal Part 2: Entity-Relationship Diagram Models

-   The point of the ER Diagram is to map out visually what the database will look like.
-   This Diagram outline **1 one-to-many** and **1 many-to-many** entity relationships.


# 1. Get set up for Django

* First, lets setup our virtual environment and server to run the app 
- Run `python3 -m venv venv` (or whichever version of this your computer uses) to create a new virtual environment (it's common practice to name your virtual environment 'venv')
- Run `source django-env/bin/activate` on Unix/MacOS or `django-env\Scripts\activate.bat` on Windows to activate the virtual environment (or whichever instruction works for you!)
- Run `pip install django` to install Django

## Run the Django Server

Use the `manage.py` file to run the server!

```
python manage.py runserver

- Go to `localhost:8000` and you should see the app home screen!








