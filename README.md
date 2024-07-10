# SIMULADOR DE ESCALONAMENTO

Interface gráfica com possibilidade de gerar e executar processos em um dos quatro algoritmos de escalonador.

## Uso: 
- Utilizar sliders para configurar a geração de processos da forma desejada.
- Clicar em "Gerar Processos".
- Escolher um escalonador para ver o grafico de Gannt e ao fechar o grafico será possível ver os dados relacionados como vazão e turnaround médio.

  
É possível rodar diferentes escalonadores no mesmo set de processos, a geração de processos só deve ser feita quando requerida pelo programa indicado pelo botão na cor cinza.


## Escalonador FCFS (FIRST COME FIRST SERVED):
### Esse algoritmo vai pegar e mandar processos para a CPU na ordem em que chegaram na fila de prontos.
## Escalonador SJF (SHORTEST JOB FIRST):
### Esse algoritmo pega processos de acordo com seu tamanho, importante se atentar que um processo maior vai ser executado primeiro caso chegue na fila de prontos antes de um processo menor.
## Escalonador de Prioridade:
### Da mesma maneira que o SJF funciona porém a organização se da pelo valor de prioridade contida no processo, sendo valores menores mais prioritizados.
### Escalonador Round-Robin:
### Vai dividir o tempo de execução entre processos a partir de um "quantum de tempo", sendo o quantum, por exemplo, 10 ms e os processos com burst time de 20 ms, o escalonador vai rodar cada processos alternativamente por 10 ms cada até o término.


## Opções:
#### Processo: É a quantidade de processos que serão gerados pelo programa para serem executados.
#### Quantum: Tamanho do quantum de tempo do escalonador round-robin, é medido em ms.
#### Burst-Time Máximo: Da a quantidade máxima de tempo de CPU que um processo pode pedir, um valor de 10 significa que os processos serão gerados com 1 até 10 ms de tempo de CPU.
#### Quantum Dinâmico: Possibilita o quantum diminuir de tamanho quando o tempo de CPU restante for menor que o quantum.
