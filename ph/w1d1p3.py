
player1=input('Enter rock, paper or scissor:')
player2=input('Enter rock, paper or scissor:')

if player1=='rock' and player2 =='scissor':
    print('Player 1 is winner')
elif player1=='paper' and player2=='rock':
    print('Player 1 is winner')
elif player1 =='scissor' and player2 =='paper':
    print('Player 1 is winner')
else:
    print('Player 2 is winner')
