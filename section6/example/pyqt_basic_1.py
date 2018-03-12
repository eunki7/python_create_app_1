import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("PyQt Label Test")
label.show()

print("Before loop")
app.exec_()
print("After loop")
