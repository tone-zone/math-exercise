from Addition_exercises import CreateAdditionExercises
from Subtraction_exercises import CreateSubtractionExercise


def main():
    while True:
        try:
            number_of_exercise = int(input("How many equations do you want to print? (Must be a number >= 1): "))
        except ValueError:
            pass
        else:
            if number_of_exercise >= 1:
                break

    while True:
        try:
            number_of_digits = int(input("1 or 2 digits?: "))
        except ValueError:
            pass
        else:
            if 1 <= number_of_digits <= 2:
                break

    while True:
        try:
            type_of_exercise = input("Choose between addition, subtraction: ")
        except ValueError:
            pass
        else:
            if type_of_exercise.lower() == "addition":
                CreateAdditionExercises(number_of_exercise, number_of_digits).addition_exercise()
                break
            elif type_of_exercise.lower() == "subtraction":
                CreateSubtractionExercise(number_of_exercise, number_of_digits).subtraction_exercise()
                break


if __name__ == "__main__":
    main()