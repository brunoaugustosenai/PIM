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
    with open('usuarios.json', 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def salvar_dados(dados):
    usuarios = {}
    com_deficiencia = 0
    sem_deficiencia = 0

    for nome, info in dados.items():
        if not isinstance(info, dict):
            continue

        deficiencia = info.get("Deficiencia", "").lower()
        if deficiencia == "nenhuma":
            sem_deficiencia += 1
        else:
            com_deficiencia += 1

        usuarios[nome] = info

    usuarios["total_com_deficiencia"] = com_deficiencia
    usuarios["total_sem_deficiencia"] = sem_deficiencia

    with open('usuarios.json', 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)

def cadastrar_email():
    while True:
        email = input("Digite seu email: ").strip().lower()
        if any(isinstance(user, dict) and user.get("Email") == email for user in dados.values()):
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
    email = cadastrar_email()
    deficiencia = cadastrar_deficiencia()
    senha = cadastrar_senha()

    dados[nome] = {
        "Usuario": nome,
        "Email": email,
        "Deficiencia": deficiencia,
        "Senha": senha
    }

    salvar_dados(dados)
    print("✅ Usuário cadastrado com sucesso!")
    print("*" * 50)
