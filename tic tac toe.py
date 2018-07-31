
# coding: utf-8

# In[18]:


from IPython.display import clear_output
def display_board(board):
    
    clear_output
    print(' '+ board[7]+' | '+ board[8]+' | '+board[9])
    print('-----------')
    print(' '+ board[4]+' | '+ board[5]+' | '+board[6])
    print('-----------')    
    print(' '+ board[1]+' | '+ board[2]+' | '+board[3])


# In[19]:


display_board([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])


# In[ ]:


def player_input():
    input()
    
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1:  Você quer ser o X ou O?').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:


def win_check(board, mark):
    return ((board[7] == mark and board [8] == mark and board[9] == mark) or #pelo topo
            (board[4] == mark and board [5] == mark and board[6] == mark) or #pelo meio
            (board[1] == mark and board [2] == mark and board[3] == mark) or #por baixo
            (board[7] == mark and board [4] == mark and board[1] == mark) or #pela esquerda
            (board[8] == mark and board [5] == mark and board[2] == mark) or #pelo meio
            (board[9] == mark and board [6] == mark and board[3] == mark) or #pela direira
            (board[7] == mark and board [5] == mark and board[3] == mark) or #diagonal
            (board[9] == mark and board [5] == mark and board[1] == mark))#diagonal


# In[ ]:


import random
def choose_first():
    if random.randInt(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    


# In[ ]:


def space_check(board, position):
    
    return board[position] == ' '


# In[ ]:


def full_board_check(board):
    for i in range(0, 10):
        if space_check(board, i):
            return False
    return True


# In[ ]:


def player_choice(board):
    position == ' '
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9) ')
        
    return int(position)


# In[ ]:


def replay():
    
    return input('Quer jogar novamente? "SIM" ou "NÃO"').lower().startswith('s')


# In[ ]:


print('Bem vindo ao jogo da velha!')

while True:
    #Defina o jogo
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+' começa!')
    
    game_on = True
    
    while game_on:
        #vez jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_market(board, player1_marker, position)
        
        #checa vitoria
        if win_check(board, player1_marker):
            display_board(board)
            print('Temos um vencedor!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 2'
        
        #vez jogador 2
        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board)
            place_market(board, player2_marker, position)
        
        #checa vitoria
        if win_check(board, player2_marker):
            display_board(board)
            print('Temos um vencedor!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 1'
            
    if not replay():
        break

