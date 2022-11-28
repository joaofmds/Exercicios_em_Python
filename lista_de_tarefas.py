import os
import json

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe.")
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo): 
    dados = tarefas
    with open(caminho_arquivo, 'w') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados
            
CAMINHO_ARQUIVO = 'aulas1.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'limpar': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None \
            else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
