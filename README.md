# GamerHUB

![Preview](assets/readMe/responsive.png)

[Link to the Live Project](#).

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
2. Navigate through the ste with ease
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
4. Be able to edit all games.
5. Be able to edit all the reviews.
6. Be able to edit all the users.
7. Be able to delete all the reviews.
8. Be able to delete all the games.
9. Be able to delete all the profiles.


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

- Game reviews: lists all game reviews that have been approved by the admin
- Log-in/Register: invites the visitor to register or login to the website

On top of these pages, a logged in/ registered user will have access to:

My Reviews: collections of all reviews left by the user. From here, they will also be able to edit or delete these reviews
Add Review: from here, a user can add a new review for a restaurant only after being approved by an admin
Edit: A user will be able to edit their own review
Add Game: from here, a user can request to add a new restaurant to the list. This request will need to be approved by an admin user.
Log-out: user can log out of their own profile

The admin user will also have access to:

Approve Games: if a user requests a game that has not yet been entered, the admin will need to approve this
Edit/Delete: only admin users will see edit/delete buttons for each game as well as a delete fucntion for each review.


<strong>4. <u>Skeleton</u></strong>

Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/2Nn1oK8aWFLJcHwU8yChCI/GamerHUB?node-id=0%3A1 "Link to GamerHUB Figma Workspace") with providing a positive user experience in mind:


<strong>4. <u>Surface</u></strong>

- <strong>Colour Scheme</strong>

     - I used the palette maker from the Coolors website to choose my color scheme.

     - The chosen colour scheme was specifically selected in order to define the tone of the game.

     - A General palette was created, with this atmosphere in mind, and was used in designing graphics and complimentary text colour:

          ![Colors](assets/readMe/color.png "General Colour Palette")



- <strong>Typography</strong>

     - The primary font chosen is [Teko](https://fonts.google.com/specimen/Teko?preview.text_type=custom&query=teko). A sans-serif typeface, Teko is geometrically shaped and is easily readable.

     - The charismatic combination of the typefaces compliments the clean aesthetic and entertaining theme set by the colour palette.

### Changes Made During Project Development 
- When looking at the wireframes it is clear to see there was been a few chaages along the way since the early stages of the idea. I originally planned for a pattern to light up
on the grid shown and the user to press the sqaures in the same pattern they had just seen. I had decided that this option was quite plain and uninviting as there was no theme involved.
I then chose to use the theme of cryptocurrencies as it is a popular topic in society at this time. I decided to use different crypto logos to create a card matching game which would be more inviting for the user. Hence the title was changed from "RECALL" to "Crypto Memory".

- In the orginal idea I wanted the game information to be placed near the bottom of the screen. As the project developed however I wanted to create a scorebaord area that held the game info/stats that could move dynamically around the screen depending on which device it was being played. This would show the current score, timer and moves as well as the area you reset the game, toggled the sound and could leave feedback for the developer.  

[Back to top ⇧](#table-of-contents)

## Features

 
### Existing Features

- **Navbar** Created using the Materialize CSS framework. Navbar has the title on the left and the menu items on the right hand side. The navbar is fully responsive and change to match the device screen its being viewed on. Menu items will depend on if teh user is a visitor, user or admin.
- **Main content:** This is where the various games will be found and reviews can be accessed.
- **Flash Messages:** These messages display just below the navbar and give confirmation to the user about actions being completed,
- **Reset button:** A button to reset the game to try again.
- **Time Counter** - A time counter, displaying the time elapsed since page load, gives users feedback on how long they have been playing, in minutes and seconds.
- **Session Storage** - The `sessionStorage` function is used to store the user score from the previous round.
- **Current Score:** To tell the player what their live score is in real time. This score counter goes up and down depending on how many correct/incorrect matches the user has.

### Features Left to Implement
- Filter restaurants by "has_vegan_options" or "has_gluten_free_options"