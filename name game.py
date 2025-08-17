import random

# Dictionary of names with categories and facts
data = {
    "celebrities": [
        ("Virat Kohli", "Indian cricketer"),
        ("Priyanka Chopra", "Indian actress and global icon"),
        ("Elon Musk", "CEO of SpaceX and Tesla")
    ],
    "movies": [
        ("Inception", "A mind-bending sci-fi thriller by Christopher Nolan"),
        ("Titanic", "Romantic tragedy set on a sinking ship"),
        ("Avatar", "Epic sci-fi about Pandora planet")
    ],
    "cities": [
        ("Hyderabad", "City of pearls in India"),
        ("Paris", "City of love and Eiffel Tower"),
        ("Tokyo", "Capital of Japan")
    ]
}

score = 0
rounds = 3

print("🎯 Welcome to the Advanced Name Guessing Game!")
print("You will get multiple hints. Guess before the hints run out!\n")

for round_num in range(1, rounds + 1):
    # Pick random category
    category = random.choice(list(data.keys()))
    name, fact = random.choice(data[category])

    # Prepare hints
    hints = [
        f"It's a {category[:-1]}",  # remove 's' from category for singular
        f"First letter: {name[0]}",
        f"Length: {len(name.replace(' ', ''))} letters (spaces not counted)",
        f"Jumbled: {''.join(random.sample(name.replace(' ', ''), len(name.replace(' ', ''))))}",
        f"Fun fact: {fact}"
    ]

    print(f"\n🔹 Round {round_num}:")
    attempts = len(hints)
    for i in range(attempts):
        guess = input(f"Guess the name (Hint {i+1}/{attempts}): ")

        if guess.lower() == name.lower():
            print("✅ Correct! You earned 1 point.")
            score += 1
            break
        else:
            print("❌ Wrong guess!")
            print("Hint:", hints[i])
    else:
        print(f"💡 Out of hints! The correct answer was: {name}")

print(f"\n🏆 Game Over! Your final score is {score}/{rounds}")
