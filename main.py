from processo import Processo
from escalonador import EscalonadorFCFS, EscalonadorSJF, EscalonadorPrioridade, EscalonadorRR
from taskgen import TaskGen


task_vector = TaskGen(0)
#task_vector = []

p1 = Processo("p1", 0, 2)
p2 = Processo("p2", 0, 15)
p3= Processo("p3", 0, 5)
task_vector.append(p1)
task_vector.append(p2)
task_vector.append(p3)

#EscalonadorFCFS(task_vector)
#EscalonadorSJF(task_vector)
#EscalonadorPrioridade(task_vector)
EscalonadorRR(task_vector)
