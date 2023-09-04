users = ['joão321','pedroMjz', 'Xiaolinmatadordeporco', 'admin', 'SiriusFxz']
passwords = ['Zeca321', 'PokerFace2323', 'Zetsu6012', 'admin', 'Crucio']

admin = False

def login(usuario, senha):
    for i in range(len(users)):
            if usuario == users[i] and senha == passwords[i]:
                return True
                
                
def register(usuario, senha):
    if usuario in users:
         return False
    else:
         users.append(usuario)
         passwords.append(senha)
         return True

registro= str(input("Você tem um registro?(Y/N) ")).upper().strip()

while registro == 'Y':
    print('=' * 30)
    user = str(input("Digite o Usuário: "))
    print('=' * 30)
    passW = str(input("Digite a senha: "))
    print('=' * 30)
    if(login(user, passW) == True):
        while user == 'admin':
            acesso = str(input('Deseja acessar as informações do usuário?(Y/N) ')).upper().strip()
            if acesso == 'Y':
                for i in range(len(users)):
                    print(f'User: {users[i]}',)
                    print(f'Password: {passwords[i]}')
                    print('=' * 30)
            elif acesso == 'N':
                break
            else:
                print('Por favor, digite um valor válido!')
        print("\nOlá, seja bem vindo!\n")
        print('=' * 30)
        break
    else:
        print("\nFalha no login, verifique seu usuário e sua senha!\n")
        print('=' * 30)
    
while registro == 'N':
        while True:
            print('=' * 30)
            userR = str(input("Digite o Usuário: "))
            print('=' * 30)
            checkUserR = str(input("Repita o Usuário: "))
            print('=' * 30)

            loginR = str(input("Digite a senha: "))   
            print('=' * 30)
            checkLoginR = str(input("Repita a senha: "))
            print('=' * 30)

            if userR == checkUserR and loginR == checkLoginR: 
                if(register(userR, loginR) == True):
                    register(userR, loginR)
                    break
                else:
                    print('=' * 30)
                    print("\nUsuário já existente!!!\n")
                    print('=' * 30)
            else:  
                print('=' * 30)
                print("\nO usuário ou a senha não batem! \n")
                print('=' * 30)

        while True:
             print('=' * 30)
             user = str(input("Digite o Usuário: "))
             print('=' * 30)
             passW = str(input("Digite a senha: "))
             print('=' * 30)

             if(login(user, passW) == True):
                print("\nOlá, seja bem vindo!\n")
                print('=' * 30)
                break
             else:
                print("\nFalha no login, verifique seu usuário e sua senha!\n")
                print('=' * 30)
        break

