import random
print("ROCK PAPER SCISSORS GAME")
print("type 'quit' to exit")

choces=("rock","paper","scissors")

user_score=0
computer_score=0
tie_score=0

while True :
    user_choice=input("Enter a choice (rock,paper,scissors):")
    computer_choice=random.choice(choces)
    print("computer_choice:",computer_choice)

    if user_choice == "quit":
      print("Final score = you:",user_score,"|computer:",computer_score,"|tie:",tie_score)
      break

    if user_choice not in choces:
      print("invalid")
      continue

    if user_choice==computer_choice:
      print("tie")
      tie_score+=1

    elif(user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
         print("you win")
         user_score+=1



    else:
      print("you lose")
      computer_score+=1

      print("user score:",user_score)
      print("computer score:",computer_score)
      print("tie score:",tie_score)


    if user_score > computer_score:
            print("user wins")
    elif computer_score > user_score:
            print("computer wins")
    else:
            print("tie")