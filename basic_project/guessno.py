import random
print("Let's play the 'Guess The Number'game ")
num =random.randint(1,100)
guess =0
while num != guess :
   guess = int(input(print("make your guess between 1 to 100:")))
   if guess >101 or guess <1 :
    print("input is outside the range , try in range ")
   elif guess < num :
    print(" guess higher ")
   elif guess > num :
    print("guess lower")
   elif guess == num :
    print(f"well done ! number was {num}")
   
