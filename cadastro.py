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
    while True:
        email = input("Digite seu email: ").strip().lower()
        # Verifica se o email já está cadastrado em algum usuário
        if any(user.get("Email") == email for user in dados.values()):
            print("Email já existe!")
        else:
            return email

def cadastrar_usuario(dados):
    while True:
        nome = input("Escolha um nome de usuário: ").strip().lower()
        if nome in dados:
            print("Nome de usuário já existe!")
            print("*" * 50)
        else:
            print("*" * 50)
            return nome

def cadastrar_deficiencia():
    print("Você possui alguma deficiência?")
    print("1 - Nenhuma")
    print("2 - Auditiva")
    print("3 - Visual")
    print("4 - Intelectual")
    print("5 - Outra")

    opcao = input("Escolha o número correspondente: ").strip()

    opcoes_deficiencia = {
        "1": "Nenhuma",
        "2": "Auditiva",
        "3": "Visual",
        "4": "Intelectual",
        "5": "Outra"
    }

    deficiencia = opcoes_deficiencia.get(opcao, "Nenhuma")
    print("*" * 50)

    if deficiencia == "Outra":
        deficiencia = input("Descreva a deficiência: ").strip()

    return deficiencia

def cadastrar_senha():
    senha = input("Escolha uma senha: ")
    print("*" * 50)
    return senha

if __name__ == "__main__":
    boas_vindas()
    dados = carregar_dados()

    nome = cadastrar_usuario(dados)
    email = cadastrar_email(dados)
    deficiencia = cadastrar_deficiencia()
    senha = cadastrar_senha()

    dados[nome] = {
        "Email": email,
        "Deficiência": deficiencia,
        "Senha": senha
    }

    salvar_dados(dados)
    print("✅ Usuário cadastrado com sucesso!")
    print("*" * 50)
