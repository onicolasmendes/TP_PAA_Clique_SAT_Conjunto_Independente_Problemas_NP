import time

def satisfatibilidade(clauses, n_vars):
    def backtrack(assignment, var_index):
        # Verificar se a atribuição parcial já viola alguma cláusula
        if not is_partial_assignment_valid(clauses, assignment, var_index):
            return False  # Poda: Não vale a pena continuar se já houver inconsistências

        # Se todas as variáveis foram atribuídas, verifica se a fórmula é satisfeita
        if var_index == n_vars:
            return check_formula(clauses, assignment)

        # Tenta atribuir True ou False para a próxima variável
        for value in [True, False]:
            assignment[var_index] = value
            if backtrack(assignment, var_index + 1):
                return True

        return False

    def check_formula(clauses, assignment):
        """Verifica se a fórmula é satisfeita para uma atribuição completa."""
        for clause in clauses:
            satisfied = False
            for i, literal in enumerate(clause):
                if literal == 1 and assignment[i]:  # Variável positiva e verdadeira
                    satisfied = True
                    break
                elif literal == 0 and not assignment[i]:  # Variável negada e falsa
                    satisfied = True
                    break
            if not satisfied:
                return False  # Se alguma cláusula não for satisfeita, retorna falso
        return True  # Todas as cláusulas foram satisfeitas

    def is_partial_assignment_valid(clauses, assignment, var_index):
        """Verifica se a atribuição parcial é válida, ou seja, se não viola alguma cláusula."""
        for clause in clauses:
            satisfied = False
            for i, literal in enumerate(clause):
                # Se estamos analisando além do índice já atribuído, ignoramos
                if assignment[i] is None:
                    continue

                if literal == 1 and assignment[i]:  # Variável positiva e verdadeira
                    satisfied = True
                    break
                elif literal == 0 and not assignment[i]:  # Variável negada e falsa
                    satisfied = True
                    break

            # Se a cláusula não é satisfeita, mas ainda temos variáveis a atribuir, ignoramos
            if not satisfied and assignment.count(None) == 0:
                return False  # Poda: Se já sabemos que não podemos satisfazer a cláusula

        return True  # Ainda pode ser possível satisfazer a fórmula

    # Inicialização da atribuição
    assignment = [None] * n_vars
    start_time = time.time()
    satisfaz = backtrack(assignment, 0)
    end_time = time.time()

    # Retorna o resultado final
    if satisfaz:
        return f"Satisfazível. Atribuição: {assignment}. Tempo de execução: {end_time - start_time:.4f} segundos"
    else:
        return f"Não satisfazível. Tempo de execução: {end_time - start_time:.4f} segundos"


def ler_entrada_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            n_vars = int(f.readline().strip())
            clauses = []
            for linha in f:
                clause = list(map(int, linha.strip().split()))
                clauses.append(clause)
        return clauses, n_vars
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return [], 0
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return [], 0

if __name__ == "__main__":
    nome_arquivo = 'sat_input.txt'
    clauses, n_vars = ler_entrada_arquivo(nome_arquivo)
    if clauses and n_vars:
        resultado = satisfatibilidade(clauses, n_vars)
        print(resultado)
    else:
        print("Erro ao processar a entrada.")
