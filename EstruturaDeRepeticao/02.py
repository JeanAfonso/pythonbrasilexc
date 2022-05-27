login = input('Usuario: ')
senha = input('Senha: ')

cont = 0


def valida(login, senha):
    valida_login = login.upper()
    valida_senha = senha.upper()
    if valida_senha == valida_login:
        print('A sua senha não pode ser igual ao login!')

        return False

    else:
        print('Senha validada com sucesso!')

        return True


while cont <= 5:
    val = valida(login, senha)
    if val:
        break
    else:
        cont += 1
        login = input('Usuario: ')
        senha = input('Senha: ')
