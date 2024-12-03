class geomf:
    tp=""
    p1=0
    p2=0
    def __init__(self,tp,p1,p2):
        self.tp=tp
        self.p1=p1
        self.p2=p2
    def rsh1(self,a,b):
        if(self.tp!="прмугл" and self.tp!="прямоугольник"):
            print("неверный тип фигуры")
            return 0
        elif(self.p1==0 or self.p2==0):
            print("одно из значений введено не верно")
            return 0
        else:
            S=a*b
            return S
print("прямоугольник")
GF1=geomf(input("тип фигуры "),float(input("значение переменной 1 ")),float(input("значение переменной 2 ")))
GF1.S=GF1.rsh1(GF1.p1,GF1.p2)
print(GF1.tp,GF1.p1,GF1.p2,GF1.S)


