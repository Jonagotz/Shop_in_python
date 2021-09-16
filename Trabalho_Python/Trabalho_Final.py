# Cadastrar novos clientes
class usuarios:
    nome = None
    cpf = None
    email = None
    senha = None
    limitecredito = None
    balanço = None  # como em dinheiro não emprestado
    cartãonumero = None
    cartãosenha = None
    lista_carrinho = []

# Cadastrar novos produtos


class produtos:
    nome = None
    valor = 0.0
    marca = None
    origem = None  # praqueles que não querem comprar da china

# Cria produtos


def cria_produtos(lista_produtos):
    # produto1
    pastad_oral = produtos()
    pastad_oral.nome = "1. Pasta de dente Oral-B"
    pastad_oral.valor = 5.99
    pastad_oral.marca = "Oral-B"
    pastad_oral.origem = "Estados Unidos"
    lista_produtos.append(pastad_oral)
    # produto2
    pastad_colgate = produtos()
    pastad_colgate.nome = "2. Pasta de dente Colgate"
    pastad_colgate.valor = 3.99
    pastad_colgate.marca = "Colgate"
    pastad_colgate.origem = "Estados Unidos"
    lista_produtos.append(pastad_colgate)
    # produto3
    arroz_1kg = produtos()
    arroz_1kg.nome = "3. Arroz 1kg"
    arroz_1kg.valor = 8.76
    arroz_1kg.marca = "João Ferro"
    arroz_1kg.origem = "Belo Horizonte"
    lista_produtos.append(arroz_1kg)
    # produto4
    arroz_2kg = produtos()
    arroz_2kg.nome = "4. Arroz 2kg"
    arroz_2kg.valor = 15.89
    arroz_2kg.marca = "João Ferro"
    arroz_2kg.origem = "Belo Horizonte"
    lista_produtos.append(arroz_2kg)
    # produto5
    macarrao_500g = produtos()
    macarrao_500g.nome = "5. Macarrão 500g"
    macarrao_500g.valor = 10.00
    macarrao_500g.marca = "galo"
    macarrao_500g.origem = "Peru"
    lista_produtos.append(macarrao_500g)
    # produto6
    macarrao_1kg = produtos()
    macarrao_1kg.nome = "6. Macarrão 1kg"
    macarrao_1kg.valor = 18.99
    macarrao_1kg.marca = "galo"
    macarrao_1kg.origem = "Peru"
    lista_produtos.append(macarrao_1kg)
    # produto7
    açucar_500g = produtos()
    açucar_500g.nome = "7. Açucar 500g"
    açucar_500g.valor = 9.99
    açucar_500g.marca = "Good Life"
    açucar_500g.origem = "Africa do Sul"
    lista_produtos.append(açucar_500g)
    # produto8
    açucar_1kg = produtos()
    açucar_1kg.nome = "8. Açucar 1kg"
    açucar_1kg.valor = 20.00
    açucar_1kg.marca = "Good Life"
    açucar_1kg.origem = "Africa do Sul"
    lista_produtos.append(açucar_1kg)
    # produto9
    feijão_200g = produtos()
    feijão_200g.nome = "9. Feijão 200g"
    feijão_200g.valor = 8.25
    feijão_200g.marca = "Ô Feijim"
    feijão_200g.origem = "Rio Grande do Sul"
    lista_produtos.append(feijão_200g)
    # produto10
    feijão_1kg = produtos()
    feijão_1kg.nome = "10. Feijão 1kg"
    feijão_1kg.valor = 18.79
    feijão_1kg.marca = "Ô Feijin"
    feijão_1kg.origem = "Rio Grande do Sul"
    lista_produtos.append(feijão_1kg)
    # produto11
    frango_sassami = produtos()
    frango_sassami.nome = "11. Frango Sassami"
    frango_sassami.valor = 23.89
    frango_sassami.marca = "Sadia"
    frango_sassami.origem = "Santa Catarina"
    lista_produtos.append(frango_sassami)
    # produto12
    carne_boi = produtos()
    carne_boi.nome = "12. Filé Mignon kg"
    carne_boi.valor = 53.00
    carne_boi.marca = "Friboi"
    carne_boi.origem = "Goiás"
    lista_produtos.append(carne_boi)
    # produto13
    cafe_pilao = produtos()
    cafe_pilao.nome = "13. Café 200g"
    cafe_pilao.valor = 5.89
    cafe_pilao.marca = "Pilão"
    cafe_pilao.origem = "África"
    lista_produtos.append(cafe_pilao)
    # produto14
    cafe_pilao1kg = produtos()
    cafe_pilao1kg.nome = "14. Café 1kg"
    cafe_pilao1kg.valor = 18.00
    cafe_pilao1kg.marca = "Pilão"
    cafe_pilao1kg.origem = "África"
    lista_produtos.append(cafe_pilao1kg)
    # produto15
    farinha_100g = produtos()
    farinha_100g.nome = "15. farinha de rosca 100g"
    farinha_100g.valor = 4.99
    farinha_100g.marca = "Rosa Branca"
    farinha_100g.origem = "Goiás"
    lista_produtos.append(farinha_100g)
    # produto16
    extrato_tomate = produtos()
    extrato_tomate.nome = "16. Extrato de tomate 200g"
    extrato_tomate.valor = 10.99
    extrato_tomate.marca = "Calore"
    extrato_tomate.origem = "Argentina"
    lista_produtos.append(extrato_tomate)
    # produto17
    azeite = produtos()
    azeite.nome = "17. Azeite extravirgem 500ml"
    azeite.valor = 12.50
    azeite.marca = "O-Live"
    azeite.origem = "Estados Unidos"
    lista_produtos.append(azeite)
    # produto18
    agua_sgas = produtos()
    agua_sgas.nome = "18. Água s/gás 500ml"
    agua_sgas.valor = 2.99
    agua_sgas.marca = "Naturágua"
    agua_sgas.origem = "Chapecó"
    lista_produtos.append(agua_sgas)
    # produto19
    coca_1l = produtos()
    coca_1l.nome = "19. Coca-Cola 1,5L"
    coca_1l.valor = 13.99
    coca_1l.marca = "Coca-Cola"
    coca_1l.origem = "Estados Unidos"
    lista_produtos.append(coca_1l)
    #produto20 - último
    coca_2l = produtos()
    coca_2l.nome = "20. Coca-Cola 2L"
    coca_2l.valor = 18.00
    coca_2l.marca = "Cola-Cola"
    coca_2l.origem = "Estados Unidos"
    lista_produtos.append(coca_2l)
    '''lista terminada de produtos'''

