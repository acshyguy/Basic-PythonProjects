import random

user_win = 0
computer_win = 0

while True:
    print("0 represent rock")
    print("1 represent paper")
    print("2 represent scissors")
    print("-1 represent exit")

    user_choice = int(input("Select among the numbers above: "))
    computer_choice = random.randint(0, 2)

    if user_choice == -1:
        break

    if 0 < user_choice > 2:
        print("Wrong input! Enter the correct input.")

    if user_choice == 1 and computer_choice == 0:
        print("You won!")
        user_win += 1

    elif user_choice == 2 and computer_choice == 1:
        print("You won!")
        user_win += 1

    elif user_choice == 0 and computer_choice == 2:
        print("You won!")
        user_win += 1

    elif user_choice == computer_choice:
        print("It is a draw.")

    else:
        print("Oops.. Computer won!")
        computer_win += 1

    print()

print("You won", user_win, "time(s).")
print("Computer won", computer_win, "time(s).")
print()
if user_win > computer_win:
    print("Congratulations! You're a genus.")
if computer_win > user_win:
    print("Computer won!")
if computer_win == user_win:
    print("None win!")
