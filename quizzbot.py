class QuizBot:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        return user_answer

    def run_quiz(self):
        for question, answer in self.questions.items():
            user_answer = self.ask_question(question)
            if user_answer == answer:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
            print()  # Add a blank line for better readability

        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


# Define your quiz questions and answers here
quiz_questions = {
    "What is the capital of France?": "paris",
    "Who wrote 'Romeo and Juliet'?": "shakespeare",
    "What is the powerhouse of the cell?": "mitochondria"
}

# Create an instance of the QuizBot and run the quiz
quiz_bot = QuizBot(quiz_questions)
quiz_bot.run_quiz()
