import pgzrun

TITLE = 'quiz game'
WIDTH = 870
HEIGHT = 650



moving = Rect (0,0,880,80) 
question = Rect (0,90,700, 150) 
timer = Rect (710,90,150, 150) 
answer1 = Rect (0,0,300, 150) 
answer2 = Rect (0,0,300,150) 
answer3 = Rect(0,0,300, 150)
answer4 = Rect (0,0,300, 150) 
skip = Rect (0,0,150, 330) 

question_index = 0
question_count = 0
questions = []

def draw():
    screen.fill('black')
    screen.draw.filled_rect(moving, 'red')
    screen.draw.filled_rect(question, 'blue')
    screen.draw.filled_rect(timer, 'blue')
    '''screen.draw.filled_rect(answer1, 'orange')
    screen.draw.filled_rect(answer2, 'orange')
    screen.draw.filled_rect(answer3, 'orange')
    screen.draw.filled_rect(answer4, 'orange')
    screen.draw.filled_rect(skip, 'green')'''

    moving_message = "Welcome to Quizz Game " + f'Q: {question_index} of {question_count}'
    screen.draw.textbox(moving_message, moving, color = 'white')

    screen.draw.textbox(questions[0], question, color = 'white')

def update():
    moving.x = moving.x -3
    if moving.right<0:
        moving.left = WIDTH

def read_questions():
    global questions, question_count
    x = open("question.txt", "r")
    for q in x:
        questions.append(q)
        question_count = question_count + 1
    x.close()
read_questions()






pgzrun.go()