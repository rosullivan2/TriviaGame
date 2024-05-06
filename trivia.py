import random

# Function to choose category and get file name associated with it
def choose_category():
    while True: 
        user_input = int(input("Which category would you like to try?\n 1. General 2. Animals 3. Food 4. Pop Culture 5. Science\n"))
        if 1 <= int(user_input) <= 5:
            if user_input == 2: 
                file_name = "animal_questions.txt"
            elif user_input == 3: 
                file_name = "food_questions.txt"
            elif user_input == 4: 
                file_name = "pop_culture_questions.txt"
            elif user_input == 5: 
                file_name = "science_questions.txt"
            else: 
                file_name = "questions.txt" 
            return file_name
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Reading the .txt file to get the questions, answer options, and the answer
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

# Function to display the question to the user
def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

# Function to get user's answer for the displayed question
def get_user_answer():
    while True:
        user_input = input("Enter your answer (1-4): ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            return int(user_input)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

# Function to implement the trivia game play
def play_trivia_game(questions, lives=3):  # Add 3 lives
    score = 0
    random.shuffle(questions)
    for question in questions:
        display_question(question)
        
        # Offer 50/50 lifeline
        if lives > 0:  # Offer lifeline if the player has remaining lives
            print("\nDo you want to use a lifeline? (Press '5' for 50/50)")
            choice = input("Enter your choice: ").strip()
            if choice.lower() == "5":
                print("Implementing 50/50 lifeline...")
                options_copy = question["options"][:]  
                correct_option = question["options"][question["answer"] - 1]  
                options_copy.remove(correct_option) 
                wrong_option = random.choice(options_copy)  
                print(f"The correct answer is either {correct_option} or {wrong_option}.")
                lives -= 1  # Decrease the number of lives after using lifeline
        
        user_answer = get_user_answer()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['options'][question['answer'] - 1]}.")
            lives -= 1  # Decrease the number of lives if the answer is wrong
            print(f"You have {lives} {'life' if lives == 1 else 'lives'} left.")  
            if lives == 0:
                print("Game Over! You ran out of lives.")
                break  # End the game if the player runs out of lives

        print()
    print(f"Game Over! Your final score is {score}/{len(questions)}.")

# Main function
def main_function():
    print("Welcome to the Trivia Game!")
    questions = read_questions_from_file(choose_category())
    play_trivia_game(questions)

if __name__ == "__main__":
    main_function()