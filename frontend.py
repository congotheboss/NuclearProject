# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

#import main
from PyQt5 import QtCore, QtGui, QtWidgets
from pyXSteam.XSteam import XSteam

#define global obj 
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS) 

class Ui_MainWindow(object):
#aici trebuie sa identifici care sunt componentele tale si sa le separi printr-un rand gol
#tot aici o sa gasesti butoanele, separale si lasa-le un comentariu 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 908)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1201, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.i_Pt = QtWidgets.QLineEdit(self.tab)
        self.i_Pt.setGeometry(QtCore.QRect(10, 56, 133, 20))
        self.i_Pt.setObjectName("i_Pt")

        self.i_T_rau = QtWidgets.QLineEdit(self.tab)
        self.i_T_rau.setGeometry(QtCore.QRect(10, 134, 133, 20))
        self.i_T_rau.setObjectName("i_T_rau")

        self.i_T_t = QtWidgets.QLineEdit(self.tab)
        self.i_T_t.setGeometry(QtCore.QRect(10, 186, 133, 20))
        self.i_T_t.setObjectName("i_T_t")

        self.i_r = QtWidgets.QLineEdit(self.tab)
        self.i_r.setGeometry(QtCore.QRect(10, 160, 133, 20))
        self.i_r.setObjectName("i_r")

        self.i_N_PJP = QtWidgets.QLineEdit(self.tab)
        self.i_N_PJP.setGeometry(QtCore.QRect(10, 238, 133, 20))
        self.i_N_PJP.setObjectName("i_N_PJP")

        self.i_p0 = QtWidgets.QLineEdit(self.tab)
        self.i_p0.setGeometry(QtCore.QRect(10, 82, 133, 20))
        self.i_p0.setObjectName("i_p0")

        self.i_N_PIP = QtWidgets.QLineEdit(self.tab)
        self.i_N_PIP.setGeometry(QtCore.QRect(10, 212, 133, 20))
        self.i_N_PIP.setObjectName("i_N_PIP")
        
        self.i_T_al = QtWidgets.QLineEdit(self.tab)
        self.i_T_al.setGeometry(QtCore.QRect(10, 108, 133, 20))
        self.i_T_al.setObjectName("i_T_al")

        self.i_d_t_min = QtWidgets.QLineEdit(self.tab)
        self.i_d_t_min.setGeometry(QtCore.QRect(11, 393, 133, 20))
        self.i_d_t_min.setObjectName("i_d_t_min")

        self.o_t_c_max = QtWidgets.QLineEdit(self.tab)
        self.o_t_c_max.setGeometry(QtCore.QRect(11, 419, 133, 20))
        self.o_t_c_max.setObjectName("o_t_c_max")

        self.i_D_t_max = QtWidgets.QLineEdit(self.tab)
        self.i_D_t_max.setGeometry(QtCore.QRect(11, 315, 133, 20))
        self.i_D_t_max.setObjectName("i_D_t_max")

        self.o_tc = QtWidgets.QLineEdit(self.tab)
        self.o_tc.setGeometry(QtCore.QRect(11, 497, 133, 20))
        self.o_tc.setObjectName("o_tc")
        
        self.o_t_c_min = QtWidgets.QLineEdit(self.tab)
        self.o_t_c_min.setGeometry(QtCore.QRect(11, 445, 133, 20))
        self.o_t_c_min.setObjectName("o_t_c_min")

        self.o_Pc = QtWidgets.QLineEdit(self.tab)
        self.o_Pc.setGeometry(QtCore.QRect(11, 471, 133, 20))
        self.o_Pc.setObjectName("o_Pc")

        self.i_d_t_max = QtWidgets.QLineEdit(self.tab)
        self.i_d_t_max.setGeometry(QtCore.QRect(11, 367, 133, 20))
        self.i_d_t_max.setObjectName("i_d_t_max")

        self.i_D_t_min = QtWidgets.QLineEdit(self.tab)
        self.i_D_t_min.setGeometry(QtCore.QRect(11, 341, 133, 20))
        self.i_D_t_min.setObjectName("i_D_t_min")
        
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(9, 9, 320, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(150, 29, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(150, 55, 196, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(150, 81, 120, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(150, 108, 150, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(150, 134, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(150, 160, 174, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(150, 186, 251, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(150, 213, 309, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(150, 239, 309, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 280, 451, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(160, 370, 251, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(160, 343, 331, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(160, 317, 331, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(160, 422, 221, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(160, 448, 171, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(160, 501, 309, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(160, 475, 371, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(160, 396, 261, 16))
        self.label_19.setObjectName("label_19")
        
        self.o_t_r1 = QtWidgets.QLineEdit(self.tab)
        self.o_t_r1.setGeometry(QtCore.QRect(370, 280, 133, 20))
        self.o_t_r1.setObjectName("o_t_r1")

        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(10, 590, 241, 16))
        self.label_20.setObjectName("label_20")

        self.o_D_t_PA = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PA.setGeometry(QtCore.QRect(260, 590, 133, 20))
        self.o_D_t_PA.setObjectName("o_D_t_PA")

        self.i_cp = QtWidgets.QLineEdit(self.tab)
        self.i_cp.setGeometry(QtCore.QRect(11, 552, 133, 20))
        self.i_cp.setObjectName("i_cp")

        self.i_D_i_PA = QtWidgets.QLineEdit(self.tab)
        self.i_D_i_PA.setGeometry(QtCore.QRect(11, 526, 133, 20))
        self.i_D_i_PA.setObjectName("i_D_i_PA")

        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(160, 556, 281, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(160, 530, 451, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 620, 501, 16))
        self.label_23.setObjectName("label_23")

        self.o_D_t_PR = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PR.setGeometry(QtCore.QRect(10, 640, 133, 20))
        self.o_D_t_PR.setObjectName("o_D_t_PR")

        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(10, 670, 251, 16))
        self.label_24.setObjectName("label_24")

        self.o_t_DEG = QtWidgets.QLineEdit(self.tab)
        self.o_t_DEG.setGeometry(QtCore.QRect(10, 690, 133, 20))
        self.o_t_DEG.setObjectName("o_t_DEG")

        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(10, 720, 461, 16))
        self.label_25.setObjectName("label_25")

        self.o_p_DEG = QtWidgets.QLineEdit(self.tab)
        self.o_p_DEG.setGeometry(QtCore.QRect(10, 740, 133, 20))
        self.o_p_DEG.setObjectName("o_p_DEG")

        self.o_p_DEG_ales = QtWidgets.QLineEdit(self.tab)
        self.o_p_DEG_ales.setGeometry(QtCore.QRect(150, 740, 133, 20))
        self.o_p_DEG_ales.setObjectName("o_p_DEG_ales")

        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(10, 770, 261, 16))
        self.label_26.setObjectName("label_26")

        self.o_t_DEG_ales = QtWidgets.QLineEdit(self.tab)
        self.o_t_DEG_ales.setGeometry(QtCore.QRect(10, 790, 133, 20))
        self.o_t_DEG_ales.setObjectName("o_t_DEG_ales")

        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(660, 10, 421, 16))
        self.label_27.setObjectName("label_27")
        self.o_D_t_PJP = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PJP.setGeometry(QtCore.QRect(660, 30, 133, 20))
        self.o_D_t_PJP.setObjectName("o_D_t_PJP")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(660, 60, 271, 16))
        self.label_28.setObjectName("label_28")
        self.o_P_ref = QtWidgets.QLineEdit(self.tab)
        self.o_P_ref.setGeometry(QtCore.QRect(660, 80, 133, 20))
        self.o_P_ref.setObjectName("o_P_ref")
        self.o_V_asp = QtWidgets.QLineEdit(self.tab)
        self.o_V_asp.setGeometry(QtCore.QRect(660, 130, 133, 20))
        self.o_V_asp.setObjectName("o_V_asp")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(660, 110, 241, 16))
        self.label_29.setObjectName("label_29")
        self.o_V_ref = QtWidgets.QLineEdit(self.tab)
        self.o_V_ref.setGeometry(QtCore.QRect(660, 180, 133, 20))
        self.o_V_ref.setObjectName("o_V_ref")
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(660, 160, 241, 16))
        self.label_30.setObjectName("label_30")
        self.i_Ita_PA = QtWidgets.QLineEdit(self.tab)
        self.i_Ita_PA.setGeometry(QtCore.QRect(660, 230, 133, 20))
        self.i_Ita_PA.setObjectName("i_Ita_PA")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(660, 210, 241, 16))
        self.label_31.setObjectName("label_31")
        self.o_D_i_PA = QtWidgets.QLineEdit(self.tab)
        self.o_D_i_PA.setGeometry(QtCore.QRect(660, 280, 133, 20))
        self.o_D_i_PA.setObjectName("o_D_i_PA")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(660, 260, 241, 16))
        self.label_32.setObjectName("label_32")
        self.o_D_t_PA_2 = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PA_2.setGeometry(QtCore.QRect(660, 330, 133, 20))
        self.o_D_t_PA_2.setObjectName("o_D_t_PA_2")
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(660, 310, 271, 16))
        self.label_33.setObjectName("label_33")
        self.o_D_t_PIP = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PIP.setGeometry(QtCore.QRect(660, 380, 133, 20))
        self.o_D_t_PIP.setObjectName("o_D_t_PIP")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(660, 360, 441, 16))
        self.label_34.setObjectName("label_34")
        self.o_D_t_PA_recalc = QtWidgets.QLineEdit(self.tab)
        self.o_D_t_PA_recalc.setGeometry(QtCore.QRect(660, 430, 133, 20))
        self.o_D_t_PA_recalc.setObjectName("o_D_t_PA_recalc")
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(660, 410, 271, 16))
        self.label_35.setObjectName("label_35")

        self.Calculeaza1 = QtWidgets.QPushButton(self.tab)
        self.Calculeaza1.setGeometry(QtCore.QRect(510, 230, 75, 23))
        self.Calculeaza1.setObjectName("Calculeaza1")
        self.Calculeaza1.clicked.connect(self.calcul1)

        self.Calculeaza2 = QtWidgets.QPushButton(self.tab)
        self.Calculeaza2.setGeometry(QtCore.QRect(520, 440, 75, 23))
        self.Calculeaza2.setObjectName("Calculeaza2")
        self.Calculeaza2.clicked.connect(self.calcul2)

        self.Calculeaza3 = QtWidgets.QPushButton(self.tab)
        self.Calculeaza3.setGeometry(QtCore.QRect(1080, 430, 75, 23))
        self.Calculeaza3.setObjectName("Calculeaza3")
        #self.Calculeaza3.clicked.connect(self.calcul3)#

        self.i_nG = QtWidgets.QLineEdit(self.tab)
        self.i_nG.setGeometry(QtCore.QRect(10, 30, 133, 20))
        self.i_nG.setObjectName("i_nG")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Calculul Parametrilor Circuitului Secundar al Reactorului de Tip PWR"))
        self.label_2.setText(_translate("MainWindow", "Numarul de grupuri nucleare nG"))
        self.label_3.setText(_translate("MainWindow", "Puterea Termica a Reactorului Nuclear Pt"))
        self.label_4.setText(_translate("MainWindow", "Presiunea aburului viu p0"))
        self.label_5.setText(_translate("MainWindow", "Temperatura de Alimentare t.al"))
        self.label_6.setText(_translate("MainWindow", "Temperatura apei raului t.rau"))
        self.label_7.setText(_translate("MainWindow", "Cota de apa de racire luata din rau r"))
        self.label_8.setText(_translate("MainWindow", "Temperatura apei provenite de la turnul de racire t.t"))
        self.label_9.setText(_translate("MainWindow", "Numarul de preincalzitoare regenerative de inalta presiune n.PIP"))
        self.label_10.setText(_translate("MainWindow", "Numarul de preincalzitoare regenerative de joasa presiune n.PJP"))
        self.label_11.setText(_translate("MainWindow", "Rezulta valoarea temperaturii apei de racire la intrarea in condensator t.r1"))
        self.label_12.setText(_translate("MainWindow", "Diferenta de temperatura maxima a condensatului "))
        self.label_13.setText(_translate("MainWindow", "Cresterea de Temperatura minima a apei de racire in condensator"))
        self.label_14.setText(_translate("MainWindow", "Cresterea de Temperatura maxima a apei de racire in condensator"))
        self.label_15.setText(_translate("MainWindow", "Temperatura condensatului maxima "))
        self.label_16.setText(_translate("MainWindow", "Temperatura condensatului minima"))
        self.label_17.setText(_translate("MainWindow", "Se citeste t.c ( P.c, x=0 ) "))
        self.label_18.setText(_translate("MainWindow", "P.c = p( t.c.min, x=0 ) si P.c p( t.c.max, x=0 ) Se alege o valoare rotunjita "))
        self.label_19.setText(_translate("MainWindow", "Diferenta de temperatura minima a condensatului "))
        self.label_20.setText(_translate("MainWindow", "Rezulta incalzirea condensatului in pompa : D.t.PA"))
        self.label_21.setText(_translate("MainWindow", "Caldura specifica a apei in stare lichida c.p kJ/kG * K"))
        self.label_22.setText(_translate("MainWindow", "Se considera cresterea de entalpie a condensatului in pompa de alimentare D.i.PA kJ/kG * K"))
        self.label_23.setText(_translate("MainWindow", "Initial se considera cresterea de temperatura a condensatului pe un preincalzitor aproximata cu D.t.PR:"))
        self.label_24.setText(_translate("MainWindow", "Rezulta temperatura la iesirea din degazor t.DEG :"))
        self.label_25.setText(_translate("MainWindow", "Rezulta presiunea  la iesirea din degazor p.DEG( t.DEG, x=0 ) cu cond p.DEG < sau = cu 7 bar :"))
        self.label_26.setText(_translate("MainWindow", "Rezulta temperatura reala la iesirea din degazor t.DEG :"))
        self.label_27.setText(_translate("MainWindow", "Se calculeaza cresterea de temperatura pe un preincalzitor de joasa presiune D.t.PJP:"))
        self.label_28.setText(_translate("MainWindow", "Presiunea la refularea pompei de alimentare este P.ref:"))
        self.label_29.setText(_translate("MainWindow", "Volumul specific al pompei la aspiratie v.asp:"))
        self.label_30.setText(_translate("MainWindow", "Volumul specific al pompei la refulare v.ref:"))
        self.label_31.setText(_translate("MainWindow", "Randamentul pompei  de alimentare ita.PA:"))
        self.label_32.setText(_translate("MainWindow", "Rezulta cresterea de entalpie in pompa D.i.PA:"))
        self.label_33.setText(_translate("MainWindow", "Cresterea de temperatura in pompa D.t.PA recalculata:"))
        self.label_34.setText(_translate("MainWindow", "Se calculeaza cresterea de temperatura pe un preincalzitor de inalta  presiune D.t.PIP:"))
        self.label_35.setText(_translate("MainWindow", "Cresterea de temperatura in pompa D.t.PA recalculata:"))
        self.Calculeaza1.setText(_translate("MainWindow", "Calculeaza"))
        self.Calculeaza2.setText(_translate("MainWindow", "Calculeaza"))
        self.Calculeaza3.setText(_translate("MainWindow", "Calculeaza"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))



#in partea de jos se face o mostenire la clasa de sus pentru a separa calculele de frontend
class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        #QtGui.QMainWindow._init_(self)
        super().__init__()
        self.setupUi(self)
    def calcul1(self):
        global v_t_r1

        v_r = float(self.i_r.text())
        v_t_rau = float(self.i_T_rau.text())
        v_T_t = float(self.i_T_t.text())
        
        
        v_t_r1 = (v_r * v_t_rau + (1-v_r) * v_T_t)


        self.o_t_r1.setText(str(v_t_r1))

    def calcul2(self):
        v_D_t_max = float(self.i_D_t_max.text())
        v_D_t_min = float(self.i_D_t_min.text())
        v_d_t_max = float(self.i_d_t_max.text())
        v_d_t_min = float(self.i_d_t_min.text())
        vi_t_r1 = float(self.o_t_r1.text())

        print(v_t_r1)

        v_t_c_min = ( vi_t_r1 + v_D_t_min + v_d_t_min)
        v_t_c_max = ( vi_t_r1 + v_D_t_max + v_d_t_max)


        self.o_t_c_min.setText(str(v_t_c_min))
        self.o_t_c_max.setText(str(v_t_c_max))
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())