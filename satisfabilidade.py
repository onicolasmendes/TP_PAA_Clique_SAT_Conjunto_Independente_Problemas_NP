import time

def verificar_formula(clausulas, variaveis): #Verifica se os valores atribuídos às variáveis satisfazem todas as cláusulas simultaneamente 
    for clausula in clausulas:
        satisfaz = False
        for i, literal in enumerate(clausula):
            if literal == 1 and variaveis[i]:  # Variável positiva e verdadeira = True
                satisfaz = True
                break #Pula para analisar a próxima clásula
            elif literal == 0 and not variaveis[i]:  # Variável negada e falsa = True
                satisfaz = True
                break #Pula para analisar a próxima clásula
            
        if not satisfaz: # Se alguma cláusula não for satisfeita, retorna falso
            return False  
        
    return True  # Todas as cláusulas foram satisfeitas

def backtrack(clausulas, variaveis, numero_variaveis):
    #Verifica se a solução parcial é consistente, estratégia para evitar busca exaustiva
    if not is_partial_solution_is_valid(clausulas, variaveis):
        return False
    
    #Se todas as variáveis estão atribuídas, verifica se as clausulas são satisfeitas simultaneamente
    if None not in variaveis:
        return verificar_formula(clausulas, variaveis)
    
    #Próxima variável a ser atribuída
    index_prox = variaveis.index(None)
    
    for valor in [True, False]:
        #Proximo passo do backtrack
        variaveis[index_prox] = valor
        if backtrack(clausulas, variaveis, numero_variaveis):
            return True
        variaveis[index_prox] = None #Caso a tentativa tenha gerado uma solução que não satisfaz, retorna o passo anterior
        
    return False
    
#Função principal que chama o backtracking
def satisfatibilidade(clausulas, numero_variaveis):
    variaveis = [None] * numero_variaveis
    start_time = time.time()
    satisfaz = backtrack(clausulas, variaveis, numero_variaveis)
    end_time = time.time()

    if satisfaz:
        return f"Satisfazível. Atribuição: {variaveis}. Tempo de execução: {end_time - start_time:.7f} segundos"
    else:
        return f"Não satisfazível. Tempo de execução: {end_time - start_time:.7f} segundos"


#Verifica se as variáveis presentes em uma cláusula estão com valores atribuídos
def ha_atribuicao_para_todas_variaveis_validas_na_clausula(clausula, variaveis):
    for i, literal in enumerate(clausula):
        if literal != -1 and variaveis[i] == None:
            return False
    return True
       
#Verifica se a solução parcial é consistente para continuar os passos do backtracking
def is_partial_solution_is_valid(clausulas, variaveis):
    for clausula in clausulas:
            if -1 in clausula: #Caso haja uma variável (ou mais) não presentes em uma cláusula
                #Verifica-se se as demais variáveis presentes possuem valores
                if ha_atribuicao_para_todas_variaveis_validas_na_clausula(clausula, variaveis):
                    satisfied = False
                    for i, literal in enumerate(clausula):
                        if literal == 1 and variaveis[i]:  # Variável positiva e verdadeira = True
                            satisfied = True
                            break
                        
                        elif literal == 0 and not variaveis[i]:  # Variável negada e falsa = True
                            satisfied = True
                            break

                    # Se a cláusula não é satisfeita, significa que não faz sentido expandir o backtrack a partir de tal solução parcial
                    if not satisfied:
                        return False  # Poda: Se já sabemos que não podemos satisfazer a cláusula

    return True  # Ainda pode ser possível satisfazer a fórmula
  
#Lê as cláusulas a partir de um arquivo previamente formatado conforme padrão exposto
def ler_entrada_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            numero_variaveis = int(f.readline().strip())
            clausulas = []
            for linha in f:
                clausula = list(map(int, linha.strip().split()))
                clausulas.append(clausula)
        return clausulas, numero_variaveis
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return [], 0
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return [], 0

if __name__ == "__main__":
    # Lista de arquivos de entrada
    arquivos = ['input/satinput/input1.txt', 
                'input/satinput/input2.txt', 
                'input/satinput/input3.txt']
    
    for nome_arquivo in arquivos:
        clausulas, numero_variaveis = ler_entrada_arquivo(nome_arquivo)
        if clausulas and numero_variaveis:
            resultado = satisfatibilidade(clausulas, numero_variaveis)
            print(f"Resultado para {nome_arquivo}: {resultado}")
        else:
            print(f"Erro ao processar a entrada do arquivo {nome_arquivo}.")