import unittest
from unittest.mock import patch
from trivia import read_questions_from_file, get_user_answer, play_trivia_game, display_question
import io

class TestTriviaGame(unittest.TestCase):
    def setUp(self):
        # Create a sample questions.txt file for testing
        with open("test_questions.txt", "w") as file:
            file.write("Question 1\nOption 1\nOption 2\nOption 3\nOption 4\n1\n")

    def tearDown(self):
        # Clean up the created file after tests
        import os
        os.remove("test_questions.txt")

    def test_read_questions_from_file(self):
        questions = read_questions_from_file("test_questions.txt")
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]["question"], "Question 1")
        self.assertEqual(questions[0]["options"], ["Option 1", "Option 2", "Option 3", "Option 4"])
        self.assertEqual(questions[0]["answer"], 1)

    def test_get_user_answer_valid_input(self):
        with patch('builtins.input', side_effect=['1']):
            self.assertEqual(get_user_answer(), 1)

    def test_get_user_answer_invalid_input_then_valid_input(self):
        with patch('builtins.input', side_effect=['invalid', '2']):
            self.assertEqual(get_user_answer(), 2)

    def test_display_question(self):
        question = {"question": "Test Question", "options": ["Option 1", "Option 2", "Option 3", "Option 4"]}
        expected_output = "Test Question\nOption 1\nOption 2\nOption 3\nOption 4\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            display_question(question)
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_play_trivia_game(self):
        questions = [{"question": "Question 1", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "answer": 3},
                     {"question": "Question 2", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "answer": 4}]
         with patch('builtins.input', side_effect=['5', '2']):  # Simulate lifeline usage (selecting option 5) and user input
         with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            play_trivia_game(questions)
            output = fake_stdout.getvalue()
            self.assertIn("Implementing 50/50 lifeline...", output)  
            self.assertIn("Correct!", output)  
            self.assertIn("Game Over! Your final score is 2/2.", output)  

if __name__ == "__main__":
    unittest.main()