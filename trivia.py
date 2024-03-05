import random

#reading the .txt file to get the questions, answer options, and the answer
def read_questions_from_file(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            question = lines[i].strip()
            options = [option.strip() for option in lines[i+1:i+5]]
            answer = int(lines[i+5].strip())
            questions.append({"question": question, "options": options, "answer": answer})
            i += 6
    return questions

#function to display the question to the user
def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)


#function to get user's answer for the displayed question
def get_user_answer():
    while True:
        user_input = input("Enter your answer (1-4): ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

#function that implements the triva game play
def play_trivia_game(questions):
    score = 0
    random.shuffle(questions)
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['options'][question['answer'] - 1]}.")
        print() 
    print(f"Game Over! Your final score is {score}/{len(questions)}.")

#main function
def main():
    questions = read_questions_from_file("questions.txt")
    print("Welcome to the Trivia Game!")
    play_trivia_game(questions)


if __name__ == "__main__":
    main()
