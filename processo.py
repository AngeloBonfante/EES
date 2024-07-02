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
    
    def exec_rr(self, q, startTime, run):
        print("Executando processo ", self.nome)
        ctx_switch = 0
        ctx_switch = ctx_switch + run
        

        if self.tempoDeCpu <= 0: # Processo terminou
            self.setStatus(3) # terminado
           #adicionar overhead
            return 

        if self.tempoDeCpu > 0: 
            self.tempoDeCpu -= q
            self.instRestantes -= (1 * q / exec_delay)
            delayer(q) # executa por q ms
            if self.tempoDeCpu <= 0: # Processo terminou
                self.setStatus(3) # terminado
                self.GanntInt.append(((startTime + ctx_switch), q))
                return self.GanntInt # retorna lista de tuplas
            else:
                self.setStatus(0) # pronto

            self.GanntInt.append(((startTime + ctx_switch), q))
            return False
        

    def reset_Gannt(self):
        self.GanntInt = []
        return
        
    
            

        
