import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import qtawesome
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QInputDialog
import matlab.engine

import triple
from interpolation import interpolation
from interpolation2 import interpolation2
from interpolation3 import interpolation3
from interpolation4 import interpolation4
from double import double
from nearest import nearest
from triple import triple


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowModality(Qt.WindowModal)
        self.eng = matlab.engine.start_matlab()

    def init_ui(self):
        # Initialize the main UI components and layout
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 11, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 11, 10)
        self.setCentralWidget(self.main_widget)

        self.left_close = QtWidgets.QPushButton("")
        self.left_close.clicked.connect(self.close)
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_label_1 = QtWidgets.QPushButton("Boundary Function")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("Image Interpolation")
        self.left_label_2.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.area-chart', color='white'), "Lagrange")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart', color='white'), "Linear")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "Hermite")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.pie-chart', color='white'), "Spline")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), "NearestN")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), "Piecewise")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), "Bilinear")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), "Bicubic")
        self.left_button_8.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 10, 0, 1, 3)

        self.right_recommend_label = QtWidgets.QLabel("Application Cases")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()
        self.right_recommend_layout = QtWidgets.QGridLayout()
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("Landform Map")
        self.recommend_button_1.setIcon(QtGui.QIcon('map.jpg'))
        self.recommend_button_1.setIconSize(QtCore.QSize(200, 200))
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_label_1 = QtWidgets.QLabel(
            "To calculate the land area of Europe, first measure the map as follows:\n"
            "Choose a convenient origin with the x-axis from west to east and the y-axis\n"
            "from south to north, divide the interval on the x-axis from the westernmost\n"
            "to the easternmost boundary points into several segments, measure the\n"
            "y-coordinates y1 and y2 of the southern and northern boundary points at\n"
            "each dividing point in the y-direction.\n"
            "Requirements: Based on the boundary point data in the table, determine the\n"
            "boundary function and draw the landform map.")

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("lena Image")
        self.recommend_button_2.setIcon(QtGui.QIcon('lena.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(200, 200))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_label_2 = QtWidgets.QLabel("Application of interpolation methods in image resizing:\n"
                                                  "Requirements: Implement image enlargement and reduction based on\n"
                                                  "two-dimensional interpolation methods.")

        self.right_recommend_layout.addWidget(self.recommend_button_1, 1, 0)
        self.right_recommend_layout.addWidget(self.recommend_label_1, 1, 7)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 5, 0)
        self.right_recommend_layout.addWidget(self.recommend_label_2, 5, 7)

        self.right_layout.addWidget(self.right_recommend_label, 0, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 8, 9)

        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                background:lightgrey;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-right:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.setWindowOpacity(0.9)  # Transparency
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)

        self.left_button_1.clicked.connect(self.left_button_1_Clicked)
        self.left_button_2.clicked.connect(self.left_button_2_Clicked)
        self.left_button_3.clicked.connect(self.left_button_3_Clicked)
        self.left_button_4.clicked.connect(self.left_button_4_Clicked)
        self.left_button_5.clicked.connect(self.left_button_5_Clicked)
        self.left_button_6.clicked.connect(self.left_button_6_Clicked)
        self.left_button_7.clicked.connect(self.left_button_7_Clicked)
        self.left_button_8.clicked.connect(self.left_button_8_Clicked)
        self.recommend_button_1.clicked.connect(self.recommend_button_1_Clicked)
        self.recommend_button_2.clicked.connect(self.recommend_button_2_Clicked)

    def left_button_1_Clicked(self):
        self.add = interpolation()
        self.add.show()
        return

    def left_button_2_Clicked(self):
        self.add = interpolation2()
        self.add.show()
        return

    def left_button_3_Clicked(self):
        self.add = interpolation3()
        self.add.show()
        return

    def left_button_4_Clicked(self):
        self.add = interpolation4()
        self.add.show()
        return

    def left_button_5_Clicked(self):
        times, ok = QInputDialog.getInt(self, 'Zoom Factor', 'Enter a positive integer')
        if ok:
            img = cv2.imread("lena.jpg")
            zoom1 = nearest.function1(img, times)
            cv2.imshow("nearest neighbor", zoom1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

    def left_button_6_Clicked(self):
        zmf, ok = QInputDialog.getDouble(self, 'Zoom Factor', 'Enter a decimal number')
        if ok:
            import cv2
            zmf = float(zmf)
            ZI = self.eng.part(zmf, nargout=1)
            img = cv2.imread("lena2.jpg")
            cv2.imshow("image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

    def left_button_7_Clicked(self):
        size, ok = QInputDialog.getInt(self, 'Image Pixels', 'Enter an integer')
        if ok:
            img = cv2.imread("lena.jpg")
            zoom2 = double.function2(img, size, size)
            cv2.imshow("Bilinear Interpolation", zoom2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

    def left_button_8_Clicked(self):
        size, ok = QInputDialog.getInt(self, 'Image Pixels', 'Enter an integer')
        if ok:
            img = cv2.imread("lena.jpg")
            zoom3 = triple.function(img, size, size)
            cv2.imshow("cubic", zoom3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

    def recommend_button_1_Clicked(self):
        img = cv2.imread("data.jpg")
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def recommend_button_2_Clicked(self):
        img = cv2.imread("lena.jpg")
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
