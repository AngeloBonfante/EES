import time


exec_delay = 20 # millisecond


def delayer(ed):
    time.sleep(ed / 1000.0)
    print(f"executed after {ed} ms")
    

class Processo:
    def __init__(self, nome, prioridade, instRestantes):
        self.status = "PRONTO"
        self.nome = nome
        self.prioridade = prioridade
        self.tempoDeCpu = instRestantes * exec_delay
        self.instRestantes = instRestantes
        self.GanntInt = []
        self.arrivalTime = 0
        self.finishTime = 0
        self.start = False
    
    def exec(self, startTime):
        print("Executando processo ", self.nome, "Prioridade", self.prioridade)
        delayer(exec_delay * self.instRestantes)
        print("Executado!")
        #self.setStatus(3)
        self.GanntInt.append((startTime, exec_delay * self.instRestantes))
        return self.GanntInt
    
    def stop(self):
        print("Parando processo ", self.nome)
        return
    
    def __str__(self):
        return self.nome
    
    def getTime(self):
        return self.instRestantes * exec_delay
    
    def getReady(self):
        if self.status == "PRONTO":
            return True
        return False
    
    def setStatus(self, v):
        if v == 0:
            self.status = "PRONTO"
        if v == 1:
            self.status = "EXEC"
        if v == 2:
            self.status = "ESPERANDO"
        if v == 3:
            self.status = "TERMINADO"
        if v == 4:
            self.status = "NOVO"
            
        return 
    
    def exec_rr(self, quantum, startTime, run, dyq):
        print("Executando processo ", self.nome)

        q = quantum
        global x
        x = 0
        ctx_switch = 0
        ctx_switch = ctx_switch + run
        if self.start == False:
            self.start = True
            self.arrivalTime = startTime + ctx_switch

        
        

        if self.tempoDeCpu <= 0: # Processo terminou
            self.setStatus(3) # terminado
           #adicionar overhead
            return 

        if self.tempoDeCpu > 0:

            if dyq == True and self.tempoDeCpu <= q:
                q = self.tempoDeCpu

            x = q

            self.tempoDeCpu -= q
            self.instRestantes -= int(q / exec_delay)
            delayer(q) # executa por q ms
            if self.tempoDeCpu <= 0: # Processo terminou
                self.setStatus(3) # terminado
                self.finishTime = startTime + q
                self.GanntInt.append(((startTime + ctx_switch), q))
                return self.GanntInt # retorna lista de tuplas
            else:
                self.setStatus(0) # pronto

            self.GanntInt.append(((startTime + ctx_switch), q))
            return False
        
    def getMetric(self):

        if self.GanntInt.__len__() <= 1:
            return (self.arrivalTime, self.finishTime)
        else:
            return (self.GanntInt[0][0], self.GanntInt[-1][0] + self.GanntInt[-1][1])

    def reset_Gannt(self):
        self.GanntInt = []
        return
    
    def getFinished(self):
        if self.status == "TERMINADO":
            return True
        return False

    def getQuantum(self):
        return x
        
