def f1(kmd, m):
    if kmd=="help":
        print("все команды:\nполучить элемент по n индексу\nполучить элементы с n по b с шагом v\nполучить n элемент с конца массива\nвыход")
    if "получить элемент по " and " индексу" in kmd:
        if n==[]:
            print("неверно составлена команда")
        else:
            if n[0]>=len(m) or len(n)!=1:
                print("такого индекса нет в массиве")
            else:
                print(m[n[0]])
    elif "получить элементы " and " по " and " с шагом " in kmd:
        if n==[]:
            print("неверно составлена команда")
        else:
            if n[1]>=len(m) or n[0]<0 or n[2]<=0 or len(n)<3:
                print("неверный диапазон")
            else:
                i=n[0]
                while i<=n[1]:
                    print(m[i])
                    i+=n[2]
    elif "получить " and " элемент с конца массива" in kmd:
        if n==[]:
            print("неверно составлена команда")
        else:
            if n[0]>len(m) or len(n)!=1:
                print("такого индекса нет в массиве")
            else:
                print(m[-n[0]-1])
    else:
        print("такой команды нет")
m1=[0,1,2,3,4,5,6,7,8,9]
p=input("запуск? (Y?)")
if(p=="Y" or p=="y"):
    print("все доступные команды в help")
while p=="Y" or p=="y":
    m2=[]
    kmd=input("ведите команду ")
    if kmd=="выход":
        break
    wm=kmd.split()
    n=[]
    for w in wm:
        if w.isnumeric():
            n.append(int(w))
    f1(kmd,m1)
    #p=input("повторить? (Y?) ")
