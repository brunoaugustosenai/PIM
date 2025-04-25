import json
import getpass
import os
import webbrowser
def boas_vindas():
    print("\n" + "*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 14 + "Faça seu Login!" + " " * 19 + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)

def carregar_dados():
    if not os.path.exists('usuarios.json'):
        return {}
    with open('usuarios.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def login():
    dados = carregar_dados()
    print('\n')
    print("_" * 50)
    email = input("Email: ")
    print("*" * 50)
    senha = getpass.getpass("Senha: ")
    print("*" * 50)

    if email in dados and dados[email]["senha"] == senha:
        print("✅ Login bem-sucedido!")
        print(f"Bem-vindo(a), {dados[email]['usuario']}!")
        print(f"Deficiência informada: {dados[email]['deficiencia']}")
    else:
        print("❌ Email ou senha incorretos.")
        return
def menu():
    while True:
        print('\n****************************')
        print('--- Bem-vindo ao nosso sistema de educação inclusivo ---')
        print('1. Lógica de Programação em Python')
        print('2. Cibersegurança')
        print('3. Banco de Dados')
        print('4. Matemática')
        print('5. Sair')
        print('****************************')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            log_py()
        elif opcao == '2':
            print("Conteúdo de Cibersegurança em construção...")
        elif opcao == '3':
            print("Conteúdo de Banco de Dados em construção...")
        elif opcao == '4':
            print("Conteúdo de Matemática em construção...")
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
def log_py():
    print("Você escolheu Lógica de Programação em Python.")
    print("Abrindo conteúdo no navegador...")
    webbrowser.open("https://www.letras.mus.br/guns-n-roses/88835/")


if __name__ == "__main__":
    boas_vindas()
    login()
    menu()