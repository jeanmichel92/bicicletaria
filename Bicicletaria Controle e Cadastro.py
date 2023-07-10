listaPecas = []   #Neste exercício será usado lista, e não tuplas, pois não sabemos o numero de peças que serão cadastradas#
#**********COMEÇO cadastrarPeca**********#
def cadastrarPeca(codigo): #função de cadastro#
    print("Você selecionou a opção de cadastrar peça")
    print("Código da Peça 00{}".format(codigo)) #código exclusivo da peça#
    peca = input("Por favor entre com o nome da peça: ")
    fabricante = input("Por favor entre com o fabricante da peça: ")
    valor = input("Por favor entre com o valor(em R$) da peça: ")
    dicionarioPeca = {"codigo" : codigo,
                      "peca" : peca,
                      "fabricante" : fabricante,
                      "valor" : valor}
    listaPecas.append(dicionarioPeca.copy())
#**********FIM cadastrarPeca**********#

#**********COMEÇO consultarPeca**********#
def consultarPeca(): #função de consulta#
    print("Você selecionou a opção de consultar peça")
    while True:
        try: #opCons usei como variavel para Opção de Consulta#
            opCons = int(input("Escolha a opção desejada:\n1- Consultar todas as peças\n"
                              "2 - Consultar Peça por código\n3- Consultar Peça por fabricante\n4 - Retornar\n>>"))
            if opCons == 1:
                print("Consultando todas as peças")
                for peca in listaPecas: #selecionar cada dicionário da minha lista(peça da lista de peças)
                    for key, value in peca.items(): #selecioanr cada conjunto chave-valor do dicionário (ex: Peça : Kit Cambio 21v)
                        print("{} : {}".format(key, value))
            elif opCons == 2:
                entrada = int (input("Digite o código da peça: "))
                for peca in listaPecas:
                    if (peca['codigo'] == entrada):
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
            elif opCons == 3:
                entrada = input("Digite o fabricante da peça: ")
                for peca in listaPecas:
                    if (peca['fabricante'] == entrada):
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
            elif opCons == 4:
                return
            else:
                print("Você digitou um número inválido")
                continue
        except:
            print("Você digitou um dado errado, por favor digite alguma opção do menu")

#**********FIM consultarPeca**********#

#**********COMEÇO removerPeca**********#
def removerPeca(): #função de remoção#
    print("Você selecionou a opção de remover peça")
    entrada = int(input("Digite o código da peça a ser removida: "))
    for peca in listaPecas:
        if (peca["codigo"] == entrada):
            listaPecas.remove(peca)
#**********FIM removerPeca**********#

#**********COMEÇO MAIN**********#
print("Bem vindo ao Controle de Estoque da Bicicletaria do Jean Michel Bete") #identificador pessoal
registroPecas = 0
while True:
    try:
        opcao = int(input("Escolha a opção desejada:\n1 - Cadastrar Peças\n"
                          "2 - Consultar Peças\n3 - Remover Peças\n4 - Sair\n>>"))
        if opcao == 1:
            registroPecas = registroPecas + 1
            cadastrarPeca(registroPecas)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print("Programa Finalizado")
            break
        else:
            print("Você digitou um número inválido")
            continue
    except:
        print("Você digitou um dado errado, por favor digite alguma opção do menu")
#**********FIM MAIN**********#