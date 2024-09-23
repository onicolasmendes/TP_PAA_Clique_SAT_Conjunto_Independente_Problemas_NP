# Trabalho Prático: Implementação de Algoritmos Satisfatibilidade, Clique e Conjunto Independente
## Descrição Geral
Este repositório contém a implementação de três algoritmos fundamentais em teoria dos grafos e lógica booleana: Satisfatibilidade (SAT), Clique e Conjunto Independente. Cada um desses problemas é resolvido utilizando diferentes técnicas de otimização e busca.

## Algoritmos Implementados

### Satisfatibilidade (SAT):
Dada uma fórmula booleana na forma normal conjuntiva (CNF), o objetivo é encontrar uma atribuição de valores-verdade que torne a fórmula verdadeira. Se não existir tal atribuição, o programa deverá informar que a fórmula é insatisfatível.

Método de Solução: Backtracking.

### Clique:
Dado um grafo, o objetivo é encontrar o maior subcconjunto de vértices tal que todas as arestas entre eles estejam presentes, formando um clique máximo.

Método de Solução: Branch and Bound.

### Conjunto Independente:
Dado um grafo, o objetivo é encontrar o maior conjunto de vértices independentes, ou seja, um conjunto em que não exista aresta entre nenhum par de vértices.

Método de Solução: Resolução por redução polinomial ao problema do Clique.

## Tecnologias Utilizadas
Linguagem: Python
Estruturas de dados: Matrizes de adjacência e fórmulas booleanas
