# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using Python and the FastAPI framework. Learn how to define API routes, validate request data with Pydantic models, and run a local development server.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Set up a FastAPI application and add basic API routes for returning JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI app instance with `FastAPI()`
- Add a root endpoint `/` that returns a welcome message
- Add a `GET /items/{item_id}` endpoint that returns item details or an error message

### 🛠️ Add request models and a POST endpoint

#### Description
Define a Pydantic model for items and add an endpoint that creates new items from request data.

#### Requirements
Completed program should:

- Define an `Item` model using `BaseModel`
- Add a `POST /items/` endpoint that accepts an `Item` in the request body
- Append the new item to the in-memory list and return it in the response

### 🛠️ Add update and delete functionality

#### Description
Extend the API with endpoints for updating and deleting items.

#### Requirements
Completed program should:

- Add a `PUT /items/{item_id}` endpoint to update an item by ID
- Add a `DELETE /items/{item_id}` endpoint to remove an item by ID
- Return clear success or error messages for each operation

---

## 💻 Run the API

Use the following command to start the development server:

```bash
uvicorn starter-code:app --reload
```
