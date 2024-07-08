import task
from plotter import GraficoGannt, RRGrafico

# ESCALONADORES RECEBEM UMA LISTA DE PROCESSOS, NAO CONFUNDIR COM A LISTA DE PRONTOS


# Faz o sort com base na ordem de chegada na lista de prontos
def ready_queue(tasks):
    return sorted(tasks, key=lambda x: x.get_ready_queue_arrival_time()) 


def EscalonadorFCFS (tasks):
    queue = ready_queue(tasks)

    start_time = 0
    aux = 0
    intervals = []
    ready_queue_arrival_times = []

    pIDs = []
    burst_times = []

    for task in queue:
        task.resetIntervals()

        interval = task.run(start_time)
        intervals.append([interval[0]])
        start_time_adjustment = interval[1]

        pIDs.append(task.pID)
        burst_times.append(task.cpu_burst_time)

        ready_queue_arrival_times.append([(task.ready_queue_arrival_time, 4)])

        if (start_time_adjustment):
            start_time += task.ready_queue_arrival_time[0][0][0]
        start_time += task.cpu_burst_time

    GraficoGannt(pIDs, intervals, ready_queue_arrival_times, False)
        
def SJF_Sorter(queue):
    sorted_queue = []
    remaining = []
    last_end_time = 999999
    for task in queue:
        if task.ready_queue_arrival_time[0][0][0] <= last_end_time:
            sorted_queue.append(task)
            last_end_time = task.ready_queue_arrival_time[0][0][0] + task.cpu_burst_time
        else:
            remaining.append(task)
    temp = []
    temp.append(sorted_queue[0])
    sorted_queue.remove(sorted_queue[0])
    sorted_queue = sorted(sorted_queue, key=lambda x: x.cpu_burst_time)
    temp.extend(sorted_queue)
    sorted_queue = temp

    if remaining != []:
        sorted_queue += SJF_Sorter(remaining)
    return sorted_queue

def EscalonadorSJF(tasks):
    queue = ready_queue(tasks)

    start_time = 0
    aux = 0
    intervals = []
    ready_queue_arrival_times = []

    pIDs = []
    sjf_queue = []

    sjf_queue = SJF_Sorter(queue)
    
    ################################ EXECUÇÃO ################################
    for task in sjf_queue:
        task.resetIntervals()
        interval = task.run(start_time)
        intervals.append([interval[0]])
        start_time_adjustment = interval[1]

        pIDs.append(task.pID)

        ready_queue_arrival_times.append([(task.ready_queue_arrival_time, 4)])

        if (start_time_adjustment):
            start_time = 0
            start_time += task.ready_queue_arrival_time[0][0][0] + task.cpu_burst_time
        else:
            start_time += task.cpu_burst_time

    GraficoGannt(pIDs, intervals, ready_queue_arrival_times, False)


    return


def Prio_Sorter(queue):
    sorted_queue = []
    remaining = []
    last_end_time = 999999
    for task in queue:
        
        if task.ready_queue_arrival_time[0][0][0] <= last_end_time:
            sorted_queue.append(task)
            last_end_time = task.ready_queue_arrival_time[0][0][0] + task.cpu_burst_time
        else:
            remaining.append(task)
    temp = []
    temp.append(sorted_queue[0])
    sorted_queue.remove(sorted_queue[0])
    sorted_queue = sorted(sorted_queue, key=lambda x: x.priority)
    temp.extend(sorted_queue)
    sorted_queue = temp

    if remaining != []:
        sorted_queue += SJF_Sorter(remaining)
    return sorted_queue



def EscalonadorPrioridade(tasks):

    queue = ready_queue(tasks)

    start_time = 0
    aux = 0
    intervals = []
    ready_queue_arrival_times = []

    pIDs = []
    prio_queue = []

    prio_queue = Prio_Sorter(queue)
    
    ################################ EXECUÇÃO ################################
    for task in prio_queue:
        task.resetIntervals()
        interval = task.run(start_time)
        intervals.append([interval[0]])
        start_time_adjustment = interval[1]

        pIDs.append(task.pID)

        ready_queue_arrival_times.append([(task.ready_queue_arrival_time, 4)])

        if (start_time_adjustment):
            start_time = 0
            start_time += task.ready_queue_arrival_time[0][0][0] + task.cpu_burst_time
        else:
            start_time += task.cpu_burst_time

    GraficoGannt(pIDs, intervals, ready_queue_arrival_times, False)


    return

def EscalonadorRR(tasks, quantum_size, dynamic_quantum):

    queue = ready_queue(tasks)
    
    start_time = 0
    pIDs = []
    to_exec = True
    run = 0
    metric = []
    throughput = 0
    i = 0
    p = 0


    #reset gannt loop 
    for task in queue:
        task.resetIntervals()

    index = queue.__len__()
    intervals = [[] for _ in range(index)]

    while to_exec:
        for task in queue:
            if task.cpu_burst_time > 0:
                #encontra qual processo esta sendo executado
                i %= index 
                # retorna intervalo ou Falso
                aux = task.run_round_robin(start_time, quantum_size, dynamic_quantum)
                start_time_adjustment = aux[1]
                #if (start_time_adjustment):
                    #start_time += task.ready_queue_arrival_time[0][0][0]
                #else:
                start_time += task.getQuantum()
                aux = aux[0]
                run += 1

                if task.__str__() not in pIDs:
                    pIDs.append(task.__str__())
                
                

                if aux != False:
                    intervals[i].append(aux)

                if task.cpu_burst_time <= 0:
                    metric.append(task.getMetric())
                    p += 1
            i += 1


        if EndChecker(queue):
            to_exec = False

    throughput += p / start_time

    RRGrafico(pIDs, intervals, 1000, metric, throughput)


    return


def EndChecker(V): 
    for task in V:
        if task.cpu_burst_time > 0:
            return False
    return True

