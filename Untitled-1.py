from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

from random import randint



main_win = QWidget()
main_win.setWindowTitle("Вікно")
main_win.move(900, 70)
main_win.resize(720, 480)
main_win.show()

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

but = QPushButton("1")
but1 = QPushButton("2")
but2 = QPushButton("3")
but3 = QPushButton("4")
but4 = QPushButton("5")

h_line1.addWidget(but, alignment= Qt.AlignLeft)
h_line1.addWidget(but1, alignment= Qt.AlignRight)
h_line2.addWidget(but2, alignment= Qt.AlignCenter)
h_line3.addWidget(but3, alignment= Qt.AlignLeft)
h_line3.addWidget(but4, alignment= Qt.AlignRight)

v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)




main_win.setLayout(v_line)

app.exec_()