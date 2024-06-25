import matplotlib.pyplot as pp
import numpy as np

def Grafico(vetor_tempo, vetor_nomes, tt):

    y = np.array(vetor_tempo)
    lbl = vetor_nomes
    pp.pie(y, labels=lbl, startangle=90, counterclock=False)
    pp.title(tt)
    pp.show()

    return

def RRGrafico(): # https://www.geeksforgeeks.org/python-basic-gantt-chart-using-matplotlib/
    
    # Declaring a figure "gnt"
    fig, gnt = pp.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 50)
    
    # Setting X-axis limits
    gnt.set_xlim(0, 160)
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Processor')
    
    # Setting ticks on y-axis
    gnt.set_yticks([15, 25, 35])
    # Labelling tickes of y-axis
    gnt.set_yticklabels(['1', '2', '3'])
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))
    
    # Declaring multiple bars in at same level and same width
    gnt.broken_barh([(110, 10), (150, 10)], (10, 9),
                            facecolors ='tab:blue')
    
    gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                                    facecolors =('tab:red'))  
   
    pp.show()


RRGrafico()