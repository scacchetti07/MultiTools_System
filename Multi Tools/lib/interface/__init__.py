from lib.skills import *
from time import sleep
code = 1010

c = {'Vazio':'\033[m','Azul':'\033[1;34m','Verde':'\033[1;32m','Ciano':'\033[1;36m','Vermelho':'\033[1;31m','Amarelo':'\033[1;33m','Roxo':'\033[1;35m'}

def titulo(txt='',cor='Vazio'):
    print(c[cor],end='')
    print('═'*40)
    print(txt.center(40))
    print('═'*40)
    print(c["Vazio"],end='')


def titulo_musica(txt='',cor='Vazio'):
    msg = len(txt) + 8
    print(c[cor],end='')
    print('⚎'*msg)
    print(txt.center(msg))
    print('⚎'*msg)
    print(c['Vazio'],end='')


def menu(lista=[],cor='Vazio'):
    while True:
        for i,v in enumerate(lista):
            print(c[cor],f'[ {i+1} ]',c['Vazio'],end='')
            print(f'{v}')
            sleep(0.5)
        resp = lib.skills.int2(' \033[32mEscolha uma das opções:\033[m ')
        return resp


def playermenu(musica,nome):
    import pygame
    plmp3 = {'Play/Pausar':'⏵⏸','Pular':'⏭','Voltar':'⏮','Loop': ' ↻','Reiniciar': '⇄','Parar':'⏹'}
    while True:
        print("\033c", end="") # Limpa Terminal
        song = musica.split('.mp3')
        titulo_musica(f' TOCANDO AGORA \033[4m{song[0]}\033[m\033[1;36m NO PLAYER MP3 \n','Ciano')
        print(f'\n{song[0].center(41)}')
        print('─'*40,lensong(musica,nome))
        print('\033[1;32m     ⇄           ⏮ ⏵⏸ ⏭           ↻\033[m')
        print(f'\033[1;33mVolume \033[1;36m♬ \033[m: \033[1;35m{(pygame.mixer.music.get_volume() * 100):.0f} %\033[m\n'.center(69))
        c = 0
        for k,i in plmp3.items():
            if c < 2:
                print(f'\033[1;36m{i:<3}\033[m \033[1;33m{k:>2}\033[m\t',end= '│ ')
                c+=1
            else:
                print(f'\033[1;36m{i:<3}\033[m \033[1;33m{k:>2}\033[m')
                c = 0
        resp = input('\033[1;34m\nEscolha uma ação: \033[m').strip().capitalize()
        if resp == "1010":
            resp = int(resp)
            seguranca(resp)
        else:
            sleep(1.5)
            return resp


def alertcode():
    code = "\033[4;36m1010\033[m\033[1;33m"
    erro = "\033[1;31mINESPERADO\033[1;33m"
    ime = "\033[1;31mIMEDIATAMENTE\033[1;33m"
    encerrar = "\033[1;31mENCERRAR\033[1;33m"
    atencao = "\033[1;36m⚠ ATENÇÃO ⚠\033[1;33m"
    print("\033[1;33m")
    print("⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌")
    print(" ┃                                                                         ┃")
    print(f" ┃                               {atencao}                               ┃")
    print(" ┃                                                                         ┃")
    print(f" ┃   CASO O CÓDIGO ENTRE EM LOOPING OU OCORRA ALGUM PROBLEMA {erro}    ┃")
    print(f" ┃          DIGITE {code} PARA {encerrar} O SISTEMA {ime}.             ┃")
    print(" ┃                                                                         ┃")
    print("⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌")
    print("\033[m")
    sleep(5)


def hora():
    from datetime import datetime
    hr = datetime.now().hour
    if 6 <= hr < 12:
        return '\033[1;33mBom dia!\033[m'
    elif 12 <= hr < 18:
        return '\033[1;31mBoa tarde!\033[m'
    else:
        return '\033[1;35mBoa Noite!\033[m'
