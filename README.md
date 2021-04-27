# Cooking With Kids
Encourage your kids to become more active in the kitchen and give them a basic knowledge of how to prepare food them self!  
  
*MongoDB database project stored in GitHub and deployed to Heroku.*

## 1.	The UX Framework (Strategy Plane)

### Introduction
The idea of this website is to create meals and snacks by follow easy instructions. Target audience is primary the younger generation. Recipes can are displayed on website for free. An options to become a user to create users own recipes to share with other users.
### Goal
Build a recipe webpage with HTML, CSS, JavaScript, Python, MongoDB, Flask technologies where users can manipulate CRUD functions (create, read, update and delete). The user will also be able to store data.  
## 1.2 User Stories (Scope Plane)

The type of users for the website are kid (13 years old or younger), guest user, parents of kids, registered users, admin user. 
  
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
* the recipes to inform if spcial material (stove, oven, microwave, etc) is needed, so my child know when to ask for my help.
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
  
#### Recipes  
In the top navbar there is a dropdown button with all recipe categories open for public. Once I select one of them rows with recipes are shown in the body. To view the you click on the name or pic.

#### Create an account  
For the first time user, the option to “Register” or “Sign In” on the first page. When choosing “Register” user have to fill in a username and a password. Then click “Create account” and the page automatically takes the user to their profile page. If user already has an account they just click on the “Sign In” button and fill in the username and password.

#### Categories  
When you’re a logged in user you will see a button in the top navbar called “Categories”. When clicked a dropdown list shows of all category options shows. Once I select one of them a list with all of those recipes should show in the main window.

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

#### Delete Account
If you like to delete your account, you should see a “Delete Profile” button in your profile when logged in. Once you click on the “Delete Profile” button you will automatically be logged out from the profile page and get a confirmation message on screen.  

## 1.4 Skeleton Plane

### The structure of the website:   

