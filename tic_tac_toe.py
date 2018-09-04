row_0 = [" ", " ", " "]
row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
board = [row_0, row_1, row_2]

def print_board():
    for row in board:
        print (row)

def ask_player():
    x = int(input("Please choose x coordinate (0-2). "))
    y = int(input("Please choose y coordinate (0-2). "))
    return x, y

def check_bugs(x,y):
    func = True
    coordinates = [0,1,2]
    
    while func:
        if x not in coordinates:
            print ("")
            print ("Wrong numbers!")
            x,y = ask_player()
            func = True
        elif y not in coordinates:
            print ("")
            print ("Wrong numbers!")
            x,y = ask_player()
            func = True
        elif x in coordinates and y in coordinates:
            if board[x][y] != " ":
                print ("This is not a free spot.")
                x,y = ask_player()
                func = True
            else:
                func = False
    return x, y
    
def print_to_board(x,y, player):
    for row_index in range(len(board)):
        for field in range(3):
            if row_index == x and field == y:
                board[row_index][field] = player
    return board

def check_if_wins(player):
    game = True 
    
    for row_index in range(len(board)):            
        if all (board[row_index][field] == player for field in range(3)):
            print ("{} is the winner.".format(player))
            game = False
            return game
           
    for field in range(3):
        if all (board[row_index][field] == player for row_index in range(len(board))):
            print ("{} is the winner.".format(player))
            game = False
            return game
            
    if row_0[0] == player and row_1[1] == player and row_2[2] == player:
        print ("Congrats! Player {} wins!".format(player))
        game = False
        return game
        
    elif row_0[2] == player and row_1[1] == player and row_2[0] == player:
        print ("Congrats! Player {} wins!".format(player))
        game = False
        return game
        
    elif (row_0[0] != " " and row_0[1] != " " and row_0[2] != " " 
    and row_1[0] != " " and row_1[1] != " " and row_1[2] != " " 
    and row_2[0] != " " and row_2[1] != " " and row_2[2] != " "):
        print ("Nobody wins.")
        game = False
        return game
        
def wanna_play_again():
    answer = input("Wanna play again? Y/N: ")
    print (answer)
    return answer
    
def zeroing_board():
    for row_index in range(len(board)):
        for field in range(3):
            board[row_index][field] = " "
    print (board)
    return board
    
def run_the_game():
    game = True
    while game: 
        
        #move1
        print ("")
        player = "X"
        print ("Player One: {}".format(player))
        print ("")
    
        x, y = ask_player()
        x, y = check_bugs(x,y)
        
        print_to_board(x,y, player)
        print ("")
        print_board()
        
        if check_if_wins(player) == False:
            answer = wanna_play_again().capitalize()
            if answer == "Y":
                board = zeroing_board()
                game = True
                run_the_game()
            elif answer == "N":
                board = print_board()
                print (board)
            
        #move2
        print ("")
        player = "O"
        print ("Player Two: {}".format(player))
        print ("")
        
        x, y = ask_player()
        x, y = check_bugs(x,y)
        
        print_to_board(x,y, player)
        print ("")
        print_board()
        
        if check_if_wins(player) == False:
            answer = wanna_play_again().capitalize()
            if answer == "Y":
                board = zeroing_board()
                game = True
                run_the_game()
            else:
                board = print_board()
                print (board)
run_the_game()