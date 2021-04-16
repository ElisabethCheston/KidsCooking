import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from PIL import Image
import glob
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# ---- Recipes ----
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/get_recipes_by_category/<category>")
def get_recipes_by_category(category):
    recipes = mongo.db.recipes.find({"category_name": category})
    return render_template("recipes.html", recipes=recipes)    

# ---- Registration ----
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")

# ---- Login ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})


        if existing_user:
                    # ensure hashed password matches user input
                    if check_password_hash(
                            existing_user["password"], request.form.get("password")):
                                session["user"] = request.form.get("username").lower()
                                flash("Welcome, {}".format(
                                    request.form.get("username")))
                                return redirect(url_for(
                                    "profile", username=session["user"]))
                    else:
                        # invalid password match
                        flash("Incorrect Username and/or Password")
                        return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# ---- Profile ----
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # if user cookie is true return to profile
    if session["user"]:
        return render_template("profile.html", username=username)    
    # if user cookie is untrue return to login
    return redirect(url_for("login"))

# ---- Logout ----
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been looged out")
    session.pop("user")
    return redirect(url_for("login"))


# ---- Add recipes ----
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "cooking_time": request.form.get("cooking_time"),
            "portons": request.form.get("portons"),                      
            "difficulty_level": request.form.get("difficulty_level"),
            "cooking_material": request.form.get("cooking_material"),
            "gluten": request.form.get("gluten"),
            "egg": request.form.get("egg"),
            "nuts": request.form.get("nuts"),
            "lactose": request.form.get("lactose"),              
            "preparation": request.form.get("preparation"),         
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)

# ---- Add categories ----

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")
    
@app.route("/snacks")
def snacks():
    return render_template("snacks.html")

@app.route("/lunch")
def lunch():
    return render_template("lunch.html")

@app.route("/dinner")
def dinner():
    return render_template("dinner.html")

@app.route("/healthy")
def healthy():
    return render_template("healthy.html")

@app.route("/sweets")
def sweets():
    return render_template("sweets.html")

@app.route("/party")
def party():
    return render_template("party.html")                   


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