![Skeleton](https://user-images.githubusercontent.com/70586630/115709898-075bfb80-a372-11eb-80aa-6ff07e7046c0.png)

### The database structure:   
 

<img width="687" alt="skeletoncooking" src="https://user-images.githubusercontent.com/70586630/114391610-fd7b1100-9b97-11eb-9e09-6957d0c69322.png">


 ### Recipe categories:    
*	Snacks  
*	Lunch  
*	Dinner  
*	Healthy  
*	Sweets  
*	Party  

### Recipe information:   

*	Category  
*	Name of the recipe  
*	Created by user  
*	image  
*	Cooking Time  
*	Portion size  
*	Difficult level  
*	Cooking materials needed   
*	Preparation  
*	Ingredients need  
*	Cooking instructions    
*	Tips on things to think about or to improve the recipe  

## 1.5	Surface Plane

### Wireframes

**First Page** 
  
  ![First Page](https://user-images.githubusercontent.com/70586630/116284959-f22a0700-a78d-11eb-9862-a5f7fc8f53ee.png)

  
  **Login**
    
![Login](https://user-images.githubusercontent.com/70586630/113860258-1b1a3600-97a6-11eb-85ae-7a2c5c8fddad.png)
  
  **Register**  
    
![Register](https://user-images.githubusercontent.com/70586630/116284979-f9e9ab80-a78d-11eb-98a1-05dd7b17aed0.png)

  
  **Profile**  
    

  
  **Categories**  
    
![Categories](https://user-images.githubusercontent.com/70586630/116285011-0241e680-a78e-11eb-815e-11190d83eab8.png)


  **Unregistered User**  
    
![Unregister user](https://user-images.githubusercontent.com/70586630/116285489-6d8bb880-a78e-11eb-8a96-05b1cbc04d37.png)

  
  **Create Recipes**  
  
![Create Recipes](https://user-images.githubusercontent.com/70586630/116285066-0ec63f00-a78e-11eb-9ab2-a5e5acf17dba.png)

  **Recipe Layout**  
    
![Recipe Layout](https://user-images.githubusercontent.com/70586630/116285092-15ed4d00-a78e-11eb-903c-d826c8c0244c.png)



## Features

### Existing Features

**Top Navbar:** [From Materialized](https://materializecss.com/navbar.html) Navbar with links aligned to the right for recipes, login, register. As a user you will have access to links create recipes and delete recipes.  
  
**Bottom Navbar:** [From Materialized](https://materializecss.com/navbar.html) Toggler with categories inspiration, nutrition.  
  
**Register Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) User create a username and password that has to be retyped for verification.  
  
**Login Form:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) With username and password.   
  
**Logout Function:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization)  
  
**Profile Page setup:** [From TravelTim at CI ](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization) Personalized profile page for logged in user. 
  
**Links:** Responsive links to recipes, forms, profile, add recipes, categories and contact.  
  
**Recipe Form:**  Includes input fields for name, ingredients, instruction, and additional notes. A dropdown menu for cooking time, difficulty options, categories, portions, cooking material, and if the recipe is free from any allergic effects.
  
**Images:** All images are taken from internet and box sized to fit the recipes pages.  

**Add Image to recipes** Code from [Gazza J MS3](https://github.com/GazzaJ/CI-MS3-W3Recipes/blob/main/templates/add_recipe.html)
  
**Flash messages:** Vertification to users when creating, editing or deleting post or deleting account.  
  
**Buttons:** In the top right coner of every recipe that profile user has created is an option to edit the recipe or delete it. When register an account or login there is a comfirmation button at the end. And in the top right corner there is a x-mark if user want to close the window without register or login.  

**Footer** [From Materialized](https://materializecss.com/footer.html) Repitition links at the bottom from the navbars, copyright information, and a back to top button.
  

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
**Dev Tools**  
  
**Error:** <img width="356" alt="Skärmavbild 2021-04-14 kl  11 11 35" src="https://user-images.githubusercontent.com/70586630/115026318-a4c2b580-9ec2-11eb-845a-648e8c6bea5f.png">  
  
**Description:** The logo and background image doesn't show in the profile and edit window throughts a 404 error.  
  
**Solution:** With hint from tutors of the static files, to edit the images source, since the pages where the logo doesn't show are 2nd sources from the base.html.
  
  
**Error:** <img width="329" alt="Skärmavbild 2021-04-14 kl  15 27 16" src="https://user-images.githubusercontent.com/70586630/115026150-71802680-9ec2-11eb-9126-fe4e0b920acd.png">
  
**Description:** Cookie error after deleting session cookies in the dev tools. 
   
**Solution:** Had to contact tutor that went in and did something so I could login. Not sure what he did.
  
  
**Error:** <img width="572" alt="Skärmavbild 2021-04-23 kl  09 34 20" src="https://user-images.githubusercontent.com/70586630/115863246-7e0dfd00-a435-11eb-8d67-9bed8c52f6a6.png">

  
**Description:** Unable to open the gitpod project and run python3 app.py to open webpage.  
  
**Solution:** Had to contact tutor that told me to go in to the project workspace and reopen the project. After that everything worked fine.  
  
  
**Error:** Unable to use the add_recipe link. 

**Description:** The add_recipe link redirects to the get_recipes page.   
  
**Solution:** Indentation was incorrect in the app.py file.  
<img width="511" alt="Skärmavbild 2021-04-23 kl  13 20 10" src="https://user-images.githubusercontent.com/70586630/115864135-c24dcd00-a436-11eb-9ddc-a12cc529cd50.png">
<img width="516" alt="Skärmavbild 2021-04-23 kl  13 19 46" src="https://user-images.githubusercontent.com/70586630/115864141-c679ea80-a436-11eb-9ad4-2d9ff5fd4ed6.png">
  
  
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

Banner  
Header background  
https://crossroads.ca/wp-content/uploads/2020/06/cooking-banner-d.jpg  
  
Logo - I made it with google fonts and cut the background in 'Images' on mac.

Categories Pictures 
Snacks  
https://www.wellandgood.com/wp-content/uploads/2019/07/GettyImages-980405988-Manuta.jpg  
  
Lunch  
https://www.parentmap.com/images/article/7762/bento_box_beauty04-e1280985383510.jpg  
  
Dinner  
https://www.froddo.com/media/blog/10%20Ideas%20for%20Kid%E2%80%99s%20Birthday%20Party%20Snacks/04%20fruit%20skewers.jpg  
  
Healthy  
https://www.froddo.com/media/blog/10%20Ideas%20for%20Kid%E2%80%99s%20Birthday%20Party%20Snacks/04%20fruit%20skewers.jpg  
  
Sweets  
https://thumbs.dreamstime.com/b/frozen-banana-chocolate-lollies-easy-homemade-vegan-sweets-lollipops-walnuts-sprinkles-kids-white-close-up-212396164.jpg 
  
Party  
http://www.kidskubby.com/wp-content/uploads/2012/07/kids-birthday-party-food-.001.jpg  

**Recipes: Image & link**
   
**Bento Box**  
Image: https://i.insider.com/5d56bae7cd978411b647d5b6?width=750&format=jpeg&auto=webp  
  
Recipes: https://peasandcrayons.com/2019/09/bento-box-lunch-ideas-for-kids.html  
  
  
**Flying Saucers**  
Image: https://www.tasteofhome.com/wp-content/uploads/2018/01/exps7948_FF163882D01_12_6b-1.jpg?w=1200  
  
recipe: https://www.tasteofhome.com/recipes/flying-saucers/  
  
  
**Crunchy Granola Sticks**  
Image: https://www.tasteofhome.com/wp-content/uploads/2018/01/Crunchy-Granola-Pretzel-Sticks_EXPS_CBZ16_193410_D05_20_5b-4.jpg?w=1200  
  
recipe: https://www.tasteofhome.com/recipes/crunchy-granola-pretzel-sticks/  
  
  
**Frozen Monkey Treat**  
Image: https://www.tasteofhome.com/wp-content/uploads/2018/01/Frozen-Chocolate-Monkey-Treats_EXPS_SSCBZ18_176690_B09_27_1b.jpg?w=1200  
  
Recipe: https://www.tasteofhome.com/recipes/frozen-chocolate-monkey-treats/  
  
  
**Chicken Broccoli Pasta**  
Image: https://www.budgetbytes.com/wp-content/uploads/2017/01/Chicken-and-Broccoli-Pasta-with-Lemon-Cream-Sauce-bowl-close-500x500.jpg  
  
Recipe: https://www.budgetbytes.com/chicken-broccoli-pasta-lemon-cream-sauce/  
  
  
**Pizza Alphabet**  
Image: https://hips.hearstapps.com/del.h-cdn.co/assets/17/49/768x768/square-1512396079-delish-kids-pizza-stockings-0011.jpg?resize=640:  
  
Recipe: https://www.delish.com/cooking/recipe-ideas/a19425405/alphabet-pizza-recipe/  


**Bluberry Peach Treat**  
Image: https://i.pinimg.com/originals/eb/30/99/eb3099d80912a48b0bba36148551d730.jpg  
  
Recipe: https://www.tasteofhome.com/recipes/rise-and-shine-parfait/  
  

**Veggi Mix**  
Image: https://tastesbetterfromscratch.com/wp-content/uploads/2017/01/Veggie-Dip-1.jpg  
  
Recipe: https://www.thechunkychef.com/garlic-and-herb-veggie-dip/  
  
  
**Magic Wands**  
Image: https://www.tasteofhome.com/wp-content/uploads/2018/01/Magic-Wands_EXPS_HCA18_34104_D02_22_7b-4.jpg?w=1200  
  
Recipe: https://www.tasteofhome.com/recipes/magic-wands/  
  
**Apple Doughnuts**  
Image: https://img.taste.com.au/BqW_bIeh/w720-h480-cfill-q80/taste/2019/01/apple-doughnuts-146416-1.jpg  
  
Recipe: https://www.taste.com.au/recipes/apple-doughnuts/28lijz9r  
    
**Choocolate-Raspberry Fonue**  
Image: https://www.tasteofhome.com/wp-content/uploads/2018/01/Chocolate-Raspberry-Fondue_EXPS_HSCBZ19_13932_B07_12_1b-1.jpg?w=1200  
  
Recipe: https://www.tasteofhome.com/recipes/chocolate-raspberry-fondue/  
  
  
  
### Acknowledgements
•	I received inspiration for this project from X

### LINKS:
