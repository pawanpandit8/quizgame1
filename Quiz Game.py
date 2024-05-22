print("***********************")
print("Welcome to My Quiz Game!!!")

question_bank=[
    {"text":"The ability of one class to aquire and attributies from another class is called ____.","answer":"A"},
    {"text":"which of the following is a type of inheritance?", "answer": "D"},
    {"text":"what is the depth of multilevel inheritance in python?", "answer": "C"}
]

options= [["A. Inheritance","B. Abstraction","C. Polymorphism","D. Objects"],
          ["A. Single","B. Double","C. Multiple","D. both A and C"],
          ["A. Two Level","B. Three Level","C. Any Level","D. None of these"],
          
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("********************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print([i])

    guess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
            print("Incorrect Answer")
            print(f"The correct answer is {question_bank[question_num]['answer']}")
            print(f"Your current score is {score}/{question_num+1}")

print(f"Your final score is {score}")
print(f"Your score is {(score/len(question_bank))*100}%")