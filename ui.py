import tkinter as tk
from pygame import mixer
from tkinter import simpledialog
from pygame import mixer
import sys
import os
from sourcecode import *

def backnoise():
    '''Sets the backround music'''
    mixer.init()
    mixer.music.load("sounds/background.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()

backnoise()
click_sound = mixer.Sound("sounds/button.mp3") # Defining the button sound


###############
RippleEffect = story() # Global function that intiates the whole game. DO NOT TOUCH
###############


class HomePage(tk.Frame):
    '''The start menu wiht a title, play game, and exit game button'''
    def __init__(self, master = None):
        '''Initializing the Home Page'''
        tk.Frame.__init__(self, master) # Initializing the frame
        self.master = master # Defining the master for widget for the main class
        self.grid() # Placing the frame in a grid layout
        self.createWidgets() # Calling for the widget function
    
    def createWidgets(self):
        '''Creating the buttons and background image'''
        SIZE = 1000 # Setting the defined size for the widgets
        self.canvas = tk.Canvas(self, width = SIZE, height = SIZE) # Sets the background size
        self.canvas.grid()
        self.background_image = tk.PhotoImage(file = "bg/home.png") # Opens the background image file
        self.canvas.create_image(0, 0, anchor = "nw", image = self.background_image) # Sets it as the background
        
        letters = ["R", "I", "P", "P", "L", "E", "", "E", "F", "F", "E", "C", "T"]
        self.labels = []

        for letter in letters: 
            label = tk.Label(self.canvas, text = letter, font = ("Impact", 50), fg = "white", bg = "black", padx = 10) # Creates a label widget for each letter
            self.labels.append(label)
        
        self.canvas.after(80, self.show()) # Setting a time delay of 80 miliseconds before it begins running the command
        
        self.quitButton = tk.Button(self.canvas, text = 'Exit Game', command = self.quit, font = ("Impact", 40), width = 10) # Defines a quit button associated to the command self.quit()
        self.quitButton.bind("<Button-1>",lambda event: click_sound.play()) # Binding it to the sound defined above
        self.canvas.create_window(SIZE//2, (SIZE//2)+(SIZE//8), window = self.quitButton) # Setting it on the window

        button = tk.Button(self.canvas, text = "Start Game", command = self.next_page, font = ("Impact", 40), width = 10) # Defines a start game button that switches pages. Associated to the command self.next_page()
        self.canvas.create_window(SIZE//2, SIZE//2, window = button) # Setting it on the window
        button.bind("<Button-1>", lambda event: click_sound.play()) # Binds the button to play the click sound

    
    def show(self, index = 0, x = 225, y = 90): # Setting the positions of the x and y placement of the letter
        '''This displays each letter of the title recursively with a specified delay between each label'''
        if index < len(self.labels): # Check if the index is within the range of letters
            self.labels[index].place(x = x, y = y) # Place the letter at the specified position (x, y)
            self.canvas.after(45, lambda: self.show(index+1, x+39.5, y)) # After 45 miliseconds, calls the show method recursively with the next index and new position
    
    def next_page(self):
        '''Calls the function in the main class to switch pages'''
        self.master.show_game_page()


##################################################################
##################################################################


class GamePage(tk.Frame):
    """The game page, including the character selection page"""
    def __init__(self, master = None):
        '''Initializes the Game Page'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        '''Creating the buttons and background image'''
        SIZE = 1000
        self.canvas = tk.Canvas(self, width = SIZE, height = SIZE) # Sets the background size
        self.canvas.grid()
        self.background_image = tk.PhotoImage(file = "bg/charbk.png") 
        self.canvas.create_image(0, 0, anchor = "nw", image = self.background_image)
        label = tk.Label(self, text = "Select A Character", font = ("Impact", 60), bg = "white", fg = "black", relief = tk.RAISED, bd = 5, padx = 10, pady = 10) # Defining the title for the page
        label.place(relx = 0.25, rely = 0.05) # Placing the title

        # Creating the character, Romy (The Designer)
        chr1 = tk.Button(self.canvas, text = 'Romy', command = self.next_page2, font = ("Impact", 30), width = 6) # Defining character buttons that switch pages
        self.canvas.create_window(SIZE//5, (SIZE-SIZE//3), window = chr1)
        chr1.bind("<Button-1>", lambda event: click_sound.play()) # Button clicking sound

        # Creating the character, Zayden (The ReadMe)
        chr2 = tk.Button(self.canvas, text = 'Zayden', command = self.next_page2, font = ("Impact", 30), width = 6)
        self.canvas.create_window(SIZE//(2.5), (SIZE-SIZE//3), window = chr2)
        chr2.bind("<Button-1>", lambda event: click_sound.play()) # Button clicking sound

        # Creating the character, Dimitri (The Scriptmaster)
        chr3 = tk.Button(self.canvas, text = 'Dimitri', command = self.next_page2, font = ("Impact", 30), width = 6)
        self.canvas.create_window(SIZE//1.67, (SIZE-SIZE//3), window = chr3)
        chr3.bind("<Button-1>", lambda event: click_sound.play()) # Button clicking sound

        # Creating the character, Ryan (The Source)
        chr4 = tk.Button(self.canvas, text = 'Ryan', command = self.next_page2, font = ("Impact", 30), width = 6)
        self.canvas.create_window(SIZE-SIZE//5, (SIZE-SIZE//3), window = chr4)
        chr4.bind("<Button-1>", lambda event: click_sound.play()) # Button clicking sound

        self.image1 = tk.PhotoImage(file = "bg/characters.png")
        self.label1 = tk.Label(self.canvas, image = self.image1) # Sets the characters image over the background
        self.label1.place(relx = 0.5, rely = 0.37, anchor = tk.CENTER)
    
    def next_page2(self):
        '''Calls the function in the main class to switch pages'''
        self.master.show_setting_page()


##################################################################
##################################################################


class SettingPage(tk.Frame):
    """The scripts page, which shows the choices of script and contains the function to read them"""
    def __init__(self, master = None):
        '''Initializing the Setting Page'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        '''Creating the buttons and background image'''
        SIZE = 1000
        self.canvas = tk.Canvas(self, width = SIZE, height = SIZE) # Sets the background size
        self.canvas.grid()
        self.background_image = tk.PhotoImage(file = "bg/home.png") 
        self.canvas.create_image(0, 0, anchor = "nw", image = self.background_image)
        label = tk.Label(self, text = "Select An Adventure", font = ("Impact", 60), bg = "white", fg = "black", relief = tk.RAISED, bd = 5, padx = 10, pady = 10)
        label.place(relx = 0.23, rely = 0.05)

        # Creates the button for script1, Spacecapade
        set1 = tk.Button(self.canvas, text = 'Spacecapade', command = lambda: (RippleEffect.legalscript('scripts/script1.txt', 'scripts/edge_rep1.txt'), self.next_page3()), font = ("Impact", 30), width = 12) # Defines a button that when presses, checks if the script is legal during construction and goes to the next page PlayPage
        self.canvas.create_window(SIZE//2, (300), window = set1)
        set1.bind("<Button-1>", lambda event: click_sound.play())

        # Creates the button for script 2, Forestrealm
        set2 = tk.Button(self.canvas, text = 'Forestrealm', command = lambda: (RippleEffect.legalscript('scripts/script2.txt', 'scripts/edge_rep2.txt'), self.next_page3()), font = ("Impact", 30), width = 12)
        self.canvas.create_window(SIZE//2, (400), window = set2)
        set2.bind("<Button-1>", lambda event: click_sound.play())

        # Creates the button for script 3, Home Alone
        set3 = tk.Button(self.canvas, text = 'Home Alone', command = lambda:(RippleEffect.legalscript('scripts/script3.txt', 'scripts/edge_rep3.txt'), self.next_page3()), font = ("Impact", 30), width = 12)
        self.canvas.create_window(SIZE//2, (500), window = set3)
        set3.bind("<Button-1>", lambda event: click_sound.play())

        # Creates the button for the user to input their own script
        set4 = tk.Button(self.canvas, text = 'Enter Your Own', command = self.user_input, font = ("Impact", 30), width = 12) # Defining a button that allows the user to input their own files to be used
        self.canvas.create_window(SIZE//2, (600), window = set4)
        set4.bind("<Button-1>", lambda event: click_sound.play())

    def next_page3(self):
        '''Calls the function in the main class to switch pages
        Updates the question and answers to begin at question 1
        Calls for the start game sound to begin'''
        self.master.next_page3.update_options() # This was added and the lambda orders were reversed. Updates the question and answers to the first page information
        self.master.show_play_page()
        self.master.next_page3.playsound()
    
    def user_input(self):
        '''Allows users to input their own files to be used as the script
        Calls for the next page'''
        user_input1 = tk.simpledialog.askstring("Input", "Enter the script file:")
        user_input2 = tk.simpledialog.askstring("Input", "Enter the edge file:")
        if user_input1 == "vinnie" and user_input2 == "vinnie":
            self.master.show_special_page()
        else:
            RippleEffect.legalscript("scripts/"+user_input1, "scripts/"+user_input2) # Adding scripts/ due to the scripts being in the scripts folder
            self.next_page3()

        
##################################################################
##################################################################


class PlayPage(tk.Frame):
    '''The main playing page'''
    def __init__(self, master = None):
        '''Initializing the Play Page'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.seconds = 3 # Defines the starting number for the countdown
        self.createWidgets()    
      
    def createWidgets(self):
        '''Creating the buttons and background image'''
        SIZE = 1000
        self.canvas = tk.Canvas(self, width = SIZE, height = SIZE) # Creates the background
        self.canvas.grid()
        self.background_image = tk.PhotoImage(file = "bg/playbk.png") 
        self.canvas.create_image(0, 0, anchor = "nw", image = self.background_image)

        # Createss the left button
        self.option1 = tk.Button(self.canvas, font = ("Arial", 20), command = self.left_button_click, width = 10, height = 3, anchor = "center", wraplength = 150) # Associates the left button to the command self.left_button_click()
        self.option1.pack_propagate(0) # Allows the button to remain at a fixed size
        self.option1_id =  self.canvas.create_window(400, (SIZE-SIZE//3), window = self.option1)
        self.canvas.itemconfig(self.option1_id, state = "hidden")
        self.option1.bind("<Button-1>", lambda event: click_sound.play())

        # Creates the right button
        self.option2 = tk.Button(self.canvas, font = ("Arial", 20), command = self.right_button_click, width = 10, height = 3, anchor = "center", wraplength = 150) # Associates the right button to the command self.right_button_click()
        self.option2_id = self.canvas.create_window(600, (SIZE-SIZE//3), window = self.option2)
        self.canvas.itemconfig(self.option2_id, state = "hidden")
        self.option2.bind("<Button-1>", lambda event: click_sound.play())

        # Creates the question box
        self.message_label = tk.Label(self, font = ("Arial", 17, "bold"), fg = "white", bg = "#073763", anchor = "center", width = 33, wraplength = 280)
        self.message_label.place(relx = 0.33, rely = 0.16)
        self.message_label.config(state = "disabled")

    def countdown(self):
        '''Countdown to the start of the game'''
        if self.seconds >=  0:  # Delete any existing timer text on the canvas
            self.canvas.delete("timer")
            if self.seconds > 0:
                self.canvas.create_text(500, 500, text = str(self.seconds), font = ("Helvetica", 100), fill = "white", tag = "timer") # Create text showing the remaining seconds
                self.seconds -=  1  # Decrement seconds
                self.master.after(2000, self.countdown) # Schedule the countdown to continue after 2 seconds
            else:
                # Enable game options and display "START GAME!" message
                self.canvas.itemconfig(self.option1_id, state = "normal")
                self.canvas.itemconfig(self.option2_id, state = "normal")
                self.message_label.config(state = "normal")
                self.canvas.create_text(500, 500, text = "START GAME!", font = ("Helvetica", 50), fill = "white", tag = "start_game")
                self.master.after(1000, self.remove_timer) # Schedule the removal of the timer after 1 second

    def remove_timer(self):
        '''Deletes the start game and timer'''
        self.canvas.delete("start_game")
    
    def playsound(self):
        '''Defines the Start Game sound'''
        mixer.music.load("sounds/countdown.mp3")
        mixer.music.set_volume(0.8)
        mixer.music.play()
        self.canvas.after(7000, backnoise) # Time delay set to 7 seconds
   
    def update_options(self):
        '''Binds the next answers and questions from the UI to the buttons and labels'''
        if RippleEffect.answer1 !=  "None": # Makes sure the answer is not an ending answer
            self.option1.config(text = RippleEffect.answer1) # Binding the next answers to the buttons
        else:
            self.option1.config(text = "Play Again", command = self.backhome) # Binding the button to restart the game
            mixer.music.load("sounds/Gameover.mp3") #playing the game over sound
            mixer.music.set_volume(0.8)
            mixer.music.play()
        if RippleEffect.answer2 !=  "None": # Makes sure the answer is not an ending answer
            self.option2.config(text = RippleEffect.answer2) # Binding the next answers to the buttons
        else:
            self.option2.config(text = "Exit Game", command = self.quit)
            mixer.music.load("sounds/Gameover.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        
        self.message_label.config(text = RippleEffect.question) # Binding the message text to the next question

    def left_button_click(self):
        '''Notifies the UI of the left button clicked and calls to update the q&a's'''
        RippleEffect.left_button_click()
        self.update_options() 

    def right_button_click(self):
        '''Notifies the UI of the right button clicked and calls to update the q&a's'''
        RippleEffect.right_button_click()
        self.update_options()
    
    def backhome(self):
        '''Restarts the game'''
        python = sys.executable
        os.execl(python, python, * sys.argv)


##################################################################
##################################################################


class SpecialPage(tk.Frame):
    '''The just for fun page'''
    def __init__(self, master = None):
        '''Initializing the Special Page'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.createWidgets()
        self.grid()
    
    def createWidgets(self):
        '''Setting the background picture and message'''
        SIZE=1000
        self.canvas = tk.Canvas(self, width = SIZE, height = SIZE, bg="black") # Sets the background size
        self.canvas.grid()
        self.background_image = tk.PhotoImage(file = "bg/special.png") # Opens the background image file
        self.label1 = tk.Label(self.canvas, image = self.background_image) # Sets the characters image over the background
        self.label1.place(relx = 0.5, rely = 0.37, anchor = tk.CENTER)


##################################################################
##################################################################


class Main(tk.Tk):
    def __init__(self):
        '''Initializing the Main Page'''
        tk.Tk.__init__(self)
        self.title('Ripple Effect') # Creates the title on the window
        self.home_page = HomePage(self)
        self.next_page = GamePage(self)
        self.next_page2 = SettingPage(self)
        self.next_page3 = PlayPage(self)
        self.specialpage = SpecialPage(self)
        self.bind('q', self.quit) # Binds the letter q to the quit function
        self.bind('r', self.restart) # Binds the letter r to the restart function
    
    def show_game_page(self):
        '''Switches from home page to the game page'''
        self.home_page.grid_forget() # Forgets the layout of the home page
        self.next_page.grid() # Sets the grid of the next page

    def show_setting_page(self):
        '''Switches from game page to settings page'''
        self.next_page.grid_forget() # Forgets the layout of the home page
        self.next_page2.grid() # Sets the grid of the next page
    
    def show_play_page(self):
        '''Switches from settings page to play page'''
        self.next_page2.grid_forget() # Forgets the layout of the home page
        self.next_page3.grid() # Sets the grid of the next page
        self.next_page3.countdown() # Initiates the countdwn on the page
    
    def show_home_page(self):
        '''Switches from play page to home page'''
        self.next_page3.grid_forget() # Forgets the layout of the home page
        self.home_page.grid() # Sets the grid of the next page
    
    def show_special_page(self):
        '''Switches from settings page to special page and plays music'''
        self.next_page3.grid_forget() # Forgets the previous layout 
        self.next_page2.grid_forget() # Forgets the previous layout 
        self.specialpage.grid()
        mixer.music.load("sounds/NGGYU.mp3") # Plays a new sound
        mixer.music.set_volume(0.8)
        mixer.music.play()

    # The following functions have not been told to the user, they are kept as sort of a "developer tools" type of function
    def quit(self, event): # Although the event variable is not used, it is needed for the function to work and bind properly
        '''Fast quit function for keyboard q'''
        sys.exit()

    def restart(self, event): # Although the event variable is not used, it is needed for the function to work and bind properly
       '''Restarts the game'''
       python = sys.executable
       os.execl(python, python, * sys.argv)

if __name__  ==  "__main__":
    app = Main()
    app.mainloop()
