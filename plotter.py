import matplotlib.pyplot as pp
import numpy as np
import time





def Grafico(vetor_tempo, vetor_nomes, tt):
    y = np.array(vetor_tempo)
    lbl = vetor_nomes
    pp.pie(y, labels=lbl, startangle=90, counterclock=False)
    pp.title(tt)
    pp.show()

    pp.clf()
    pp.close()
    
    return

def GraficoGannt(v_n, gannt, maxTime):


   

    fig, gnt = pp.subplots()
    gnt.set_ylim(0, (gannt.__len__() * 10) + 15)
    gnt.set_xlim(0, maxTime + 20)
    gnt.xaxis.set_units("ms")
    gnt.set_xlabel('tempo')
    gnt.set_ylabel('processos')
    x = v_n.__len__()
    tickList = []
    for y in range(x):
        tickList.append((15 + (10 * y)))
    gnt.set_yticks(tickList)
    gnt.set_yticklabels(v_n)
    gnt.grid(True)

    colors = np.random.rand(x, 3)
    
    for y in range(x):
        if y < len(gannt):
            gnt.broken_barh(gannt[y][0], (10 * (y + 1), 10), facecolors =colors[y])            
   
    pp.show()
    pp.clf()
    pp.close()
    return

def RRGrafico(v_n, gannt, maxTime): # https://www.geeksforgeeks.org/python-basic-gantt-chart-using-matplotlib/
   
    # Declaring a figure "gnt"
    fig, gnt = pp.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, (gannt.__len__() * 10) + 15)
    
    # Setting X-axis limits
    gnt.set_xlim(0, maxTime + 20)
    gnt.xaxis.set_units("ms")
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('tempo')
    gnt.set_ylabel('processos')
    
    # Setting ticks on y-axis
    x = v_n.__len__()
    tickList = []
    for y in range(x):
        tickList.append((15 + (10 * y)))


    gnt.set_yticks(tickList)
    # Labelling tickes of y-axis
    gnt.set_yticklabels(v_n)
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    #[(startsAt, EndAtPlus)] (posx lenghty)
    colors = np.random.rand(x, 3)
    for y in range(x):
        if y < len(gannt):
            gnt.broken_barh(gannt[y][0], (10 * (y + 1), 10), facecolors =colors[y])            
    #pp.savefig('gantt.jpg')
    pp.savefig('gantt.png')
    print("Show(rr)")
    pp.show()
    

def r():
    
    GraficoGannt(["a", "b"], [ [ [(0, 20)] ],[ [(20,40)] ] ], 90)
    return



    
       
    
   


