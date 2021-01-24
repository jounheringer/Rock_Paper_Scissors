from random import randint
from time import sleep

# Color
r = '\033[0;31m'
g = '\033[0;32m'
y = '\033[0;33m'
b = '\033[0;34m'
ce = '\033[m'

rounds = 0
tie = 0
win = 0
lose = 0
lim = 3

print(f'{g}-'*30)
print(f"Let's play rock paper scissors, best out of 3")
print(f'-'*30,ce)
sleep(1)

while True:
    while rounds < lim:
        com = randint(1, 3)

        print(f'{g}{rounds+1}º Round')

        print(f'Chosse between Rock(R), Paper(P) and Scissor(S): ')
        while True:
            try:
                opt = str(input(f'Which will you chosse?{ce} ')).upper()
            except:
                print(f'{r}Try to type the correct name{ce}')
            else:
                break
        sleep(0.5)

        if opt[0] == 'R':
            if com == 1:
                print(f'{y}Tie{ce}')
                tie += 1
            if com == 2:
                print(f'{r}You Lost{ce}')
                lose += 1
                rounds += 1
            if com == 3:
                print(f'{b}You won{ce}')
                win += 1
                rounds += 1
        elif opt[0] == 'P':
            if com == 1:
                print(f'{b}You won{ce}')
                win += 1
                rounds += 1
            if com == 2:
                print(f'{y}Tie{ce}')
                tie += 1
            if com == 3:
                print(f'{r}You Lost{ce}')
                lose += 1
                rounds += 1
        elif opt[0] == 'S':
            if com == 1:
                print(f'{r}You Lost{ce}')
                lose += 1
                rounds += 1
            if com == 2:
                print(f'{b}You won{ce}')
                win += 1
                rounds += 1
            if com == 3:
                print(f'{y}Tie{ce}')
                tie += 1
        else:
            print(f'{r}Try again{ce}')
        sleep(0.5)
        print('-'*30)
        
    if lose > win:
        print(f'{r}Looks like the computer won{ce}')
    if lose < win:
        print(f'{b}Looks like you won the game{ce}')
    
    while True:
        try:
            again = str(input(f'{g}Wanna try again? (Y/N){ce} ')).upper()
        except:
            print(f'{r}Try to answer in the right way{ce}')
        else:
            break
    if again == 'Y':
        rounds = 0
        print(f'{b}Nice, lets go again{ce}')
        print('...')
        sleep(1)
    if again == 'N':
        print(f'{r}Ok, see you next time{ce}')
        sleep(0.5)
        break

print(f'You won {win} times, lost {lose} times, and tied {tie} times')