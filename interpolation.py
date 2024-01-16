from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys
from PyQt5.QtWidgets import QApplication
from interface import interface


class interpolation(QWidget):
    def __init__(self, parent=None):
        super(interpolation, self).__init__(parent)
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
        # 以文本的形式输出到多行文本框
        self.textEdit.setPlainText(
                '(57658109730182110525481*x^26)/25711008708143844408671393477458601640355247900524685364822016\n'
                ' - (61769313510069788074139*x^25)/12554203470773361527671578846415332832204710888928069025792\n'
                ' + (31406276860072422879867*x^24)/6129982163463555433433388108601236734474956488734408704\n'
                ' - (80666065412148554849437*x^23)/23945242826029513411849172299223580994042798784118784\n'
                ' + (36710634156635525547799*x^22)/23384026197294446691258957323460528314494920687616\n'
                ' - (12598357176612480544621*x^21)/22835963083295358096932575511191922182123945984\n'
                ' + (27094538794586933286711*x^20)/178405961588244985132285746181186892047843328\n'
                ' - (46809273709491177051813*x^19)/1393796574908163946345982392040522594123776\n'
                ' + (16524179790512108896255*x^18)/2722258935367507707706996859454145691648\n'
                ' - (38605017414917222941203*x^17)/42535295865117307932921825928971026432\n'
                ' + (37619183706245893183745*x^16)/332306998946228968225951765070086144\n'
                ' - (7687291038320253369447*x^15)/649037107316853453566312041152512\n'
                ' + (660911191966006897837*x^14)/633825300114114700748351602688\n'
                ' - (24508713872672003059561*x^13)/316912650057057350374175801344\n'
                ' + (23909857773093373069553*x^12)/4951760157141521099596496896\n'
                ' - (19586366284364385474449*x^11)/77371252455336267181195264\n'
                ' + (26824534391520192505513*x^10)/2417851639229258349412352\n'
                ' - (476669100911628356067*x^9)/1180591620717411303424\n'
                ' + (14273556089364367320323*x^8)/1180591620717411303424\n'
                ' - (21710913935456973094281*x^7)/73786976294838206464\n'
                ' + (6600661010787640105973*x^6)/1152921504606846976\n'
                ' - (12555500597537603511851*x^5)/144115188075855872\n'
                ' + (4529899049582565491741*x^4)/4503599627370496\n'
                ' - (9495935165638841389335*x^3)/1125899906842624\n'
                ' + (6754329659761478659017*x^2)/140737488355328\n'
                ' - (1443793630793629476951*x)/8796093022208\n'
                ' + 4435562528315095594873/17592186044416')


    def btnPress2_clicked(self):
        inter = interface()
        inter.lagrange()
        return


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWin = interpolation()
#     myWin.show()
#     sys.exit(app.exec_())
