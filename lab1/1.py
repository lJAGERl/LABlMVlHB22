import random
def func1(a,b,c):
    m=0
    p=' '
    if (a>0):
        if m<a:
            m=a
            p='a'
        if m<b:
            m=b
            p='b'
        if m<c:
            m=c
            p='c'
        print("Наибольшее значение ",p,'=',m)
    else:
        print(-1)
a=int(input("Введите целое число для а "))
b=random.randint(-15,25)
c=random.randint(-25,15)
print('a=',a,',','b=',b,',','c=',c)
func1(a,b,c)
