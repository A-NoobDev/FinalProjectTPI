from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


# Placeholder posts data (replace with your database interaction)
posts = [
    {"id": 1, "title": "Post 1", "content": "Content of post 1", },
    {"id": 2, "title": "Post 2", "content": "Content of post 2", },
]


# ----------------------- Route for displaying the main page
@app.route("/")
def index():
    is_dark_theme = request.cookies.get(
        "theme") == "dark"  # Check for dark theme cookie
    post = request.args.get('post')  # Get the post from the URL parameters
    if post:
        # Find the post with the given ID
        post = next((p for p in posts if str(p["id"]) == post), None)
    return render_template("index.html", posts=posts, is_dark_theme=is_dark_theme, updated_post=post)


@app.route("/post/<int:id>/edit", methods=["GET", "POST"])
def edit_post(id):
    post = next((p for p in posts if p["id"] == id), None)
    if not post:
        return render_template("error.html", message="Post not found")

    if request.method == "GET":
        return render_template("new.html", post=post, edit_mode=True)
    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if post:
            post["title"] = title
            post["content"] = content

            # Pass the updated post to the index template
            updated_post = {"id": post["id"], "title": post["title"], "content": post["content"]}
            return redirect(url_for("index", post=updated_post))

        else:
            return render_template("error.html", message="Post not found")

# ---------------------- Route for create or edit a post


@app.route("/create_or_edit_post", methods=["GET", "POST"])
def create_or_edit_post():
    id = request.args.get("id", None)

    if id:
        return redirect(url_for("edit_post", id=id))
    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        # Simulate adding post to data
        new_post = {"id": len(posts) + 1, "title": title,
                    "content": content, }
        posts.append(new_post)
        return redirect(url_for("index"))

    return render_template("new.html", edit_mode=bool(id))

# ----------------------- Route for creating new posts


@app.route("/new", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new.html", edit_mode=False)

    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        # Simulate adding post to data
        new_post = {"id": len(posts) + 1, "title": title,
                    "content": content, }
        posts.append(new_post)
        return redirect(url_for("index"))


# ----------------------- Route for viewing individual posts
@app.route("/post/<int:id>", methods=["GET"])
def post(id):
    post = [p for p in posts if p["id"] == id]
    if not post:
        # Handle case where no post is found (e.g., display an error message)
        return render_template("error.html", message="Post not found")
    else:
        return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)
