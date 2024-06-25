from processo import Processo
from escalonador import EscalonadorFCFS, EscalonadorSJF, EscalonadorPrioridade, EscalonadorRR
from taskgen import TaskGen


task_vector = TaskGen(10)

 
#EscalonadorFCFS(task_vector)
#EscalonadorSJF(task_vector)
#EscalonadorPrioridade(task_vector)
EscalonadorRR(task_vector)
