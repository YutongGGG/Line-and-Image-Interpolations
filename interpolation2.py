from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys
from PyQt5.QtWidgets import QApplication
from interface import interface


class interpolation2(QWidget):
    def __init__(self, parent=None):
        super(interpolation2, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Interpolation Polynomial")

    def setUpUI(self):
        self.resize(800, 800)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton('Show Polynomial')
        self.btnPress2 = QPushButton('Show Image')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)

        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        self.btnPress2.clicked.connect(self.btnPress2_clicked)

    def btnPress1_clicked(self):
        self.textEdit.setPlainText('y = (2*x)/7 + 42\n'
                                   'y = (4*x)/5 + 183/5\n'
                                   'y = (2*x)/3 + 115/3\n'
                                   'y = 50\n'
                                   'y = 1466/13 - (24*x)/13\n'
                                   'y = 119 - 2*x\n'
                                   'y = 30\n'
                                   'y = x/2 + 6\n'
                                   'y = (2*x)/5 + 58/5\n'
                                   'y = 784/15 - (4*x)/15\n'
                                   'y = (7*x)/8 - 415/16\n'
                                   'y = x - 71/2\n'
                                   'y = (2*x)/21 + 112/3\n'
                                   'y = 503/5 - (3*x)/5\n'
                                   'y = 791/5 - (6*x)/5\n'
                                   'y = 515/3 - (4*x)/3\n'
                                   'y = 241 - 2*x\n'
                                   'y = (4*x)/5 - 286/5\n'
                                   'y = (66*x)/13 - 6943/13\n'
                                   'y = 3075/11 - (20*x)/11\n'
                                   'y = 129/2 - x/13\n'
                                   'y = 1140/11 - (4*x)/11\n'
                                   'y = 123 - x/2\n'
                                   'y = 4*x - 534\n'
                                   'y = 66\n'
                                   'y = 2*x - 248\n')

    def btnPress2_clicked(self):
        inter = interface()
        inter.xianxingfenduan()
        return


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWin = interpolation2()
#     myWin.show()
#     sys.exit(app.exec_())
