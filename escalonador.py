from plotter import Grafico, RRGrafico, GraficoGannt

#v_n = [] # VETOR NOME E TEMPO
#v_t = [] 

troca_de_contexto = 1 # ms



def EscalonadorFCFS (task_vector): #FCFS
    
    startTime = 0
    id = task_vector.__len__()
    i = 0
    gannt =  [[] for _ in range(id)]
    maxtime = 0
    readyArrival = [0 for _ in range(id)]

    ready_vector = task_vector[:]
    v_n = [] 
    v_t = [] 
    for task in ready_vector:
        task.reset_Gannt()
        aux = task.exec(startTime)
        v_n.append(task.__str__())
        v_t.append(task.getTime())
        startTime += task.getTime()
        gannt[i].append(aux)
        readyArrival[i] = task.getReadyVecArrival()
        maxtime += task.getTime()
        i += 1


    #Grafico(v_t, v_n, "FCFS")
    GraficoGannt(v_n, gannt, maxtime, readyArrival, True)
    return

def EscalonadorSJF (task_vector, concurrency, preemptive): #SJF

    startTime = 0
    id = task_vector.__len__()
    i = 0
    gannt2 =  [[] for _ in range(id)]
    maxtime = 0
    readyArrival = [0 for _ in range(id)]

    ready_vector = task_vector[:]
    v_n = [] 
    v_t = []
    

    if concurrency:
        sorted_vector = ConcurrentSorter(ready_vector)
    else:
        sorted_vector = Sorter(ready_vector, 0)

    for task in sorted_vector:
        task.reset_Gannt()
        aux = task.exec(startTime)
        v_n.append(task.__str__())
        v_t.append(task.getTime())
        startTime += task.getTime()
        gannt2[i].append(aux)
        readyArrival[i] = task.getReadyVecArrival()
        maxtime += task.getTime()
        i += 1

    #Grafico(v_t,v_n,"SJF")
    GraficoGannt(v_n, gannt2, maxtime, readyArrival, concurrency)
    
    return







def EscalonadorPrioridade (task_vector):
    startTime = 0
    id = task_vector.__len__()
    i = 0
    gannt2 =  [[] for _ in range(id)]
    maxtime = 0


    ready_vector = task_vector[:]
    v_n = [] 
    v_t = []
    sorted_vector = Sorter(ready_vector, 1)
    for task in sorted_vector:
        task.reset_Gannt()
        aux = task.exec(startTime)
        v_n.append(task.__str__())
        v_t.append(task.getTime())
        startTime += task.getTime()
        gannt2[i].append(aux)
        maxtime += task.getTime()
        i += 1


    #Grafico(v_t,v_n,"PRIORIDADE")
    GraficoGannt(v_n, gannt2, maxtime)

    return

def EscalonadorRR (task_vector, quantum, dyq):
    ready_vector = task_vector.copy()
    v_n = [] 
    startTime = 0
    toExec = True
    maxTime = 0
    run = 0
    metric = []
    throughput = 0
    i = 0
    p = 0


    for t in ready_vector:
        print(t.tempoDeCpu)
    

    toExecVct = toExecFilter(ready_vector)
    for task in toExecVct:
        maxTime += task.tempoDeCpu 
        task.reset_Gannt()

    index = toExecVct.__len__() 
    #InterGannts = []
    InterGannts = [[] for _ in range(index)] # lista de lista de tuples
    while toExec:
        for task in toExecVct:
            if task.getReady():
                i %= index # diz qual processo esta sendo trabalhado
                aux = task.exec_rr(quantum, startTime, run, dyq) # retorna uma lista de tuplas ou falso
                run += 1
                if task.__str__() not in v_n:
                    v_n.append(task.__str__())

                if dyq:
                    startTime += task.getQuantum()
                else:
                    startTime += quantum

                if aux != False:
                    InterGannts[i].append(aux)
                
                if task.getFinished():
                    metric.append(task.getMetric())
                    p += 1
                
            i += 1

        if EndChecker(toExecVct):
            toExec = False
        
    throughput += p / startTime
    RRGrafico(v_n, InterGannts, maxTime, metric, throughput)

   

    return




def Sorter(t_v, tipo):

    sorted_t_v = []
    

    if tipo == 0:
        sorted_t_v = sorted(t_v,key=lambda task: task.tempoDeCpu)
    if tipo == 1:
        sorted_t_v = sorted(t_v,key=lambda task: task.prioridade)

    return sorted_t_v


def ConcurrentSorter(tasks):

    if tasks.__len__() == 0:
        return
    
    sortedTasks = []
    temp = []

    # copy tasks to deepcopy list
    auxTasks = tasks.copy()

    for task in auxTasks:

        if auxTasks.__len__() == 0:
            return 

        cputime = task.getTime()
        len = auxTasks.__len__()
        markedForRemoval = []
        name = task.__str__() 
        normalizationArrivalTime = auxTasks[0].getVecArrivalTime()

        for i in range(len):
            if auxTasks[i].getVecArrivalTime() <= cputime + normalizationArrivalTime:
                temp.append(auxTasks[i])
                markedForRemoval.append(auxTasks[i])
        
        for i in markedForRemoval:
            auxTasks.remove(i)

        temp = sorted(temp, key=lambda task: task.getTime()) 
        # remove from temp task with name
        for i in temp:
            if i.__str__() == name:
                temp.remove(i)
        
        sortedTasks.append(tasks[0])
        sortedTasks.extend(temp)
        
        #sortedTasks.extend(ConcurrentSorter(auxTasks))
        auxTasks = sorted(auxTasks, key=lambda task: task.getVecArrivalTime())
        if auxTasks.__len__() != 0:
            rtn = ConcurrentSorter(auxTasks)
            sortedTasks.extend(rtn)

        break
        



    #sortedTasks = sorted(temp, key=lambda task: task.getTime()) # sort by time
    #sortedTasks.append(ConcurrentSorter(auxTasks))
    

    return sortedTasks
        
   

    

            


   
   
            
        




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
