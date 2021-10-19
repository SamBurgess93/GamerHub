import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")

@app.route("/get_games")
def get_games():

    # Find and display all games in database
    games = list(mongo.db.games.find())
    return render_template(
        "games.html", games=games
    )


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    games = list(mongo.db.games.find({"$text": {"$search": query}}))
    return render_template(
        "games.html", games=games
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # checking if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # checking if the passwords match on registration page
        user_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if user_password != confirm_password:
            flash("Your passwords do not match, please try again")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "is_admin": False,
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()

        flash(
            "Welcome {}, you have registered and are logged in ".format(
                request.form.get("username")
            )
        )
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            
            # Check if the hashed password matches the user's password
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}, you have successfully logged in".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            #username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session users username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = list(mongo.db.reviews.find(
        {"author": session["user"]}))
    games = list(mongo.db.games.find(
        {"created_by": session["user"]}))
    if session["user"]:
        return render_template(
            "profile.html", 
            username=username,
            reviews=reviews,
            games=games,
            )
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_game", methods=["GET", "POST"])
def add_game():

    if request.method == "POST":

        # Check if the game is already in the database
        existing_game = mongo.db.technologies.find_one(
            {"game_name": request.form.get("game_name")}
        )

        if existing_game:
            flash("This game already exists")
            return redirect(url_for("add_game"))

        # Add the new game to the database
        newgame = {
            "game_name": request.form.get("game_name"),
            "category_name": request.form.get("category_name"),
            "game_image": request.form.get("game_image"),
            "game_description": request.form.get(
                "game_description"),
            "created_by": session["user"],
            "added_on": datetime.now().strftime("%d, %B, %Y at %H:%M"),
            "editted_on": "No edits yet",
        }
        mongo.db.games.insert_one(newgame)
        flash("You have successfully added a new game, thank you!")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_game.html",
        page_title="Add a Game",
        categories=categories,
    )

@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):

    # Edit a game in database
    if request.method == "POST":
        gamename = mongo.db.games

        filter = {"_id": ObjectId(game_id)}

        newvalues = {
            "$set": {
                "category_name": request.form.get("category_name"),
                "game_image": request.form.get("game_image"),
                "game_description": request.form.get(
                    "game_description"),
            }
        }

        gamename.update_one(filter, newvalues)
        flash("Your game has been updated. Thank you!")
        return redirect(url_for("profile", username=session["user"]))

    game = mongo.db.games.find_one(
        {"_id": ObjectId(game_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_game.html", game=game, categories=categories
    )


@app.route("/delete_game/<game_id>")
def delete_game(game_id):

    # Find and then delete reviews on a game from database
    game_name = mongo.db.games.find_one(
        {"_id": ObjectId(game_id)}
    ).get("game_name")
    mongo.db.reviews.remove({"game_name": game_name})

    # Delete a game from database
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Your games has been deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/add_review", methods=["POST"])
def add_review():

    if "user" in session:

        # Add a review to the database if logged in
        review = {
            "game_name": request.form.get("game_name"),
            "game_review": request.form.get("game_review"),
            "author": session["user"],
            "created_on": datetime.now().strftime("%d, %B, %Y at %H:%M"),
            "editted_on": "No edits yet",
        }

        mongo.db.reviews.insert_one(review)
        flash("Your review has been added")
        return redirect(url_for("profile", username=session["user"]))
    else:
        # If person is not registered redirect them to register page
        flash("You must be registered to add a review")
        return redirect(url_for("register"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # Delete a review from the database
    flash("Your review has been deleted")
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_review/<review_id>", methods={"GET", "POST"})
def edit_review(review_id):

    # Edit a review in database
    if request.method == "POST":

        created_on = mongo.db.reviews.find_one(
            {"_id": ObjectId(review_id)}).get(
            "created_on"
        )

        author = mongo.db.reviews.find_one(
            {"_id": ObjectId(review_id)}).get("author")

        editted_review = {
            "game_name": request.form.get("game_name"),
            "game_review": request.form.get("game_review"),
            "author": author,
            "created_on": created_on,
            "editted_on": datetime.now().strftime("%d, %B, %Y at %H:%M"),
        }
        mongo.db.reviews.update(
            {"_id": ObjectId(review_id)}, editted_review)

        flash("Your review has been changed")
        return redirect(url_for("profile", username=session["user"]))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


@app.route("/reviews/<game_id>", methods=["GET", "POST"])
def reviews(game_id):
    game = mongo.db.games.find_one(
        {"_id": ObjectId(game_id)})
    reviews = list(mongo.db.reviews.find(
        {"game_name": game["game_name"]}))
    return render_template(
        "reviews.html",
        game=game,
        reviews=reviews,
        page_title="Reviews",
    )


@app.route("/manage_categories")
def manage_categories():
    categories = list(mongo.db.categories.find())
    games = list(mongo.db.games.find())
    reviews = list(mongo.db.reviews.find())
    return render_template(
        "manage_categories.html",
        categories=categories,
        games=games,
        reviews=reviews,
        page_title="Manage the Sites Genres",
    )


@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    # Add a new category to the database
    if request.method == "POST":

        # Check if the category is already in the database
        existing_category = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")}
        )

        if existing_category:
            flash("This category already exists")
            return redirect(url_for("add_category"))

        newcategory = {"category_name": request.form.get(
            "category_name")}
        mongo.db.categories.insert_one(newcategory)
        flash("You have successfully added a new category.")
        return redirect(url_for("manage_categories"))

    return render_template(
        "add_category.html", page_title="Add a new Genre")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # Edit a game in database
    if request.method == "POST":
        edittedcategory = {"category_name": request.form.get("category_name")}
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, edittedcategory)
        flash("The category was successfully editted")
        return redirect(url_for("manage_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template(
        "edit_category.html", category=category,
        page_title="Edit this Category"
    )


@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    # Delete the category from database
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("You have deleted this category")
    return redirect(url_for("manage_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
