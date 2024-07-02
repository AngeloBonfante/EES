from processo import Processo
from escalonador import EscalonadorFCFS, EscalonadorSJF, EscalonadorPrioridade, EscalonadorRR
from taskgen import TaskGen
from plotter import RRGrafico


task_vector = TaskGen(0)
#task_vector = []

pX = Processo("A", 0, 5)
pY = Processo("B", 0, 1)
pZ= Processo("C", 0, 7)
task_vector.append(pX)
task_vector.append(pY)
task_vector.append(pZ)


#EscalonadorSJF(task_vector)
#EscalonadorPrioridade(task_vector)
EscalonadorRR(task_vector)
EscalonadorFCFS(task_vector)
