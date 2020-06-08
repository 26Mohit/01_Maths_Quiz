import random

# Generate number of questions that user has entered
selected_questions = int(input("please enter number of questions:"))

# Generate numbers according to the values entered by user
lowest = int(input("please enter a low number"))
highest = int(input("please enter a high number"))
range = lowest-highest
num_1 = random.randint(lowest, highest)
num_2 = random.randint(lowest, highest)

question = "{} x {} = ".format(num_1, num_2)
correct = num_1 * num_2
answer = int(input(question))

if answer == correct:
  print("Great job")
else:
  print("oops")

