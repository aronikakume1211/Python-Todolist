score = 0
questions = [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "2 + 2 = ?", "a": "4"},
    {"q": "What color is the sky?", "a": "Blue"},
]

for q in questions:
    answer = input(q["q"] + " ")
    if answer.lower() == q["a"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("You scored", score, "out of", len(questions))
