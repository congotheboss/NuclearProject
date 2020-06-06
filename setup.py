nG = 0.0
pT = 0.0
vO  = 0.0
tAL = 0.0
tRAU = 0.0
r = 0.0
tT = 0.0
nPIP = 0.0
nPJP = 0.0
dT_min =0.0
dT_max =0.0
dt_min =0.0
dt_max =0.0
dict = {}
vector = []
class Variabile (object):
    def __init__(self):
       self.inputuri()
       self.tempCond()
       exit()

    def inputuri(self):
        self.nG = float(input("Nr. de grupuri nucleare "))
        vector.append(self.nG)
        self.pT = float(input("Puterea termica a reactorului "))
        vector.append(self.pT)
        self.vO  = float(input ("Presiunea aburului viu "))
        self.tAL = float(input("Temperatura de alimentare "))
        self.tRAU = float(input("Temperatura apei raului "))
        self.r = float(input ("Cota de apa de racire luata din rau "))
        self.tT = float(input ("Temperatura apei provenite de la turnul de racire "))
        self.nPIP = float(input ("Numarul de preincalzitoare regenerative de inalta presiune "))
        self.nPJP = float(input ("Numarul de preincalzitoare regenerative de joasa presiune "))
        
        self.tR1 = ( self.r * self.tRAU + (1-self.r) *self.tT)
        print ("Valoare temperaturii apei de racire la intrare in condensator", self.tR1)
        print(vector)
        return self.tR1
        
       
        
    def tempCond(self):
        temp = self.tR1
        self.dT_min = float(input("Cresterea de temperatura minima "))
        self.dT_max = float(input("Cresterea de temperatura maxima "))
        self.dt_min = float(input("Diferenta de temperatura a condensatului minima "))
        self.dt_max = float(input("Diferenta de temperatura a condensatului maxima "))

        self.tc_min = (temp + self.dT_min + self.dt_min)
        self.tc_max = (temp + self.dT_max + self.dt_max)
        print("Temperatura Condensatului maxima respectiv minima", self.tc_max,";" ,self.tc_min)
    
if __name__ == "__main__":
    Variabile().__init__()
