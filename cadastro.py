import json
import os

def boas_vindas():
    print("\n" + "*" * 50)
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
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def salvar_dados(dados):
    with open('usuarios.json', 'w') as file:
        json.dump(dados, file, indent=4)

def cadastrar_email(dados):
    email = input("Digite seu email: ")
    if email in dados:
        print("Email já existe!")
        print("*" * 50)
        return None
    print("*" * 50)
    return email

def cadastrar_usuario():
    nome = input("Escolha um nome de usuário: ")
    print("*" * 50)
    return nome

def cadastrar_deficiencia():
    defic = input("Diga qual deficiência você possui (ou digite 'nenhuma'): ")
    print("*" * 50)
    return defic

def cadastrar_senha():
    senha = input("Escolha uma senha: ")
    print("*" * 50)
    return senha

if __name__ == "__main__":
    boas_vindas()
    dados = carregar_dados()

    email = cadastrar_email(dados)
    if email:
        nome = cadastrar_usuario()
        deficiencia = cadastrar_deficiencia()
        senha = cadastrar_senha()

        dados[email] = {
            "usuario": nome,
            "deficiencia": deficiencia,
            "senha": senha
        }

        salvar_dados(dados)
        print("✅ Usuário cadastrado com sucesso!")
        print("*" * 50)
