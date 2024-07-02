from plotter import Grafico, RRGrafico, pp

#v_n = [] # VETOR NOME E TEMPO
#v_t = [] 

troca_de_contexto = 1 # ms



def EscalonadorFCFS (task_vector): #FCFS
    ready_vector = task_vector[:]
    v_n = [] 
    v_t = [] 
    for task in ready_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())

    Grafico(v_t, v_n, "FCFS")
    return

def EscalonadorSJF (task_vector): #SJF
    ready_vector = task_vector[:]
    v_n = [] 
    v_t = []
    sorted_vector = Sorter(ready_vector, 0)
    for task in sorted_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())

    Grafico(v_t,v_n,"SJF")
    return


def EscalonadorPrioridade (task_vector):
    ready_vector = task_vector[:]
    v_n = [] 
    v_t = []
    sorted_vector = Sorter(ready_vector, 1)
    for task in sorted_vector:
        task.exec()
        v_n.append(task.__str__())
        v_t.append(task.getTime())
    Grafico(v_t,v_n,"PRIORIDADE")
    return

def EscalonadorRR (task_vector):
    ready_vector = task_vector.copy()
    v_n = [] 
    quantum = 20 # ms
    startTime = 0
    toExec = True
    maxTime = 0
    run = 0
    
    i = 0
    

    for t in ready_vector:
        print(t.tempoDeCpu)
    

    toExecVct = toExecFilter(ready_vector)
    for task in toExecVct:
        maxTime += task.tempoDeCpu

    index = toExecVct.__len__() 
    #InterGannts = []
    InterGannts = [[] for _ in range(index)] # lista de lista de tuples
    while toExec:
        for task in toExecVct:
            if task.getReady():
                i %= index # diz qual processo esta sendo trabalhado
                aux = task.exec_rr(quantum, startTime, run) # retorna uma lista de tuplas ou falso
                run += 1
                if task.__str__() not in v_n:
                    v_n.append(task.__str__())
                startTime += quantum
                if aux != False:
                    InterGannts[i].append(aux)
                    
            i += 1

        if EndChecker(toExecVct):
            toExec = False
        
    print("RRG STARTED")
    RRGrafico(v_n, InterGannts, maxTime)

   

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
