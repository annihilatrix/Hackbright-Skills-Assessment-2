class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init___(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def add_question(self, question, correct_answer):
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        # keep track of score
        score = 0
        # iterate through question in questions list
        for question in self.questions:
            # provide the question to the student and see if response is correct
            if question.ask_and_evaluate():
                # answer is right, increment score
                score += 1.0

        return score


def take_test(exam, student):
    # administer the exam to the student    
    # assign score to student as new attribute score
    student.score = exam.administer()


def example():
    # create exam
    # add a few questions to exam
    new_exam = Exam("skills assessment")
    new_exam.add_question("Which cat is derpy? ", "Turtle")
    new_exam.add_question("Which cat is talkative? ", "Mini")
    new_exam.add_question("Who do we love more? ", "We love them both!")
    # creates student
    katie = Student('Katie', 'Simmons', '419 Thornton')
    # administers test to that student
    new_score = take_test(new_exam, katie)
    print new_score

example()
