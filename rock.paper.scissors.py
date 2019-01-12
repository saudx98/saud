import random
def rps():
    computer_choice = random.randint["rock, paper, scissors"]
    if computer_choice == ("rock"):
        computer_choice_rock()
    elif computer_choice == ("paper"):
        computer_choice_paper()
    else:
        computer_choice_scissors()
def computer_choice_rock():
    user_choice = input [" rock, paper, scissors:"]
    if user_choice =="rock":
        print"Tie"
    if user_choice =="paper":
        print" You won"
    if user_choice =="scissors":
        print"You won"
    else:
        print"oh oh try again"
def computer_choice_paper():
    user_choice = input [" rock, paper, scissors:"]
    if user_choice =="rock":
        print"You won"
    if user_choice =="paper":
        print"Tie"
    if user_choice =="scissors":
        print"You won"
    else:
        print"oh oh try again"
def computer_choice_scissors():
    user_choice = input (" rock, paper, scissors:")
    if user_choice =="rock":
        print"You won"
    if user_choice =="paper":
        print"You won"
    if user_choice =="scissors":
        print"Tie"
    else:
        print"oh oh try again"
