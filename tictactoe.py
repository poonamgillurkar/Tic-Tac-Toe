def print_board(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])
	

def select_symbol():
    symbol=''
    while symbol!='x' and symbol!='o':
        symbol=input('User pick symbol x or o:')
    if symbol=='x':
        return ('x','o')
    else:
        return ('o','x')
		

def insert_symbol(board,symbol,location):
    board[location]=symbol
	

def check_result(board,symbol):
    return ((board[0] == board[1]== board[2]==symbol) or
    (board[3] == board[4]== board[5]==symbol) or
    (board[6] == board[7]== board[8]==symbol) or
    (board[0] == board[3]== board[6]==symbol) or
    (board[1] == board[4]== board[7]==symbol) or
    (board[2] == board[5]== board[8]==symbol) or
    (board[0] == board[4]== board[8]==symbol) or
    (board[2] == board[4]== board[6]==symbol))
	
	
def loc_available(board, location):
    return board[location]==' '
	
	
def no_space(board):
    for i in range(9):
        if loc_available(board,i):
            return False
    return True
	
	
def user_location(board):
    location=-1
    while location not in [0,1,2,3,4,5,6,7,8] or not loc_available(board,location):
        location=int(input("Enter the location to place symbol :"))
    return location
	
	
def restart():
    pick=input("Start again? y/n :")
    return pick=='y'
	
	
import random
def comp_location(board):
    location=-1
    while location not in [0,1,2,3,4,5,6,7,8] or not loc_available(board,location):
        location=random.randint(0,8)
    return location
	
	
while True:
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    user_symbol, comp_symbol = select_symbol()
    print("User always starts first.")
    chance="User"
    
    while True:
        print_board(board)
        if chance=="User":
            location=user_location(board)
            insert_symbol(board,user_symbol,location)

            if check_result(board,user_symbol):
                print_board(board)
                print("User wins!!")
                break
                
            else:
                if no_space(board):
                    print_board(board)
                    print("Game tied!!")
                    break

                else:
                    chance="Computer"
                    
        else:
            location=comp_location(board)
            insert_symbol(board,comp_symbol,location)

            if check_result(board,comp_symbol):
                print_board(board)
                print("Computer wins!!")
                break
                
            else:
                if no_space(board):
                    print_board(board)
                    print("Game tied!!")
                    break

                else:
                    chance="User"
                
    if not restart():
        break
