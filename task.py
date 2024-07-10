


class Task:
    def __init__(self, process_id, burst_time, priority, ready_queue_arrival_time):
        # Para execução
        self.pID = process_id
        self.priority = priority
        self.cpu_burst_time = burst_time
        self.start = False

        # Para o gráfico
        self.time_intervals = [] 

        # Para o algoritmo de escalonamento
        self.exec_start_time = None
        self.exec_end_time = None
        self.ready_queue_arrival_time = ready_queue_arrival_time
        
        
    # retorna o intervalo de tempo que esse processo levou para ser executado
    #start_time é o quando o processo começa a ser executado
    def run(self, start_time):
        aux = False
        self.exec_start_time = start_time
        if start_time < self.ready_queue_arrival_time[0][0][0]:
            self.time_intervals.append((self.ready_queue_arrival_time[0][0][0], self.cpu_burst_time))
            aux = True
            return (self.time_intervals, aux)
        self.time_intervals.append((start_time, self.cpu_burst_time))
        return (self.time_intervals, aux)

    def __str__(self):
        return 'Task: %s' % self.pID
    
    def run_round_robin(self, start_time, quantum_standard, dynamic_quantum):

        final_exec = False
        global quantum
        quantum = quantum_standard

        # checa se o processo terminou
        def burst_end_check(self):
            if self.cpu_burst_time <= 0:
                return True
            else:
                return False
            
        if self.cpu_burst_time <= 0:
            return 
        

        # processo chegou antes de chegar na fila de prontos
        early = False
        #if start_time < self.ready_queue_arrival_time[0][0][0]:
            #early = True
            
           

    
        # processo foi executado pela primeira vez
        if self.start == False:
            self.start = True
            self.exec_start_time = start_time # + overhead

        # checar se o quantum vai ser dinâmico, também implica que essa vai ser a execução final
        if dynamic_quantum == True and self.cpu_burst_time <= quantum:
            quantum = self.cpu_burst_time
            final_exec = True

        

        # começar execução
        self.cpu_burst_time -= quantum
        if early:
            self.time_intervals.append((self.ready_queue_arrival_time[0][0][0], quantum))
        else:
            self.time_intervals.append((start_time, quantum))


        # programa acabou de executar
        if burst_end_check(self) == True:
            final_exec = True
            self.exec_end_time = start_time + quantum
            return (self.time_intervals, early)


        # programa ainda não acabou de executar
        return (False, early)
        
    
    def getQuantum(self):
        return quantum

    def get_ready_queue_arrival_time(self):
        return self.ready_queue_arrival_time
    
    def getMetric(self):
        if self.time_intervals.__len__() <= 1:
            return (self.exec_start_time, self.exec_end_time)
        else:
            return (self.time_intervals[0][0], self.time_intervals[-1][0] + self.time_intervals[-1][1])


    def resetIntervals(self):
        self.time_intervals = []
        return
    
    def getStartEnd(self):
        return (self.exec_start_time, self.exec_end_time)
        



        
        

