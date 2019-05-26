import random
import time
def displayintro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
print()

def choosecave():
    cave = ''
    while cave != '1' and cave != '2':
       print('Which cave will you go into? (1 or 2)')
       cave = input()
       return cave

def checkcave (chosencave):
    print('You approach the cave...')
    time.sleep(2)
    print ('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you!')
    print()
    time.sleep(2)

    friendlycave = random.randint(1,2)

    if chosencave == str(friendlycave):
           print('Gives you his treasure!')
    else:
              print('Gobbles you down in one bite!')

playagain = 'yes'
while playagain == 'yes' or playagain == 'y':
          displayintro()
          cavenumber = choosecave()
          checkcave (cavenumber)

          print ('Do you want to play again ? (yes or no) ' )
          playagain = input()
          
