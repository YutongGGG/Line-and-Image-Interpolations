from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys
from PyQt5.QtWidgets import QApplication
from interface import interface


class interpolation3(QWidget):
    def __init__(self, parent=None):
        super(interpolation3, self).__init__(parent)
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
        self.textEdit.setPlainText('(7524706155761123*x^53)/32592575621351777380295131014550050576823494298654980010178247189670100796213387298934358016 '
                                   '- (8256132567685893*x^52)/7957171782556586274486115970349133441607298412757563479047423630290551952200534008528896 '
                                   '+ (4417206741827271*x^51)/1942668892225729070919461906823518906642406839052139521251812409738904285205208498176 '
                                   '- (1535780379748287*x^50)/474284397516047136454946754595585670566993857190463750305618264096412179005177856 '
                                   '+ (6242703177855265*x^49)/1852673427797059126777135760139006525652319754650249024631321344126610074238976 '
                                   '- (4941943557340547*x^48)/1809251394333065553493296640760748560207343510400633813116524750123642650624 '
                                   '+ (6345771729852007*x^47)/3533694129556768659166595001485837031654967793751237916243212402585239552 '
                                   '- (3396710687024461*x^46)/3450873173395281893717377931138512726225554486085193277581262111899648 '
                                   '+ (3092971062911063*x^45)/6739986666787659948666753771754907668409286105635143120275902562304 '
                                   '- (4864133491578653*x^44)/26328072917139296674479506920917608079723773850137277813577744384 '
                                   '+ (6683904974479329*x^43)/102844034832575377634685573909834406561420991602098741459288064 '
                                   '- (1012581692390607*x^42)/50216813883093446110686315385661331328818843555712276103168 '
                                   '+ (4362550020912437*x^41)/784637716923335095479473677900958302012794430558004314112 '
                                   '- (8403972900785751*x^40)/6129982163463555433433388108601236734474956488734408704 '
                                   '+ (7276145529476921*x^39)/23945242826029513411849172299223580994042798784118784 '
                                   '- (5687042705814213*x^38)/93536104789177786765035829293842113257979682750464 '
                                   '+ (251698622782667*x^37)/22835963083295358096932575511191922182123945984 '
                                   '- (5182997683813783*x^36)/2854495385411919762116571938898990272765493248 '
                                   '+ (6076986238493717*x^35)/22300745198530623141535718272648361505980416 '
                                   '- (3252356142954121*x^34)/87112285931760246646623899502532662132736 '
                                   '+ (3183564352193009*x^33)/680564733841876926926749214863536422912 '
                                   '- (5707337464843343*x^32)/10633823966279326983230456482242756608 '
                                   '+ (1172482023635551*x^31)/20769187434139310514121985316880384 '
                                   '- (3535821327843537*x^30)/649037107316853453566312041152512 '
                                   '+ (4894106128016041*x^29)/10141204801825835211973625643008 '
                                   '- (3110194269197707*x^28)/79228162514264337593543950336 '
                                   '+ (7260282761965863*x^27)/2475880078570760549798248448 '
                                   '- (7780604981346665*x^26)/38685626227668133590597632 '
                                   '+ (3826491679110493*x^25)/302231454903657293676544 '
                                   '- (3452316357143945*x^24)/4722366482869645213696 '
                                   '+ (2854607665368189*x^23)/73786976294838206464 '
                                   '- (8643642357449989*x^22)/4611686018427387904 '
                                   '+ (5982179590963443*x^21)/72057594037927936 '
                                   '- (3779147689132971*x^20)/1125899906842624 '
                                   '+ (8700244390162187*x^19)/70368744177664 '
                                   '- (2275900142038387*x^18)/549755813888 '
                                   '+ (1079578030384251*x^17)/8589934592 '
                                   '- (3703337575479973*x^16)/1073741824 '
                                   '+ (5722030714231191*x^15)/67108864 '
                                   '- (7932727417963789*x^14)/4194304 '
                                   '+ (4911080165264033*x^13)/131072 '
                                   '- (5401911557533443*x^12)/8192 '
                                   '+ (2622748410706789*x^11)/256 '
                                   '- (2231846376078433*x^10)/16 '
                                   '+ 1649796423291146*x^9 '
                                   '- 16771585870416816*x^8 '
                                   '+ 144649866065204960*x^7 '
                                   '- 1041207906221924608*x^6 '
                                   '+ 6123148012881221632*x^5 '
                                   '- 28581238270670573568*x^4 '
                                   '+ 101580007647381323776*x^3 '
                                   '- 257520021435778826240*x^2 '
                                   '+ 413648127838317641728*x '
                                   '- 315532527746996699136')


    def btnPress2_clicked(self):
        inter = interface()
        inter.baoxing()
        return


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWin = interpolation3()
#     myWin.show()
#     sys.exit(app.exec_())
