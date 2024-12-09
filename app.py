from flask import Flask, request, render_template, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Library class
class Library:
    def __init__(self):
        self.books = {}  # Store books with book_id as key
        self.members = {}  # Store members with member_id as key
        self.admin_token = None

    def login(self, username, password):
        if username == "admin" and password == "password123":
            self.admin_token = str(uuid.uuid4())
            return self.admin_token
        else:
            return None

    def is_authenticated(self, token):
        return token == self.admin_token

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            return f"Book with ID {book_id} already exists."
        else:
            self.books[book_id] = {"title": title, "author": author, "copies": copies}
            return f"Book '{title}' added successfully!"

    def view_books(self):
        return self.books

    def search_books(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
        return results

    def add_member(self, member_id, name, email):
        if member_id in self.members:
            return f"Member with ID {member_id} already exists."
        else:
            self.members[member_id] = {"name": name, "email": email}
            return f"Member '{name}' added successfully!"

    def view_members(self):
        return self.members


# Initialize library
library = Library()

# Routes
@app.route("/")
def home():
    if "token" not in session:
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        token = library.login(username, password)
        if token:
            session["token"] = token
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if "token" not in session:
        return redirect(url_for("login"))

    message = ""
    if request.method == "POST":
        book_id = request.form["book_id"]
        title = request.form["title"]
        author = request.form["author"]
        copies = int(request.form["copies"])
        message = library.add_book(book_id, title, author, copies)
        return render_template("add_book.html", message=message, back_to_home=True)

    return render_template("add_book.html")


@app.route("/view_books")
def view_books():
    if "token" not in session:
        return redirect(url_for("login"))
    books = library.view_books()
    return render_template("view_books.html", books=books, back_to_home=True)


@app.route("/search_books", methods=["GET", "POST"])
def search_books():
    if "token" not in session:
        return redirect(url_for("login"))

    results = []
    if request.method == "POST":
        keyword = request.form["keyword"]
        results = library.search_books(keyword)
    return render_template("search_books.html", results=results, back_to_home=True)


@app.route("/add_member", methods=["GET", "POST"])
def add_member():
    if "token" not in session:
        return redirect(url_for("login"))

    message = ""
    if request.method == "POST":
        member_id = request.form["member_id"]
        name = request.form["name"]
        email = request.form["email"]
        message = library.add_member(member_id, name, email)
        return render_template("add_member.html", message=message, back_to_home=True)

    return render_template("add_member.html")


@app.route("/view_members")
def view_members():
    if "token" not in session:
        return redirect(url_for("login"))
    members = library.view_members()
    return render_template("view_members.html", members=members, back_to_home=True)


@app.route("/logout")
def logout():
    session.pop("token", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
