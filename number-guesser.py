import random

class Guesser:
    def __init__(self, min_num=1, max_num=10, max_guesses=4, max_hints=3):
        self.min_num = min_num
        self.max_num = max_num
        self.number = random.randint(min_num, max_num)
        self.guesses_left = max_guesses
        self.hints_left = max_hints

    def get_factors(self):
        return [i for i in range(1, self.number + 1) if self.number % i == 0]

    def get_multiples(self):
        multiples = [self.number * i for i in range(2, 6)]
        return [m for m in multiples if m <= self.max_num]

    def give_hint(self):
        if self.hints_left <= 0:
            print("Sorry, you’ve used all your hints.")
            return
        
        hint_type = random.choice(["a", "b", "c"])  # factors/multiples, larger/smaller, parity

        if hint_type == "a":
            factors = self.get_factors()
            multiples = self.get_multiples()

            if factors and multiples:
                choice = random.choice(["factors", "multiples"])
            elif factors:
                choice = "factors"
            elif multiples:
                choice = "multiples"
            else:
                print("I can’t find any factors or multiples — that might tell you something!")
                return

            if choice == "factors":
                print(f" Hint: One factor of the number is {random.choice(factors)}.")
            else:
                print(f" Hint: One multiple of the number is {random.choice(multiples)}.")

        elif hint_type == "b":
            # Larger or smaller number within range
            if self.number > self.min_num and self.number < self.max_num:
                choice = random.choice(["larger", "smaller"])
            elif self.number == self.min_num:
                choice = "larger"
            else:
                choice = "smaller"

            if choice == "larger":
                hint_num = random.randint(self.number + 1, self.max_num)
                print(f" Hint: The number is smaller than {hint_num}.")
            else:
                hint_num = random.randint(self.min_num, self.number - 1)
                print(f" Hint: The number is larger than {hint_num}.")

        elif hint_type == "c":
            parity = "even" if self.number % 2 == 0 else "odd"
            print(f" Hint: The number is {parity}.")

        self.hints_left -= 1
        print(f" You have {self.hints_left} hints and {self.guesses_left} guesses left.\n")

    def play(self):
        print(" Hi! I’m your Number Guesser Bot.")
        print(f"I’ve guessed a number between {self.min_num} and {self.max_num}. You have {self.guesses_left} guesses!")
        print("You can type 'hint' for a clue (up to 3 hints). Let’s play!\n")

        while self.guesses_left > 0:
            user_input = input("Your guess: ").lower()

            if user_input == "hint":
                self.give_hint()
                continue

            if not user_input.isdigit():
                print(" Invalid input! Please enter a number or type 'hint'.\n")
                continue

            guess = int(user_input)
            if guess < self.min_num or guess > self.max_num:
                print(f" Please guess within the range {self.min_num}-{self.max_num}.\n")
                continue

            if guess == self.number:
                print(f" Congratulations! You guessed it right — the number was {self.number}!")
                return
            else:
                self.guesses_left -= 1
                if self.guesses_left > 0:
                    print(f" Wrong guess. Try again!")
                    print(f"You have {self.guesses_left} guesses and {self.hints_left} hints left.\n")
                else:
                    print(f" Out of guesses! The number was {self.number}. Better luck next time!")


# Create an object and play the game
if __name__ == "__main__":
    game = Guesser()
    game.play()
