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

def GraficoGannt(v_n, gannt, taskCpuArrival, opt):


    maxTime = gannt[-1][0][-1][0] + gannt[-1][0][-1][1]
   

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

        if y > 0 and opt:
            gnt.broken_barh(taskCpuArrival[y][0], (10 * (y + 1), 10), facecolors ="black")   


        if y < len(gannt):
            gnt.broken_barh(gannt[y][0], (10 * (y + 1), 10), facecolors =colors[y])            
   
    pp.show()
    pp.clf()
    pp.close()
    return

def RRGrafico(v_n, gannt, maxTime, metrics, throughput): # https://www.geeksforgeeks.org/python-basic-gantt-chart-using-matplotlib/
   


    maxTim = gannt[-1][0][-1][0] + gannt[-1][0][-1][1] + 100


    # Declaring a figure "gnt"
    fig, gnt = pp.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(-10, (gannt.__len__() * 10) + 15)
    
    # Setting X-axis limits
    gnt.set_xlim(0, maxTim)
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
    
    a = turnaround(metrics)

    pp.text(2, 2, f"TURNAROUND: {a} ms", fontsize=10)
    pp.text(2, 4, f"THROUGHPUT: {round(throughput, 2)} Insts", fontsize=10)

    print(maxTim)
    print(gannt[-1][0][-1][0] + gannt[-1][0][-1][1])


    pp.savefig('gantt.png')
    
    pp.show()
    

def r():
    
    GraficoGannt(["a", "b"], [ [ [(0, 20)] ],[ [(20,40)] ] ], 90)
    return



def turnaround(data):
    avg = []
    for x in data:
        start = x[0]
        end = x[1]
        turnaround = end - start
        avg.append(turnaround)
    
    return sum(avg) / len(avg)



       
    
   


