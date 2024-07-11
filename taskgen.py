from task import Task
import random

# Gerador de tarefas

def TaskGen(n, rgn, rgn_arrival):

    tasks = []
    print(f"Gerando {n} tarefas\n\n")
    for x in range(n):
        nome = f"P{x}"
        inst = random.randint(1, rgn)
        prio = random.randint(1, 6)
        arr = 0 + x * random.randint(0, rgn_arrival)

        if x == 0:
            taskVecArrival = [[(0, 0)]]
        else:
            taskVecArrival = [[(arr, 4)]]

        p = Task(nome, inst, prio, taskVecArrival)
        tasks.append(p)

        #sort tasks by taskVecArrival
        tasks = sorted(tasks, key=lambda x: x.ready_queue_arrival_time[0][0][0])

    for task in tasks:
        print(f"{task.pID} burst: {task.cpu_burst_time}ms prioridade:{task.priority} chegada:{task.ready_queue_arrival_time[0][0][0]} ms")

    return tasks


# Tarefas básicas para teste

def getBasic():
    tasks = []
    taskVecArrival = [[(0, 4)]]
    p = Task("A", 10, 5, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(5, 4)]]
    p = Task("B", 5, 4, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(6, 4)]]
    p = Task("C", 19, 2, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(4, 4)]]
    p = Task("D", 2, 1, taskVecArrival)
    tasks.append(p)

    taskVecArrival = [[(50, 4)]]
    p = Task("E", 10, 4, taskVecArrival)
    #tasks.append(p)

    #taskVecArrival = [[(420, 4)]]
    #p = Task("F", 40, 2, taskVecArrival)
    #tasks.append(p)

    





    return tasks