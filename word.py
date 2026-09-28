import random

words = ["python", "computer", "program", "school", "keyboard"]

score = 0

print("===== Word Scramble Game =====")

while True:
    word = random.choice(words)

    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = "".join(scrambled)

    print("\nScrambled Word:", scrambled_word)

    answer = input("Guess the word (or type exit): ")

    if answer.lower() == "exit":
        break

    if answer.lower() == word:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong!")
        print("Correct word:", word)

print("\nGame Over!")
print("Your Score:", score)
