import random

# Generate number of questions that user has entered
# Generate numbers according to the values entered by user
# Generate questions according to the level user chose
selected_questions = int(input("please enter number of questions:"))
lowest = int(input("please enter a low number"))
highest = int(input("please enter a high number"))
for selected_questions in range(selected_questions):
    range = lowest-highest
    num_1 = random.randint(lowest, highest)
    num_2 = random.randint(lowest, highest)
    sign = ['+', '-', '*']
    levels = random.choice(sign)
    question = "{} {} {} = ".format(num_1, levels, num_2)
    correct = eval(str(num_1) + levels + str(num_2))
    answer = int(input(question))

    if answer == correct:
      print("Great job")
    else:
      print(correct)
      print("oops")

