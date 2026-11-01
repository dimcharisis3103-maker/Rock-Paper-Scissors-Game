#rock paper scisors
import random
choices = ['rock', 'paper', 'scissors']
c = 0 
h = 0
#colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'  # Resets to normal color
while c!=3 and h!=3:
    cc = random.choice(choices)
    x = str(input('Choose paper, rock or scissors '))
    if x == 'rock' and cc == 'rock':
        print(f'{YELLOW}Tie{RESET}')
    elif x == 'paper' and cc == 'paper':
        print(f'{YELLOW}Tie{RESET}')
    elif x == 'scissors' and cc == 'scissors':
        print(f'{YELLOW}Tie{RESET}')
    elif x == 'paper':
        if cc == 'scissors':
            print(f'{RED}Computer wins this round{RESET}')
            c +=1
        elif cc == 'rock':
            print(f'{GREEN}You win this round{RESET}')
            h +=1
    elif x == 'rock':
        if cc == 'paper':
            print(f'{RED}Computer wins this round{RESET}')
            c +=1
        elif cc == 'scissors':
            print(f'{GREEN}You win this round{RESET}')
            h +=1
    elif x == 'scissors':
        if cc == 'rock':
            print(f'{RED}Computer wins this round{RESET}')
            c +=1
        elif cc == 'paper':
            print(f'{GREEN}You win this round{RESET}')
            h +=1
    else:
        print('Not acceptable answer')
if c > h:
    print('Computer wins')
    print(f'{c}:{h}')
else:
    print('You win')
    print(f'{h}:{c}')