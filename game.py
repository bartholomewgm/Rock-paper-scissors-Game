import random

CHOICES = ["rock", "paper", "scissors"]
SCORE_FILE = "scores.json"


class ScoreBoard:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0

    def update(self, winner):
        if winner == "user":
            self.user_wins += 1
        elif winner == "computer":
            self.computer_wins += 1

    def display(self):
        print(
            f"Score — Player: {self.user_wins}, Computer: {self.computer_wins}"
        )

    def save(self):
        with open(SCORE_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"Player: {self.user_wins}, Computer: {self.computer_wins}\n"
            )


def computer_choice():
    return random.choice(CHOICES)


def user_choice():
    return input("Enter rock, paper, scissors or exit: ").lower()


def determine_winner(user, computer):
    if user == computer:
        return "draw"

    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }

    if (user, computer) in wins:
        return "user"
    return "computer"


def game_loop():
    scoreboard = ScoreBoard()

    print("Rock-Paper-Scissors Game")
    print("To exit, enter 'exit'")

    while True:
        user = user_choice()

        if user == "exit":
            print("The game is over.")
            scoreboard.save()
            break

        if user not in CHOICES:
            print("Incorrect input. Try again.")
            continue

        computer = computer_choice()
        print(f"The computer selected: {computer}")

        result = determine_winner(user, computer)

        if result == "draw":
            print("Draw!")
        elif result == "user":
            print("You've won!")
        else:
            print("The computer won!")

        scoreboard.update(result)
        scoreboard.display()


def main():
    game_loop()


if __name__ == "__main__":
    main()
