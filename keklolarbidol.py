from tkinter import *
import  time

StepTime=1
mapRob=[[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]


#               СОЗДАНИЕ ПОЛЯ
tk=Tk()
canvas=Canvas(tk, width=300, height=300)
canvas.pack()
a=10
b=10
c=0
for i in range(6):
    canvas.create_line(b,10,b,300)
    b+=60
for i in range(6):
    canvas.create_line(10,a,300,a)
    a+=60
#               список роботов
rob0=canvas.create_rectangle(5,5,15,15,fill='red')
rob1=canvas.create_rectangle(65,5,75,15,fill='blue')
sc=[[1,[0,0],[2,2],rob0,False,True],          #[index,[начальныекоорд],[цель],[номер][поворот][старт позишн],[endпозишн]
    [2,[0,1],[4,3],rob1,False,False]]
numb=0
#               КОНЕЦ ПОЛЯ
def start():
    global sc,numb
    if sc[numb][1][1]!=0 and sc[numb][5]==False:
        if mapRob[0][sc[numb][1][1]-1]==0:
            sc[numb][1][1]=0
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
        print(index, CordN, CordEnd)
        if mapRob[CordN+1][0]==0:
            mapRob[CordN + 1][0]=index
            mapRob[CordN][0]=0
            sc[numb][1][0]=CordN+1
            for k in range(0,61):
                canvas.move(sc[numb][3], 0, 1)
                tk.update()
                time.sleep(0.005)
        else:
            time.sleep(StepTime)
            print('CLOSE')
def povorot():
    global sc, numb
    CordN = sc[numb][1][0]
    CordEnd = sc[numb][2][0]
    per=sc[numb][4]
    if CordN == CordEnd and per==False:
        time.sleep(StepTime)
        sc[numb][4]=True
        print('povorot')
def GorStep():
    global sc, numb
    if sc[numb][1][0]==sc[numb][2][0]:
        index=sc[numb][0]
        CordN=sc[numb][1][1]
        CordEnd=sc[numb][2][1]
        i=sc[numb][1][0]
        if CordN!=CordEnd:
            print(index, CordN, CordEnd)
            if mapRob[i][CordN+1]==0:
                mapRob[i][CordN+1]=index
                mapRob[i][CordN]=0
                sc[numb][1][1]=CordN+1
                for k in range(0,61):
                    canvas.move(sc[numb][3], 1, 0)
                    tk.update()
                    time.sleep(0.005)
            else:
                time.sleep(StepTime)
                print('close')
while c!=2:
    for j in range(2):
        numb =j
        start()
        VertStep()
        povorot()
        GorStep()
        print(c,mapRob)
    if mapRob[sc[numb][2][0]][sc[numb][2][1]]==sc[numb][0] :
        c+=1


tk.mainloop()