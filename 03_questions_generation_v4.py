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
    num_3 = (num_1*num_1)
    question = "√{} = ".format(num_3)
    correct = (num_3**(1/2))
    answer = int(input(question))
    if answer == correct:
      print("Great job")
    else:
      print("oops")
      print(correct)

