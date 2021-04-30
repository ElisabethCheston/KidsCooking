# Cooking With Kids
Encourage your kids to become more active in the kitchen and give them a basic knowledge of how to prepare food them self!  
  
*MongoDB database project stored in GitHub and deployed to Heroku.*  
  
# Table of contents
  
[The UX Framework (Strategy Plane)](#strategyplane)  
  * [Introduction](#introduction)  
  * [Goal](#goal) 

[User Stories (Scope Plane)](#ux) 

[Structure plane](#structureplane)  
  * [Typography](#typography)  
  * [Color](#color)  
  * [Interactiv Design & Informatiove Architecture](#idandia)  


[Skeleton Plane](#skeletonplane)  
  * [The structure of the website](#skeleton)  
  * [The database structure](#database)  
  * [Recipe categories](#recipecat)  
  * [Recipe information](#recipeinfo) 
  
[Surface Plane](#surfaceplane)  
  * [Wireframes](#wireframes)  
  
[Features](#features)  
  * [Existing Features](#existingfeat)  
  * [Features Left to Implement](#featimpl)  
  
[Technologies Used](#usertech)  

[Testing](#testing)  

[Deployment](#deployment)  

[Credits](#credit)  
  * [Content](#content)  
  * [Media](#media)  
  * [Acknowledgements](#Acknowledgements)  
  * [Links](#link)    
    

## The UX Framework (Strategy Plane)<a name="strategyplane"></a>


### Introduction<a name="introduction"></a>
The idea of this website is to create meals and snacks by follow easy instructions. Target audience is primary the younger generation. Recipes can are displayed on website for free. An options to become a user to create users own recipes to share with other users.  
  
### Goal<a name="goal"></a>
Build a recipe webpage with HTML, CSS, JavaScript, Python, MongoDB, Flask technologies where users can manipulate CRUD functions (create, read, update and delete). The user will also be able to store data. 

## User Stories (Scope Plane)<a name="ux"></a>

The type of users for the website are kid, guest user, parents of kids, registered users, admin user. 
  
**Kids goals**  
As a kid I want:  
*	the recipes to be easy to find on the website, so I won’t lose interest.
*	the recipes to be easy to follow and be understandable, so I won’t be discouraged to make things in the kitchen.
*	the webpage to have an appealing layout with fun picture, so I would be inspired to try the recipes.

**Guest user goals**  
As a guest user I want:  
*	navigation to be easy on the website, so I won’t be discouraged to use the website.
*	have the option to register as a user, if I like the page and want to see more.
*	information on purpose of website and how it’s used, so I would know what it’s about.
*	all links to work without error, so I wont chose to search of other pages.

**Parent goals:**  
As a parent I want:  
* the only communication possible is through posts that are public, to prevent unsupervised contact with predators or bad influences.

**Registered user goals**  
As a registered user I want:  
* to share my own recipes, so others can try them.
* to know how advance the recipes are, so I can consider if I can or want to make it.
* to be able to delete my recipes, if I don't want to display it.  
* to be able to edit my recipes, if want to change something with it.  

**Admin and Goals**  
As an admin I want:  
* to be able to create new categories, if it's needed.  
* to be able to edit or delete categories, if it's needed. 
* users to be able to contact me if something is wrong with the website.


## Structure plane<a name="structureplane"></a>


### Typography<a name="typography"></a>

Font style used for the website is Atma and Oswald. Atma for headers and logo and Oswald for all other text.  


### Color<a name="color"></a>


Except for black and white the 3 basic colors used through the website are:  
  
•	Light gray    
•	Purple  
•	limegreen  


### Interactiv Design & Informatiove Architecture<a name="idandia"></a>

  
#### Recipes
  
In the top navbar there is a dropdown button with all recipe categories open for public. Once I select one of them rows with recipes are shown in the body. To view the you click on the name or pic.

#### Create an account
  
For the first time user, the option to “Register” or “Sign In” on the first page. When choosing “Register” user have to fill in a username and a password. Then click “Create account” and the page automatically takes the user to their profile page. If user already has an account they just click on the “Sign In” button and fill in the username and password.

#### Categories
  
When you’re a logged in user you will see a button in the top navbar called “Categories”. When clicked a dropdown list shows of all category options shows. Once I select one of them a list with all of those recipes should show in the main window.
  
For Admin, the categories link in top navbar gives access to add/edit/delete the categories.


#### Create Recipe Posts
  
As a registered user you should see a button called “Create Recipes” in your profile. Once clicked it should clear how to fill in the fields. 

#### Edit Recipe Post  
By clicking on the "Edit" button on your recipe you should be able to open up the edit form and save the changes. 

#### Delete Post  
If you want to delete a post, it should be easily done by clicking on “Delete Recipe” button on the page of your recipe. You will get a confirmation message that the post has been deleted.

#### Sign In  
In the top navbar the “Sign In” button should be displayed if your an unregistered user or if you not logged in yet.

#### Sign Out
The “Sign Out” button in the top navbar should be clickable and log you out of your account. You will get a confirmation popup message that you've been logged out.
  


## Skeleton Plane<a name="skeletonplane"></a>

### The structure of the website:<a name="skeleton"></a>   

![Skeleton](https://user-images.githubusercontent.com/70586630/116575146-abafe600-a90e-11eb-9f2f-34dedb006980.png)


### The database structure:<a name="database"></a>   
  
<img width="687" alt="skeletoncooking" src="https://user-images.githubusercontent.com/70586630/114391610-fd7b1100-9b97-11eb-9e09-6957d0c69322.png">

 ### Recipe categories:<a name="recipecat"></a>   
     
*	Snacks  
*	Lunch  
*	Dinner  
*	Healthy  
*	Sweets  
*	Party  


### Recipe information:<a name="recipeinfo"></a>   
    
*	Category  
*	Name of the recipe  
*	Created by user  
*	Recipe Image  
*	Cooking Time  
*	Portion size  
*	Difficult level  
*	Ingredients need  
*	Cooking instructions    
*	Tips on things to think about or to improve the recipe  


## Surface Plane:<a name="surfaceplane"></a>   
 

### Wireframes:<a name="wireframes"></a>   
 

**First Page** 
  
![First Page](https://user-images.githubusercontent.com/70586630/116575261-c4200080-a90e-11eb-8606-5b5d5c304977.png)

  
  **Login**
    
![Login](https://user-images.githubusercontent.com/70586630/116579177-6b526700-a912-11eb-8de6-63625b99f421.png)

  
  **Register**  
    
![Register](https://user-images.githubusercontent.com/70586630/116284979-f9e9ab80-a78d-11eb-98a1-05dd7b17aed0.png)

  
  **Admin Profile**  
    
![Admin Profile](https://user-images.githubusercontent.com/70586630/116575541-047f7e80-a90f-11eb-89a1-d4119d731c58.png)  

  **Add Category**  
    
  ![Add Category](https://user-images.githubusercontent.com/70586630/116578591-dd767c00-a911-11eb-80d3-041d4ee41e5c.png)  
  
  **Manage Categories**  
  
  ![Managing Categories](https://user-images.githubusercontent.com/70586630/116578567-d5b6d780-a911-11eb-993b-72e9f3f160c4.png)  

  
  **Categories**  
    
![Categories](https://user-images.githubusercontent.com/70586630/116575513-ffbaca80-a90e-11eb-8c96-f44c2646a7ac.png)


  **Unregistered User**  
    
![Unregister user](https://user-images.githubusercontent.com/70586630/116575496-fb8ead00-a90e-11eb-8a16-caa0c1f585bf.png)


  
  **Create Recipes**  
  
![Create Recipes](https://user-images.githubusercontent.com/70586630/116575478-f6c9f900-a90e-11eb-907d-d44156eea0a0.png)


  **Recipe Layout**  
    
![Recipe Layout](https://user-images.githubusercontent.com/70586630/116590234-cc336c80-a91d-11eb-9062-64531dd69af5.png)





## Features:<a name="features"></a>   
 

### Existing Features:<a name="existingfeat"></a>   
  
**Popup window First Page:** [From Materialized](https://materializecss.com/modals.html)  
  
As using The Category layout as First Page layout, a popup show for welcoming and explaining short the page perpose.  

**Top Navbar:** [From Materialized](https://materializecss.com/navbar.html) 

Navbar with links aligned to the right for recipes, login, register. As a user you will have access to links create recipes and delete recipes.  
  
**Bottom Navbar:** [From Materialized](https://materializecss.com/navbar.html) 

Toggler with categories inspiration, nutrition.  
  
**Register Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

User create a username and password that get stored in the database under user.
  
**Login Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

Login with username and password.   
  
**Logout Function:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization)  
  
  When user logout it brings them back to the login site.

  
**Profile Page setup:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) 

Personalized profile page for logged in user. If you have created any recipes then they will show here.
  
  Admin's profile is a little different. It will give access to editing categories.  
    
  
**Links:** 
Responsive links to recipes, forms, profile, add recipes, categories and contact.  
  
**Recipe Form:**  

Includes input fields for name, ingredients, instruction, and additional notes. A dropdown menu for cooking time, difficulty options, categories, portions. The information saved in  database.  
  
**Edit/delete Recipe:**  

If user wants to edit recipe it will call for selected recipe and open it in the add recipe layout. If user choose to delet recipe it will bring them back to category site.  
  
**Images:** 

All images are taken from internet and box sized to fit the recipes pages, except for the logo and categoriy pictures. They are save in the project with reference under media.  
  

**Add Image to recipes** Code from [Gazza J MS3](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/templates/add_recipe.html)  

With help from Gazza's project, I used the funtion of adding url to the database recipe and display it.
  
**Flash messages:** 

Vertification to users when creating, editing or deleting post or deleting account. 
  
**Recipe Buttons:** 

In the top right coner of every recipe that profile user has created is an option to edit the recipe or delete it. When register an account or login there is a comfirmation button at the end.    

**Footer** [From Materialized](https://materializecss.com/footer.html) 

Repitition links at the bottom from the navbars, copyright information, and a back to top button.
  
  **Bring to Top Button :**  
  
  [Icon](https://fontawesome.com/icons/chevron-up) used. Code from [w3s](https://www.w3schools.com/icons/tryit.asp?filename=tryicons_fa-chevron-up).



### Features Left to Implement:<a name="featimpl"></a>   
 
**Subscription** Could be added of weekly updates.  
**Categories** More categories could be added if needed.  
**Delete** Delete account function, either for Admin or user.

## Technologies Used:<a name="usertech"></a>   
 
**Text Editor:**
  * [GitPod](https://gitpod.com/) – the editor to build, commit, and push data to GitHub.  
  
**Control System:**
  * [GitHub](https://github.com/) – used to host the project.  
  
**Database:**
  * [MongoDB](https://mongodb.com/) – cloud based service used for managing the database. 
   
**Platform Host:**
  * [Heroku](https://heroku.com/) – Cloud based platform for deployment of app.  
  
**Key Generator:**
  * [RandomKeygen](https://randomkeygen.com/) – used to create user key for website.  
  
**Languages:**
  * [HTML](https://sv.wikipedia.org/wiki/HTML) – for the basic structure of the project.
  * [CSS](https://sv.wikipedia.org/wiki/Cascading_Style_Sheets) –for the overall style of website.
  * [JavaScript](https://developer.mozilla.org/sv-SE/docs/Web/JavaScript) - used to activate fuctions
  *	[jQuery](https://jquery.com/) – used as the main JavaScript function.
  *	[Python](https://www.python.org/) – for the backend of project.  
  
**Frameworks:**
  * [Materialize](https://materializecss.com/about.html) – For Navbar
  *	[Flask](https://flask.palletsprojects.com/en/1.1.x/) –  
  *	[Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) -  
  
**Style:**
  *	[Google Fonts](https://fonts.google.com/) – For using and Oswald and Atma fonts on website.
  *	[Balsamiq Wireframes](https://balsamiq.com/wireframes/) – used for the websites wireframes. 
   
**Validations:**
  *	[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Validate CSS
  *	[W3C HTML Validator](https://validator.w3.org/) - Validate HTML
  *	[Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Errors in console
  *	Jshint](https://jshint.com/) - Validate JavaScript
  *	[PEP8](https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585183&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1012697&gclid=Cj0KCQjwsLWDBhCmARIsAPSL3_2C6LOJLPqHUShlkvBE9h1MLyob2wlSsid-Apq1nfjIaiqkO6zEWvkaAoPvEALw_wcB) – for validate the Python code.  
  

## Testing<a name="testing"></a>  
  
[Testing.md](Testing.md)  
  
    

## Deployment<a name="deployment"></a>
Deployment for this GitHub repository project is done through Heroku through the following steps;

**1. Heroku**
  * Create an account on Heroku and Login
  *	We have to register the MongoDB database information for the project. Under “Settings” scroll down to “Config Vars”. We need to add following variables for our env.py to secure the webpage;

    *	IP : (Add ip address)
    *	PORT : (0.0.0.0)
    *	SECRET_KEY : (Add secret key)
    *	MONGO_URI : (Add string from MongoDB cluster connection button)
    *	MONGO_DBNAME : (Add your MongoDB project name)

*	To create new application, click on “New” on the dashboard and then choose “Create new app”.
* Choose an app name without spaces.
*	Click on Deployment and choose the deployment method of your choice (in this case it GitHub).
*	Click on your GitHub Name that appears in the window as a dropdown list and select your project.
*	Click on the “Connect” button for sync app and project.
  
**2.	GitPod**  
*	Create 2 new files in terminal called Procfile and requirements.txt for connecting project information to Heroku. 

*	$ echo web: python app.py > Procfile
*	$ pip3 freeze – local > requirements.txt  

*	$ git status  
(To check that all required app installed equals to the list in requirements.txt.)

*	Commit the files to GitHub by typing this in the terminal; 
*	$git add requirements. txt 
*	$ git commit -m “Add requirements.txt”
*	$ git push  
(Do the same for Procfile (remember that it’s a big “P”. Double check your GitHub project.) 
  
**3.	Heroku**
*	Go back to Heroku. Under “Deploy” section select the “Enable Automatic Deploys” for Automatic Deploys and select “Deployment Branch” for Manual Deploy.
    
*(Heroku connects with GitHub and start building the app with the required packages. Confirmation in the bottom of the window will show when its done.)*  
* Your project is now deployed and updates every time you push information to GitHub. 

#### Run the project locally

Clone the project:  
  
*	Log in to GitHub and locate the repository you like to clone.
*	Click on the  “Code” button on the left side of the GitPod.
*	In the dropdown menu click on the HTTP option in the left top corner.
*	Click on the copy icon for the repository url.
*	In your local IDE choose the location where you want your clone directory.
*	Type “git clone” in Terminal and paste the url. Enter.  
  
Clone to GitHub Desktop:  
  
*	Log in to GitHub and locate the repository you like to clone.
*	Click on the  “Code” button on the left side of the GitPod.
*	In the dropdown menu click on the HTTP option in the left top corner.
*	Click on the “Open with GitHub Desktop.  
*	Then follow the prompts GitHub Desktop instructions to complete the clone.  

## Credits<a name=”credit”></a>

 
### Content<a name=”content”></a>


### Media<a name=”media”></a>

Link to [Media.md](Media.md) information.
  
  
  
### Acknowledgements<a name=””>acknowled</a>
•	I received inspiration for this project from X


### LINKS:<a name=”link”></a>
