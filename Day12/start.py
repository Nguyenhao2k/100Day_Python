from random import randint


def check_answer(guess, answer, turn):
    if guess > answer:
        print("It's high!!")
        return turn - 1
    elif guess < answer:
        print("It's low!!")
        return turn - 1
    else:
        print(f"You got the answer {answer}")

check_answer(int(input("Enter a number:")), randint(1, 10), 10)