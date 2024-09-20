import itertools
from colorama import init, Fore
import os

# Inicializa o colorama
init(autoreset=True)

def ler_entrada_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()
        num_variaveis = int(linhas[0].strip())
        clausulas = [list(map(int, linha.strip().split())) for linha in linhas[1:]]
    return clausulas, num_variaveis

def gerar_tabela_verdade(clausulas, num_variaveis):
    table = []
    for valores in itertools.product([0, 1], repeat=num_variaveis):
        row = list(valores)
        satisfied_clauses = []
        
        for clause in clausulas:
            satisfied = False
            for i, literal in enumerate(clause):
                if literal == 1 and row[i] == 1:  # variável normal
                    satisfied = True
                elif literal == 0 and row[i] == 0:  # variável negada
                    satisfied = True
                elif literal == -1:  # variável não presente
                    continue
            satisfied_clauses.append(satisfied)
        
        table.append((row, satisfied_clauses))
    return table

if __name__ == "__main__":
    arquivos = ['input1.txt', 'input2.txt', 'input3.txt']  # Nomes dos arquivos
    pasta = 'input/satinput/'  # Substitua pelo caminho correto da sua pasta

    for arquivo in arquivos:
        nome_arquivo = os.path.join(pasta, arquivo)
        clausulas, num_variaveis = ler_entrada_arquivo(nome_arquivo)
        
        tabela = gerar_tabela_verdade(clausulas, num_variaveis)
        
        # Exibindo a tabela verdade
        print(f"\nTabela Verdade para {arquivo}:")
        print("Valores de variáveis: [v1, v2, v3], Cláusulas Satisfeitas")
        for row, satisfied in tabela:
            if all(satisfied):
                print(Fore.GREEN + f" {row} -> {satisfied}")  # Todas as cláusulas satisfeitas
            else:
                print(Fore.RED + f" {row} -> {satisfied}")    # Alguma cláusula não satisfeita
