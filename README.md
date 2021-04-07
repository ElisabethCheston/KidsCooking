# Cooking With Kids
Encourage your kids to become more active in the kitchen and give them a basic knowledge of how to prepare food them self!  
  
*MongoDB database project stored in GitHub and deployed to Heroku.*

## 1.	The UX Framework (Strategy Plane)

### Introduction
The idea of this website is to create meals and snacks by follow easy instructions. Target audience is primary the younger generation. For all recipes recommended for kids 13 years old or younger will be displayed for free. To see more advanced recipes and create own recipe posts you have to become a registered user. 
### Goal
Build a recipe webpage with HTML, CSS, JavaScript, Python, MongoDB, Flask technologies where users can manipulate CRUD functions (create, read, update and delete). The user will also be able to store data.  
## 1.2 User Stories (Scope Plane)

The type of users for the website are kid (13 years old or younger), guest user, parents of kids, registered users, admin user. 
  
**Kids goals**  
As a kid I want:  
*	recipes to be easy to find on the website, so I won’t lose interest.
*	the recipes to be easy to follow and be understandable, so I won’t be discouraged to make things in the kitchen.
*	the webpage to have an appealing layout with fun picture, so I would be inspired to try the recipes.

**Guest user goals**  
As a guest user I want:  
*	Navigation to be easy on the website, so I won’t be discouraged to use the website.
*	Have the option to register as a user, if I like the page and want to see more.
*	Information on purpose of website and how it’s used, so I would know what it’s about.
*	All links to work without error, so I wont chose to search of other pages.

**Parent goals:**  
As a parent I want:  
* The recipes to state any common allergies, to prevent breakouts.
* The recipes to inform if help with stove or oven is needed, so my child know when to ask for help if needed.
* the only communication possible is through posts that are public, to prevent unsupervised contact with predators or bad influences.

**Registered user goals**  
As a registered user I want:  
* to see inspiring pictures of recipes, so I would like to try to make it.
* recipes to be easy to follow, so I won’t be discouraged and quit.
* to share my own recipes, so others can try them.
* to know how advance the recipes are, so I can consider if I can or want to make it.
* to give feedback on recipes, to let the creator and other users know.
* to be able to delete my account, in case I like to cancel my registration.

**Admin and Goals**  
As an admin I want:  
* to have access all content and activity on the website.
* to have the possibility to delete users and posts if needed.
* users to be able to contact me if something is wrong with the website.


## 1.3 Structure plane

### Typography

Font style used for the website is Atma and Oswald. Atma for headers and logo and Oswald for all other text.

### Color

Except for black and white the 3 basic colors used through the website are:  
  
•	Light gray    
•	Purple  
•	limegreen  

### Interactiv Design & Informatiove Architecture
  
#### Public Recipes  
In the top navbar there is a dropdown button with all recipe categories open for public. Once I select one of them rows with recipes are shown in the body. To view the you click on the name or pic.

#### Create an account  
For the first time user, the option to “Register” or “Sign In” on the first page. When choosing “Register” user have to fill in a username and a password. Then click “Create account” and the page automatically takes the user to their profile page. If user already has an account they just click on the “Sign In” button and fill in the username and password.

#### Categories  
When you’re a logged in user you will see a button in the top navbar called “Categories”. When clicked a dropdown list shows of all category options shows. Once I select one of them a list with all of those recipes should show in the main window.

#### Create Recipe Posts  
As a registered user you should see a button called “Create Recipes” in your profile. Once clicked it should clear how to fill in the fields. Once submitted you should reseve a message that the post won’t be available to public until it’s been reviewed by admin.

#### Edit Recipe Post  
By clicking on the "Edit" button on your recipe you should be able to open up the edit form and save the changes. Again, once submitted you should reseve a message that the post won’t be available to public until it’s been reviewed by admin.

#### Delete Post  
If you want to delete a post, it should be easily done by clicking on “Delete Recipe” button on the page of your recipe. You will get a confirmation message that the post has been deleted.

#### Sign In  
In the top navbar the “Sign In” button should be displayed if your an unregistered user or if you not logged in yet.

#### Sign Out
The “Sign Out” button in the top navbar should be clickable and log you out of your account. You will get a confirmation popup message that you've been logged out.

#### Delete Account
If you like to delete your account, you should see a “Delete Profile” button in your profile when logged in. Once you click on the “Delete Profile” button you will automatically be logged out from the profile page and get a confirmation message on screen.  

## 1.4 Skeleton Plane

### The structure of the website:   

