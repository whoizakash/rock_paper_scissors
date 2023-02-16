
# █░░ █ █▄▄ █▀█ ▄▀█ █▀█ █▄█
# █▄▄ █ █▄█ █▀▄ █▀█ █▀▄ ░█░

from random import randint





print('********************************')
print("...Rock.......")
print("...Paper......")
print("...Scissors...")
print('********************************')





# █▀ █▀▀ █▀█ █▀█ █▀▀
# ▄█ █▄▄ █▄█ █▀▄ ██▄

player_w = 0
computer_w = 0
winning_score = 3

while player_w < winning_score and computer_w <winning_score:
    
    print(f'Player score:{player_w} Computer score:{computer_w}')

    # User Input
    player = input('Enter your choice: ').lower()

    if player == 'quit' or player=='q':
        break

    # Choice
    random_number = randint(0,2)

    if random_number == 0:
        computer = 'rock'
    elif random_number == 1:
        computer = 'paper'
    elif random_number == 2:
        computer = 'scissors'

    print(f"The computer plays: {computer}")

    # Logic
    if player == computer:
        print("Its a tie!")
    # 1
    elif player =='rock':
        if computer =='paper':
            print('Computer wins!')
            computer_w +=1
        else:
            print("Player wins!")
            player_w +=1
    # 2
    elif player =='paper':
        if computer =='rock':
            print('Player wins!')
            player_w +=1
        else:
            print("Computer wins!")
            computer_w +=1
    # 3
    elif player =='scissors':
        if computer =='rock':
            print('Computer wins!')
            computer_w +=1
        else:
            print("Player wins!")
            player_w +=1

    else:
        print('Invalid move!')

if player_w > computer_w:
    print('Wow congrats! you win.')

elif player_w == computer_w:
    print('Its a tie.')

else:
    print('Oh bad luck!, The Computer wins :(')

print('********************************')
print('Final Score')
print(f'Player score:{player_w} Computer score:{computer_w}')
print('********************************')


