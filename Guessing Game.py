#gassing game
from random import randint
while True:
 gassing_number=int(input("enter your gassing number: "))
 random_number=randint(1,5)
 if gassing_number==random_number:
    print("you won")
 else:
    print("you lost")
 print(random_number)
