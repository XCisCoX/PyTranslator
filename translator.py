from cProfile import label
from PyQt5.QtWidgets import QApplication,QLabel
app = QApplication([])
label=QLabel('Hello PEDAA SAAG')
label.show()
app.exec_()