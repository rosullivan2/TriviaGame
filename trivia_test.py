import unittest
from trivia import get_user_answer

class TestTriviaGame(unittest.TestCase):
    def test_get_user_answer(self):
        # Test if the function returns the correct answer based on user input
        question = {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"}
        self.assertEqual(get_user_answer(question), "Paris")

        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
