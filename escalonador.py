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
    quantum = 20 # ms
    startTime = 0
    toExec = True
    Terminados = []
    
    i = 0
    j = 0

    for t in task_vector:
        print(t.tempoDeCpu)
    

    toExecVct = toExecFilter(task_vector)
      # lista de lista de tuples
    index = toExecVct.__len__() 
    #InterGannts = []
    InterGannts = [[] for _ in range(index)]
    while toExec:
        for task in toExecVct:
            if task.getReady():
                i %= index # diz qual processo esta sendo trabalhado
                aux = task.exec_rr(quantum, startTime) # retorna uma lista de tuplas ou falso
                if task.__str__() not in v_n:
                    v_n.append(task.__str__())
                startTime += quantum
                #toExecVct = toExecFilter(toExecVct)
                if aux != False:
                    InterGannts[i].append(aux)
            i += 1

        if EndChecker(toExecVct):
            toExec = False
        

    RRGrafico(v_n, InterGannts, 350)

   

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

def toTermFilter(V): 
    Vector = []
    for task in V:
        if task.status == "TERMINADO":
            Vector.append(task)
    return Vector

def EndChecker(V): 
    for task in V:
        if task.status == "PRONTO":
            return False
    return True
