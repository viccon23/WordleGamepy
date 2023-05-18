# WordieGamepy

  Wordie is a Wordle clone created by a group of collegues with the purpose of creating a challenging and entertaining game.
  
The rules of the game are simple:
  You are given a limited number of attempts and time (Both depending on the difficulty chosen) to guess a randomly chosen word from
the program, with the only source of clues being your previous guesses and the placement of the letters:
  - Any letters that appear with a green background are in the chosen word and correct spot
  - Any letters that appear with a yellow background are in the chosen word, but not in the correct spot
  - Any letters that appear with a gray background are not in the chosen word, and not in the correct spot

Below is a Flow Diagram that better visualizes the program's function

![Flow Diagram](https://github.com/viccon23/WordleGamepy/assets/123285276/0c6bad59-9d0a-45bb-8070-5854d2702cf1)

 In essence, each difficulty is encapsulated in a function that contains multiple functions to get the correct word, set up the spacing of how far apart each letter should be to match the tiles, a class for creating the string and for creating the keyboard in the bottom, and functions to check the word if it’s correct.
 
 There were 3 packages installed for this program: Pygame, Sys, and random, so be sure to have those installed to have the program work as intended. Additionally, 
if you have your computer screen zoomed in, then the keyboard and game board will not show correctly. You can change them via your computer settings.

  This program works best with resolutions 1920x1080 and above.
