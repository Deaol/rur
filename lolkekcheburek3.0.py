from tkinter import *
import  time
mapRob=[]
k=10
StepTime=1
for i in range(k):
    mapRob.append([0] * k)
a=10
b=10
#1-начальные|2 конечные|3 id|4 повороты|5стрт|6 деливерт# косяки перепутала х и у и он не останавливается
class Robot:
    n = 0  # kolvo robotov
    c = -65
    d=-65
    def __init__(self,canvas):
        self.canvas=canvas
        self.id=canvas.create_rectangle(10,10,20,20,fill='red')
        self.canvas.move(self.id,Robot.c+60,Robot.d+60)
        self.startcord=[0,Robot.n]
        self.finalcord=[int(input('x')),int(input('y'))]
        self.povorot = [False,False]
        if self.startcord[1]==0:
            self.startpos=True
        else:
            self.startpos=False
        self.delivered=False
        Robot.n+=1
        Robot.c += 60

        print(Robot.n, Robot.c)
    def start(self,mapRob,canvas):
        if self.startcord[1]!=0 and self.startpos==False:
            if mapRob[0][self.startcord[1]-1]==0:
                self.startcord[1]-=1
                if self.startcord[1]==0:
                    self.startpos=True
                for k in range(0,60):
                    canvas.move(self.id,-1,0)
                    tk.update()
                    time.sleep(0.001)
    def VertStep(self,mapRob,canvas):
        if self.startcord[0]!=self.finalcord[0]:
            if mapRob[self.startcord[0]+1][0]==0:
                mapRob[self.startcord[0]+1][0]=self.id
                mapRob[self.startcord[0]][0] =0
                self.startcord[0]+=1
                for k in range(0,60):
                    canvas.move(self.id,0,1)
                    tk.update()
                    time.sleep(0.001)
            else:
                time.sleep(StepTime)
                print('clo3e')
    def povorot(self,mapRob):
        if self.startcord[0]==self.finalcord[0] and self.povorot[0]==False:
            time.sleep(StepTime)
            self.povorot[0]=True
            print('pov')
        elif self.startcord[1]==len(mapRob)-1 and self.povorot[1]==False:
            time.sleep(StepTime)
            self.povorot[1]=True
            print('shit')
        elif self.startcord[0]==0 and (self.startcord[1]==0 or self.startcord[1]==len(mapRob)-1):
            time.sleep(StepTime)
            print('gg')
    def GorStep(self,mapRob,canvas):
        if self.startcord[0]==self.finalcord[0]:
            if self.startcord[1]!=self.finalcord[1]:
                if mapRob[self.startcord[0]][self.startcord[1]+1]==0:
                    mapRob[self.startcord[0]][self.startcord[1] + 1]=self.id
                    mapRob[self.startcord[0]][self.startcord[1]]=0
                    self.startcord[1]+=1
                    for k in range(0, 60):
                        canvas.move(self.id, 1, 0)
                        tk.update()
                        time.sleep(0.005)
                else:
                    time.sleep(StepTime)
                    print('cl;;se')
    def Fuckgobackgor(self,mapRob,canvas):
        if self.startcord[1]+1!=len(mapRob) and self.startcord[0]!=0:
            if mapRob[self.startcord[0]][self.startcord[1]+1]==0:
                mapRob[self.startcord[0]][self.startcord[1] + 1]=self.id
                mapRob[self.startcord[0]][self.startcord[1]] =0
                self.startcord[1]+=1
                for k in range(0, 60):
                    canvas.move(self.id, 1, 0)
                    tk.update()
                    time.sleep(0.001)
            else:
                time.sleep(StepTime)
                print('CLOSE')
    def Fuckgobackvert(self,mapRob,canvas):
        if self.startcord[0]!=0 and self.startcord[1]==len(mapRob)-1:
            if mapRob[self.startcord[0]-1][len(mapRob)-1]==0:
                mapRob[self.startcord[0]-1][len(mapRob)-1]=self.id
                mapRob[self.startcord[0]][len(mapRob) - 1] =0
                self.startcord[0]-=1
                for k in range(0, 60):
                    canvas.move(self.id, 0, -1)
                    tk.update()
                    time.sleep(0.005)
            else:
                time.sleep(StepTime)
                print('CLOSE')
    def final(self,mapRob,canvas):
        if self.startcord[0]==0 and self.startcord[1]!=0:
            if mapRob[self.startcord[0]][self.startcord[1]-1]==0:
                mapRob[self.startcord[0]][self.startcord[1] - 1] =self.id
                mapRob[self.startcord[0]][self.startcord[1]] =0
                self.startcord[1]-=1
                for k in range(0, 60):
                    canvas.move(self.id, -1, 0)
                    tk.update()
                    time.sleep(0.005)
    def cikl(self,mapRob,canvas):
        if self.delivered==False:
            self.start(mapRob,canvas)
            self.VertStep(mapRob,canvas)

            self.GorStep(mapRob,canvas)
        if mapRob[self.finalcord[0]][self.finalcord[1]]==self.id:
            self.delivered=True
            time.sleep(StepTime)
            print('del')
        if self.delivered==True:
            self.Fuckgobackgor(mapRob,canvas)

            self.Fuckgobackvert(mapRob,canvas)

            self.final(mapRob,canvas)

tk=Tk()

canvas=Canvas(tk, width=k*60, height=k*60)
canvas.pack()

for i in range(10):
    canvas.create_line(b,10,b,(k-1)*60+10)
    b+=60
for i in range(10):
    canvas.create_line(10,a,(k-1)*60+10,a)
    a+=60

rob=Robot(canvas)

while rob.delivered!=True:
    rob.cikl(mapRob,canvas)

    for i in range(10):
        print(mapRob[i])
    tk.update()
tk.mainloop()