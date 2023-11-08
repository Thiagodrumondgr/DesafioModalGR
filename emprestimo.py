import datetime

def calculate():
    dataAdmissao = datetime.datetime.min
    salario = 0
    emprestimo = 0

    nome = input("Nome do funcionário: ")

    dataAdmissaoDigitada = input("Data de admissão (dd/MM/yyyy): ")
    dataAdmissao = datetime.datetime.strptime(dataAdmissaoDigitada, "%d/%m/%Y")
    if dataAdmissao == datetime.datetime.min:
        raise ValueError("Data inválida")
    if dataAdmissao > datetime.datetime.now() - datetime.timedelta(days=5*365):
        print("Agradecemos o seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    salarioDigitado = input("Salário atual (somente número inteiro): ")
    salario = int(salarioDigitado)
    if salario == 0:
        raise ValueError("Valor salário inválido")
    if salario % 2 != 0:
        print("O salário precisa ser múltiplo de 2 e par")
        return
    emprestimoDigitado = input("Valor empréstimo (somente número inteiro): ")
    emprestimo = int(emprestimoDigitado)
    if emprestimo == 0:
        raise ValueError("Valor empréstimo inválido")
    if emprestimo % 2 != 0:
        print("O empréstimo precisa ser múltiplo de 2 e par")
    if emprestimo > 2 * salario:
        print("O valor do empréstimo solicitado não pode ultrapassar o dobro do seu salário")
        return

    print("Escolha:")
    print("1 para impressão em notas de maior valor (100, 50 e inferiores)")
    print("2 para impressão em notas de menor valor (20, 10, 5 e 2)")
    print("3 para impressão em notas meio a meio")
    opcaoDigitada = input("opção: ")
    if opcaoDigitada not in ["1", "2", "3"]:
        raise ValueError("Opção inválida")
    if opcaoDigitada == "1":
        calcula_notas_maior_valor(emprestimo)
    elif opcaoDigitada == "2":
        calcula_notas_menor_valor(emprestimo)
    else:
        metade = emprestimo // 2
        calcula_notas_maior_valor(metade)
        calcula_notas_menor_valor(metade)

    print("FIM")

def calcula_notas_maior_valor(emprestimo):
    emprestimo_inicial = emprestimo
    quantidade_notas100 = 0
    quantidade_notas50 = 0
    quantidade_notas20 = 0
    quantidade_notas10 = 0
    quantidade_notas5 = 0
    quantidade_notas2 = 0

    while emprestimo >= 100:
        quantidade_notas100 += 1
        emprestimo -= 100
    while emprestimo >= 50 and (emprestimo % 50 > 20):
        quantidade_notas50 += 1
        emprestimo -= 50
    while emprestimo >= 20 and (emprestimo % 20 > 10):
        quantidade_notas20 += 1
        emprestimo -= 20
    while emprestimo >= 10 and (emprestimo % 10 > 5):
        quantidade_notas10 += 1
        emprestimo -= 10
    while emprestimo >= 5 and (emprestimo % 5 > 2):
        quantidade_notas5 += 1
        emprestimo -= 5
    while emprestimo >= 2:
        quantidade_notas2 += 1
        emprestimo -= 2

    print(f"Notas de maior valor para empréstimo de R$ {emprestimo_inicial}: ")
    print(f"{quantidade_notas100} nota(s) de R$ 100")
    print(f"{quantidade_notas50} nota(s) de R$ 50")
    print(f"{quantidade_notas20} nota(s) de R$ 20")
    print(f"{quantidade_notas10} nota(s) de R$ 10")
    print(f"{quantidade_notas5} nota(s) de R$ 05")
    print(f"{quantidade_notas2} nota(s) de R$ 02")

def calcula_notas_menor_valor(emprestimo):
    emprestimo_inicial = emprestimo
    quantidade_notas20 = 0
    quantidade_notas10 = 0
    quantidade_notas5 = 0
    quantidade_notas2 = 0

    while emprestimo >= 20 and (emprestimo % 20 > 10):
        quantidade_notas20 += 1
        emprestimo -= 20
    while emprestimo >= 10 and (emprestimo % 10 > 5):
        quantidade_notas10 += 1
        emprestimo -= 10
    while emprestimo >= 5 and (emprestimo % 5 > 2):
        quantidade_notas5 += 1
        emprestimo -= 5
    while emprestimo >= 2:
        quantidade_notas2 += 1
        emprestimo -= 2

    print(f"Notas de menor valor para empréstimo de R$ {emprestimo_inicial}: ")
    print(f"{quantidade_notas20} nota(s) de R$ 20")
    print(f"{quantidade_notas10} nota(s) de R$ 10")
    print(f"{quantidade_notas5} nota(s) de R$ 05")
    print(f"{quantidade_notas2} nota(s) de R$ 02")

calculate()