# 1 - Cadastro do cliente


def cadastramento(lista_usuarios, usuario_logado):
    usuario = usuarios()
    InfoUsuario = []
    while True:
        usuario.nome = str(input("digite o seu Nome: "))
        Senha = input("Digite a senha para sua conta: ")
        if len(Senha) > 8:
            print("Senha muito grande, tente uma menor")
            continue
        Cpf = (input("Digite o seu CPF: "))
        if Cpf in lista_usuarios:  # ou for invalido por outro motivo, checar o site que o prof mandou no trabalho
            print("Esse CPF já existe")
            continue
        elif len(Cpf) != 11:
            print("Esse CPF é inválido, por favor digite novamente um CPF válido")
            continue
        Email = input("Digite o seu email: ")
        if "@" not in Email or Email in lista_usuarios or ".com" not in Email:
            print("Email invalido ou já cadastrado, por favor digite um Email válido")
            continue
        Cartão = input("Digite os numeros do cartão: ")
        if len(Cartão) < 16:
            print("Numero invalido")
            continue
        Senha_Cartão = input("Digite a senha do cartão: ")
        if len(Senha_Cartão) > 4:
            print("Senha invalida")
            continue
        LimiteCredito = float(input("Digite o seu limite de credito atual: "))
        LimiteCredito = -LimiteCredito
        Balanço = 0
        usuario.cpf = Cpf
        usuario.email = Email
        usuario.senha = Senha
        usuario.limitecredito = LimiteCredito
        usuario.balanço = 0
        usuario.cartãonumero = Cartão
        usuario.cartãosenha = Senha_Cartão
        lista_usuarios.append(usuario)

        usuario_logado.nome = usuario.nome
        usuario_logado.cpf = Cpf
        usuario_logado.email = Email
        usuario_logado.senha = Senha
        usuario_logado.limitecredito = LimiteCredito
        usuario_logado.balanço = 0
        usuario_logado.cartãonumero = Cartão
        usuario_logado.cartãosenha = Senha_Cartão

        return lista_usuarios, usuario_logado


