import time
from cliquemax import clique

def complemento_grafo(grafo, n):
    # Cria o grafo complementar
    return [[1 - grafo[i][j] if i != j else 0 for j in range(n)] for i in range(n)]

def conjunto_independente(grafo, n):
    grafo_complemento = complemento_grafo(grafo, n)
    return clique(grafo_complemento, n)

if __name__ == "__main__":
    # Lê o grafo de um arquivo
    with open('conjindinput.txt', 'r') as f:
        n = int(f.readline().strip())
        grafo = [list(map(int, linha.split())) for linha in f.readlines()]

    # Mede o tempo de execução
    start_time = time.time()
    conjunto_independente_maximo = conjunto_independente(grafo, n)
    end_time = time.time()

    # Imprime o conjunto independente máximo encontrado e o tempo de execução
    print("Conjunto independente máximo:", conjunto_independente_maximo)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
