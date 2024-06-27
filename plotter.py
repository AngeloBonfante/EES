import matplotlib.pyplot as pp
import numpy as np

def Grafico(vetor_tempo, vetor_nomes, tt):

    y = np.array(vetor_tempo)
    lbl = vetor_nomes
    pp.pie(y, labels=lbl, startangle=90, counterclock=False)
    pp.title(tt)
    pp.show()

    return

def RRGrafico(v_n, gannt, maxTime): # https://www.geeksforgeeks.org/python-basic-gantt-chart-using-matplotlib/
    
    # Declaring a figure "gnt"
    fig, gnt = pp.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, gannt.__len__() * 10)
    
    # Setting X-axis limits
    gnt.set_xlim(0, maxTime + 20)
    
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

    for y in range(x):
        if y < len(gannt):
            gnt.broken_barh(gannt[y][0], (10 * (y + 1), 9), facecolors =('tab:orange'))            
    #pp.savefig('gantt.jpg')
    pp.savefig('gantt.png')
    pp.show()