# 2 - Consultar cliente
def consulta_cliente(lista_usuarios):  # fucniona com oq eu add na opcao, ou seja não ia por causa que a lista_uauarios tava vazia, so dai precisa ver pra se não tiver nada na lista dizer que não tem, e tirar o fixo da opcao
    cpf_consulta = input("Digite o CPF: ")
    for usuario in lista_usuarios:
        if cpf_consulta == usuario.cpf:
            print(f"O nome do cliente é {usuario.nome}")
            print(f"O email do cliente é {usuario.email}")
        else:
            print("Usuário não cadastrado")


#3 - Compra
# dar uns continues ou while true pra continuar a perguntar (nos lugar certo), testar


def compra(usuario_logado):
    produto_comprar = input("Digite o produto que gotaria de comprar: ")
    for i in range(len(usuario_logado.lista_carrinho)):
        if produto_comprar == usuario_logado.lista_carrinho[i]:
            variavel_temporaria_pra_testar_limite_credito = usuario_logado.balanço
            variavel_temporaria_pra_testar_limite_credito -= usuario_logado.lista_carrinho[i].valor
            if variavel_temporaria_pra_testar_limite_credito >= usuario_logado.limitecredito:
                usuario_logado.balanço = variavel_temporaria_pra_testar_limite_credito
                print("Produto comprado com sucesso! Ele chegará a você em até 14 dias.")
                tira_do_carrinho = input(
                    "Deseja retirar o produto de seu carrinho? Digite 'sim' para confirmar: ")
                if tira_do_carrinho == "sim" or tira_do_carrinho == "Sim":
                    usuario_logado.lista_carrinho.remove(
                        usuario_logado.lista_carrinho[i])  # checar
                    print("Produto removido do carrinho com sucesso.")
                    return usuario_logado
                else:
                    print("O produto não foi removido")
            # fui fazendo aqui primeiro e dai notei que podiamos usar como um add balanço, chamar a função aqui pra integração (os prof vai falar se nos não fazer) - Pedro
            else:
                adicionar_mais_credito = input(
                    "Tal ordem varia o seu balanço exceder o seu limite de credito. Gostaria de adicionar mais a sua conta? Digite 'sim' para confirmar")
                if adicionar_mais_credito == "sim" or adicionar_mais_credito == "Sim":
                    chances_pra_senha = 3
                    while chances_pra_senha <= 0:
                        confirmar_a_senha = input(
                            "Digite a senha do seu cartão de credito: ")
                        if confirmar_a_senha == usuario_logado.cartãosenha:
                            mais_balanço = int(
                                input("Digite o quando deseja adicionar: "))
                            usuario_logado.balanço + + mais_balanço
                            # dar um return pro menu principal ou voltar pro começo da def - Pedro
                            print(
                                f"Ordem realiazada com sucesso! Você agora tem {usuario_logado.balanço} na sua conta")
                        elif confirmar_a_senha != usuario_logado.cartãosenha and chances_pra_senha > 0:
                            chances_pra_senha -= 1
                            print(
                                f"Essa senha está incorreta, tente novamnete {chances_pra_senha} tentativas restantes")
                        elif chances_pra_senha == 0:
                            print("tentativas esgotadas.")
                            return
                else:
                    print("returnando ao menu...")
                    return
        else:
            print("Esse produto não se encontra na lista. Tente novamente")

