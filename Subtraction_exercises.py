from Addition_exercises import CreateAdditionExercises
import random


class CreateSubtractionExercise(CreateAdditionExercises):

    def __init__(self, number_of_exercise=10, number_of_digits=1):
        CreateAdditionExercises.__init__(self)
        self.number_of_exercise = number_of_exercise
        self.number_of_digits = number_of_digits

    def subtraction_exercise(self):
        if self.number_of_digits == 2:
            self.num_limit = 21
        while self.start_number < int(self.number_of_exercise):
            numbers = [random.randrange(self.num_limit) for i in range(2)]
            if numbers[0] < numbers[1]:
                numbers = numbers[::-1]
            try:
                question = int(input("{} - {} = ".format(*numbers)))
                answer = numbers[0] - numbers[1]
                if question == answer:
                    self.right_answers += 1
                else:
                    pass
                self.start_number += 1
            except ValueError:
                self.start_number += 1
        print(f"Results: {self.right_answers} / {self.start_number}")


if __name__ == "__main__":
 pass