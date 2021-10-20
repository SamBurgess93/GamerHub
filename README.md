# GamerHUB

![Preview](assets/readme/responsive.PNG)

[Link to the Live Project](https://gamer-hub-sam.herokuapp.com/).

GamerHUB is a website where users can leave reviews on their favorite video games. All visitors to the website can read these reviews, but only members can add reviews or edit their own review.

## Table of contents
1. [UX](#ux)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Development Planes](#development-planes)
    4. [Changes Made During Project Development](#changes-made-during-project-development)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features to Implement in the future](#features-to-implement-in-the-future)
3. [Technologies Used](#technologies-used)
     1. [Main Languages Used](#main-languages-used)
     2. [Additional Languages Used](#additional-languages-used)
     3. [Frameworks and Programs Used](#frameworks-and-programs-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
     1. [Deploying on GitHub Pages](#deploying-on-github-pages)
     2. [Forking the Repository](#forking-the-repository)
     3. [Creating a Clone](#creating-a-clone)
6. [Credits](#credits)
     1. [Images](#images)
     2. [Code](#code)
7. [Acknowledgements](#acknowledgements)
***

## UX 
### Project Goals
The scope of this project is to create a user centric website using the Flask, Python, MongoDB and Heroku.
 
This is my third Milestone Project that must be developed as part of my Full Stack software development course with Code Institute.

The primary goal of the GamerHUB website is to create a community of likeminded people with similar interests to collaborate and share information and experiences with games they have played. Registered users can leave reviews of games they have played.


### User Stories


**As a first time user, I want to:**

1. Easily understand the main purpose of the website.
2. Navigate through the site with ease
3. Be able to register and create my own account.


**As a frequent user, I want to:**
1. To search for specific games
2. Login to my own account.
3. Add a game review.
4. Edit a game review that I had made previously.
5. Delete a game review.
6. Logout from my own profile.


**As a frequent admin user, I want to:**
1. Be able to see all the games.
2. Be able to see all the reviews.
3. Be able to see all the users.
4. Be able to create new genres.
5. Be able to edit all the genres.
6. Be able to delete all the genres.
7. 


### Development Planes

In order to design and create the GamerHUB, the developer distinguished the required functionality of the site and how it would answer the user stories, as described above, using the **Five Development Planes**:

<strong>1. <u>Strategy</u></strong>

The GamerHUB is an online platform to access reviews of various video games with front-end and back-end functionality, developed using HTML, JavaScript, CSS, Python, Flask, and MongoDB. The main objective is to create a platform which is intuitive and allows the user to easily navigate and find reviews for their favourite games.


<strong>2. <u>Scope</u></strong>

The scope was created from using the Strategy previously defined. This allowed us to align the features to deliver on the strategy. This was seperated into two categories:
- **Content Requirements**
     - The player will be looking for:
          - Dynamic and inviting visuals
          - Simple and vibrant content
          

- **Functionality Requirements**
     - The user will be able to:
          - Search with ease using a search bar
          - Log In to their own profile
          - Add their own reviews
          - Access full CRUD functionality


<strong>3. <u>Structure</u></strong>

When looking at my structural plane I wanted to restrict certain functionality depending on the type of user accessing the site.

Visitors (not registered users) will only only have access to the following:

- Game reviews: lists all game reviews that have been added by registered users
- Log-in/Register: invites the visitor to register or login to the website

On top of these pages, a logged in/ registered user will have access to:

My Games: collections of all reviews games left by the user From here, they will be able to edit or delete their games.
Add Review: from here, a user can add a review for a new game or add a new review on an existing game.
Edit: A user will be able to edit their own reviews.
Add Game: from here, a user can add a new game to the list.
Log-out: user can log out of their own profile.

The admin user will also have access to:

Add Genre: the admin will be able to add new genres to be available for users to pick.
Edit/Delete: only admin users will see edit/delete buttons for each genre.


<strong>4. <u>Skeleton</u></strong>

Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/2Nn1oK8aWFLJcHwU8yChCI/GamerHUB?node-id=0%3A1 "Link to GamerHUB Figma Workspace") with providing a positive user experience in mind:


<strong>5. <u>Surface</u></strong>

- <strong>Colour Scheme</strong>

     - I used the palette maker from the Coolors website to choose my color scheme.

     - The chosen colour scheme was specifically selected in order to define the tone of the game.

     - A General palette was created, with this atmosphere in mind, and was used in designing graphics and complimentary text colour:

          ![Colors](assets/readme/gamerhub.png "General Colour Palette")



- <strong>Typography</strong>

     - The primary font chosen is [Lato](https://fonts.google.com/specimen/Lato). A sans-serif typeface, Lato is geometrically shaped and is easily readable.

     - The charismatic combination of the typefaces compliments the clean aesthetic and entertaining theme set by the colour palette.

### Changes Made During Project Development 
- When looking at the wireframes it is clear to see there was been a few chaanges along the way since the early stages of the idea. I had originally wanted to smaller grids and fit more cards in a row, I decided to change this and add more info in each cards such as "description", "genre", "created by" and "added on" and thus changed to one card per row.

- In the orginal idea I wanted to have a background image but I after some time I went for a simpler plain background inviting the user to focus more on the games and the websites features.

[Back to top ⇧](#table-of-contents)

## Features

 
### Existing Features

- **Navbar** Created using the Materialize CSS framework. Navbar has the title on the left and the menu items on the right hand side. The navbar is fully responsive and changes to match the device screen its being viewed on. Menu items will depend on if the user is a visitor, user or admin.
- **Main content:** This is where the various games will be found and reviews can be accessed.
- **Search Bar:** This will allow the user to find a specific game by name or genre.
- **Flash Messages:** These messages display just below the navbar and give confirmation to the user about actions being completed.
- **Add New Game:** Allows the user to add a new game.
- **Profile:** Allows the user to see their own games and reviews. Users will have the ability to edit and delete games/reviews from this page.
- **LogIn/Register :** Allows the user to login and register for the website.

### Features Left to Implement
- **Donations:** Would allow the user to make donations to the website to support future development.
- **Star Rating:** Users could choose a star rating when adding a game. Or leave a star rating for an existing game.
- **Filter** Filter games be certain criteria such as genre.

## Technologies Used

### Languages and Frameworks

- HTML for main structure of the website.
- CSS to add custom styling to the project.
- [Materialize](https://materializecss.com/) to utilise the grid system and various precoded card panels and buttons
- [JQuery](https://code.jquery.com/) required to use some interactive elements on the materialize
- [Jinja](jinja.palletsprojects.com) to be able to re-use certain elements from similar pages
- [Flask](https://flask.palletsprojects.com/) to be used for the python element of the project

### Applications

- [MongoDB](https://www.mongodb.com/) the database chosen for the project to store all the data.
- [Gitpod](https://gitpod.io/) the development platform for the project.
- [GitHub](https://github.com/) for version control and to store the project after pushing.
- [Heroku](https://www.heroku.com) to deploy the project.
- [Figma](https://figma.com/) used to create the wireframes for the project.
- [Am I Responsive?](http://ami.responsivedesign.is/) Used to generate mockup imagery to be used.


## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, use following steps:

1. Create the app in Heroku.
2. Run the `npm install -g heroku` command in the terminal window to install heroku in the workspace.
3. Run the `heroku login -i` command in the terminal window and enter credentials to login to Heroku.
4. Add and committ the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Create a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

  ```echo web: python <fileName.py> > Procfile```

8. Run the `git push -u heroku main` command in the terminal window to push the app to Heroku.
9. Login to the Heroku page and Entered the following Config Var in Heroku:
   - IP : `0.0.0.0`
   - PORT : `5000`
   - MONGO_URI :`mongodb+srv://<username>:<password></password>@<cluster_name>.9kpcw.mongodb.net/<database></database>?retryWrites=true&w=majority` 
   - SECRET_KEY : `<your_secret_key>`
10. Select Deploy option on Heroku and choose Github as Deployment method then connect to Github and search for repositery to connect by providing the repo name on search box.
11. Heroku will then detect the repo on Github then, click connect
12. Choose main branch as branch to deploy and click Enable automatic Deploys
13. your project has now deployed to Heroku
14. In the top right of the heroku dashboard press the "Open App" button to view your deployed Heroku app.

[Back to top ⇧](#table-of-contents)

## Credits 

### Images
### Code 
I consulted the following sites to better understand some elements of code:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
               https://www.w3schools.com/css/css3_object-fit.asp
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Codepen](https://codepen.io/ "Link to Codepen page")
- [JSfiddle](https://jsfiddle.net/ "Link to JSfiddle page")

## Acknowledgements

- I would like to thank my friends and family for their time and opinions on the website.
- I would like to thank my mentor, Seun, for her help and constructive feedback throughout the project.

[Back to top ⇧](#table-of-contents)