import json
import getpass
import os

def carregar_dados():
    if not os.path.exists('usuarios.json'):
        return {}
    with open('usuarios.json', 'r') as file:
        return json.load(file)

def login():
    dados = carregar_dados()
    username = input("Nome de usuário: ")
    password = getpass.getpass("Senha: ")
    if dados.get(username) == password:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

if __name__ == "__main__":
    login()