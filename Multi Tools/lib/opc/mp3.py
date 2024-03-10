from lib.skills import *
from lib.interface import *

def mp3(nome='DESCONHECIDO'):
    while True:
        print("\033c", end="") # Limpa Terminal
        pasta = 'mp3player'
        usrdir = f'Playlists de {nome}'
        criarpasta(pasta,usrdir)
        titulo(f'       🎼 PLAYER MP3 by \033[4m{nome.upper()}\033[m\033[1;34m 🎼','Azul')
        sleep(0.8)
        r = menu(['Criar nova Playlist','Ver playlists','Tocar uma música aleatória','Baixar novas músicas',f'Voltar para \033[1;36m{nome.upper()} MULTI TOOLS\033[m'],'Vermelho')
        match r:
            case 1:
                titulo(' 📂 CRIANDO SUA NOVA PLAYLIST 📂 ','Roxo')
                sleep(1.5)
                mp3playlist(usrdir,nome)
            case 2:
                titulo(' 📁 LISTANDO AS SUAS PLAYLISTS 📁 ','Roxo')
                sleep(1.5)
                verplaylist(nome)
            case 3:
                titulo('    🎧 ESCOLHENDO UMA MÚSICA ALEATÓRIA... 🎧  ','Verde')
                sleep(1.5)
                random_musica(nome)
            case 4:
                titulo(' 💾 ACESSANDO CAMPOS DE DOWNLOAD 💾 ','Amarelo')
                sleep(1.5)
                downloadyt(nome)
            case 5:
                titulo(f'  🛑 VOLTANDO PARA O \033[1;36m{nome.upper()} MULTI TOOLS\033[1;31m 🛑 ','Vermelho')
                sleep(1)
                break
            case _:
                print('\033[1;31m Digite uma opção VÁLIDA.\033[m')
        