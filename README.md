Ripple Effect README

Names - Student Number:
Dimitri Perron - 2230233
Romy Nissan - 2230908
Ryan El-Khoury - 2230344
Zayden Kung'u - 2232072

Overview
Ripple Effect is an interactive computer game designed to give users a captivating adventure experience that is inspired off the mobile game, "Lifeline". Using various intricate data structures, the game offers a user-friendly interface and extensive customization options. Developed in Python, it leverages directed graphs, nested dictionaries, and classes to process structured text files seamlessly, enabling users to immerse themselves in fully customizable narratives with consequences tied to their in-game decisions.

Features
Interactive Gameplay: Users navigate through a directed graph, presented with choices that dictate the progression of their adventure.

Customizable Storylines: The game allows for extensive customization, offering different storylines and replayability.

Graphical User Interface (GUI): A visually appealing and intuitive interface enhances the user experience, making navigation effortless.

Immersive Sound Effects: Sound elements contribute to the immersive atmosphere, enhancing the overall gaming experience.


Installation and to Play
Ensure Python is installed on your system.
If there are any module errors, go to the terminal and type: pip3 install MODULENAME
If there are any module errors and you are using HomeBrew use: brew install MODULENAME
To play, run the main game file, ui.py, using the Python interpreter.

Select one of the preloaded stories or submit your own.

*IF PLAYING PRELOADED STORY***
	1. Follow the on-screen instructions to play the game. There are numerous endings, so each story may be replayed with a different outcome.

***IF PLAYING OWN STORY***
	1. Submit the text file name of your script and edge file. Please put the files in the scripts folder
	Scripts must be formatted in the following way:
		- There can be no space between Question: and the actual question
		- There can be no space between Answer1:/Answer2: and their respective answers
		- If you wish to enter comments or text not related to the story, please start the line/text with a "#"

	*Question Number*
	Question:*enter desired prompt*
	Answer1:*enter desired answer1*
	Answer2:*enter desired answer2*
	*repeat format for next question*

	Script File Example:
	1
	Question:You are on a path, and you have the choice of going left or right. Where do you go?
	Answer1:Left
	Answer2:Right
	2
	Question:You go left, and see a dragon sleeping on the ground. You have a choice of running away to the forest up ahead or fighting it with a sword on the ground near it. What do you do?
	Answer1:Run to the forest
	Answer2:Pick up the sword and fight

	2.Submit the text file of links(edges) between questions
	Edge files must be formatted in the following way:
	*page number* *next page number*

	Edge Representation Example:
	1 2
	1 3
	2 4
	2 5
	3 6
	3 7 

Usage
Launch the game python program. Follow on-screen prompts to make choices that shape the narrative.
Experience the consequences of your decisions as the story unfolds. Enjoy the immersive gameplay enhanced by sound effects and a user-friendly interface.

Keywords
Data structures, user-friendly, user interface, Python, computer game, interactive fiction
