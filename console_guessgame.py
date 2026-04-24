import random


# =========================
# STYLING FUNCTIONS
# =========================
def line():
    print("=" * 45)


def title():
    line()
    print("🎯  NUMBER GUESSING GAME")
    line()


def get_valid_guess(min_val, max_val):
    while True:
        try:
            guess = int(input(f"👉 Enter your guess ({min_val}-{max_val}): "))
            return guess
        except ValueError:
            print("❌ Invalid input! Please enter a number only.")


# =========================
# GAME ROUND
# =========================
def play_round(round_number):
    min_val = 1
    max_val = 100 + (round_number - 1) * 50
    secret_number = random.randint(min_val, max_val)

    attempts = 7
    used = 0

    print("\n")
    title()
    print(f"📌 Round: {round_number}")
    print(f"🎯 Guess a number between {min_val} and {max_val}")
    print("⏳ You have 7 attempts!")
    line()

    while attempts > 0:
        guess = get_valid_guess(min_val, max_val)

        used += 1
        attempts -= 1

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print("\n🎉 Congratulations!")
            print(f"✔ You found it in {used} attempts")
            line()
            return True

        print(f"⏳ Attempts left: {attempts}")
        line()

    print("\n❌ GAME OVER")
    print(f"🔢 The correct number was: {secret_number}")
    line()
    return False


# =========================
# MAIN GAME LOOP
# =========================
def main():
    round_number = 1

    print("✨ Welcome to the Guessing Game ✨")

    while True:
        play_round(round_number)

        choice = input("\n🔁 Do you want to continue? (y/n): ").lower()

        if choice == "y":
            round_number += 1
            print("\n🔥 Next round gets harder!")
        else:
            print("\n👋 Thanks for playing!")
            break


# RUN PROGRAM
if __name__ == "__main__":
    main()