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
    def rsh2(self,r):
        if(self.tp!="крг" and self.tp!="круг"):
            print("неверный тип фигуры")
            return 0
        elif(self.p1==0 ):
            print("одно значений введено не верно")
            return 0
        else:
            S=3.14*r**2 
            return S
    def rsh3(self,d1,d2):
        if(self.tp!="рмб" and self.tp!="ромб"):
            print("неверный тип фигуры")
            return 0
        elif(self.p1==0 or self.p2==0):
            print("одно из значений введено не верно")
            return 0
        else:
            S=d1*d2/2
            return S
class rctn(geomf):#прямоугольник
    n=0
    def __init__(self,n,tp,p1,p2):
        super().__init__(tp,p1,p2)
        self.n=n
class crc(geomf):#круг
    n=0
    def __init__(self,n,tp,p1,p2):
        super().__init__(tp,p1,p2)
        self.n=n
class rhmb(geomf):#ромб
    n=0
    def __init__(self,n,tp,p1,p2):
        super().__init__(tp,p1,p2)
        self.n=n
print("прямоугольник")
GFO1=rctn(int(input("номер фигуры ")),input("тип фигуры "),float(input("значение переменной 1 ")),float(input("значение переменной 2 ")))
GF1=geomf(GFO1.tp,GFO1.p1,GFO1.p2)
GF1.S=GF1.rsh1(GF1.p1,GF1.p2)
print(GF1.tp,GF1.p1,GF1.p2,GF1.S)
print("круг")
GFO2=crc(int(input("номер фигуры ")),input("тип фигуры "),float(input("значение переменной 1 ")),0)
GF2=geomf(GFO2.tp,GFO2.p1,GFO2.p2)
GF2.p2=GF2.rsh2(GF2.p1)
print(GF2.tp,GF2.p1,GF2.p2)
print("ромб")
GFO3=rhmb(int(input("номер фигуры ")),input("тип фигуры "),float(input("значение переменной 1 ")),float(input("значение переменной 2 ")))
GF3=geomf(GFO3.tp,GFO3.p1,GFO3.p2)
GF3.S=GF3.rsh3(GF3.p1,GF3.p2)
print(GF3.tp,GF3.p1,GF3.p2,GF3.S)

