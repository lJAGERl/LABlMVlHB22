import random
import time
m=[random.randint(0,101) for i in range(1000000)]
def bls(M):#сортировка пузырьком
    for i in range(0,len(M)-1):
        s=False
        for j in range(0,len(M)-i-1):
            if M[j]>M[j+1]:
                M[j],M[j+1]=M[j+1],M[j]
                s=True
        if not s:
            break
    print(M)
def sls(M):#сортировка выбором
    for i in range(0,len(M)):
        n=i
        for j in range(i,len(M)):
            if M[j]<M[n]:
                n=j
        M[i],M[n]=M[n],M[i]
    print(M)
t1=0
t2=0
p=input("вывести не сортированный массив?(Y/N)? ")
if p=="y" or p=="Y":
    print(m)
p=input("выполнить сортировку пузырьком?(Y/N)? ")
if p=="y" or p=="Y":
    t1=time.time()
    m1=bls(m)
    t2=time.time()
    print("Время сортировки ", t2-t1)
p=input("выполнить сортировку выбором?(Y/N)? ")
if p=="y" or p=="Y":
    t1=time.time()
    m2=sls(m)
    t2=time.time()
    print("Время сортировки ", t2-t1)

        

