# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1103, 824)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(460, 20, 621, 591))
        self.graphicsView.setObjectName("graphicsView")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(10, 340, 411, 24))
        self.label_12.setObjectName("label_12")
        self.temperaturaApaIntrareCondensator = QtWidgets.QLineEdit(Dialog)
        self.temperaturaApaIntrareCondensator.setGeometry(QtCore.QRect(10, 370, 81, 24))
        self.temperaturaApaIntrareCondensator.setObjectName("temperaturaApaIntrareCondensator")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 510, 181, 24))
        self.label_13.setObjectName("label_13")


        self.temperaturaCondensat = QtWidgets.QLineEdit(Dialog)
        self.temperaturaCondensat.setGeometry(QtCore.QRect(240, 510, 81, 24))
        self.temperaturaCondensat.setObjectName("temperaturaCondensat")
        

        self.diferentaTempCondensatorMax_2 = QtWidgets.QLineEdit(Dialog)
        self.diferentaTempCondensatorMax_2.setGeometry(QtCore.QRect(100, 460, 81, 24))
        self.diferentaTempCondensatorMax_2.setObjectName("diferentaTempCondensatorMax_2")
        self.diferentaTempCondensatorMin = QtWidgets.QLineEdit(Dialog)
        self.diferentaTempCondensatorMin.setGeometry(QtCore.QRect(100, 420, 81, 24))
        self.diferentaTempCondensatorMin.setObjectName("diferentaTempCondensatorMin")
        self.diferentaTempCondensatMin = QtWidgets.QLineEdit(Dialog)
        self.diferentaTempCondensatMin.setGeometry(QtCore.QRect(340, 420, 81, 24))
        self.diferentaTempCondensatMin.setObjectName("diferentaTempCondensatMin")
        self.diferentaTempCondensatMax = QtWidgets.QLineEdit(Dialog)
        self.diferentaTempCondensatMax.setGeometry(QtCore.QRect(340, 460, 81, 24))
        self.diferentaTempCondensatMax.setObjectName("diferentaTempCondensatMax")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(20, 420, 41, 24))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(20, 460, 41, 24))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(280, 460, 41, 24))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(280, 420, 41, 24))
        self.label_17.setObjectName("label_17")


        self.calcul = QtWidgets.QPushButton(Dialog)
        self.calcul.setGeometry(QtCore.QRect(350, 510, 93, 28))
        self.calcul.setObjectName("calcul")#
        
        self.calcul.clicked.connect(self.calculator)


        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 139, 305))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.numarGrupuriNucleare = QtWidgets.QLineEdit(self.widget)
        self.numarGrupuriNucleare.setObjectName("numarGrupuriNucleare")
        self.verticalLayout.addWidget(self.numarGrupuriNucleare)
        self.putereTermicaReactor = QtWidgets.QLineEdit(self.widget)
        self.putereTermicaReactor.setObjectName("putereTermicaReactor")
        self.verticalLayout.addWidget(self.putereTermicaReactor)
        self.presiuneAburViu = QtWidgets.QLineEdit(self.widget)
        self.presiuneAburViu.setObjectName("presiuneAburViu")
        self.verticalLayout.addWidget(self.presiuneAburViu)
        self.temperaturaApaAlimentare = QtWidgets.QLineEdit(self.widget)
        self.temperaturaApaAlimentare.setObjectName("temperaturaApaAlimentare")
        self.verticalLayout.addWidget(self.temperaturaApaAlimentare)
        self.temperaturaApaRau = QtWidgets.QLineEdit(self.widget)
        self.temperaturaApaRau.setText("")
        self.temperaturaApaRau.setObjectName("temperaturaApaRau")
        self.verticalLayout.addWidget(self.temperaturaApaRau)
        self.cotaApaRacireRau = QtWidgets.QLineEdit(self.widget)
        self.cotaApaRacireRau.setObjectName("cotaApaRacireRau")
        self.verticalLayout.addWidget(self.cotaApaRacireRau)
        self.temperaturaApaTurnRacire = QtWidgets.QLineEdit(self.widget)
        self.temperaturaApaTurnRacire.setObjectName("temperaturaApaTurnRacire")
        self.verticalLayout.addWidget(self.temperaturaApaTurnRacire)
        self.numarPreincalzitoareRegen = QtWidgets.QLineEdit(self.widget)
        self.numarPreincalzitoareRegen.setObjectName("numarPreincalzitoareRegen")
        self.verticalLayout.addWidget(self.numarPreincalzitoareRegen)
        self.preincalzitoareJoasa = QtWidgets.QLineEdit(self.widget)
        self.preincalzitoareJoasa.setObjectName("preincalzitoareJoasa")
        self.verticalLayout.addWidget(self.preincalzitoareJoasa)
        self.preincalzitoareInalta = QtWidgets.QLineEdit(self.widget)
        self.preincalzitoareInalta.setObjectName("preincalzitoareInalta")
        self.verticalLayout.addWidget(self.preincalzitoareInalta)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(161, 20, 281, 301))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_12.setText(_translate("Dialog", "Rezulta din ecuatia de bilant t.r1 temp. apei la intrare in Condensator"))
        self.label_13.setText(_translate("Dialog", "Temperatura condensatului t.c :"))
        self.label_14.setText(_translate("Dialog", "Dt.min"))
        self.label_15.setText(_translate("Dialog", "dt.max"))
        self.label_16.setText(_translate("Dialog", "dt.max"))
        self.label_17.setText(_translate("Dialog", "Dt.min"))
        self.calcul.setText(_translate("Dialog", "PushButton"))
        self.label_2.setText(_translate("Dialog", "Nr. Gr. nucleare: nG"))
        self.label_3.setText(_translate("Dialog", "Puterea Termica a reactorului: Pt"))
        self.label_4.setText(_translate("Dialog", "Presiunea aburului viu: p0"))
        self.label_5.setText(_translate("Dialog", "Temperatura apei de alimentare: t.al"))
        self.label.setText(_translate("Dialog", "Temperatura apei raului: t.rau"))
        self.label_6.setText(_translate("Dialog", "cota de apa de racire luata din rau: r"))
        self.label_7.setText(_translate("Dialog", "Temp. apei provenite de la turnul de racire: t.t"))
        self.label_8.setText(_translate("Dialog", "Numarul de preincalzitoare regenerative: nPR"))
        self.label_10.setText(_translate("Dialog", "Preincalzitoare de joasa presiune: nPJP"))
        self.label_9.setText(_translate("Dialog", "Preincalzitoare de inalta presiune: nPIP"))


    def calculator(self):
        r = self.cotaApaRacireRau.text()
        d = self.diferentaTempCondensatMax.text()
        calculCACAT  = float(r) * float(d) 
        cacatPraf = str(calculCACAT)
        self.temperaturaCondensat.setText(cacatPraf)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
