import random

# Define a list of questions with their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "answer": "Mars"
    },
    {
        "question": "When did Facebook launch?",
        "options": ["2012", "2010", "2000", "2004"],
        "answer": "2004"
    },
    # Add more questions here
]

def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")

def get_user_answer(question):
    while True:
        try:
            answer_index = int(input("Enter your answer (1, 2, 3, 4): ")) - 1
            if 0 <= answer_index < len(question["options"]):
                return question["options"][answer_index]
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_trivia_game(questions):
    score = 0
    random.shuffle(questions)  # Shuffle the questions to randomize the order
    for question in questions:
        display_question(question)
        user_answer = get_user_answer(question)
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
        print()
    print(f"Game Over! Your final score is {score}/{len(questions)}.")

# Main function to start the game
def main():
    print("Welcome to the Trivia Game!")
    play_trivia_game(questions)

if __name__ == "__main__":
    main()
