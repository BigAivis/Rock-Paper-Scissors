import random

bot = random.randint(1,3)
user = input("Choose your weapon: ")
user = user.capitalize()

if bot == 1:
    bot = "Rock"
elif bot == 2:
    bot = "Paper"
elif bot == 3:
    bot = "Scissors"
print(f"Bot choose his weapon: {bot}")

if user == "Scissors" or user == "Rock" or user == "Paper":
  
  if bot == user:
    print("It is a tie!")

  elif (bot == "Scissors" and user == "Paper") or (bot == "Paper" and user == "Rock") or (bot == "Rock" and user == "Scissors"):
    print("YOU LOST my G")

  else:
    print("YOU WIN! You stroong, I got to get better")

else:
    print("It's rock paper n scissors dumbass!")
