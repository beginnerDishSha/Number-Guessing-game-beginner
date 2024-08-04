import random

def user_start_work():
    print("WELCOME TO NUMBER GUESSING GAME")
    print("Press Y to start \nPress N to Exit")


    while True:
        user_start_input = input("Enter your Response: ")

        if user_start_input in ["Y","y"]:
            print("Perfect Let's Start the GAME")
            pass
        elif user_start_input in ["N","n"]:
            print("You have exited the game")
            return False
        else:
            print("Please provide a valid response Y or N")
            continue


        break

def game(name):

    print(f"Welcome {name} I hope you will enjoy the game")

    print("Please select your range for this game")

    while True:

        first = input("Enter starting number: ")
        last = input("Enter last number: ")


        if not first.isdigit() or not last.isdigit():
            print("Please enter integers")
            continue

        elif int(first) < 0 or int(last) < 0:
            print("Negatives are not allowed")
            continue

        else:
            first, last = int(first), int(last)
            comp_num = random.randrange(first, last)

        break

    print("You can exit by typing 'Exit' in game")

    user_attempt = []

    while True:

        user_input = input("Please enter your guess: ")

        if user_input in ["EXIT","exit","Exit"]:
            print("Thanks for playing game")
            break
        elif not user_input.isdigit():
            print("Please enter a valid integer")
            continue

        user_input = int(user_input)

        if user_input == comp_num:
            user_attempt.append(user_input)
            print(f"Your Guess is correct ans is {comp_num} ")
            break
        else:
            if user_input in range(comp_num - 3, comp_num+ 3):
                user_attempt.append(user_input)
                print("You are very close")
            elif user_input not in range(comp_num - 3, comp_num  + 3):
                user_attempt.append(user_input)
                print("You are Far from answer")

    return f"Number of attempts taken is: {len(user_attempt)}"

def main_game():

    name = input("What is your name: ")

    if user_start_work() == False:
        quit()
    else:
        pass

    res = game(name)
    print(res)

main_game()
