import json
import os

def boas_vindas():
    print("\n" + "*" * 51)
    print("*" + " " * 48 + "*")
    print("*" + " " * 14 + "SEJA BEM-VINDO(A)!" + " " * 16 + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print()
    print("🔐 Sistema de Login e Cadastro de Usuários 🔐")
    print("🧠 Desenvolvido com Python 🧠 ")
    print("\n" + "-" * 50 + "\n")


def carregar_dados():
    if not os.path.exists('usuarios.json'):
        return {}
    with open('usuarios.json', 'r') as file:
        return json.load(file)

def salvar_dados(dados):
    with open('usuarios.json', 'w') as file:
        json.dump(dados, file)

def cadastrar_usuario():
    dados = carregar_dados()
    username = input("Escolha um nome de usuário: ")
    if username in dados:
        print("Usuário já existe!")
        return
    password = input("Escolha uma senha: ")
    dados[username] = password
    salvar_dados(dados)
    print("Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    boas_vindas()
    cadastrar_usuario()
