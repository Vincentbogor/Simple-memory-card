#create a memory card application

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QButtonGroup, QPushButton, QLabel)
from random import shuffle, randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFixedSize(225, 225)

submit = QPushButton('Done (✿◠‿◠)')
lb_Question = QLabel('Which character has 7 strokes?')

RadioGroupBox = QGroupBox('Options ⬇️')
rbtn1 = QRadioButton('五')
rbtn2 = QRadioButton('你')
rbtn3 = QRadioButton('零')
rbtn4 = QRadioButton('𰻞') 

result = QLabel('ヾ(≧▽≦*)o')
answer = QLabel('Answer is 你')
answerGroup = QGroupBox('Results ⬇️')

RadioButtonGroup = QButtonGroup()
RadioButtonGroup.addButton(rbtn1)
RadioButtonGroup.addButton(rbtn2)
RadioButtonGroup.addButton(rbtn3)
RadioButtonGroup.addButton(rbtn4)

AnswerGroupBox = QVBoxLayout()
AnswerGroupBox.addWidget(result)
AnswerGroupBox.addWidget(answer)
answerGroup.setLayout(AnswerGroupBox)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(answerGroup)
answerGroup.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(submit, stretch=1)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    answerGroup.show()
    submit.setText("Next question")

def show_question():
    answerGroup.hide()
    RadioGroupBox.show()
    submit.setText('Done (✿◠‿◠)')

    RadioButtonGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioButtonGroup.setExclusive(True)

answerList = [rbtn1, rbtn2, rbtn3, rbtn4]
shuffle(answerList)

class ask_list():
    def __init__(self, question, ans, wro1, wro2, wro3):
        self.question = question
        self.ans = ans
        self.wro1 = wro1
        self.wro2 = wro2
        self.wro3 = wro3

ask1 = ask_list('Red light on a traffic light means', 'stop', 'go', 'slow', 'race')
ask2 = ask_list('Which one is a fish?', 'Shark', 'Dolphin', 'Whale', 'Jellyfish')
ask3 = ask_list('Which chinese character has 7 strokes?', '你', '五', '零', '𰻞')
ask4 = ask_list('Which one is a color?', 'Pink', 'Black', 'White', 'Brown')
ask5 = ask_list('Which color is anti-neon?', 'Brown', 'Yellow', 'Pink', 'Tangerine')
ask6 = ask_list('Which one is the impostor?', '🟠', '🔴', '🔴', '🔴')
ask7 = ask_list('Which emoji is not in the unicode 13.0 library?', 'Seahorse', 'bridge', 'disco ball', 'teapot')
ask8 = ask_list('Which one is a fruit?', 'Apple', 'Carrot', 'Potato', 'Celery')
ask9 = ask_list('Which one means “fast”?', 'race', 'crawl', 'park', 'idle')
ask10 = ask_list('Which one is edible?', 'Stone', 'Foxglove', 'Castor Bean', 'Oleander')

query_list = list()
query_list.append(ask1)
query_list.append(ask2)
query_list.append(ask3)
query_list.append(ask4)
query_list.append(ask5)
query_list.append(ask6)
query_list.append(ask7)
query_list.append(ask8)
query_list.append(ask9)
query_list.append(ask10)

window.total = 0
window.value = 0
window.query_now =-1
def next_query():
    window.total += 1
    randomizer = randint(0, len(query_list)-1)
    ask(query_list[randomizer])


def ask(query):
    shuffle(answerList)
    answerList[0].setText(query.ans)
    answerList[1].setText(query.wro1)
    answerList[2].setText(query.wro2)
    answerList[3].setText(query.wro3)
    lb_Question.setText(query.question)
    answer.setText(query.ans)
    show_question()

def check_answer():
    if answerList[0].isChecked():
        result.setText("(✿◡‿◡)")
        window.value += 1
    else:
        result.setText('(╯°□°）╯︵ ┻━┻')
    print('--------------------------------')
    print('Total ammount of questions: ', window.total)
    print('Total ammount of correct answers: ', window.value)
    print('Grade: ', (window.value / window.total) * 100)
    show_result()

def Beta():
    if submit.text() == 'Done (✿◠‿◠)':
        check_answer()
    else:
        next_query()

next_query()
submit.clicked.connect(Beta)
window.setLayout(layout_card)
window.show()
app.exec()