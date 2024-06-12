lista = []
nome = str(input('Qual o seu nome? '))
cargo = str(input('Usuario ou administrador? '))
if cargo.upper() == 'USUARIO':   
    while True:
        print(f'Olá, {nome}')
        print('1. Pesquisar produto \n2. Catalogo de produtos \n3. Carrinho de compras \n4. Sair')
        opc = str(input('Qual a opção desejada? '))
        if opc == '1':
            print('')
            print('Pesquisar produto:')
            print('')


        elif opc == '2':
            print(' ')
            print('Catalogo de produtos:')
            print(' ')
            for i in range(len(lista)):
                print(f"{i} - {lista} '\n'")
        elif opc == '3':
            print(' ')
            print('Carrinho de compras:')
            print(' ')
        elif opc == '4':
            print('Obrigado por acessar o sistema')
            break
        elif opc != '1' and opc != '2' and opc != '3' and opc != '4':
            print(' ')
            print(' ')
            print(' ')
            print('Opção invalida')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
elif cargo.upper() == 'ADMINISTRADOR':
    login = str(input('Insira o seu usuario: '))
    senha = str(input('Insira a sua senha: '))
    adm = 'ADMIN'
    sen = '1234'
    if login.upper() == adm and senha == sen:
        print('lerolero')
    else:
        print('Usuario ou senha incorreto')
        ten = str(input('Deseja tentar novamente? S/N '))
        if ten.upper() == 'S':
            login = str(input('Insira o seu usuario: '))
            senha = str(input('Insira a sua senha: '))
            if login.upper() == adm and senha == sen:
                print('Conectado')