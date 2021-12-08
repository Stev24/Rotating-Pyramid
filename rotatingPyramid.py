import math
import curses
import time

w = curses.initscr()

height = 2
rayon = 3
K2 = 5
screen_width = 61
K1 = screen_width*K2*3/(8*(rayon))
mx = round(screen_width/2)

rows, cols = (31, screen_width)

arrayOfChar = [".",",",":",";","=","#","@"] # 0 - 6

#w = curses.newwin(25,100,0,0)
#print("zMax:", curses.LINES)  
#print("xMax:", curses.COLS)

def curses_main(w):
    for B in range(1000):
        #time.sleep(0.04)
        w.erase()
        B = B*math.pi/180

        arr = [[' ' for x in range(cols)] for y in range(rows)]
        arrOFBrightness = [[ 0 for x in range(cols)] for y in range(rows)]

        steps = 20
        for step in range(steps+1):
            z = height/steps*step
            R = (z-height)*rayon/(-height)

            
            for k in range(4):
                Omega1 = math.pi/4+k*math.pi/2


                for i in range(31):
                    Omega2 =  ((3*math.pi/4-math.pi/4)/30)*i + math.pi/4 + k*math.pi/2

                    if ( k == 0 or k == 2 ) :
                        x = R*math.sin(Omega1)*( (math.cos(Omega2)/math.sin(Omega2))*math.cos(B) - math.sin(B))
                        y = R*math.sin(Omega1)*( (math.cos(Omega2)/math.sin(Omega2))*math.sin(B) + math.cos(B))
                        if (k==0) : 
                            L = (height/rayon)*math.sqrt(2)*math.cos(B)+1
                        elif ( k ==2) : 
                            L = (-height/rayon)*math.sqrt(2)*math.cos(B)+1
                    else:
                        x = R*math.cos(Omega1)*(  math.cos(B) - (math.sin(Omega2)/math.cos(Omega2))*math.sin(B) )
                        y = R*math.cos(Omega1)*(  math.sin(B) + (math.sin(Omega2)/math.cos(Omega2))*math.cos(B) )
                        if (k == 1) : 
                            L = (-height/rayon)*math.sqrt(2)*math.sin(B)+1
                        elif ( k == 3) : 
                            L = (height/rayon)*math.sqrt(2)*math.sin(B)+1
                    

                    x = int(round(x*K1/K2))
                    #Brightness = L
                    z1 = int(round(z*K1/K2))
                    if ( arrOFBrightness[rows-z1-2][mx+x] < L):
                        arrOFBrightness[rows-z1-2][mx+x] = L
                    #print("angle",B)
                    #print("k",k, "i",i)
                    
                    #print("Rayon",R)
                    #print(Omega1, Omega2)
                    #print()
                    #x = int(round(x/1.5,10))
                    #z = int(round(z/1.5,10))
                    index = int(round((L/2.5)*6))  # -1.4 , 6
                    #and arrOFdepth[20-z1][15+x] == y
                    if (index >=0 and arrOFBrightness[rows-z1-2][mx+x] == L ):
                        #arr[20-z1][15+x] = arrayOfChar[index]
                        print("Coord: ","x:",x,"y:",y,"z:",z1,"ratio:", K1/K2, "L:", L)
                        #w.addstr(30, 100, ".")
                        w.addstr(rows-z1-10, mx+x+20, arrayOfChar[index])
                        #print("Coord: ","x:",x,"y:",y,"z:",z1,"ratio:", K1/K2, "L:", L)


                

        # output window
        #for r in arr :
        #    for c in r:
        #        print(c,end = "  ")
        #    print()
        #print("", end="")

        w.addstr(20, 80, '')
        w.refresh()
        
    w.getch()

curses.wrapper(curses_main)



