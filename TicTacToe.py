#Tic-Tac-Toe
import random,time
grid=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
free=[-1,-1,-1,-1,-1,-1,-1,-1,-1]

def printboard(move=0):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==-1:
                if move==0:
                    print(i*3+j+1,end=" ")
                else:
                    print(" ",end=" ")
            elif grid[i][j]==1:
                print("O",end=" ")
            else:
                print("X",end=" ")

            if ((i*3)+j+1)%3!=0:
                print("|",end=" ")
        if i<2:
            print("\n--+---+--")
        else:
            print()
    print()

def user_turn():
    place=int(input())-1
    if (free[place]==-1):
        grid[place//3][place%3]=1
        free[place]=1
        # print(grid)
    elif free[place]==1 or free[place]==2:
        print("Invalid Input ,try again...")
        user_turn()

def opponent_logic():
    possibility=[]
    for i in range(len(grid)):

        if grid[i][0]==grid[i][1]==1 or grid[i][0]==grid[i][1]==2:
            possibility.append(i*3+3)
        if grid[i][0]==grid[i][2]==1 or grid[i][0]==grid[i][2]==2:
            possibility.append(i*3+2)
        if  grid[i][1]==grid[i][2]==1 or grid[i][1]==grid[i][2]==2:
            possibility.append(i*3+1)
        if grid[0][i]==grid[1][i]==1 or grid[0][i]==grid[1][i]==2:
            possibility.append(7+i)
        if grid[0][i]==grid[2][i]==1 or grid[0][i]==grid[2][i]==2:
            possibility.append(4+i)
        if grid[1][i]==grid[2][i]==1 or grid[1][i]==grid[2][i]==2:
            possibility.append(1+i)
    if grid[0][0]==grid[1][1]==1 or grid[0][0]==grid[1][1]==2:
        possibility.append(9)
    if grid[1][1]==grid[2][2]==1 or grid[1][1]==grid[2][2]==2:
        possibility.append(1)
    if grid[0][2]==grid[1][1]==1 or grid[0][2]==grid[1][1]==2:
        possibility.append(7)
    if grid[1][1]==grid[2][0]==1 or grid[1][1]==grid[2][0]==2:
        possibility.append(3)
    if (free[4]==-1):
        possibility.append(5)
    
    return opponent_turn(possibility)

def opponent_turn(possibility):
    possibility=list(filter(lambda x:free[x-1]==-1,possibility))
    
    if len(possibility):
        if difficulty=="H": 
            turn =possibility[0]-1
            possibility.pop(0)
        elif difficulty=="M":
            possibility+=random.sample([i for i in range(len(free)) if free[i]==-1],2)
            turn =random.choice(possibility[0:len(possibility)//2])-1
        elif difficulty=="E":
            possibility+=[i for i in range(len(free)) if free[i]==-1]
            turn =random.choice(possibility)-1
    else:
        turn =random.randint(0,8)



    if free[turn]==-1:
        grid[turn//3][turn%3]=2
        free[turn]=2
    elif free[turn]==1 or free[turn]==2:
        opponent_turn(possibility)
def check_win():
    win=False
    for i in range(len(grid)):
        if grid[i][0]==grid[i][1]==grid[i][2]==1:
            win=True
        if grid[0][i]==grid[1][i]==grid[2][i]==1:
            win=True
        if grid[0][0]==grid[1][1]==grid[2][2]==1 or grid[0][2]==grid[1][1]==grid[2][0]==1:
            win=True
    return win

def check_lose():
    lose=False
    for i in range(len(grid)):
        if grid[i][0]==grid[i][1]==grid[i][2]==2:
            lose=True
        if grid[0][i]==grid[1][i]==grid[2][i]==2:
            lose=True
        if grid[0][0]==grid[1][1]==grid[2][2]==2 or grid[0][2]==grid[1][1]==grid[2][0]==2:
            lose=True
    return lose

print("You are O, your opponent is X\nChoose difficulty [Easy (E) ,Medium (M) ,Hard (H)]")
difficulty=input().upper()
while difficulty not in ["E","H","M"]:
    print("Invalid difficulty setting ,choose from E, M, H")

printboard()
print("These are the indexes for playing ,Enter your number to start...")
while (-1 in free):
    time.sleep(1)
    printboard(1)
    user_turn()
    
    if (-1 not in free):
        printboard(1)
        print("It's a Tie !");
        break;
    
    if (check_win()):
        printboard(1)
        print("You WIN")
        break
    printboard(1)
    print("Opponent's Turn...")
    time.sleep(0.5)
    opponent_logic()
    if (check_lose()):
        printboard(1)
        print("You LOST")
        break
