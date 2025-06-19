class QuizBrain:
    def __init__(self,q_list):
        self.score = 0
        self.question_number=0
        self.question_list= q_list


    def still_has_questions(self):

        return self.question_number<len(self.question_list)


    def next_question(self):
        current_question=self.question_list[self.question_number]

        user_answer=input(f'Q.{self.question_number} : {current_question.que} (True/False?):').strip().lower()
        correct_answer=str(current_question.answer).lower()
        if user_answer==correct_answer:
            print(f'Correct Answer! {user_answer}')
            self.score=self.score+1
            print(f'Your current score is {self.score}')
        elif user_answer!=correct_answer:
            print(f'Incorrect Answer! {user_answer}')
            print(f'correct answer: {self.question_list[self.question_number].answer}')
            print(f'Your current score is {self.score}')
        self.question_number = self.question_number + 1



