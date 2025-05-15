import json
import getpass
import os
import webbrowser
import pyttsx3

deficiencia_usuario_logado = None  

def falar(texto):
    if deficiencia_usuario_logado not in ["nenhuma", "auditiva"]:
        engine = pyttsx3.init('sapi5')
        engine.setProperty('volume', 1.0)
        engine.say(texto)
        engine.runAndWait()

def menu_login():
    print("" + "*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 14 + "SEJA BEM-VINDO(A)!" + " " * 16 + "*")
    print("*" + " " * 14 + "Faça seu Login!" +" " * 19 + "*")
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


def login():
    global deficiencia_usuario_logado
    dados = carregar_dados()
    print('\n')
    print("_" * 50)
    usuario = input("Nome de usuário: ").strip().lower()
    print("*" * 50)
    senha = getpass.getpass("Senha: ")
    print("*" * 50)

    for email, info in dados.items():
        if  info["usuario"] == usuario and info["senha"] == senha:
            print("✅ Login bem-sucedido!")
            print(f"Bem-vindo(a), {usuario}!")
            deficiencia_usuario_logado = info['deficiencia'].lower()
            print(f"Deficiência informada: {deficiencia_usuario_logado}")

            falar(f"Login realizado com sucesso. Bem-vindo ou bem-vinda, {usuario}")
            return

    print("❌ Nome de usuário ou senha incorretos.")
    return


def menu_materia():
    while True:
        print("*" * 50)
        texto_menu = (
            "--- Bem-vindo ao nosso sistema de educação inclusivo ---\n"
            "1. Lógica de Programação em Python\n"
            "2. Cibersegurança\n"
            "3. Tecnologia Da Informação\n"
            "4. Matemática e suas Tecnologias\n"
            "5. Sair"
        )
        print(texto_menu)
        print("*" * 50)

        falar("Escolha uma das matérias disponíveis: "
              "1 - Lógica de Programação em Python, "
              "2 - Cibersegurança, "
              "3 - Tecnologia da Informação, "
              "4 - Matemática e suas Tecnologias, "
              "ou 5 para sair.")

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            log_py()
        elif opcao == '2':
            cibersegurança()
        elif opcao == '3':
            TI()
        elif opcao == '4':
            matematica()
        elif opcao == '5':
            falar("Saindo do sistema. Até a próxima!")
            print('Saindo...')
            break
        else:
            print('Opção inválida!')
            falar("Opção inválida. Tente novamente.")

def log_py():
    texto = "Você escolheu Lógica de Programação em Python. Abrindo conteúdo no navegador..."
    print(texto)
    falar(texto)
    webbrowser.open("https://youtu.be/jBIPvXHRYpg?si=l74A98RrbQviakKk")

def cibersegurança():
    texto = "Você escolheu Cibersegurança. Abrindo conteúdo no navegador..."
    print(texto)
    falar(texto)
    webbrowser.open("https://youtu.be/KvPtIl-Gz2E?si=zgi65JPjRt-wxg3a")

def TI():
    texto = "Você escolheu Tecnologia da Informação. Abrindo conteúdo no navegador..."
    print(texto)
    falar(texto)
    webbrowser.open("https://youtu.be/-g1XrbcRC54?si=IOgvQ0G8ofnTGZQO")

def matematica():
    texto = "Você escolheu Matemática e suas Tecnologias. Abrindo conteúdo no navegador..."
    print(texto)
    falar(texto)
    webbrowser.open("https://www.youtube.com/watch?v=eioW24KwR00&list=PLr8_lF5KXtXoIe2f4JaxSAGRnNEilTtkp")

if __name__ == "__main__":
    menu_login()
    login()
    menu_materia()