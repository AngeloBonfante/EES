from processo import Processo
import random

def TaskGen(n, rgn):

    tasks = []

    for x in range(n):
        nome = f"P{x}"
        inst = random.randint(1, rgn)
        prio = random.randint(1, 6)
        p = Processo(nome, prio, inst)
        tasks.append(p)

    return tasks