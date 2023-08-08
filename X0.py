#!/usr/bin/env python
# coding: utf-8

# In[15]:


from IPython.display import clear_output
'''Board layout and positions'''
def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[16]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[17]:


def player_input():
    marker=''
    
    while not(marker=='X' or marker=='O'):
        marker=input('Player 1 you want to be X or O ?').upper()
                     
    if marker =='X':
        return ('X','O')
    else:
        return ('O','X')


# In[18]:


player_input()


# In[19]:


'''Placing the marker'''
def place_marker(board,marker,position):
    board[position]=marker


# In[20]:


place_marker(test_board,'%',6)
place_marker(test_board,'*',1)
display_board(test_board)


# In[21]:


# checking if someone won
def win_check(board,mark):
    
    return((board[7]==board[8]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[9]==board[5]==board[1]==mark))


# In[22]:


win_check(test_board,'X')


# In[23]:


import random

def choose_first():
    if random.randint(0, 1) ==0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[24]:


#Empty space checking
def space_check(board, position):
    
    return board[position] == ' '


# In[25]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[26]:


#Next position 
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[27]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




