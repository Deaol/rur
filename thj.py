pol = []
for i in range(3):
    pol.append([0]*3)
play = 0
x = 0
y = 0
sit = 0
def win(q):
    tag = 0
    a=0
    for j in range (3):
        if pol[0][j] == pol[1][j] == pol[2][j] != 0:
            tag = 1
    for j in range (3):
        if pol[j][0] == pol[j][1] == pol[j][2] != 0:
            tag = 1
    if pol[0][0] == pol[1][1] == pol[2][2] != 0:
        tag = 1
    elif pol[2][0] == pol[1][1] == pol[0][2] != 0:
        tag = 1
    for i in range(3):
        for j in range(3):
            if pol[i][j] == 0:
                a+=1
    if a==0:
        tag=1
    return tag


def comp():
    global pol
    a=2
    b=2
    tag1=0
    for i in range(2):
        for j in range(1,3):
            if pol[0][i] == pol[0][j] == -1 and pol[0][j-1] == 0:
                if i != j:
                    pol[0][a]=1
                    tag1+=1
                    break
                
                
            if pol[2][i] == pol[2][j] == -1 and pol[2][j-1] == 0:
                if i != j:
                    pol[2][a]=1
                    tag1+=1
                    break
            a-=1
    for i in range(2):
        for j in range(1,3):
            if pol[i][0] == pol[j][0] == -1 and pol[j-1][0] == 0:
                if i != j:
                    pol[b][0]=1
                    tag1+=1
                    break
            
            if pol[i][2] == pol[j][2] == -1 and pol[j-1][2] == 0:
                if i != j:
                    pol[b][2]=1
                    tag1+=1
                    break
            b-=1
    if tag1==0:
        for i in range(3):
            for j in range (3):
                if pol[i][j] ==0:
                    pol[i][j]=1
                    break
            
                

def player():
    global  x, y, pol
    y = int(input('vert'))
    x = int(input('gor'))
    pol[y][x] = -1
def pole():
    for str in pol:
        print(str)

pol[1][1] = 1
player()
if pol[0][1] or pol[1][0] or pol[1][2] or pol[2][1] == -1:                   #ситуэйшен
    sit = 1


for i in range (1):
    if sit == 1:                                           #если изи вин(net)
        pol[0][0] = 1
        pole()
        player()
        if pol[2][2]==0:
            pol[2][2] = 1
            pole()
            print('loser')
            break
        elif (pol[1][0] == -1) or (pol[1][2] == -1):
            pol[0][2] = 1
            pole()
            player()
            if  pol[0][1] == 0:
                pol[0][1] = 1
                pole()
                print('loser')
                break
            else:
                pol[2][0]=1
                pole()
                print('loser')
                break #ситуэйшен2
        else:
            pol[2][0] = 1
            pole()
            player()
            
            if  pol[1][0] == 0:
                pol[1][0] = 1
                pole()
                print('loser')
                break
            else:
                pol[0][2]=1
                pole()
                print('loser')
                break   
    else:
        if pol[0][0]==0:
            pol[0][0]=1
        else:
            pol[0][2]=1
        while play==0:
            pole()
            player()
            comp()
            play=win(pol)
            if play==1:
                print('синк эбаут ит')
                pole()
                break
                
        
    
    
