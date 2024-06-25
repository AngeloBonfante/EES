import time


exec_delay = 10 # millisecond

def delayer(ed, mode):
    if mode == 1:
        time.sleep(ed / 1000.0)
        return
    time.sleep(ed / 1000.0)
    print(f"executed after {ed} ms")
    

class Processo:
    def __init__(self, nome, prioridade, instRestantes):
        self.status = "PRONTO"
        self.nome = nome
        self.prioridade = prioridade
        self.tempoDeCpu = instRestantes * exec_delay
        self.instRestantes = instRestantes
    
    def exec(self):
        print("Executando processo ", self.nome, "Prioridade", self.prioridade)
        delayer(exec_delay * self.instRestantes)
        print("Executado!")
        self.setStatus(3)
        return
    
    def stop(self):
        print("Parando processo ", self.nome)
        return
    
    def __str__(self):
        return self.nome
    
    def getTime(self):
        return self.instRestantes * exec_delay
    
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
    
    def exec_rr(self, q):
        print("Executando processo ", self.nome)

        if self.tempoDeCpu <= 0: # Processo terminou
            self.setStatus(3)
            return
        if self.tempoDeCpu > 0: 
            self.tempoDeCpu -= q
            delayer(q, 1) # executa por q ms
            self.setStatus(0)
            return
            


        print("Executado!")
        return
