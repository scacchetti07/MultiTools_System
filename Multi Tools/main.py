from lib.interface import *
from lib.opc import *
from lib.skills import *

print("\033c", end="") # Limpa Terminal
titulo(' PÁGINA DE LOGIN ','Ciano')
while True:
    nome = input('Digite seu nome para começarmos: ').title()
    if nome == '' or len(nome) == 1:
        print('\033[1;31mERRO! Digite um nome válido.\033[m')
    else:
        break
sleep(1.5)

if lib.opc.perfil(nome):
    print(f'\033[1;34m\nCriando um Perfil somente para você \033[1;33m{nome.title()}!\033[m')
    sleep(1.5)
    print('\033[1;36mEstamos montando um espaço completo para você...\033[m')
    sleep(1.5)
else:
    print(f'\033[1;36m\nBem vindo de volta \033[1;33m{nome.title()}\033[m\033[1;36m!\033[m')
    sleep(1.5)
    print('\033[1;36mEstamos remontando o espaço para você.\033[m')
    sleep(1.5)

print("\033c", end="") # Limpa Terminal
alertcode() # Mensagem de alerta sobre código de segurança.

while True:
    print("\033c", end="") # Limpa Terminal
    titulo(f'   🪐 {nome.upper()} MULTI TOOLS 🪐   ','Azul')
    sleep(1)
    print(f' Olá \033[1;34m{nome.title()}, {hora()}\033[m')
    sleep(0.5)
    resp = menu(['Cadastro de Pessoas', 'Calculadora', 'Bloco de Anotações','MP3 Player','Sair do Programa'],'Ciano') # adicionar a função de relógio digital na v2.0 usando TKINTER
    match resp:
        case 1:
            titulo(' 📓 ACESSANDO CADASTRO DE PESSOAS 📓 ','Amarelo')
            sleep(3)
            print("\033c", end="") # Limpa Terminal
            registro2(nome)
        case 2:
            titulo(' 🧮 ACESSANDO CALCULADORA 🧮 ','Roxo')
            sleep(3)
            print("\033c", end="") # Limpa Terminal
            calculadora(nome)
        case 3:
            titulo(' 📝 ACESSANDO ANOTAÇÕES 📝 ','Verde')
            sleep(3)
            print("\033c", end="") # Limpa Terminal
            bloco(nome)
        case 4:
            titulo(' 🎸 ACESSANDO PLAYER MP3 🎸 ','Azul')
            sleep(3)
            print("\033c", end="") # Limpa Terminal
            mp3(nome)      
        case 5:
            titulo(' 🛑 ENCERRANDO O MULTI TOOLS 🛑 ','Vermelho')
            sleep(3)
            print(f"\033[1;33mTchau {nome}! Nós da MULTI TOOLS, estaremos ansiosamente esperando seu retorno.\033[m")
            break
        case _:
            print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
            print("\033c", end="") # Limpa Terminal
    