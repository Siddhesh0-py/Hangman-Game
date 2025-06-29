import random

words = ["apple", "tiger", "betroot", "water", "light"]
word = random.choice(words)
guessed_words = ["_"] * len(word)
chances = 6
guessed_letters = []

while chances > 0 and "_" in guessed_words:
    print("Word:", " ".join(guessed_words))
    print("Guessed letters:", guessed_letters)
    guess = input("Enter the letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed it!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_words[i] = guess
        print("Correct!")
    else:
        chances -= 1
        print(f"Wrong! {chances} left for you")


if "_" not in guessed_words:
    print("Congratulations! You won the game:", word)
else:
    print("Game over! The word was:", word)
