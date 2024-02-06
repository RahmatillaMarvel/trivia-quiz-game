class Question:
    """A class to represent a question.

    Attributes:
        text (str): The text of the question.
        answer (str): The correct answer to the question.
    """

    def __init__(self, text: str, answer: str) -> None:
        """Initialize a Question object with text and answer."""
        self.text = text
        self.answer = answer
