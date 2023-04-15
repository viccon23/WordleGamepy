import random
import sys
import pygame

from wordsMedium import *
from wordsEasy import *
from wordsHard import *
pygame.init()
# Constants
WIDTH, HEIGHT = 633, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
BACKGROUNDEASY = pygame.image.load("assets/StartingTilesEasy.png")
BACKGROUNDHARD = pygame.image.load("assets/StartingTilesHard.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
BACKGROUND_RECTEASY = BACKGROUND.get_rect(center=(317, 302))
BACKGROUND_RECTHARD = BACKGROUND.get_rect(center=(320, 300))


ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

## Keyboard
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
##Letter Font
GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

#Global Variables
current_guess = []

current_guess_string = ""

current_letter_bg_x = 110
current_letter_bg_xEASY = 90




## Guesses start at zero
guesses_count = 0
    # guesses is a 2D list that will store guesses. A guess will be a list of letters.
    # The list will be iterated through and each letter in each guess will be drawn on the screen.
## Amount of guesses will be different for every function


#guessesHARD = [[]] * 4

# Indicators is a list storing all the Indicators object. An indicator basically the keyboard you see when you are playing the game.
indicators = []

game_result = ""
#Gets from list of 5-letter words
CORRECT_WORDEASY = random.choice(WORDSEASY)
CORRECT_WORDMED = random.choice(WORDSMED)
CORRECT_WORDHARD = random.choice(WORDSHARD)
##############################################################################################################################################################################
## FOR MEDIUM MODE
def mediumMode():
        ## Screen Display
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    pygame.display.update()

    LETTER_X_SPACINGMED = 85
    LETTER_Y_SPACINGMED = 12

    ## Size of Letter in Text box
    LETTER_SIZE = 75


    guessesMED = [[]] * 6


    class Letter:
        def __init__(self, text, bg_position):
            # Initializes all the variables, including text, color, position, size, etc.
            self.bg_color = "white"
            self.text_color = "black"
            self.bg_position = bg_position
            self.bg_x = bg_position[0]
            self.bg_y = bg_position[1]
            self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
            self.text = text
            self.text_position = (self.bg_x+36, self.bg_position[1]+34)
            self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.text_position)

        def draw(self):
            # Puts the letter and text on the screen at the desired positions.
            pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
            if self.bg_color == "white":
                pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
            self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

        def delete(self):
            # Fills the letter's spot with the default square, emptying it.
            pygame.draw.rect(SCREEN, "white", self.bg_rect)
            pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
            pygame.display.update()

    class Indicator:
        def __init__(self, x, y, letter):
            # Initializes variables such as color, size, position, and letter.
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, 57, 75)
            self.bg_color = OUTLINE

        def draw(self):
            # Puts the indicator and its text on the screen at the desired position.
            pygame.draw.rect(SCREEN, self.bg_color, self.rect)
            self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
            self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
            SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

    # Drawing the indicators on the screen.

    indicator_x, indicator_y = 20, 600

    for i in range(3):
        for letter in ALPHABET[i]:
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 60
        indicator_y += 100
        if i == 0:
            indicator_x = 50
        elif i == 1:
            indicator_x = 105

    def check_guess(guess_to_check):
        # Goes through each letter and checks if it should be green, yellow, or grey.
        global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
        game_decided = False
        for i in range(5):
            lowercase_letter = guess_to_check[i].text.lower()
            if lowercase_letter in CORRECT_WORDMED:
                if lowercase_letter == CORRECT_WORDMED[i]:
                    guess_to_check[i].bg_color = GREEN
                    for indicator in indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = GREEN
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    if not game_decided:
                        game_result = "W"
                else:
                    guess_to_check[i].bg_color = YELLOW
                    for indicator in indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = YELLOW
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    game_result = ""
                    game_decided = True
            else:
                guess_to_check[i].bg_color = GREY
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREY
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
            guess_to_check[i].draw()
            pygame.display.update()
        
        guesses_count += 1
        current_guess = []
        current_guess_string = ""
        current_letter_bg_x = 110

        if guesses_count == 6 and game_result == "":
            game_result = "L"

    def play_again():
        # Puts the play again text on the screen.
        pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
        play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
        word_was_text = play_again_font.render(f"The word was {CORRECT_WORDMED}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
        SCREEN.blit(word_was_text, word_was_rect)
        SCREEN.blit(play_again_text, play_again_rect)
        pygame.display.update()

    def reset():
        # Resets all global variables to their default states.
        global guesses_count, CORRECT_WORDMED, guessesMED, current_guess, current_guess_string, game_result
        SCREEN.fill("white")
        SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
        guesses_count = 0
        CORRECT_WORDMED = random.choice(WORDSMED)
        guessesMED = [[]] * 6
        current_guess = []
        current_guess_string = ""
        game_result = ""
        pygame.display.update()
        for indicator in indicators:
            indicator.bg_color = OUTLINE
            indicator.draw()

    def create_new_letter():
        # Creates a new letter and adds it to the guess.
        global current_guess_string, current_letter_bg_x
        current_guess_string += key_pressed
        new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+LETTER_Y_SPACINGMED))
        current_letter_bg_x += LETTER_X_SPACINGMED
        guessesMED[guesses_count].append(new_letter)
        current_guess.append(new_letter)
        for guess in guessesMED:
            for letter in guess:
                letter.draw()

    def delete_letter():
        # Deletes the last letter from the guess.
        global current_guess_string, current_letter_bg_x
        guessesMED[guesses_count][-1].delete()
        guessesMED[guesses_count].pop()
        current_guess_string = current_guess_string[:-1]
        current_guess.pop()
        current_letter_bg_x -= LETTER_X_SPACINGMED

    while True:
        if game_result != "":
            play_again()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_result != "":
                        reset()
                        titleScreen()
                    else:
                        if len(current_guess_string) == 5 and current_guess_string.lower() in WORDSMED:
                            check_guess(current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            create_new_letter()


##############################################################################################################################################################################
## FOR EASY MODE
def easyMode():
        ## Screen Display
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUNDEASY, BACKGROUND_RECTEASY)
    pygame.display.update()
    # Easy
    LETTER_SIZEEASY=64
    



    LETTER_X_SPACINGEASY = 71
    LETTER_Y_SPACINGEASY = 15

    guessesEASY = [[]] * 7


    class Letter:
        def __init__(self, text, bg_position):
            # Initializes all the variables, including text, color, position, size, etc.
            self.bg_color = "white"
            self.text_color = "black"
            self.bg_position = bg_position
            self.bg_x = bg_position[0]+88
            self.bg_y = bg_position[1]
            ## Affects the position of rectangles
            self.bg_rect = (self.bg_x, self.bg_y, LETTER_SIZEEASY, LETTER_SIZEEASY)
            self.text = text
            self.text_position = (self.bg_x+32, self.bg_position[1]+30)
            self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.text_position)

        def draw(self):
            # Puts the letter and text on the screen at the desired positions.
            pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
            if self.bg_color == "white":
                pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 2)
            self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

        def delete(self):
            # Fills the letter's spot with the default square, emptying it.
            pygame.draw.rect(SCREEN, "white", self.bg_rect)
            pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
            pygame.display.update()

    class Indicator:
        def __init__(self, x, y, letter):
            # Initializes variables such as color, size, position, and letter.
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, 57, 75)
            self.bg_color = OUTLINE

        def draw(self):
            # Puts the indicator and its text on the screen at the desired position.
            pygame.draw.rect(SCREEN, self.bg_color, self.rect)
            self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
            self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
            SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

    # Drawing the indicators on the screen.

    indicator_x, indicator_y = 20, 600

    for i in range(3):
        for letter in ALPHABET[i]:
            new_indicator = Indicator(indicator_x, indicator_y, letter)
            indicators.append(new_indicator)
            new_indicator.draw()
            indicator_x += 60
        indicator_y += 100
        if i == 0:
            indicator_x = 50
        elif i == 1:
            indicator_x = 105

    def check_guess(guess_to_check):
        # Goes through each letter and checks if it should be green, yellow, or grey.
        global current_guess, current_guess_string, guesses_count, current_letter_bg_xEASY, game_result
        game_decided = False
        for i in range(4):
            lowercase_letter = guess_to_check[i].text.lower()
            if lowercase_letter in CORRECT_WORDEASY:
                if lowercase_letter == CORRECT_WORDEASY[i]:
                    guess_to_check[i].bg_color = GREEN
                    for indicator in indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = GREEN
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    if not game_decided:
                        game_result = "W"
                else:
                    guess_to_check[i].bg_color = YELLOW
                    for indicator in indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = YELLOW
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    game_result = ""
                    game_decided = True
            else:
                guess_to_check[i].bg_color = GREY
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREY
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
            guess_to_check[i].draw()
            pygame.display.update()
        
        guesses_count += 1
        current_guess = []
        current_guess_string = ""
        current_letter_bg_xEASY = 90

        if guesses_count == 7 and game_result == "":
            game_result = "L"

    def play_again():
        # Puts the play again text on the screen.
        pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
        play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
        word_was_text = play_again_font.render(f"The word was {CORRECT_WORDEASY}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
        SCREEN.blit(word_was_text, word_was_rect)
        SCREEN.blit(play_again_text, play_again_rect)
        pygame.display.update()

    def reset():
        # Resets all global variables to their default states.
        global guesses_count, CORRECT_WORDEASY, guessesEASY, current_guess, current_guess_string, game_result
        SCREEN.fill("white")
        SCREEN.blit(BACKGROUNDEASY, BACKGROUND_RECTEASY)
        guesses_count = 0
        CORRECT_WORDEASY = random.choice(WORDSEASY)
        guessesEASY = [[]] * 7
        current_guess = []
        current_guess_string = ""
        game_result = ""
        pygame.display.update()
        for indicator in indicators:
            indicator.bg_color = OUTLINE
            indicator.draw()

    def create_new_letter():
        # Creates a new letter and adds it to the guess.
        global current_guess_string, current_letter_bg_xEASY
        current_guess_string += key_pressed
        ## Affects the spacing of the new word guess after each attedmpt
        new_letter = Letter(key_pressed, (current_letter_bg_xEASY, guesses_count*85+LETTER_Y_SPACINGEASY))
        current_letter_bg_xEASY += LETTER_X_SPACINGEASY
        guessesEASY[guesses_count].append(new_letter)
        current_guess.append(new_letter)
        for guess in guessesEASY:
            for letter in guess:
                letter.draw()

    def delete_letter():
        # Deletes the last letter from the guess.
        global current_guess_string, current_letter_bg_xEASY
        guessesEASY[guesses_count][-1].delete()
        guessesEASY[guesses_count].pop()
        current_guess_string = current_guess_string[:-1]
        current_guess.pop()
        current_letter_bg_xEASY -= LETTER_X_SPACINGEASY

    while True:
        if game_result != "":
            play_again()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_result != "":
                        reset()
                        titleScreen()
                    else:
                        if len(current_guess_string) == 4 and current_guess_string.lower() in WORDSEASY:
                            check_guess(current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        ## Change length of word you can type
                        if len(current_guess_string) < 4:
                            create_new_letter()

##############################################################################################################################################################################
## Title Screen
def titleScreen():
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    pygame.display.update

    # Set up the display
    screen_width, screen_height = WIDTH, HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Wordle")

    # Create the title font
    title_font = pygame.font.SysFont("Arial", 120)
    # Set up the font
    font = pygame.font.SysFont("Arial", 52)

    # Create the title text surface
    title_text = title_font.render("Wordle", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(screen_width/2, screen_height/4))

    # Create the difficulty buttons
    button_width, button_height = 200, 50
    button_x = screen_width/2 - button_width/2
    easy_button_rect = pygame.Rect(button_x, screen_height/2, button_width, button_height)
    medium_button_rect = pygame.Rect(button_x, screen_height/2 + button_height*1.5, button_width, button_height)
    hard_button_rect = pygame.Rect(button_x, screen_height/2 + button_height*3, button_width, button_height)
    easy_button_text = font.render("Easy", True, (0, 0, 0))
    easy_button_text_rect = easy_button_text.get_rect(center=easy_button_rect.center)
    medium_button_text = font.render("Medium", True, (0, 0, 0))
    medium_button_text_rect = medium_button_text.get_rect(center=medium_button_rect.center)
    hard_button_text = font.render("Hard", True, (0, 0, 0))
    hard_button_text_rect = hard_button_text.get_rect(center=hard_button_rect.center)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked
                if easy_button_rect.collidepoint(event.pos):
                    easyMode()
                elif medium_button_rect.collidepoint(event.pos):
                    mediumMode()
                elif hard_button_rect.collidepoint(event.pos):
                    pass
                    
        # Draw the screen
        screen.fill((255, 255, 255))
        screen.blit(title_text, title_rect)
        pygame.draw.rect(screen, (0, 0, 0), easy_button_rect, 3) # draw outer rectangle
        pygame.draw.rect(screen, (255, 255, 255), easy_button_rect.inflate(-6, -6)) # draw inner rectangle
        screen.blit(easy_button_text, easy_button_text_rect)
        pygame.draw.rect(screen, (0, 0, 0), medium_button_rect, 3) # draw outer rectangle
        pygame.draw.rect(screen, (255, 255, 255), medium_button_rect.inflate(-6, -6)) # draw inner rectangle
        screen.blit(medium_button_text, medium_button_text_rect)
        pygame.draw.rect(screen, (0, 0, 0), hard_button_rect, 3) # draw outer rectangle
        pygame.draw.rect(screen, (255, 255, 255), hard_button_rect.inflate(-6, -6)) # draw inner rectangle
        screen.blit(hard_button_text, hard_button_text_rect)
        pygame.display.flip()
    # Clean up
    pygame.quit()


# Program will start with Title Screen
titleScreen()


