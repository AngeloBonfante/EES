import tkinter as tk
from tkinter import messagebox
from functools import partial  # Import functools.partial
import copy

from taskgen import TaskGen
from escalonador import EscalonadorFCFS, EscalonadorPrioridade, EscalonadorRR, EscalonadorSJF

app = tk.Tk()
app.title("Escalonador")
app.geometry("200x210")  # Set the window size (optional)

# Global task vector
task_vect_imut = []

def getTasks(num_tasks):
    global task_vect_imut
    task_vect_imut = TaskGen(num_tasks)
    messagebox.showinfo("Information", f"{num_tasks} Tasks Generated!")

def runFCFS():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorFCFS(task_vect)
        messagebox.showinfo("Information", "FCFS Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runSJF():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorSJF(task_vect)
        messagebox.showinfo("Information", "SJF Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runPrio():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorPrioridade(task_vect)
        messagebox.showinfo("Information", "Priority Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

def runRR():
    task_vect = copy.deepcopy(task_vect_imut)
    if task_vect:
        EscalonadorRR(task_vect)
        messagebox.showinfo("Information", "RR Scheduler Run!")
    else:
        messagebox.showwarning("Warning", "No tasks to schedule!")

# FCFS
lbl = tk.Label(app, text="FCFS")
lbl.grid(row=0, column=0, padx=10, pady=10, sticky="e")
btn = tk.Button(app, text="RUN", command=runFCFS)
btn.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# SJF
lbl2 = tk.Label(app, text="SJF")
lbl2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
btn2 = tk.Button(app, text="RUN", command=runSJF)
btn2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# PRIORITY
lbl3 = tk.Label(app, text="PRIORITY")
lbl3.grid(row=2, column=0, padx=10, pady=10, sticky="e")
btn3 = tk.Button(app, text="RUN", command=runPrio)
btn3.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# ROUND-ROBIN
lbl4 = tk.Label(app, text="ROUND-ROBIN")
lbl4.grid(row=3, column=0, padx=10, pady=10, sticky="e")
btn4 = tk.Button(app, text="RUN", command=runRR)
btn4.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# GERAR PROCESSOS with a parameter using functools.partial
lbl5 = tk.Label(app, text="Gerador")
lbl5.grid(row=4, column=0, padx=10, pady=10, sticky="e")
# Use functools.partial to pass the desired number of tasks to getTasks
btn5 = tk.Button(app, text="RUN", command=partial(getTasks, 5))
btn5.grid(row=4, column=1, padx=10, pady=10, sticky="w")

app.mainloop()
