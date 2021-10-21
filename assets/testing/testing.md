# Testing

- [Go back to the project and README file](https://github.com/SamBurgess93/GamerHub)
- [Go to the live project here!](https://gamer-hub-sam.herokuapp.com/)

## Table of Contents
1. [Automated Testing](#automated-testing)
2. [Manual Testing](#manual-testing)
3. [User Testing](#user-testing)
4. [Bugs found during development](#bugs-found-during-development)
5. [Bugs found while testing manually](#bugs-found-while-testing-manually)

## Automated Testing
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
    - GamerHub passed the W3C CSS Validator without any errors apart form parse errors associated with the jinja templating. 20th Oct - 2021
- [W3C Markup Validation](https://validator.w3.org/)
    - This project passed the W3C Markup Validator without any errors. 20th Oct - 2021
- [JSHint](https://jshint.com/)
    - This project was validated with JSHint validator on 20th Oct 2021 with 0 errors


## Manual testing
All manual tests were done in the following browsers:
- Firefox
- Google Chrome
- Microsoft Edge
- Safari 

During each stage of the development if errors were encountered they were addressed before proceeding.

At every step of development the errors highlighted in the code were addressed before proceeeding. Friends and family members reviewed the site to identify bugs and give feedback on user experience. The devices that were used to test on Google Chrome Dev Tools were;
- iPad
- iPad Pro
- iPhone 5/SE
- iPhone 6/7/8
- Galaxy S5

I also tested with other screens I have also;

- Samsung S9 mobile
- 23.8" Desktop Screen (1920 x 1080)
- Laptop 14" (1920 x 1080)

- Checking Responsiveness.
    - Check that the content fits into the different viewports with no side scroll behaviour.
    - Check that on smaller screen the cards are 3 in each row with scoreboard below.
    - Check that modals pops up and closes correctly!

## User testing
The user testing is based on the user stores from the README file.

**As a first time user, I want to:**

1. **..Easily understand the main purpose of the website..**
    - Upon enetering the website you instantly presented with the list of games which lets the user know what the website is about and invites them to interact.
2. **..Navigate through the site with ease..**
    - The home page has the Navbar which allows the use to navigate around with ease.
3. **..See all game reviews..**
    - All visitors can see the reviews for each game by clicking on the see review button on the games individual card.
4. **..Be able to register and create my own account...**
    - The register link is visible on the navbar for all visitors. This instantly brings the new user to the register page where they can create their own account.

**As a frequent user, I want to:**

1. **..To search for specific games..**
    - The search bar is visible on the homepage for all users. This search form searches through all games via a keyword which the user enters.
2. **..Login to my own account...**
    - Users who have created their own profile can log back in by navigating to the login page on the navbar.
3. **..Add a game..**
    - The add a game link is only visible on the navbar for logged in users. This page has a form which insists on the user filling in all the details necessary for a game. It guides the user what to enter via the placeholder text.
4. **..Add a game review..**
    - All logged in users can add a review to any game via the button on the games card on the home page.
5. **..Edit/delete a game I entered previously..**
    - This functionality is available to logged in users from their profile page. The link to the profile page is only visible to logged in users.
6. **..Edit/delete a game review that I had made previously..**
    - This functionality is available to logged in users from their profile page. The link to the profile page is only visible to logged in users.
7. **..Logout from my own profile...**
    - The log out option is only available to users who are logged in. When a user logs out the user is removed from the session cookie and the navbar goes back to the display for visitors.

**As an admin, I want to:**
1. **..Be able to create add, edit and delete genres..**
    - The admin is the only one with access to the "manage genres" link in the navbar and can add new genres, edit or delete them.
 

## Bugs
* **Fixed!** When a registered user editted their reviews on a game the "game-name" would populate as None. This was due to the name field in the 'edit game' form being disabled. Once I removed this it worked as expected.
* **Not fixed!** When adding a game it can be difficult for a user to validate a image address, especiallt if the image address is encrypted