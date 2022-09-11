from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random


number = '0'
stop_sl = ['-', '+', '*', ':']

# Окна
app = QApplication([])
main_win = QWidget()

# Свойства окон и стили виджетов
main_win.setWindowTitle('Калькулятор')
main_win.setFixedSize(500, 300)
app.setStyleSheet("QLabel{font-size: 18pt;}")

# Объекты
lbl = QLabel('0')
btn_1 = QPushButton('1')
btn_2 = QPushButton('2')
btn_3 = QPushButton('3')
btn_4 = QPushButton('4')
btn_5 = QPushButton('5')
btn_6 = QPushButton('6')
btn_7 = QPushButton('7')
btn_8 = QPushButton('8')
btn_9 = QPushButton('9')
btn_0 = QPushButton('0')
btn_minus = QPushButton('-')
btn_plus = QPushButton('+')
btn_equare = QPushButton('=')
btn_um = QPushButton('*')
btn_del = QPushButton('DEL')
btn_dl = QPushButton(":")
btn_random = QPushButton('RANDOM NUMBER (1 to 100)')
btn_del_all = QPushButton('DEL ALL')

# Лэйауты
main_v = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
h6 = QHBoxLayout()


# Расположение виджетов

h1.addWidget(lbl, alignment=Qt.AlignRight)
h2.addWidget(btn_1)
h2.addWidget(btn_2)
h2.addWidget(btn_3)
h3.addWidget(btn_4)
h3.addWidget(btn_5)
h3.addWidget(btn_6)
h4.addWidget(btn_7)
h4.addWidget(btn_8)
h4.addWidget(btn_9)
h5.addWidget(btn_del)
h5.addWidget(btn_0)
h5.addWidget(btn_equare)
h2.addWidget(btn_plus)
h3.addWidget(btn_minus)
h4.addWidget(btn_um)
h5.addWidget(btn_dl)
h6.addWidget(btn_del_all)
h6.addWidget(btn_random)


main_v.addLayout(h1)
main_v.addLayout(h2)
main_v.addLayout(h3)
main_v.addLayout(h4)
main_v.addLayout(h5)
main_v.addLayout(h6)
main_win.setLayout(main_v)

# Функции
def btn_0f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(0)
    lbl.setText(str(number))

def btn_1f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(1)
    lbl.setText(str(number))

def btn_2f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(2)
    lbl.setText(str(number))

def btn_3f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(3)
    lbl.setText(str(number))

def btn_4f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(4)
    lbl.setText(str(number))

def btn_5f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(5)
    lbl.setText(str(number))

def btn_6f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(6)
    lbl.setText(str(number))

def btn_7f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(7)
    lbl.setText(str(number))

def btn_8f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(8)
    lbl.setText(str(number))

def btn_9f():
    global number
    if number == '0':
        number = ''
    elif len(number) == 19:
        number = '0'
        lbl.setText('Слишком много символов!(20)')
        return False
    number = number + str(9)
    lbl.setText(str(number))

def plus():
    global number
    global stop_sl
    try:
        if number[-1] in stop_sl or number == '0':
            pass
        elif len(number) == 19:
            number = '0'
            lbl.setText('Слишком много символов!(20)')
        else:
            number = number + '+'
            lbl.setText(str(number))
    except:
        number = '0'
        lbl.setText('Ошибка!')

def minus():
    global number
    global stop_sl
    try:
        if number[-1] in stop_sl or number == '0':
            pass
        elif len(number) == 19:
            number = '0'
            lbl.setText('Слишком много символов!(20)')
        else:
            number = number + '-'
            lbl.setText(str(number))
    except:
        number = '0'
        lbl.setText('Ошибка!')

def um():
    global number
    global stop_sl
    try:
        if number[-1] in stop_sl or number == '0':
            pass
        elif len(number) == 19:
            number = '0'
            lbl.setText('Слишком много символов!(20)')
        else:
            number = number + '*'
            lbl.setText(str(number))
    except:
        number = '0'
        lbl.setText('Ошибка!')

def dl():
    global number
    global stop_sl
    try:
        if number[-1] in stop_sl or number == '0':
            pass
        elif len(number) == 19:
            number = '0'
            lbl.setText('Слишком много символов!(20)')
        else:
            number = number + '/'
            lbl.setText(str(number))
    except:
        number = '0'
        lbl.setText('Ошибка!')

def equare():
    global number
    try:
        global stop_sl

        if number[-1] in stop_sl or number == '0':
           pass
        elif len(number) == 19:
           number = '0'
           lbl.setText(number)
        else:
            try:
                lbl.setText(str(eval(number)))

                number = ''
            except:

                number = '0'
                lbl.setText('Ошибка!')
    except:
        number = '0'
        lbl.setText('Ошибка!')
 


def delit_all():
    global number
    number = '0'
    lbl.setText(number)

def delit():
    global number
    try:
        if number == 0:
           return False
        nl = len(number) - 1
        number = number[0:nl]
        if number == '':
           number = 0
        lbl.setText(number)
    except:
        number = '0'
        lbl.setText(number)

def randomf():
    global number
    number = str(random.randint(0, 100))
    lbl.setText(number)
# Конекты

btn_0.clicked.connect(btn_0f)
btn_1.clicked.connect(btn_1f)
btn_2.clicked.connect(btn_2f)
btn_3.clicked.connect(btn_3f)
btn_4.clicked.connect(btn_4f)
btn_5.clicked.connect(btn_5f)
btn_6.clicked.connect(btn_6f)
btn_7.clicked.connect(btn_7f)
btn_8.clicked.connect(btn_8f)
btn_9.clicked.connect(btn_9f)
btn_equare.clicked.connect(equare)
btn_plus.clicked.connect(plus)
btn_minus.clicked.connect(minus)
btn_um.clicked.connect(um)
btn_dl.clicked.connect(dl)
btn_del.clicked.connect(delit)
btn_del_all.clicked.connect(delit_all)
btn_random.clicked.connect(randomf)

main_win.show()
app.exec_()