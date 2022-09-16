
quiz = {
    "quesion1": {
        "question": "is orange a fruits? ",
        "answer": "yes"
    },
    "quetion2": {
        "question": "Is yam a tuber? ",
        "answer": "yes"
    },
    "question3": {
        "question": "Spell Cab: ",
        "answer": "Cab"
    },
    "question4": {
        "question": "Spell eyes from the back? ",
        "answer": "seye"
    },
    "question5": {
        "question": "Is Ada a noun? ",
        "answer": "yes"
    },
    "question6": {
        "question": "What is the name of the president of nigeria? ",
        "answer": "Buhari"
    },
    "question7": {
        "question": "Is Nigeria your country? ",
        "answer": "yes"
    },
    "question8": {
        "question": "Are you a christian? ",
        "answer": "yes"
    },
    "question9": {
        "question": "What is your favorite color? ",
        "answer": "Green"
    },
    "question10": {
        "question": "spell ? ",
        "answer": "question mark"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print('Your score is: ' + str(score))
        print('')

    else:
        print('Incorrect')
        print('The answer is: ' + value['answer'])
        print('Your score is: ' + str(score))
        print('you got ' + str(score) + ' Out of 10 question')
        print('your percentage ' + str(int(score / 10 * 100)))
