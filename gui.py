import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functools import partial  
import copy

from taskgen import TaskGen, getBasic
from escalonador import EscalonadorFCFS, EscalonadorPrioridade, EscalonadorRR, EscalonadorSJF

taskGenVal = 1
quantum = 10
instRange = 30
rgn_arrival = 0
dyq = False
con = False
preemp = False

throughput = 0
AverageTurnaround = 0

def get_slider_value(x):
    value = slider.get()
    labelVal.config(text=f"Processos: {int(value)}")
    global taskGenVal
    taskGenVal = int(value)
    btn_change(False)

def get_quantum_value(x):
    value = quantum_slider.get()
    labelQuantum.config(text=f"Quantum: {int(value)}")
    global quantum
    quantum = int(value)

def get_instRange_value(x):
    value = instRange_slider.get()
    labelInstRange.config(text=f"Burst Time Máximo: {int(value)}")
    global instRange
    instRange = int(value)
    btn_change(False)

def get_arrivalRange_value(x):
    value = arrivalRange_slider.get()
    labelArrivalRange.config(text=f"Tempo de Chegada Máximo: {int(value)}")
    global rgn_arrival
    rgn_arrival = int(value)
    btn_change(False)

def btn_change(mode):

    if mode:
        style.configure("Custom.TButton", background="green", foreground="white", focuscolor='')
        btn5.config(text=f"Processos Gerados")
    else:
        style.configure("Custom.TButton", background="gray", foreground="black", focuscolor='', activeBackground='gray', activeForeground="white", text="Gerar Processos")
        btn5.config(text=f"Gerar Processos")
    return








app = tk.Tk()
app.title("Escalonador")
#app.geometry("280x265")  # Set the window size (optional)
app.resizable(False, False)  # Disable window resizing


# Global task vector
task_vect_imut = []
#task_vect_imut = getBasic()


style = ttk.Style(app)
style.theme_use('clam')
style.configure('TButton', width=15)

style.map("Custom.TButton",
          background=[('active', 'green')],
          foreground=[('active', 'white')])

def getTasks(num_tasks):
    global task_vect_imut

    task_vect_imut = TaskGen(num_tasks, instRange, rgn_arrival)
    #task_vect_imut = getBasic()
  
    #messagebox.showinfo("Information", f"{num_tasks} Tasks Generated!")
    

    btn_change(True)


def runTaskGen():
    getTasks(taskGenVal)

def runFCFS():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        aux = EscalonadorFCFS(task_vect)
        global AverageTurnaround 
        global throughput
        AverageTurnaround = aux[0]
        throughput = aux[1]
        EntryInserter(throughput, AverageTurnaround)
        #messagebox.showinfo("Information", "FCFS Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runSJF():
    task_vect = task_vect_imut.copy()
    if task_vect:
        aux = EscalonadorSJF(task_vect)
        global AverageTurnaround 
        global throughput
        AverageTurnaround = aux[0]
        throughput = aux[1]
        EntryInserter(throughput, AverageTurnaround)
        #messagebox.showinfo("Information", "SJF Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runPrio():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        aux = EscalonadorPrioridade(task_vect)
        global AverageTurnaround 
        global throughput
        AverageTurnaround = aux[0]
        throughput = aux[1]
        EntryInserter(throughput, AverageTurnaround)
        #messagebox.showinfo("Information", "Priority Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runRR():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        aux = EscalonadorRR(task_vect, quantum, dyq)
        global AverageTurnaround 
        global throughput
        AverageTurnaround = aux[0]
        throughput = aux[1]
        EntryInserter(throughput, AverageTurnaround)
        #messagebox.showinfo("Information", "RR Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")


btn = ttk.Button(app, text="FCFS", command=runFCFS)
btn.grid(row=0, column=0, padx=10, pady=10, sticky="w" )


btn2 = ttk.Button(app, text="SJF", command=runSJF)
btn2.grid(row=0, column=1, padx=10, pady=10, sticky="w")


btn3 = ttk.Button(app, text="PRIORIDADE", command=runPrio)
btn3.grid(row=1, column=0, padx=10, pady=10, sticky="w")


btn4 = ttk.Button(app, text="ROUND-ROBIN", command=runRR)
btn4.grid(row=1, column=1, padx=10, pady=10, sticky="w")

btn5 = ttk.Button(app, text="Gerar Processos", command=runTaskGen, style="Custom.TButton")
btn5.grid(row=4, column=0, padx=10, pady=0,columnspan=2, sticky="ew")
style.configure("Custom.TButton", background="gray", foreground="white")


slider = ttk.Scale(app, from_=1, to=30, orient="horizontal", command=get_slider_value)
slider.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

labelVal = tk.Label(app, text="Processos: 1", font=("Arial", 10))
labelVal.grid(row=6, column=0, columnspan=2, padx=10, pady=0)


quantum_slider = ttk.Scale(app, from_=1, to=100, orient="horizontal", command=get_quantum_value)
quantum_slider.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelQuantum = tk.Label(app, text="Quantum: 10", font=("Arial", 10))
labelQuantum.grid(row=8, column=0, columnspan=2, padx=10, pady=0)


instRange_slider = ttk.Scale(app, from_=1, to=100, orient="horizontal", command=get_instRange_value)
instRange_slider.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelInstRange = tk.Label(app, text="Burst Time Máximo: 30", font=("Arial", 10))
labelInstRange.grid(row=10, column=0, columnspan=2, padx=10, pady=0)

arrivalRange_slider = ttk.Scale(app, from_=0, to=100, orient="horizontal", command=get_arrivalRange_value)
arrivalRange_slider.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelArrivalRange = tk.Label(app, text="Tempo de Chegada Máximo: 0", font=("Arial", 10))
labelArrivalRange.grid(row=12, column=0, columnspan=2, padx=10, pady=0)

def dynQ():
    global dyq 
    if dyq == True:
        dyq = False
    else:
        dyq = True

dynamicQbtn = ttk.Checkbutton(app, text="Quantum Dinamico", command=dynQ)
dynamicQbtn.grid(row=13, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

def preemptive():
    global preemp
    if preemp == True:
        preemp = False
    else:
        preemp = True


entryT = tk.Entry(app, width=20)
entryT.grid(row=14, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
entryT.insert(0, "Default Value")
entryT.config(state='disabled')

entryV = tk.Entry(app, width=20)
entryV.grid(row=15, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
entryV.insert(0, "Default Value")
entryV.config(state='disabled')


def activatorEntry(mode):
    if mode:
        entryT.config(state='normal')
        entryV.config(state='normal')
    else:
        entryT.config(state='disabled')
        entryV.config(state='disabled')

def EntryInserter(throughput, AverageTurnaround):
    activatorEntry(True)
    entryT.delete(0, tk.END)
    entryV.delete(0, tk.END)
    entryT.insert(0, f"Turnaround Médio: {int(AverageTurnaround)} ms")
    entryV.insert(0, f"Throughput: {round(throughput, 2)} ms/instrução")
    activatorEntry(False)





#app.mainloop()


