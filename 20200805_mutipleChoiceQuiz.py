from Questions import Question
q1 = "your favourite singer\n" + \
     "(a) MJ (b)z23"
a1 = 'a'
q2 = "your favourite game\n" + \
     "(a) csgo (b) dota2"
a2 = 'b'

question1 = Question(q1, a1)
question2 = Question(q2, a2)

questions = [
    question1,
    question2
]

score = 0

for index in questions:
    print(index.prompt)
    youAnswer = input("enter your answer")
    if index.answer == youAnswer:
        print("your are right")
        score += 1
    else:
        print("wrong")

print("your score is:" + str(score) + "/" + "2")