import tkinter as tk
from tkinter import ttk

class Processo:
    def __init__(self, pid, tempo_burst):
        self.pid = pid
        self.tempo_burst = tempo_burst
        self.tempo_espera = 0
        self.tempo_turnaround = 0
        self.tempo_resposta = -1  # -1 indica que ainda não foi executado

# Inicializar a lista de processos globalmente
processos = []

def executar_fifo():
    global processos
    tempo_atual = 0

    for processo in processos:
        processo.tempo_espera = tempo_atual
        processo.tempo_turnaround = processo.tempo_espera + processo.tempo_burst
        processo.tempo_resposta = processo.tempo_espera  # Tempo de resposta é igual ao tempo de espera no FIFO
        tempo_atual += processo.tempo_burst

    atualizar_resultado()

def adicionar_processo():
    global processos
    try:
        pid = int(entrada_pid.get())
        tempo_burst = int(tempo_entrada_bust.get())
        processos.append(Processo(pid, tempo_burst))
        atualizar_lista_processos()  # Atualizar a exibição da lista de processos
        limpar_entradas()
    except ValueError:
        resultado_texto.set("Por favor, insira valores válidos.")

def atualizar_lista_processos():
    global processos
    lista_processos.delete(0, tk.END)
    for processo in processos:
        lista_processos.insert(tk.END, f"PID: {processo.pid} | Burst Time: {processo.tempo_burst}")

def limpar_entradas():
    entrada_pid.delete(0, tk.END)
    tempo_entrada_bust.delete(0, tk.END)

def atualizar_resultado():
    global processos
    if processos:
        result_str = "\n".join([
            f"PID: {processo.pid} | Tempo de Burst: {processo.tempo_burst} | Tempo de Espera: {processo.tempo_espera}"
            f" | Tempo de Turnaround: {processo.tempo_turnaround} | Tempo de Resposta: {processo.tempo_resposta}"
            for processo in processos
        ])
        resultado_texto.set(result_str)
    else:
        resultado_texto.set("Nenhum processo adicionado.")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Gerenciador de Processos FIFO")

# Definindo um estilo para os widgets ttk
style = ttk.Style()
style.theme_use('clam')

# Personalizar o estilo dos widgets
style.configure('TLabel', background='#34495E', foreground='white', font=('Helvetica', 12), padx=10, pady=5)
style.configure('TEntry', fieldbackground='#D5DBDB', font=('Helvetica', 12))
style.configure('TButton', background='#1E90FF', foreground='white', font=('Helvetica', 12), padx=10, pady=5)

# Frame principal
frame_principal = ttk.Frame(janela, padding=20)
frame_principal.grid(row=0, column=0, sticky="nsew")

# Labels e Entradas para PID e Tempo de Burst
ttk.Label(frame_principal, text="PID do Processo:").grid(row=0, column=0, sticky="w")
entrada_pid = ttk.Entry(frame_principal)
entrada_pid.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_principal, text="Tempo de Burst do Processo:").grid(row=1, column=0, sticky="w")
tempo_entrada_bust = ttk.Entry(frame_principal)
tempo_entrada_bust.grid(row=1, column=1, padx=5, pady=5)

# Botão para adicionar processo
botao_adicionar = ttk.Button(frame_principal, text="Adicionar Processo", command=adicionar_processo)
botao_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

# Lista de processos adicionados
lista_processos = tk.Listbox(frame_principal, width=50, height=10, bg='#D5DBDB', font=('Helvetica', 12))
lista_processos.grid(row=3, column=0, columnspan=2, pady=10)

# Botão para executar o escalonamento FIFO
botao_executar = ttk.Button(frame_principal, text="Executar Escalonamento", command=executar_fifo)
botao_executar.grid(row=4, column=0, columnspan=2, pady=10)

# Texto de resultado para exibir os dados dos processos
resultado_texto = tk.StringVar()
resultado_label = ttk.Label(frame_principal, textvariable=resultado_texto, justify="left")
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

# Ajustar o tamanho das colunas e linhas do frame principal
frame_principal.columnconfigure(0, weight=1)
frame_principal.columnconfigure(1, weight=1)
frame_principal.rowconfigure(5, weight=1)

# Configurações finais da janela principal
janela.configure(bg='#34495E')  # Cor de fundo da janela principal
janela.geometry("500x500")  # Tamanho inicial da janela

# Iniciar loop de eventos da interface gráfica
janela.mainloop()