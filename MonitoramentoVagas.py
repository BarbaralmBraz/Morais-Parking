
vagaCarro = []
vagaMoto = []
vagaOnibus = []
vagasReservadas = {}


# é criada uma lista de tuplas onde o primeiro elemento da tupla é um número 0 para livre e 1 para ocupada.
# o segundo elemento da tupla guardará a palca do veiculo ou alguma palavra especial como por ex. reservado.
def criarVagas(lista, numVagas):
    for i in range(numVagas):
        lista.append((0, ""))



def ocuparVaga(lista, vaga, placa):
  if vaga >= 0 and vaga < len(lista):
        if lista[vaga][0] == 0:
            lista[vaga] = (1,placa)
        else:
            print("Vaga ocupada")
  else:
      print("Vaga não existe")


def liberarVaga(lista,vaga):
    if vaga >= 0 and vaga < len(lista):
        if lista[vaga][0] == 1:
            lista[vaga] = (0, "")
        else:
            print("Vaga não está ocupada")
    else:
        print("Vaga não existe")


# recebe uma lista de tuplas referente as vagas e olha o primeiro elemento da tupla para saber se a vaga está
# disponivel ou ocupada.
def contarVaga(lista):
    cont = 0
    for vaga in lista:
        if not vaga [0]:
          cont += 1

    return cont



def retornaLista(tipoVeiculo):
    if tipoVeiculo == "c":
        return vagaCarro
    elif tipoVeiculo == "m":
        return vagaMoto
    elif tipoVeiculo == "o":
        return vagaOnibus
    else:
        print("Opção inválida")



# recebe as vagas que se deseja reservar e os usuarios permitidos ambos separados por espaço,
# o tipo de veiculo e a descrição que seria um codigo de identificação.
def reservarVagas(vagas,usuarios,tipoVeiculo,descricao):
    listaVagas = retornaLista(tipoVeiculo)

    # transforma a string de vagas recebida em uma lista de strings.
    vagasDesejadas = vagas.split()
    usuariosEspeciais = usuarios.split()
    vagasDisponiveis = []

    # verifica se as vagas desejadas estão disponiveis, caso sim, cria novas vagas reservadas
    # e as modifica em suas listas de origem passando 1 para tornarem ocupadas e o valor "reservado"
    # onde seria a placa.
    for vaga in vagasDesejadas:
        if listaVagas [int(vaga)][0] == 0:
            vagasDisponiveis.append((0, ""))
            ocuparVaga(listaVagas,int(vaga), "reservado")
        else:
            print(" A vaga ",vaga,"não está disponível ")

    if len(vagasDisponiveis) > 0:

        # caso não exista o codigo de reserva passado, o mesmo é criado no dicionario.
        if descricao not in vagasReservadas.keys():
            vagasReservadas[descricao] = {}

         # para cada reserva podem ser adicionadas vagas para as 3 categorias de veiculos.
        vagasReservadas[descricao][tipoVeiculo] = [vagasDisponiveis, usuariosEspeciais, vagasDesejadas]



def ocuparVagaReservada(codigo,tipoVeiculo,placa,numeroVaga):
    if codigo in vagasReservadas.keys():
        reservas = vagasReservadas.get(codigo)
        if tipoVeiculo in reservas.keys():
            reservasTipo = reservas.get(tipoVeiculo)
            usuariosPermitidos = reservasTipo[1]
            if placa in usuariosPermitidos:
                ocuparVaga(reservasTipo[0],numeroVaga,placa)
            else:
                print("Usuario não permitido")
        else:
            print("Não existem vagas deste tipo reservadas")
    else:
        print(" Não existe reserva com esse codigo")



def liberarVagaReservada(codigo,tipoVeiculo,numeroVaga):
    reservas = vagasReservadas.get(codigo)
    reservasTipo = reservas.get(tipoVeiculo)
    liberarVaga(reservasTipo[0],numeroVaga)


