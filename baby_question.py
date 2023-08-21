from random import choice

questions = ["Why is the sky blue?: ", "Why is  the earth spherical?: ",
             "How many planets do we have?: " ]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because" :
    answer = input ("Why?: ").strip().lower()

print("Oh... Okay")
