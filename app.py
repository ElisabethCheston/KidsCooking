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

# ---- Home ----
@app.route("/")
@app.route("/index")
def index():
    
    return render_template("index.html")

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

# ---- Logout ----
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been looged out")
    session.pop("user")
    return redirect(url_for("login"))

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

# ---- Recipes ----
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)

# ---- Collections ----
# recipe_coll = mongo.db.recipes
# category_coll = mongo.db.categories

# ---- Items per Page ----
per_page = 6    

# ---- Add recipes ----
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":
        
        recipe = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "url_img": request.form.get("url_img"),
            "cooking_time": request.form.get("cooking_time"),
            "portions": request.form.get("portions"),                      
            "difficulty_level": request.form.get("difficulty_level"),
            "cooking_material": request.form.getlist("cooking_material"),            
            "preparation": request.form.get("preparation"),         
            "ingredients": request.form.get("ingredients"), 
            "instructions": request.form.get("instructions"),
            "tips": request.form.get("tips"), 
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# ---- Edit recipes ----
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "url_img": request.form.get("url_img"),
            "cooking_time": request.form.get("cooking_time"),
            "portions": request.form.get("portions"),                      
            "difficulty_level": request.form.get("difficulty_level"),
            "cooking_material": request.form.getlist("cooking_material"),            
            "preparation": request.form.get("preparation"),         
            "ingredients": request.form.get("ingredients"), 
            "instructions": request.form.get("instructions"),
            "tips": request.form.get("tips"), 
            "created_by": session["user"]
        }
        mongo.db.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        # return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

# ---- Delete recipes ----


# ---- Recipe by category ----
@app.route("/get_recipe_by_category/<category>")
def get_recipes_by_category(category):
    recipe = mongo.db.recipes.find({"category_name": category})
    return render_template("recipes.html", recipe=recipe)    

# ---- Categories ----
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")
  
# ---- Categories ----
@app.route("/snacks", methods=["GET", "POST"])
def snacks():
    snacks_recipes = mongo.db.recipes.find({"recipe_types": "Snacks"})
    print(snacks_recipes)
    return render_template("snacks.html", snacks_recipes=snacks_recipes, page='snacks')

@app.route("/lunch", methods=["GET", "POST"])
def lunch():
    lunch_recipes = mongo.db.recipes.find({"recipe_types": "Lunch"})
    print(lunch_recipes)
    return render_template("lunch.html", lunch_recipes=lunch_recipes, page='lunch')

@app.route("/dinner", methods=["GET", "POST"])
def dinner():
    dinner_recipes = mongo.db.recipes.find({"recipe_type": "Dinner"})
    print(dinner_recipes)
    return render_template("dinner.html", dinner_recipes=dinner_recipes, page='dinner')

@app.route("/healthy", methods=["GET", "POST"])
def healthy():
    healthy_recipes = mongo.db.recipes.find({"recipe_type": "Healthy"})
    print(healthy_recipes)
    return render_template("healthy.html", healthy_recipes=healthy_recipes, page='healthy')

@app.route("/sweets", methods=["GET", "POST"])
def sweets():
    sweets_recipes = mongo.db.recipes.find({"recipe_type": "Sweets"})
    print(sweets_recipes)
    return render_template("dinner.html", sweets_recipes=sweets_recipes, page='sweets')

@app.route("/party", methods=["GET", "POST"])
def party():
    party_recipes = mongo.db.recipes.find({"recipe_type": "Party"})
    print(party_recipes)
    return render_template("dinner.html", party_recipes=party_recipes, page='party')

@app.route("/recipes", methods=["GET", "POST"])
def recipes():
    all_recipes = mongo.db.recipes.find({"recipe_type": "All Recipes"})
    print(all_recipes)
    return render_template("dinner.html", all_recipes=all_recipes, page='recipes')

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
