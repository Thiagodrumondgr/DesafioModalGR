import datetime

def criar_pasta_aniversariantes():
    
    with open("consultores.txt", "r") as arquivo:
       
        linhas = arquivo.readlines()

    # Cria uma lista com os dados dos aniversariantes
    aniversariantes = []
    mes_atual = datetime.datetime.now().month # Verifica o mês atual
    
    for linha in linhas:
      
        dados = linha.strip().split(" | ")

        data_nascimento = datetime.datetime.strptime(dados[2], "%d/%m/%Y")

        # Verifica se a data de nascimento é do mês corrente
        if data_nascimento.month == mes_atual:
            aniversariantes.append(dados)
            
    # Cria o arquivo de aniversariantes
    with open("aniversariantes.txt", "w") as arquivo:
        for dados in aniversariantes:
            arquivo.write(" ".join(dados) + "\n")

criar_pasta_aniversariantes()
