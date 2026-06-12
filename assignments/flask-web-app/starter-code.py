from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

items = [
    {"id": 1, "name": "Notebook", "description": "A blank notebook"},
    {"id": 2, "name": "Pencil", "description": "A pencil for writing"},
]

template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Item List</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      table { width: 100%; border-collapse: collapse; margin-bottom: 1rem; }
      th, td { border: 1px solid #ccc; padding: 0.5rem; }
      th { background: #f4f4f4; }
      form { margin-bottom: 1rem; }
      input, textarea { width: 100%; padding: 0.5rem; margin: 0.25rem 0; }
      .actions a { margin-right: 0.5rem; }
    </style>
  </head>
  <body>
    <h1>Flask Item List</h1>

    <h2>Add a new item</h2>
    <form method="post" action="/items">
      <label>Name</label>
      <input type="text" name="name" required>
      <label>Description</label>
      <textarea name="description"></textarea>
      <button type="submit">Add Item</button>
    </form>

    <h2>Current items</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {% for item in items %}
        <tr>
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.description }}</td>
          <td class="actions">
            <a href="/items/{{ item.id }}/edit">Edit</a>
            <a href="/items/{{ item.id }}/delete">Delete</a>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>
'''

edit_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Edit Item</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      input, textarea { width: 100%; padding: 0.5rem; margin: 0.25rem 0; }
      a { display: inline-block; margin-top: 1rem; }
    </style>
  </head>
  <body>
    <h1>Edit Item</h1>
    <form method="post" action="/items/{{ item.id }}/edit">
      <label>Name</label>
      <input type="text" name="name" value="{{ item.name }}" required>
      <label>Description</label>
      <textarea name="description">{{ item.description }}</textarea>
      <button type="submit">Save Changes</button>
    </form>
    <a href="/">Back to list</a>
  </body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(template, items=items)

@app.route("/items", methods=["POST"])
def add_item():
    name = request.form.get("name")
    description = request.form.get("description", "")
    new_id = max((item["id"] for item in items), default=0) + 1
    items.append({"id": new_id, "name": name, "description": description})
    return redirect(url_for("index"))

@app.route("/items/<int:item_id>/edit", methods=["GET", "POST"])
def edit_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404

    if request.method == "POST":
        item["name"] = request.form.get("name")
        item["description"] = request.form.get("description", "")
        return redirect(url_for("index"))

    return render_template_string(edit_template, item=item)

@app.route("/items/<int:item_id>/delete")
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
