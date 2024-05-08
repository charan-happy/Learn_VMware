# title : Rockpaper Scissors Game using Python tkinter 

## About :
    > It is a game with three choices, rock ,paper and scissors. Two players can play this game. In our case, The user and the computer. Each one has to make one choice from the three.

    > if rock and scissor come, rock wins. if rock and paper come, paper wins. If paper and scissor come, scissor wins. If both the choices are the same, then no one will win. Both the user and the computer will not get a point.


## code explanation
> The code first creates an instance of the Tkinter root object.
> Next, it sets the geometry of the window to be 300×300 pixels.
> The title of the window is also set.
Finally, a list called computer_value is created and initialized with three values: Rock, Paper, and Scissors.
> Next, a function named reset_game() is defined.
> This function will be used to initialize all of the game elements (b1 through b3) at once.
> In this function, each game element’s state (Rock, Paper, or Scissors) is set to “active”.
> Finally, the function ends by calling another function named analyze which will display all of the game information in a dialog box.
> The code first imports the required library, Tkinter.
> After that, it creates an object named root and sets its geometry to be 300×300.
> Next, it sets the title of the game to Rock Paper Scissor Game.
Next, the code defines a variable called computer_value which will store three values: 0 for Rock, 1 for Paper and 2 for Scissors.
> The next line of code initializes the computer_value variable with these values.
The last line of code in this snippet is called reset_game().
> This line instructs the game to set all three states of the b1[], b2[], and b3[] variables to “active”.
> The code starts by creating three variables: b1, b2, and b3.
> The first two (b1 and b2) are boolean variables that will store information about the state of the buttons.
> The third variable (b3) is a text variable that will store the name of the button.
> The next line of code sets up a simple if statement to check whether the player has selected rock or not.
> If the player has selected rock, then computer_value[str(random.randint(0,2))] will be “Rock”.
> This value is stored in c_v and it will be used later in the code to determine what action to take.
Next, an Analyze() function is created.
> This function takes one parameter: str(random.randint(0,2)).
> This parameter tells the Analyze() function which number to use as input for randomizing between 0 and 2 (inclusive).
So if you wanted to randomly choose between 1 and 3 instead of 0 and 2, you would replace “random.randint” with “random.”
in this line of code.
> The next line of code calls the Analyze() function with str(random.randint(0,
> The code firstly defines three variables – b1, b2 and b3.
> These variables will each hold a boolean value, which will indicate the state of the button – i.e.
whether it is enabled or disabled.
> Next, the code checks to see if the player has selected rock as their choice for the game.
> If they have, then the code sets the variable c_v to “Rock”, and proceeds to execute various other code blocks depending on this value.
> If c_v is not “Rock”, then the code block checks to see if computer_value[str(random.randint(0,2))] is equal to “Rock”.
> If it is, then this means that the computer has
The code starts by creating two labels, l1 and l4.
> The first label, l1, will display the computer’s value in the text box.
The second label, l4, will display the player’s value in the text box.
> Next, the code creates three buttons: button_disable(), button_enable(), and ispaper().
The button_disable() function disable the button.
> The button_enable() function enables the button.
Finally, ispaper() determines whether or not the player selected paper (by checking to see if c_v equals “Paper”).
> If it does, then match_result will be set to “Match Draw.”
Otherwise, match_result will be set to “Computer Win.”
> Now let’s look at each part of this code in more detail.
The first line of code creates a variable called c_v.
> This variable stores information about which type of rock-paper-scissors game has been started (computer vs. player).
> The next line of code sets c_v to equal computer_value[str(random.randint(0, 2))].
> This line uses a random number generator to create a new string that stores the computer’s
> The code will display different messages depending on the value of the c_v variable.
> If c_v is equal to “Rock”, then the code will print out “Computer Win”.
> If c_v is equal to “Scissor”, then the code will print out “Match Draw”.
Finally, if c_v is any other value, then the code will print out “Player Win”.
> To disable the buttons, you can use the following code: button_disable() method. 