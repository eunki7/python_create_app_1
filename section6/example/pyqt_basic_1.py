import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
#print(sys.argv)
label = QLabel("PyQT First Test!")
label.show()

print("Before Loop")
app.exec_()
print("After Loop")
