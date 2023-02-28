import random
import os.path
import json
random.seed()

def draw_board(board):
    print('-----------')
    print('|' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + '|') #Prints Row 1
    print('-----------')
    print('|' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + '|') #Prints Row 2
    print('-----------')
    print('|' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + '|') #Prints Row 3
    print('-----------')

def welcome(board):
    print("Welcome to a simple tic tac toe game in python \n The board layout is shown below:")

    # Calling the draw_board() function to draw the board in the output.
    draw_board(board)

    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    # Sets the value of all rows and columns to ' '.
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

def get_player_move(board):
    while True:
        # Stores the desired square where the player wants to put their cross.
        player_move = input(" 1 2 3 \n 4 5 6 \n 7 8 9 \n choose your square:")

        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_move = int(player_move) - 1

            # Checking if the square is empty or not.
            if board[int(player_move / 3)][player_move % 3] == ' ':
                return int(player_move / 3), player_move % 3
            else:
                print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def choose_computer_move(board):
    # A simple code for deciding a move of computer.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return i, j


def check_for_win(board, mark):
    # Checks if the game is won or lost depending on the arrangements of the noughts and crosses.
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
            (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
            (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
            (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False

def check_for_draw(board):
    # Checks every space and returns True if every space is occupied.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game(board):
    """Resets all the values of the board to ' ' by calling the initialise_board() function
    while passing the board argument."""
    initialise_board(board)

    while True:
        """Gets the move from the player and stores it in player_move variable.
            by using get_player_move() function with board argument."""
        player_move = get_player_move(board)

        if player_move != None:
            # Puts the X in the desired square.
            board[player_move[0]][player_move[1]] = "X"
            draw_board(board)

            # Checks if the player has won the game after their move.
            if check_for_win(board, "X"):
                return 1

            # Check if the game is draw
            elif check_for_draw(board):
                return 0

            """Stores the move of the computer in computer_move variable
             by using function choose_computer_move() with board argument"""
            computer_move = choose_computer_move(board)

            #Sets 0 to the square choosen by the computer.
            board[computer_move[0]][computer_move[1]] = "O"
            print("Computer made a choice")

            # Displays the board after computer move, to the player.
            draw_board(board)

            # Checks if the player loss after the computer's move.
            if check_for_win(board, "O"):
                return -1

            # Checks if the game is draw, after the computer's move.
            elif check_for_draw(board):
                return 0

            else:
                """ If the game is not won, lost, or drawed, the loop continues, 
                    prompting the user for their next move."""
                continue


def menu():
        choice = input("1. Play game\n2. Save score\n3. Leaderboard \nq. Quit\nEnter your choice: ")

        """checking if the choice is a valid character i.e. (1, 2, 3, q)
         if the choice is a valid character it is returned."""
        if choice in ['1', '2', '3', 'q']:
            return choice

        else:
            """if choice is not a valid character the loop runs continuously, 
            prompting the user for the right input."""
            print("Invalid input! Please enter a valid choice.")

def load_scores():
    #Loads the leaderboard and returns it in the form of key value pairs.
    try:
        # Opening the file in read mode.
        with open("leaderboard.txt", "r") as file:
            """using json.load() object to return the data within the leaderboard.txt in 
                the form of key value pairs."""
            leaderboard = json.load(file)
    except:
        # If the leaderboard file does not exist then creates a new one.
        leaderboard = {}

    return leaderboard

def save_score(score):

    # Asking the name of the player
    player_name = input("Enter your name: ")

    try:
        with open("leaderboard.txt", "r") as file:
            """Using json.load() object to return the data within the leaderboard.txt in 
            the form of key value pairs."""
            data = json.load(file)
    except:
        data = {}
        # Links the name and score of the player
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        #uses json.dump() object to write the text
        json.dump(data, file)



def display_leaderboard(leaders):

    print("Name: Score")

    #Prints the name and score of all saved players in leaderboard.txt.
    for name, score in leaders.items():
        print(f"{name}: {score}")


def main():
    # Establishing a 3x3 two dimension array for storing the noughts and crosses.
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    """Calling the welcome function to display the welcome message,
         and passing argument board to display the board layout."""
    welcome(board)

    # A variable to record the total wins and losses.
    total_score = 0

    # Using infinite while loop to continuously run the program until the user presses q.
    while True:
        # Calling menu() function and storing its returned value in variable choice.
        choice = menu()

        # Case 1: When the user inputs 1 to Play the game.
        if choice == '1':
            #Calls the play_game() function and passing argument board
            score = play_game(board)

            """Increases or decreases the value total_score 
             depending on if the player won or lost the game"""
            total_score += score
            print('Your current score is:', total_score)

        # Case 2: If the user decides to Save their score.
        if choice == '2':
            # save_score() function is called.
            save_score(total_score)

        # Case 3: If the user decides to check the leaderboards.
        if choice == '3':
            # Calls load_scores() function and saves its returned value in leader_board variable
            leader_board = load_scores()

            """ Displays the leaderboard by calling the display_leaderboard() function 
             with argument leader_board """
            display_leaderboard(leader_board)

        # Case 4: If the user decides to quit the game.
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return

# Program execution begins here
if __name__ == '__main__':
    main()



