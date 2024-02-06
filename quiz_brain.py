import html
class QuizBrain:
    """A class to represent a quiz.

    Attributes:
        question_number (int): The current question number.
        question_list (list): A list of Question objects.
        score (int): The player's current score.
    """

    def __init__(self, question_list: list) -> None:
        """Initialize a QuizBrain object with a list of questions."""
        self.question_number: int = 0
        self.question_list: list = question_list
        self.score: int = 0
    
    def still_has_questions(self):
        """Check if there are still questions remaining in the quiz."""
        return self.question_number < len(self.question_list)
            
    def next_question(self):
        """Present the next question to the player."""
        current_question: dict = self.question_list[self.question_number]
        question_text: str = html.unescape(current_question.text)
        self.question_number += 1 
        user_answer = input(f'Q.{self.question_number}: {question_text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer: str, true_answer: str):
        """Check if the user's answer matches the true answer and update the score."""
        if user_answer.lower() == true_answer.lower():
            self.score += 1
            print('You got it')
        else:
            print('Sorry, that\'s wrong')
        print(f'Your score is {self.score}\n')
