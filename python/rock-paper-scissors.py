import random


while True:
    p1 = input('rock, paper, scissors?\n').lower()
    if (p1 == 'rock'):
        p1 = 1
        break
    elif (p1 == 'paper'):
        p1 = 2
        break
    elif (p1 == 'scissors'):
        p1 = 3
        break
    else:
        print('\nplease input a valid choice')


p2 = random.randrange(0, 4)
win = 0


if (p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2):
    win = 1
elif (p1 == p2):
    win = 2


print('')
if win == 1:
    print('You win!')
elif win == 0:
    print('You lost!')
else:
    print('Tie!')
print('')