# 5? acidionar credito #cara acho que não faz esse "pagar conta", ja que a gente ta usando um sistema de balanço e credito, bem mais ao estilo da Steam(o que não ta errado, é só uma decisão de como guardar dinheiro)


def adicionar_balanço(usuario_logado):  # testar
    chances_pra_senha = 3
    while chances_pra_senha <= 0:
        confirmar_a_senha = input("Digite a senha do seu cartão de credito: ")
        if confirmar_a_senha == usuario_logado.cartãosenha:
            mais_balanço = int(input("Digite o quando deseja adicionar: "))
            usuario_logado.balanço += mais_balanço
            print(
                f"Ordem realiazada com sucesso! Você agora tem {usuario_logado.balanço} na sua conta")
            return usuario_logado  # testar se fica "grudado" a mudança - Pedro
        elif confirmar_a_senha != usuario_logado.cartãosenha and chances_pra_senha > 0:
            chances_pra_senha -= 1
            print(
                f"Essa senha está incorreta, tente novamnete {chances_pra_senha} tentativas restantes")
        elif chances_pra_senha == 0:
            print("tentativas esgotadas.")
            return
        else:
            print("returnando ao menu...")
            return

# 6 Adicione Produto: (admin only) checar o check na lista, não sei se é pel


def novo_produto(lista_produtos):
    produto = produtos()
    adicione_produto_nome = input(
        "Digite o numero do novo produto e seu nome: ")
    adicione_produto_marca = input("Digite a marca do novo produto: ")
    for i in range(len(lista_produtos)):
        if adicione_produto_nome == lista_produtos[i].nome and adicione_produto_marca == lista_produtos[i].marca:
            print("Esse produto ja existe")
            # continue?
            # talvez add uma opção de return se colocar pra dar continue
        else:
            confirme = input(
                f"Você está adicionando o produto {adicione_produto_nome} da marca '{adicione_produto_marca}', deseja continuar? Digite 'sim' para confirmar ou 'não' para retornar': ")
            if confirme == "sim" or confirme == "Sim":
                produto.nome = adicione_produto_nome
                produto.marca = adicione_produto_marca
                produto.valor = float(
                    input("Digite o preço do novo produto: "))
                produto.origem = input("Digite a origem do novo produto: ")
                lista_produtos.append(produto)
                print(
                    f"Produto {adicione_produto_nome} da marca {adicione_produto_marca} adicionado pelo valor de R${produto.valor}")
                return lista_produtos
            elif confirme == 'não' or confirme == 'Não':
                print("Produto não adicionado")
                return
            else:
                continue

# 7 Lista produtos


# chamar ela dentro das funções onde lista os produtos - Pedro
def listar_produtos(lista_produtos):
    for produtos in lista_produtos:
        print(produtos.nome, end=" da marca ")
        print(f"'{produtos.marca}'", end=" fabricado em ")
        print(produtos.origem, end=" por ")
        print(f"R${produtos.valor}")
        print()
    print()  # função pronta

# (numero a ser decidido) Adicionar item ao carrinho (testar) (adiconar a opção DO MENU para listar os produtos ou pelo menos a opção listar carrinho? seria legal pela integração, não precisar voltar ao menu e tals)

# versão nova, add um cria_produtos na opcao


