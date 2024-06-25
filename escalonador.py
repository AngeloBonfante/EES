from plotter import Grafico, RRGrafico

v_n = [] # VETOR NOME E TEMPO
v_t = [] 



def EscalonadorFCFS (task_vector): #FCFS
    
    for task in task_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())

    Grafico(v_t, v_n, "FCFS")
    return

def EscalonadorSJF (task_vector): #SJF
    sorted_vector = Sorter(task_vector, 0)
    for task in sorted_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())

    Grafico(v_t,v_n,"SJF")
    return


def EscalonadorPrioridade (task_vector):
    sorted_vector = Sorter(task_vector, 1)
    for task in sorted_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())
    Grafico(v_t,v_n,"PRIORIDADE")
    return

def EscalonadorRR (task_vector):
    v_t_start = []
    v_t_end = []
    quantum = 20 # ms
    toExec = True
    for t in task_vector:
        print(t.tempoDeCpu)
    toExecVct = toExecFilter(task_vector)


    while toExec:
        i = 0
        for task in toExecVct:
            task.exec_rr(quantum)
            v_n.append(task.__str__())
            v_t.append(task.getTime())
            
        toExecVct = toExecFilter(task_vector)
        
        if toExecVct.__len__() == 0:
            toExec = False 
        i += 1

    RRGrafico(v_t_start,v_t_end, v_n)

   

    return



def Sorter(t_v, tipo):

    sorted_t_v = []
    

    if tipo == 0:
        sorted_t_v = sorted(t_v,key=lambda task: task.tempoDeCpu)
    if tipo == 1:
        sorted_t_v = sorted(t_v,key=lambda task: task.prioridade)

    return sorted_t_v

def toExecFilter(V): 
    Vector = []
    for task in V:
        if task.status == "PRONTO":
            Vector.append(task)
    return Vector
            