def listarVagas(lista):
    saida = ""
    vagasPorLinha = 0
    for i in range(len(lista)):
        vagasPorLinha += 1
        saida += str(i) + ": " + str(lista[i])
        if vagasPorLinha == 5:
            saida += "\n"
            vagasPorLinha = 0

        else:
            saida += " "

    return saida



def main(privilegios):

    rodar = True
    while rodar:
        msg = " Digite uma opção a baixo: \n(o) Ocupar vaga \n(d) Desocupar vaga \n(v) Verificar vagas  \n(l) Listar vagas \n"
        if privilegios:
            msg += "(r) Reservar vagas \n(s)Sair para o menu anterior \n>"
        else:
            msg += "(s)Sair para o menu anterior \n>"
        opcao = input(msg)
        if opcao.lower() == "o":
            tipoVaga = input("Tipo de vaga: \n(r) Reservada \n(n) Normal \n")
            tipoVeiculo = input("Tipo de veiculo: \n(c) Carro \n(m) Moto  \n(o) ônibus  \n")
            vaga = int(input("Vaga: "))
            placa = input("Placa: ")

            if tipoVaga.lower() == "r":
                codigoReserva = input("Codigo da reserva: ")
                ocuparVagaReservada(codigoReserva,tipoVeiculo,placa,vaga)
            elif tipoVaga.lower() == "n":
                vagas = retornaLista(tipoVeiculo)
                ocuparVaga(vagas, vaga, placa)
            else:
                print("opção invalida")


        if opcao.lower() == "d":
            tipoVaga = input("Tipo de vaga:  \n(r) Reservada, \n(n) Normal \n")
            tipoVeiculo = input("Tipo de veiculo: \n(c) Carro \n(m) Moto  \n(o) ônibus  \n")
            vaga = int(input("Vaga: "))

            if tipoVaga.lower() == "r":
                codigoReserva = input("Codigo da reserva: ")
                liberarVagaReservada(codigoReserva, tipoVeiculo, vaga)

            elif tipoVaga.lower() == "n":
                vagas = retornaLista(tipoVeiculo)
                liberarVaga(vagas, vaga)
            else:
                print("opção invalida")


        if opcao.lower() == "s":
            rodar = False

        if opcao.lower() == "v":
            vagasCarro = contarVaga(vagaCarro)
            vagasMoto = contarVaga(vagaMoto)
            vagasOnibus = contarVaga(vagaOnibus)

            print("Vagas disponiveis para carro: ", vagasCarro)
            print("Vagas disponiveis para moto: ", vagasMoto)
            print("Vagas disponiveis para onibus: ", vagasOnibus)

        if opcao.lower() == "r" and privilegios:
            vagas = input("Quais vagas reservar: ")
            usuarios = input("Para quais usuáios ou finalidade: ")
            tipoVeiculo = input("Tipo de vaga: ")
            descricao = input("Código da reserva: ")
            reservarVagas(vagas,usuarios,tipoVeiculo,descricao)

        if opcao.lower() == "l":

            tipoVaga = input("Tipo de vaga:  \n(r) Reservada \n(n) Normal \n")
            tipoVeiculo = input("Tipo de veiculo: \n(c) Carro \n(m) Moto  \n(o) Ônibus)  \n")
            if tipoVaga == "r":
                codigoReserva = input("Codigo da reserva: ")
                if codigoReserva in vagasReservadas.keys():
                    vagasListar = vagasReservadas.get(codigoReserva)
                    vagasListar = vagasListar.get(tipoVeiculo)[0]
                    saida = listarVagas(vagasListar)
                else:
                    saida = "Codigo de reserva não existe"

            elif tipoVaga.lower() == "n":
                vagasListar = retornaLista(tipoVeiculo)
                saida = listarVagas(vagasListar)

            else:
                saida = "opção invalida"
            print(saida)

criarVagas(vagaCarro, 20)
criarVagas(vagaMoto, 5)
criarVagas(vagaOnibus, 3)








