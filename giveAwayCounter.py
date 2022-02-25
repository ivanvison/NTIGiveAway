import random, time
from giveAwayArrays import *

#Contadorsito
t = 10
for count in range(t):
    print(t," ",random.choice(coolMsgs))
    time.sleep(1)
    t-= 1

#Random Name
randomCoolName = random.choice(coolNames)

#The system is rigged
#while randomCoolName != 'Evan':
#    print('NOT A Winner :( -',randomCoolName)
#    randomCoolName = random.choice(coolNames)
#    time.sleep(1)


print("Winner!!! -",randomCoolName)
print("Gracias a Gomez Diaz, a Cerveceria Nacional, Acroarte, al pueblo dominicano!")
if(randomCoolName == 'Sugeiri'):
    print('ALLAAA!!! LO WAWAWAAAAAAA!!!!!!!!')

