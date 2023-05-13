import random


class CreateAdditionExercises:

    def __init__(self, number_of_exercise=10, number_of_digits=1):
        self.number_of_exercise = number_of_exercise
        self.number_of_digits = number_of_digits
        self.start_number = 0
        self.right_answers = 0
        self.num_limit = 10

    def addition_exercise(self):
        if self.number_of_digits == 2:
            self.num_limit = 21
        while self.start_number < int(self.number_of_exercise):
            numbers = [random.randrange(self.num_limit) for i in range(2)]
            try:
                question = input("{} + {} = ".format(*numbers))
                answer = sum(numbers)
                if int(question) == answer:
                    self.right_answers += 1
                else:
                    pass
                self.start_number += 1
            except ValueError:
                self.start_number += 1
        print(f"Results: {self.right_answers} / {self.start_number}")


if __name__ == "__main__":
    pass