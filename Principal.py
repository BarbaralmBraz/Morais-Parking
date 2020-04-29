# coding: utf-8

# Bárbara Larissa de Medeiros Braz
# Jonathan Moura
# Suzana Freitas

import MonitoramentoVagas


def cadastrarFuncionario(funcionario, vetorLinhaFuncionario):
    quantFuncionario = int(input("Quantos funcionários você quer cadastrar? "))
    if quantFuncionario !=0:
        i = 0
        while i< quantFuncionario:
            for linha in range(0, quantFuncionario):
                for coluna in range(0, quantFuncionario):
                    nome = input ("Digite o nome do funcionário: ")
                    matricula = input ("Digite a matrícula do funcionário: ")
                    senha = input("Digite sua senha: ")
                    vetorLinhaFuncionario.append(nome)
                    vetorLinhaFuncionario.append(matricula)
                    vetorLinhaFuncionario.append(senha)
                    i = i+1
                funcionario.append(vetorLinhaFuncionario)
        print(funcionario)
    else:
        return 0

def cadastrarVeiculo(veiculo, vetorLinhaVeiculo):
    quantVeiculo = int(input("Quantos veiculos deseja cadastrar? "))
    if quantVeiculo != 0:
        i = 0
        while i < quantVeiculo:
            for linha in range(0,quantVeiculo):
                for coluna in range(0,quantVeiculo):
                    nome = input("Digite o nome do aluno: ")
                    matricula = input("Digite a matricula do aluno: ")
                    curso = input("Digite o curso do aluno: ")
                    placa = input("Digite a placa do carro: ")
                    vaga = input("Vaga especial? (S/N) ")
                    vetorLinhaVeiculo.append(nome)
                    vetorLinhaVeiculo.append(matricula)
                    vetorLinhaVeiculo.append(curso)
                    vetorLinhaVeiculo.append(placa)
                    vetorLinhaVeiculo.append(vaga)
                    i = i + 1
                veiculo.append(vetorLinhaVeiculo)
        print(veiculo)
    else:
        return 0


#funcionalidades do funcionario do estacionamento
def funcEstacionamento(login, veiculo, vetorLinhaVeiculo, removerVeiculo):

    print("1. Logar no sistema")

    print("2. Cadastrar novos veiculos")
    print("3. Remover veículos")
    print("4. Monitorar o estacionamento")
    print("5. Cadastrar ocorrencia no estacionamento")
    print("6. Cadastrar eventos no estacionamento ")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        print("Essa função ainda não está disponivel")
        funcEstacionamento(login, veiculo, vetorLinhaVeiculo, removerVeiculo)
    elif opcao == "2":
        if cadastrarVeiculo(veiculo, vetorLinhaVeiculo) != 0:
            print("Veículo cadastrado com sucesso!")
    elif opcao == "3":
        if removerVeiculo(removerVeiculo) != 0:
            print("Veículo removido com sucesso!")
    elif opcao == "4":
        MonitoramentoVagas.main(False)

    elif opcao == "5":
        print("Essa função ainda não está disponivel")
        funcEstacionamento(login, veiculo, vetorLinhaVeiculo, removerVeiculo)
    elif opcao == "6":
        print("Essa função ainda não está disponivel")
        funcEstacionamento(login, veiculo, vetorLinhaVeiculo, removerVeiculo)
    elif opcao == "0":
        print("sair!")
        return 0

#funcionalidades do funcionario do RH
def funcRH(login, funcionario, vetorLinhaFuncionario, permissaoAE):

    print("1. Logar no sistema")
    print("2. Cadastrar novos funcionários")
    print("3. Permitir acesso para área especial")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        print("Essa função ainda não está disponivel")
        funcRH(login, funcionario, vetorLinhaFuncionario, permissaoAE)
    elif opcao == "2":
        if cadastrarFuncionario(funcionario, vetorLinhaFuncionario) != 0:
            print("Funcionario cadastrado com sucesso!")
    elif opcao == "3":
        print("Essa função ainda não está disponivel")
        funcRH(login, funcionario, vetorLinhaFuncionario, permissaoAE)
    elif opcao == "0":
        print("sair!")
        return 0

#funcionalidades do gestor
def gestor(login, relatorio):

    print("1. Logar no sistema")
    print("2. Monitorar estacionamento")
    print("3. Vizualizar relatório")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
        print("Essa função ainda não está disponivel")
        gestor(login, relatorio)
    elif opcao == "2":
        MonitoramentoVagas.main(True)
    elif opcao == "3":
         print("Essa função ainda não está disponivel")
         gestor(login, relatorio)


    elif opcao == "0":
        print("sair!")
        return 0


#menu principal que ira chamar as funcoes de funcionario estacionamento, funcionario RH e gestor
def menuPrincipal(login, veiculo, vetorLinhaVeiculo, removerVeiculo, relatorio, funcionario, vetorLinhaFuncionario, permissaoAE):
    print("Bem vindo ao Morais Parking! Por favor, identifique-se.")
    print("1. Funcionario do Estacionamento")
    print("2. Funcionario do RH")
    print("3. Gestor")
    print("0. Sair")

    opcao = input("_")
    if opcao == "1":
          funcEstacionamento(login, veiculo, vetorLinhaVeiculo, removerVeiculo)

    elif opcao == "2":
         funcRH(login, funcionario, vetorLinhaFuncionario, permissaoAE)

    elif opcao == "3":
         gestor(login, relatorio)

    elif opcao == "0":
        print("sair!")
        return 0

#funcao principal que ira chamar o menu principal e guardar todos os vetores
def main():

    login = []
    veiculo = []
    vetorLinhaVeiculo = []
    removerVeiculo = []


    funcionario = []
    vetorLinhaFuncionario = []
    permissaoAE = []

    relatorio = []
    areaEspecial = []

    while True:
        if menuPrincipal(login, veiculo, vetorLinhaVeiculo, removerVeiculo, relatorio, funcionario, vetorLinhaFuncionario, permissaoAE) != 0:
            print()
        else:
            break

main()