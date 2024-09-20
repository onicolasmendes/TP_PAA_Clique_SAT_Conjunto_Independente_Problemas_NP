import time
from cliquemax import maxclique

def complemento_grafo(grafo, n):
   for i in range(n):
       for j in range(n):
           if i != j: #Desconsiderando a presença de "1" na diagonal principal, conforme orientado pelo professor
            if grafo[i][j] == 0:
               grafo[i][j] = 1
            else:
               grafo[i][j] = 0
   return grafo

def conjunto_independente(grafo, n):
    grafo_complemento = complemento_grafo(grafo, n)
    return maxclique(grafo_complemento, n)

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
    print("Conjunto independente máximo:", conjunto_independente_maximo[0])
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