def Add_Carrinho(usuario_logado, lista_usuarios, lista_produtos):
    selecione_produto = int(
        input("digite o numero do produto que deseja adicionar: "))
    if selecione_produto <= len(lista_produtos) + 1:
        # pra ir nos produtos certos, ja que o cliente não sabe que a listagem começa em "0"
        selecione_produto -= 1
        for i in range(len(lista_produtos)):
            if lista_produtos[selecione_produto]:
                # não sei pq n vai (antigo, testar se continua verdade) - Pedro
                print(lista_produtos[selecione_produto])
                BotaNoCarrinho = input(
                    "Deseja depositar esse produto no carrinho? Digite 'sim':")
                if BotaNoCarrinho == "sim" or BotaNoCarrinho == "Sim":
                    # testei rapidinho no vscode e pode ter esse negocio de 2 pontos, se der pau é por causa do cogido - pedro
                    usuario_logado.lista_carrinho.append(
                        lista_produtos[selecione_produto])
                    # qualquer caso bota um numero
                    print(
                        f"Produto {lista_produtos[selecione_produto].nome} adicionado ao carrinho")
                    return
                else:
                    print("Produto não adicionado.")
                    return
            else:
                print("Numero invalido.")
                return
    else:
        print("Numero invalido.")
        return

# 4 Carrinho de compras (testar) Adicionar item ao carrinho (testar) (adiconar a opção DO MENU para listar os produtos? seria legal pela integração, não precisar voltar ao menu e tals)


def listar_carrinho(lista_carrinho):
    for produtos in lista_carrinho:
        print(produtos.nome + " ", produtos.valor)
    print()

# 8 Login (TESTAR BEM)


def login(lista_usuarios, usuario_logado, nivel_de_permissão):
    Email = input("Digite o seu email: ")
    for i in range(len(lista_usuarios)):
        if Email == lista_usuarios[i].email:
            Senha = input("Digite a sua senha: ")
            for j in range(len(lista_usuarios)):
                if Senha == lista_usuarios[i].senha and Email == "AdminSuperFoda@MeuServiçoDeEmail.com":
                    print(f"Bem vindo(a) Admin {lista_usuarios[i].nome}!")
                    usuario_logado.nome = lista_usuarios[i].nome
                    usuario_logado.cpf = lista_usuarios[i].cpf
                    usuario_logado.email = lista_usuarios[i].email
                    usuario_logado.senha = lista_usuarios[i].senha
                    usuario_logado.limitecredito = lista_usuarios[i].limitecredito
                    usuario_logado.balanço = lista_usuarios[i].balanço
                    usuario_logado.cartãonumero = lista_usuarios[i].cartãonumero
                    usuario_logado.cartãosenha = lista_usuarios[i].cartãosenha
                    usuario_logado.lista_carrinho = lista_usuarios[i].lista_carrinho
                    nivel_de_permissão = 2
                    return lista_usuarios, usuario_logado, nivel_de_permissão
                elif Senha == lista_usuarios[i].senha:
                    print(f"Bem vindo(a) {lista_usuarios[i].nome}!")
                    usuario_logado.nome = lista_usuarios[i].nome
                    usuario_logado.cpf = lista_usuarios[i].cpf
                    usuario_logado.email = lista_usuarios[i].email
                    usuario_logado.senha = lista_usuarios[i].senha
                    usuario_logado.limitecredito = lista_usuarios[i].limitecredito
                    usuario_logado.balanço = lista_usuarios[i].balanço
                    usuario_logado.cartãonumero = lista_usuarios[i].cartãonumero
                    usuario_logado.cartãosenha = lista_usuarios[i].cartãosenha
                    usuario_logado.lista_carrinho = lista_usuarios[i].lista_carrinho
                    nivel_de_permissão = 1
                    return lista_usuarios, usuario_logado, nivel_de_permissão
            else:
                print("Senha incorreta")
        else:
            print("Esse email está incorreto e/ou não cadastrado")
            return


