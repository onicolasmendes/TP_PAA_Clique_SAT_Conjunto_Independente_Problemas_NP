import time

def eCompleta(vertices_restantes): #Verifica se a solução é completa, ou seja, se não há mais vértices a serem adicionados ao clique
    if len(vertices_restantes) == 0:
        return True
    return False

def ePromissora(clique_atual, vertices_restantes, melhor_clique): #Verifica se o eventual clique tem potencial de ser melhor que a solução melhor atual
    if (len(clique_atual)+len(vertices_restantes)) > len(melhor_clique[0]):
        return True
    return False

def vertices_com_arestas_com_v(v, vertices, grafo):
    vertices_com_arestas_com_v = []
    for w in vertices:
        if grafo[v][w] == 1: #Vértice com aresta com vértice V
            vertices_com_arestas_com_v.append(w)
    return vertices_com_arestas_com_v
        
def branch_and_bound(clique_atual, vertices_restantes, melhor_clique, grafo):
    if eCompleta(vertices_restantes):
        melhor_clique[0] = clique_atual[:]
       
    for v in vertices_restantes:
        novos_vertices_restantes = vertices_com_arestas_com_v(v, vertices_restantes, grafo) #Adiciona todos os vértices como promissores que possuem aresta com o vértice v, garante que todas as soluções serão consistentes
        clique_atual.append(v) #Adiciona v ao conjunto de clique atual para eventualmente explorar uma solução que o contém
        if(ePromissora(clique_atual, novos_vertices_restantes, melhor_clique)): #Poda
            branch_and_bound(clique_atual, novos_vertices_restantes, melhor_clique, grafo)
        clique_atual.pop() #Remove v do clique atual para explorar uma eventual solução utilizando o próximo vértice do for

def maxclique(grafo, n):
    melhor_clique = [[0]] #Solução melhor inicial
    
    branch_and_bound([], list(range(n)), melhor_clique, grafo) #Solução inicial = []
    
    return melhor_clique

if __name__ == "__main__":
    # Lê o grafo de um arquivo
    with open('clique_input.txt', 'r') as f:
        n = int(f.readline().strip())
        grafo = [list(map(int, linha.split())) for linha in f.readlines()]

    # Mede o tempo de execução
    start_time = time.time()
    clique_maximo = maxclique(grafo, n)
    end_time = time.time()

    # Imprime o clique máximo encontrado e o tempo de execução
    print("Clique máximo:", clique_maximo[0])
    print(f"Tempo de execução: {end_time - start_time:.7f} segundos")
