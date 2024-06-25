from processo import Processo
import random

def TaskGen(n):

    tasks = []

    for x in range(n):
        nome = f"P{x}"
        inst = random.randint(1, 7)
        prio = random.randint(1, 10)
        p = Processo(nome, prio, inst)
        tasks.append(p)

    return tasks