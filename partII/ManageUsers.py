def perguntar():
    return input(
        'O que deseja realizar?\n' +
        '< I > - inserir um usuário\n' +
        '< P > - pesquisar um usuário\n' +
        '< E > - excluir um usuário\n' +
        '< L > - listar um usuário\n'
    ).upper()

def inserir(users):
    nome = input('nome: ' )
    idade = input('idade: ')
    email = input('email: ')
    login = input('login: ')
    users[login] = [nome, idade, email]

users = {}
opt = perguntar()

if opt == 'I':
    inserir(users)
    print(users)
    perguntar()
# elif opt == 'P':
#     pesquisar(users)
