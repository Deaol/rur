from tkinter import *
import  time
n=int(input('колво роботов'))
k=10 #размер поля
mapRob=[]
StepTime=1
for i in range(k):
    mapRob.append([0] * k)

#               СОЗДАНИЕ ПОЛЯ
tk=Tk()
canvas=Canvas(tk, width=k*60, height=k*60)
canvas.pack()
a=10
b=10
c = -55
d = -45

for i in range(10):
    canvas.create_line(b,10,b,(k-1)*60+10)
    b+=60
for i in range(10):
    canvas.create_line(10,a,(k-1)*60+10,a)
    a+=60


sc=[]
for i in range(n):
    x=int(input('куда х'))
    y = int(input('куда y'))
    f=canvas.create_rectangle(c+60,5,d+60,15,fill='red')
    c+=60
    d+=60
    sc.append([i+1])
    sc[i].append([0])
    sc[i][1].append(i)
    sc[i].append([x])
    sc[i][2].append(y)
    sc[i].append(f)
    sc[i].append([False])
    sc[i][4].append(False)
    if i ==0:
        sc[i].append(True)
    else:
        sc[i].append(False)
    sc[i].append(False)
roblist=len(sc)

def start():
    global sc,numb
    if sc[numb][1][1]!=0 and sc[numb][5]==False :
        if mapRob[0][sc[numb][1][1]-1]==0:
            sc[numb][1][1]-=1
            if sc[numb][1][1]==0:
                sc[numb][5] =True
            for k in range(0,60):
                canvas.move(sc[numb][3], -1, 0)
                tk.update()
                time.sleep(0.005)
def VertStep():
    global sc,numb
    index=sc[numb][0]
    CordN=sc[numb][1][0]
    CordEnd=sc[numb][2][0]

    if CordN!=CordEnd:
        if mapRob[CordN+1][0]==0:
            mapRob[CordN + 1][0]=index
            mapRob[CordN][0]=0
            sc[numb][1][0]=CordN+1
            for k in range(0,60):
                canvas.move(sc[numb][3], 0, 1)
                tk.update()
                time.sleep(0.005)
        else:
            time.sleep(StepTime)
            print('CLOSE')
def povorot():
    global sc, numb,mapRob
    CordN = sc[numb][1][0]
    CordEnd = sc[numb][2][0]
    if CordN == CordEnd and sc[numb][4][0]==False:
        time.sleep(StepTime)
        sc[numb][4][0]=True
        print('povorot')
    elif sc[numb][1][1] == len(mapRob) - 1 and sc[numb][4][1] == False:
        time.sleep(StepTime)
        sc[numb][4][1]=True
        print('povor2')
    elif CordN==0 and (sc[numb][1][1]==0 or sc[numb][1][1]==len(mapRob)-1):
        time.sleep(StepTime)
        print('gg')
def GorStep():
    global sc, numb
    if sc[numb][1][0]==sc[numb][2][0]:
        index=sc[numb][0]
        CordN=sc[numb][1][1]
        CordEnd=sc[numb][2][1]
        i=sc[numb][1][0]
        if CordN!=CordEnd:
            if mapRob[i][CordN+1]==0:
                mapRob[i][CordN+1]=index
                mapRob[i][CordN]=0
                sc[numb][1][1]=CordN+1
                for k in range(0,60):
                    canvas.move(sc[numb][3], 1, 0)
                    tk.update()
                    time.sleep(0.005)
            else:
                time.sleep(StepTime)

                print('close')

def GoBackGor():
    global sc,mapRob,numb
    CordX=sc[numb][1][1]
    CordY = sc[numb][1][0]
    index=sc[numb][0]
    i = sc[numb][1][0]
    if CordX+1!=len(mapRob) and CordY!=0:
        if mapRob[i][CordX+1] == 0:
            mapRob[i][CordX + 1]=index
            mapRob[i][CordX]=0
            sc[numb][1][1] = CordX + 1
            for k in range(0,60):
                    canvas.move(sc[numb][3], 1, 0)
                    tk.update()
                    time.sleep(0.005)
        else:
            time.sleep(StepTime)
            print('CLOSE')
def GoBAckVer():
    global sc,mapRob,numb
    CordY = sc[numb][1][0]
    CordX = sc[numb][1][1]
    index = sc[numb][0]
    Cordnulindx=len(mapRob)-1
    if CordY != 0 and CordX== Cordnulindx:
        if mapRob[CordY-1][Cordnulindx]==0:
            mapRob[CordY-1][Cordnulindx] =index
            mapRob[CordY][Cordnulindx] =0
            sc[numb][1][0]=CordY-1
            for k in range(0,60):
                canvas.move(sc[numb][3], 0, -1)
                tk.update()
                time.sleep(0.005)
        else:
            time.sleep(StepTime)
            print('CLOSE')

def final():
    global sc, mapRob,numb
    CordX=sc[numb][1][1]
    index=sc[numb][0]
    CordY = sc[numb][1][0]
    if CordY==0 and CordX!=0:
        if mapRob[CordY][CordX-1]==0:
            mapRob[CordY][CordX - 1] =index
            mapRob[CordY][CordX] =0
            sc[numb][1][1] = CordX - 1
            for k in range(0,60):
                canvas.move(sc[numb][3], -1, 0)
                tk.update()
                time.sleep(0.005)
    if CordX==0 and CordY==0:
        sc[numb][5]=True
        sc[numb][4]=False
h=0
c=0
while h!=roblist:
    for j in range(roblist):
        numb =j
        if sc[numb][6]==False:
            start()
            VertStep()
            povorot()
            GorStep()
        if mapRob[sc[numb][2][0]][sc[numb][2][1]]==sc[numb][0] :
            sc[numb][6]=True
            time.sleep(1)
            print('delivert',numb)
        if sc[numb][6]==True:
            GoBackGor()
            povorot()
            GoBAckVer()
            povorot()
            final()
    for i in range (roblist):
        if mapRob[0][i]!=0:  # -1 т.к индекс емае
            h += 1

    if h==roblist:
        for i in range(1,roblist):
            sc[i][4]=False
            sc[i][5]=False
    else:
        h=0

print('done',sc)
tk.mainloop()