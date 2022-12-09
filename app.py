
# Não terminais
non_terminals = ["E","E0","A","B","X","OPX","P","EP","FP","S","T"]

# Terminais
terminals = ["id", "+", "-", 
             "/", "*","(",")","a","c","s"]

# Regras
R = {
        "E0":[["E"],["S"],["T","E"]],
        "E":[["B","OPX"],["P","EP"]],
        "B":[["b"]],
        "OPX":[["OP","A"]],
        "OP":[["+"],["-"],["/"],["*"]],
        "A":[["a"]],
        "P":[["("]],
        "EP":[["X","FP"]],
        "FP":[[")"]],
        "X":[["id"]],
        "S":[["s"]],
        "T": [["S","OP"]]
    }
    
def cykParse(w):
    n = len(w)
      
    # Inicializa a tabela
    T = [[set([]) for j in range(n)] for i in range(n)]
  
    # Preenchendo a tabela
    for j in range(0, n):
  
        # Verificando regras
        for lhs, rule in R.items():
            for rhs in rule:
                  
                # Se for terminal
                if len(rhs) == 1 and \
                rhs[0] == w[j]:
                    T[j][j].add(lhs)
  
        for i in range(j, -1, -1):   
                  
            for k in range(i, j + 1):     
  
                 # Verificando regras
                for lhs, rule in R.items():
                    for rhs in rule:
                          
                        # Se for terminal
                        if len(rhs) == 2 and \
                        rhs[0] in T[i][k] and \
                        rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
  
    # Verifica se pertence a gramática
    if len(T[0][n-1]) != 0:
        print("True")
    else:
        print("False")

w = "c / b + a".split()

# Chama função

cykParse(w)