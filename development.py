from pyXSteam.XSteam import XSteam
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS) 
print (steamTable.hL_p(220.0))
print (steamTable.h_pt(60,200))
p = 505
t = 20
print(steamTable.h_pt(p,t))


# Rezultartle unei ecuatii 
d_pjp = 26.424
tc = 32.88
t_i_pjp1 = tc
t_e_pjp1 = t_i_pjp1 + d_pjp

#frontend 



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
