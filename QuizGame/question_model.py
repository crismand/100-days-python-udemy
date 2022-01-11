

class Question:
    """Model of a True/False question with attributes text and answer"""

    def __init__(self, text, answer):
        """Initialize the Question object given the text and the answer for T/F statements"""
        self.text = text
        self.answer = answer
