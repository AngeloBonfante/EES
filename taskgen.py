from processo import Processo
import random

def TaskGen(n, rgn):

    tasks = []
    

    for x in range(n):
        nome = f"P{x}"
        inst = random.randint(1, rgn)
        prio = random.randint(1, 6)
        arr = 0 + x * random.randint(0, 50)

        if x == 0:
            taskVecArrival = [[(0, 0)]]
        else:
            taskVecArrival = [[(arr, 4)]]

        p = Processo(nome, prio, inst, taskVecArrival)
        tasks.append(p)

        #sort tasks by taskVecArrival
        tasks = sorted(tasks, key=lambda x: x.readyVecArrival[0][0][0])

    return tasks


def getBasic():
    tasks = []
    taskVecArrival = [[(0, 4)]]
    p = Processo("P0", 1, 5, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(50, 4)]]
    p = Processo("P1", 2, 4, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(100, 4)]]
    p = Processo("P2", 3, 2, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(160, 4)]]
    p = Processo("P3", 4, 2, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(380, 4)]]
    p = Processo("P4", 4, 4, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(290, 4)]]
    p = Processo("P5", 4, 2, taskVecArrival)
    tasks.append(p)

    





    return tasks