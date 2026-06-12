# 📘 Assignment: Building a CRUD Web App with Flask

## 🎯 Objective

Build a simple web application using Flask. Learn how to handle browser requests, render HTML pages, and implement create/read/update/delete (CRUD) operations using Python.

## 📝 Tasks

### 🛠️ Set up the Flask application

#### Description
Create the Flask application and route the homepage so users can see the web app running.

#### Requirements
Completed program should:

- Create a Flask app instance
- Define a route for `/` that returns an HTML page listing items
- Start the Flask development server successfully

### 🛠️ Add create and read functionality

#### Description
Add a form to add new items and display the current item list on the homepage.

#### Requirements
Completed program should:

- Include a `POST` route to add new items from form data
- Store items in an in-memory list
- Display all stored items on the homepage

### 🛠️ Add update and delete operations

#### Description
Extend the app to support editing and removing items from the list.

#### Requirements
Completed program should:

- Provide routes for updating items by ID
- Provide routes for deleting items by ID
- Update the homepage to offer edit and delete actions for each item

---

## 💻 Run the app

Install Flask and run the starter code with:

```bash
pip install flask
python starter-code.py
```

Open `http://127.0.0.1:5000` in your browser to use the app.