'''
#(numero a ser decidido) Login (TESTAR BEM)
def login(lista_usuarios, nivel_de_permissão): #botar uma variavel q = 0 (pode ser outra) por fora, dai no menu ter certas opções dizendo que são restritas para cadastrados (q = 1) ou admins (q = 2)
    Email = input("Digite o seu email: ")
    for i in range(len(lista_usuarios)): #tem que checar se o mesmo email e senha estão na mesma lista da matriz
        if Email == lista_usuarios[i].email:
            Senha = input("Digite a sua senha: ")
            for j in range(len(lista_usuarios)):
              if Senha == lista_usuarios[i].senha and Email == "AdminSuperFoda@MeuServiçoDeEmail.com":
                print(f"Bem vindo(a) Admin {lista_usuarios[i].nome}!")
                nivel_de_permissão = 2
                return 
              elif Senha in lista_usuarios[i].senha:
                print(f"Bem vindo(a) {lista_usuarios[i].nome}!")
                nivel_de_permissão = 1
                return #algo?
              else:
                print("Senha incorreta")
        else:
            print("Esse email está incorreto e/ou não cadastrado")
            return
        
        



        if Senha in ListaUsuariosMatrix[i][4] and Email == "AdminSuperFoda@MeuServiçoDeEmail.com": #vai checar se o i é o mesmo? Ou vai so ver se ambos existem? Caso a ultima opção não serve. talvez algum jeito de dar "lock" no """i""" com outra variavel ou algo do tipo?
            print(f"Bem vindo(a) Admin {ListaUsuariosMatrix[i][1]}!") #pode ser um admin feito manualmente, sem opção de virar um no programa
            #global q = 2 ##acho que uma varivel global não machuca
        elif Senha in ListaUsuariosMatrix[i][4]:
            print(f"Bem vindo(a) {ListaUsuariosMatrix[i][1]}!")
            #global q = 1
        else:
            print(f"Senha incorreta")


  
def novoproduto(listaprodutos): #podemos usar pra caso o admin queira adicionar/tirar produtos - Jonathan
    item = str(input("Digite  nome do novo produto: "))
    Item = produtos()
    InfoProduto = [] # variável talvez global - Jonathan
    Nome = item
    Marca = input("Digite a marca do produto: ")
    Valor = float(input("Digite o valor do produto: "))
    Origem = str(input("Digite a origem do produto: "))
    Item.nome = Nome
    Item.marca = Marca
    Item.valor = Valor
    Item.origem = Origem
    #for produto in listaprodutos: Brute force check pra n listar literalmente o mesmo produto? por mais que pudessem so vender por 1 centavo a menos e ngm notaria que ja existe
    #ListaProdutosClasse.append(produto)
    InfoProduto.append(Nome)
    InfoProduto.append(Marca)
    InfoProduto.append(Valor)
    InfoProduto.append(Origem)
    ListaProdutosMatrix.append(InfoProduto)

        #CarrinhoDessaPessoa.append(ListaProdutosMatrix[i])

'''

# Menu principal


