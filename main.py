from processo import Processo
from escalonador import EscalonadorFCFS, EscalonadorSJF, EscalonadorPrioridade, EscalonadorRR
from taskgen import TaskGen


task_vector = TaskGen(10)
#task_vector = []

pX = Processo("A", 0, 10)
pY = Processo("B", 0, 15)
pZ= Processo("C", 0, 5)
task_vector.append(pX)
task_vector.append(pY)
task_vector.append(pZ)

#EscalonadorFCFS(task_vector)
#EscalonadorSJF(task_vector)
#EscalonadorPrioridade(task_vector)
EscalonadorRR(task_vector)
