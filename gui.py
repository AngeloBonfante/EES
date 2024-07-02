import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functools import partial  # Import functools.partial
import copy

from taskgen import TaskGen
from escalonador import EscalonadorFCFS, EscalonadorPrioridade, EscalonadorRR, EscalonadorSJF

taskGenVal = 1
quantum = 20
instRange = 5

def get_slider_value(x):
    value = slider.get()
    labelVal.config(text=f"Processos: {int(value)}")
    global taskGenVal
    taskGenVal = int(value)

def get_quantum_value(x):
    value = quantum_slider.get()
    labelQuantum.config(text=f"Quantum: {int(value)}")
    global quantum
    quantum = int(value)

def get_instRange_value(x):
    value = instRange_slider.get()
    labelInstRange.config(text=f"Max Insts por Processo: {int(value)}")
    global instRange
    instRange = int(value)




app = tk.Tk()
app.title("Escalonador")
#app.geometry("280x265")  # Set the window size (optional)
app.resizable(False, False)  # Disable window resizing


# Global task vector
task_vect_imut = []


style = ttk.Style(app)
style.theme_use('clam')
style.configure('TButton', width=15)


def getTasks(num_tasks):
    global task_vect_imut

    task_vect_imut = TaskGen(num_tasks, instRange)
  
    messagebox.showinfo("Information", f"{num_tasks} Tasks Generated!")


def runTaskGen():
    getTasks(taskGenVal)

def runFCFS():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorFCFS(task_vect)
        #messagebox.showinfo("Information", "FCFS Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runSJF():
    task_vect = task_vect_imut.copy()
    if task_vect:
        EscalonadorSJF(task_vect)
        #messagebox.showinfo("Information", "SJF Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runPrio():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorPrioridade(task_vect)
        #messagebox.showinfo("Information", "Priority Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runRR():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorRR(task_vect, quantum)
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


# Use functools.partial to pass the desired number of tasks to getTasks
btn5 = ttk.Button(app, text="Gerar Processos", command=runTaskGen)
btn5.grid(row=4, column=0, padx=10, pady=0,columnspan=2, sticky="ew")

slider = ttk.Scale(app, from_=1, to=30, orient="horizontal", command=get_slider_value)
slider.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelVal = tk.Label(app, text="Processos: 1", font=("Arial", 10))
labelVal.grid(row=6, column=0, columnspan=2, padx=10, pady=0)


quantum_slider = ttk.Scale(app, from_=1, to=100, orient="horizontal", command=get_quantum_value)
quantum_slider.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelQuantum = tk.Label(app, text="Quantum: 20", font=("Arial", 10))
labelQuantum.grid(row=8, column=0, columnspan=2, padx=10, pady=0)


instRange_slider = ttk.Scale(app, from_=1, to=50, orient="horizontal", command=get_instRange_value)
instRange_slider.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
labelInstRange = tk.Label(app, text="Max Insts por Processo: 5", font=("Arial", 10))
labelInstRange.grid(row=10, column=0, columnspan=2, padx=10, pady=0)




app.mainloop()


