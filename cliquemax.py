import time

def clique(grafo, n):
    melhor_clique = []

    def branch_and_bound(clique_atual, vertices_restantes):
        nonlocal melhor_clique
        if len(vertices_restantes) == 0:
            if len(clique_atual) > len(melhor_clique):
                melhor_clique = clique_atual[:]
            return

        for v in vertices_restantes:
            novos_vertices_restantes = [w for w in vertices_restantes if grafo[v][w] == 1]
            clique_atual.append(v)
            branch_and_bound(clique_atual, novos_vertices_restantes)
            clique_atual.pop()

    branch_and_bound([], list(range(n)))
    return melhor_clique

if __name__ == "__main__":
    # Lê o grafo de um arquivo
    with open('clique_input.txt', 'r') as f:
        n = int(f.readline().strip())
        grafo = [list(map(int, linha.split())) for linha in f.readlines()]

    # Mede o tempo de execução
    start_time = time.time()
    clique_maximo = clique(grafo, n)
    end_time = time.time()

    # Imprime o clique máximo encontrado e o tempo de execução
    print("Clique máximo:", clique_maximo)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
