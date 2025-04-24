import json
import getpass
import os
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

if __name__ == "__main__":
    boas_vindas()
    login()
