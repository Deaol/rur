mas=[]
stl=False
k=9
n =10
for i in range(n):
    mas.append(0)
mas[0]=1


def dvig1():
    global mas,n
    b=0
    for i in range(n):
        if mas[i]==1:
            b=i
    if mas[b+1]==0:
        mas[b+1]=1
        mas[b]=0

def dvignaz():
    global mas,n
    b=0
    for i in range(n):
        if mas[i]==1:
            b=i

    if mas[b - 1] == 0:
        mas[b-1]=1
        mas[b]=0

def dvig2():
    global mas,n
    b=0
    for i in range(n):
        if mas[i]==2:
            b=i
    if mas[b - 1] == 0:
        mas[b-1]=2
        mas[b]=0
def prov():
    global mas,n,stl
    for i in range(n-1):
        if mas[i]!=0 and mas[i+1]!=0:
            stl=True
            while mas[0]!=1:
                dvignaz()
        if mas[0]==2:
            stl=False
for i in range(12):
    if stl==False:
        dvig1()
    dvig2()
    prov()
    print(mas)