def menu():
    while True:
        opcao = "-1"
        usuario_logado = usuarios()
        nivel_de_permissão = 0
        lista_usuarios = []
        lista_produtos = []
        nivel_de_permissão = 2  # por enquanto
        opcao = input("Olá, Seja bem vindo! Esse é o menu principal, escolha dentre as seguinte opções:\n\n1- Cadastro\n2- Consultar cliente\n3- Compra\n4- Carrinho de compras\n5- Pagar conta\n6- Adicionar item\n7- Listar produtos\n8- Login\n0- Sair\n")

        if opcao == "1":
            print("Opção selecionada: Cadastro")
            cadastramento(lista_usuarios, usuario_logado)

        elif opcao == "2":
            print("Opção selecionada: Consultar cliente")
            #usuario = usuarios()
            #usuario.cpf = 123
            lista_usuarios.append(usuario)
            consulta_cliente(lista_usuarios)

        elif opcao == "3":
            if nivel_de_permissão == 1 or nivel_de_permissão == 2:
                print("Opção selecionada: Compra")
                # ta aqui pra não printar de novo se o cliente errar o nome do produto - Pedro
                print(usuario_logado.lista_carrinho)
                compra(usuario_logado)  # usar a lista_carrinho dele
            else:
                print("Faça o login para acessar essa opção")

        elif opcao == "4":
            if nivel_de_permissão == 1 or nivel_de_permissão == 2:
                # ou fazer uma opção de so lista (ineficiente e o prof não vai gotar se não tiver integração de tu ja poder ir pro add_carrinho) ou ja ir pro add_carrinho
                print("Opção selecionada: Carrinho de compras")
                # (ja ir pro add_carrinho sendo o que prefiro)
                cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
                Add_Carrinho(usuario_logado, lista_produtos, lista_produtos)
            else:
                print("Faça o login para acessar essa opção")

        elif opcao == "5":
            if nivel_de_permissão == 1 or nivel_de_permissão == 2:
                print("Opção selecionada: Pagar conta")
                adicionar_balanço(usuario_logado)
            else:
                print("Faça o login para acessar essa opção")

        elif opcao == "6":
            if nivel_de_permissão == 2:
                print("Opção selecionada: Adicionar item")
                cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
                novo_produto(lista_produtos)
                listar_produtos(lista_produtos)
            elif nivel_de_permissão == 1:
                print("Essa opção é somente para admins")
            else:
                print("Faça o login para acessar essa opção")

        elif opcao == "7":
            if nivel_de_permissão == 1 or nivel_de_permissão == 2:
                print("Opção selecionada: Listar produtos")
                cria_produtos(lista_produtos)
                listar_produtos(lista_produtos)
            else:
                print("Faça o login para acessar essa opção")

        elif opcao == "8":  # LEIA: levando o usuario_logado junto pra dar um clear e deixar as pessoas trocar de conta mesmo sem logout, ler o ultimo comentario ainda dentro do menu
            if nivel_de_permissão == 0:
                print()
                if usuario_logado.nome != None:
                    are_you_sure = (
                        "Tem certeza? Usar essa opção fará você sair de sua conta atual. Digite 'sim' para confirmar: ")
                    if are_you_sure == "sim" or are_you_sure == "Sim":
                        print("Opção selecionada: Login")
                        login(lista_usuarios, usuario_logado, nivel_de_permissão)
                    else:
                        return
                else:
                    print("Opção selecionada: Login")
                    login(lista_usuarios, usuario_logado, nivel_de_permissão)
            else:
                print("Você já fez o Login")
                return

            # if nivel_de_permissão == 0:
                #print("Opção selecionada: Login")
                # forçar o cadastramento? tipo em um programa normal não precisariaa que, j ele sempre ta rodando no server e não precisa executar dnv pra
                #login(lista_usuarios, usuario_logado, nivel_de_permissão)
            # else:  # não dormir
                #print("Você já fez o Login")

        elif opcao == "0":
            print("Opção selecionada: Sair")
            break

        else:
            print("Opção inválida, tente novamente")


menu()

# if nivel_de_permissão == 0:
# print()
# if usuario_logado.nome != None:
# are_you_sure = (
# "Tem certeza? Usar essa opção fará você sair de sua conta atual. Digite 'sim' para confirmar: ")
# if are_you_sure == "sim" or are_you_sure == "Sim":
#print("Opção selecionada: Login")
#login(lista_usuarios, usuario_logado, nivel_de_permissão)
# else:
# return
# else:
#print("Opção selecionada: Login")
#login(lista_usuarios, usuario_logado, nivel_de_permissão)
# else:
#print("Você já fez o Login")
# return


# lista do que precisa fazer:
# 1: debug debug debug debug
# 2?: ver sobre colocar o usuario_logado em tudo que precisa e dar um clear na classe quando precisa (ja feito?)
# 3: (importante pra nota extra) adicionar o listar produtos e add carrinho nos lugar onde precisa, (dificil) => dar a chance do usuario ir de um pro outro(dar um return com uma variavel que muda a opção?) (penultimo)
# teve um bug bem maluco com esse codigo, vou deixar colado ele aq, tenta botar ele você na OPCAO do login