import math
import matplotlib.pyplot as plt 
#taking inpot for the starting and ending of the graph.
start = int (input('for where do u want to satrt the graph: '))
end = int(input('where do you want to end your graph: '))
i = start

pi = math.pi

sinl = []
cosl = []
il =[]
#making a list of sinx cosx and angle 
while i < end:
    x = i*(pi/180)
    sinx = math.sin(x)
    tanx = math.tan(x)
    if x%(2*pi) == 0:
    	cosx = 1
    elif x%(2*pi) == pi:
    	cosx = -1
    else:
    	cosx = sinx/tanx

    sinl.append(sinx)
    cosl.append(cosx)
    il.append(i)
    i += 1

#loting bot the sinx and cosx graph one at a time using same axis
plt.plot(il, sinl)
plt.plot(il, cosl)
#labeling the axis and the graph
plt.xlabel('X')
plt.ylabel('sinX and casXx')
    
plt.title("sinx n cosx  graph")

#print graph
plt.show()