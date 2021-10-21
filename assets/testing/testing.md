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
    - This project was validated with JSHint validator on 2oth Oct 2021 with 0 errors


## Manual testing
All manual tests were done in the following browsers:
- Firefox
- Google Chrome
- Microsoft Edge
- Safari 

1. Firstly I would open each browser and confirm that the content loads correctly.

2. I would test the two main sections (cards and scoreboard) seperately on each browser
    
    - Card Section 
        - When the page is loaded click the first card and confirm the audio plays and card stays flipped over.
        - Confirm timer has started.
        - When clicking second card confirm audio fires:
            - If card matches both cards stay flipped and audio fires, move counter changes by one and +50 points added to score
            - If card doesnt match both cards flip back over and audio fires, move counter changes by one and -20 points to score.
        - Confirm that a third card cant be clicked on until unmatched cards flip back over, board is locked.
        - When all cards are matched, timer stops, modal pops up congratulating the player.

    - Scoreboard Section 
        - When the reset button is clicked all page reloads, counters go to zero and all cards flip back over.
        - When clicking on the speaker icon the background music starts playing and the icon changes to a speaker icon that is playing sound. 
        - When the speaker icon is clicked again the music stops.
        - When clicking the question mark icon the 'How to play' modal pops up. Check the close modal icon closes the modal.

All of the above tests were done in the Google Chrome Device Toolbar on the following devices:

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

**As a player, I want to:**

1. **..play a game I enjoy**
    - Testing our memory is a classic way of having fun. The sense of achievement gained from finding a matching pair 
    makes this game enjoyable and entcies the user to come back and keep playing.
2. **..Make the process of starting the game intuitive..**
    - The design of the cards themselves invite the user to click on them hence starting the game.
3. **..To be able track my progress during the game, with a clear score counter..**
    - the scoreboard section contains the score counter that live tracks the score, whether it goes up or down.
4. **..Clearly know when my answers are correct through audio feedback..**
    - The sounds effects used are subtle and are only used when a player finds a correct match.
5. **..Have the ability to toggle background music on or off..**
    - The electronic background music is optional and can be toggled on and off by the speaker icon.
6. **..View the score for my previous session, creating a target to beat..**
    - In the scoreboard section the previous rounds score is displayed underneath the live score.
7. **..Have the ability to communicate with the developer to provide feedback on the overall experience, to improve the game..**
    - The player has the ability to leave some feedback to improve the game by using the contact us modal.
8. **..Have the option to play the game on any device, whether it be desktop, tablet or mobile phone..**
    - The player will be able to play on any device as the design is simplistic and responsive to any screen size.

## Bugs
* **Fixed!** When testing the game on my iPhone/iPad the memory cards wouldn't turn properly when clicking on them. 
This seemed to look fine when I tried the game out in device toolbar in my Chrome browser. 
The feature of flipping the cards did not seem to be supported by Safari browsers so I solved this problem by 
adding a webkit attribute in my css code.
* **Fixed!** When I was first testing the responsiveness of my code it didnt look great on smaller devices. This is when I 