<img width="687" alt="skeletoncooking" src="https://user-images.githubusercontent.com/70586630/113631652-0c2e6900-966a-11eb-85c7-89f3bedb2d38.png">

### The database structure:   
<img width="585" alt="databaseCooking" src="https://user-images.githubusercontent.com/70586630/113631615-0042a700-966a-11eb-928b-f24183569cf8.png">  

 ### Recipe categories:    
•	Snacks  
•	Lunch  
•	Dinner  
•	Healthy  
•	Sweets  
•	Party  

### Recipe information:   
•	Cooking Time  
•	Portion size  
•	Difficult level  
•	Cooking materials needed  
•	Name of the recipe  
•	Ingredients need  
•	Easy cooking instructions  
•	Gluten free, egg free, nut free, dairy free  
•	Tips on things to think about or to improve the recipe  

## 1.5	Surface Plane

### Wireframes

**First Page**
  
![First Page](https://user-images.githubusercontent.com/70586630/113860954-f1154380-97a6-11eb-95b8-2935392ec0fd.png)
  
  **Login**
    
![Login](https://user-images.githubusercontent.com/70586630/113860258-1b1a3600-97a6-11eb-85ae-7a2c5c8fddad.png)
  
  **Register**
    
![Register](https://user-images.githubusercontent.com/70586630/113860237-16ee1880-97a6-11eb-896a-a710acaedac6.png)
  
  **Profile**
    
![Login Profile](https://user-images.githubusercontent.com/70586630/113854470-2f0e6980-979f-11eb-8e27-c8c4cd0354ee.png)
  
  **Categories**  
    
![Recipes](https://user-images.githubusercontent.com/70586630/113854480-3170c380-979f-11eb-92e6-8f88c72a4056.png)

  **Recipes**  
    
![Selections](https://user-images.githubusercontent.com/70586630/113854473-2fa70000-979f-11eb-8309-64c91c93d75d.png)
  
  **Create Recipes**
    
![CreateRecipes](https://user-images.githubusercontent.com/70586630/113854487-333a8700-979f-11eb-8aa5-d119752091f6.png)
  
  **Recipe Layout**
    
![RecipeLayout](https://user-images.githubusercontent.com/70586630/113854492-35044a80-979f-11eb-9da2-093cf861bc45.png)



## Features

### Existing Features

**Top Navbar:** Navbar with links aligned to the right for recipes, login, register. As a user you will have access to links create recipes and delete recipes.  
  
**Bottom Navbar:** Toggler with categories inspiration, nutrition, logout.  
  
**Register Form:** User create a username and password that has to be retyped for verification.  
  
**Login Form:** With username and password.  
  
**Responsive Pages:**  
  
**Links:** Responsive links to recipes.  
  
**Style Layout:**  
  
**Recipe Form:**  
  
**Images:** All images are taken from internet and box sized to fit the recipes pages.  
  
**Flash messages:** Vertification to users when creating, editing or deleting post or deleting account.  
  
**Buttons:** For editing, deleting, creating accounts and recipes.  
  

### Features Left to Implement

**Subscription** Could be added of weekly updates.  
**Categories** More categories could be added if needed.   

## Technologies Used

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
  
## Testing

Make a separate .md file and link it (Idea from https://github.com/juanstelling/MS3_breaktasty/blob/master/TESTING.md )

### Manual 

### Responsivness

### Browser

### Devices

### User Stories

### Validator

### Bugs


## Deployment
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

## Credits
  
### Content
  
### Media

**Recipes**
  
Unregistered Users  
*	Animal sandwiches
*	Pancake Animals
*	Bento Box
*	Pizza Toast
*	Spider Dog
*	Power Snack
*	Snack Square
*	Pasta Salad
*	Chicken Broccoli Pasta
  
Registered User
* Flying Sausers
*	Crunchy Granola Sticks
*	Frozen Banana Treat  
  
Images  
  
**Recipe Images**  
Unregistered Users  
*	Animal sandwiches
*	Pancake Animals
*	Bento Box
*	Pizza Toast
*	Spider Dog
*	Power Snack
*	Snack Square
*	Pasta Salad
*	Chicken Broccoli Pasta  
  
Registered User  
*	Flying Sausers
*	Crunchy Granola Sticks
*	Frozen Banana Treat

### Acknowledgements
•	I received inspiration for this project from X

### LINKS:

![image](https://user-images.githubusercontent.com/70586630/113582793-1a0fca00-9629-11eb-8d84-3f38a36a00c3.png)
