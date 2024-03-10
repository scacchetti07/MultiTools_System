import lib.interface
from lib.skills import *
from moviepy.editor import *
from pygame import mixer
from time import sleep

def int2(txt='Digite um valor: ',code=1010):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f'\033[1;31m ERRO! NÃO FOI DIGITADO UM NÚMERO!\033[m')
        except (KeyboardInterrupt):
            print("\033[1;34mCOMANDO DESABILITADO! Caso necessário, digite \"1010\".\033[m")
        else:
            if num == code:
                seguranca(num)
            else:
                return num


def seguranca(txt,code=1010):
    # possivelmente adicionar uma opção de personalizar o código de segurança
    from os import kill,getpid
    from signal import SIGTERM
    if txt == code:
        try:
            pid = getpid()
            print("\033[1;41mPROGRAMA ENCERRADO PELO CÓDIGO DE SEGURANÇA.\033[m")    
            kill(pid,SIGTERM)       
        except OSError:
            print("Falha o sair do sistema.")         
        except Exception as e:
            print(f"Erro: {e}")
    else:
        return None
    

def verifSN(msg='Quero continuar [S/N]? ',code="1010"):
    while True:
        try:
            resp = input(msg).strip().upper()
        except (KeyboardInterrupt):
            print("\033[1;34mCOMANDO DESABILITADO! Caso necessário, digite \"1010\".\033[m")
        else:
            if resp == code:
                resp = int(resp)
                seguranca(resp)
            elif resp not in 'SN' or resp == '':
                print('\033[1;31mERRO! Digite uma opção válida.\033[m')
            else:
                return resp


def criarpasta(pasta,usrdir):
    import os
    if os.path.exists(f'lib\\opc\\{pasta}\\{usrdir}') == False:
        try:
            os.mkdir(f'lib\\opc\\{pasta}\\{usrdir}')
        except FileExistsError:
            print(end='')
        except:
            print('\033[1;31mOcorreu um erro ao criar o diretório.\033[m')
        else:
            print(f'\033[1;32mNovo diretório \"{usrdir}\" criado com SUCESSO!\033[m')


def removerarquivo(nome='Untitled.txt',fold='Pasta',usrdir='Notas de DESCONHECIDO'):
    import os
    try:
        os.remove(f'lib\\opc\\{fold}\\{usrdir}\\{nome}')
        sleep(2)
    except Exception as e:
        print('\033[1;31mERRO! Não foi possível remover o arquivo desejado!\033[m')
        # print(f'Erro ocorrido: {e}')
        sleep(1)
    else:
        return True
    

# Bloco de Notas

def criarNotas(arquivo='Untitled.txt',pasta='temp',usrdir='Notas de Desconhecido'):
    try:
        a = open(f'lib\\opc\\{pasta}\\{usrdir}\\{arquivo}','x+',encoding="utf-8")
        a.close()
    except (FileExistsError):
        print(end='')
    except (FileNotFoundError):
        print(f'\033[31mO Arquivo "{arquivo}" não foi encontrados no Sistema\033[m')
    else:
        print(f'\033[1;32mO Arquivo {arquivo} foi criado com SUCESSO!!\033[m')


def veranot(nome='Untitled.txt',usrdir='Notas de DESCONHECIDO'):
    try:
        a = open(f'lib\\opc\\Anotacoes\\{usrdir}\\{nome}','r')
    except (FileNotFoundError):
        print('\033[1;31mERRO! O arquivo escrito não existe no sistema!\033[m')
        return False
    else:
        lib.interface.titulo(f'       ANOTAÇÃO \033[4m{nome}\033[m\033[1;33m       ','Amarelo')
        sleep(1)
        for l in a.readlines():
            print(l.strip())
        print()
        return True


def editaranot(msg='',nome='Untitled.txt',usrdir='Notas de Desconhecido'):
    try:
        a = open(f'lib\\opc\\Anotacoes\\{usrdir}\\{nome}','a',encoding="utf-8")
    except:
        print(f'\033[1;31mOcorreu um erro ao abrir o arquivo {nome}\033[m')
    else:
        try:
            a.write(f'{msg}\n')
        except:
            print('\033[1;31mOcorreu um erro ao escrever a mesnsagem no arquivo.\033[m')
        else:
            print('\033[1;32mTexto adicionado com sucesso!\033[m')
            sleep(1.5)
    finally:
        a.close()


# Registro de Usuários

def criarCadastro(arquivo='Untitled.txt',pasta='temp'):
    try:
        a = open(f'lib\\opc\\{pasta}\\{arquivo}','x+',encoding="utf-8")
        a.close()
    except (FileExistsError):
        print('',end='')
    except (FileNotFoundError):
        print(f'\033[31mO Arquivo "{arquivo}" não foi encontrados no Sistema\033[m')
    else:
        print(f'\033[1;32mO Arquivo {arquivo} foi criado com SUCESSO!!\033[m')


def registrar(dados,nome='DESCONHECIDO'):
    try:
        a = open(f'lib\\opc\\Registros\\Cadastros de {nome}.txt','a',encoding="utf-8")
    except:
        print('\033[1;31mOcorreu um ERRO ao abrir a lista de Registro!\033[m')
        sleep(1.5)
    else:
        try:
            a.write(f'════════════════════| Dados de {dados["Nome:"]} |════════════════════\n')
            for k,e in dados.items():
                a.write(f"\t{k:<30} \t\t{e:>5}\n")
        except Exception: 
            print('\033[1;31mOcorreu um ERRO ao registrar os dados na lista\033[m')
            sleep(1.5)
        else:
            print(f'\n\033[1;32mDados de \"{dados["Nome:"]}\" foram SALVOS com sucesso!!\033[m')
            sleep(1.5)
    finally:
        a.close()


def leiaregistros(nome='DESCONHECIDO'):
    try:
        a = open(f'lib\\opc\\Registros\\Cadastros de {nome}.txt','r',encoding="utf-8")
    except FileExistsError:
        print(end='')
    except:
        print('\033[1;31mOcorreu um ERRO ao abrir o arquivo\033[m')
    else:
        for l in a.readlines():
            print(l.strip())
            sleep(0.5)


# Mp3 Player
            
def removermp4(nome,path):
    import os
    try:
        os.remove(f'{path}\\{nome}')
        sleep(2)
    except Exception as e:
        print('\033[1;31mERRO! Não foi possível remover o arquivo desejado!\033[m')
        print(f'Erro ocorrido: {e}')
        sleep(1)
    else:
        return True


def addmusica(usrdir,nome,playlist):
    from shutil import copy2
    from os import listdir
    default = listdir(f'lib\\opc\\mp3player\\Playlists de {nome.title()}\\Musicas de {nome.title()}')
    if playlist == f"Musicas de {nome.title()}":
        return "ofc"
    else:
        for i,m in enumerate(default):
            print(f"\033[1;36m[ {i+1} ]\033[m \033[4m{m}\033[m")
            sleep(0.3)
        mus = int2("\nDigite a \033[1;36mposição\033[m da música para adicionar (Digite \033[1;34m0\033[m para voltar ao menu): ")
        if mus == 0:
            return False
        elif mus > len(default):
            print("\033[1;31mPosição Incorreta! Tente novamente.\033[m")
            sleep(0.4)
        else:
            try:
                copy2(f"lib\\opc\\mp3player\\{usrdir}\\Musicas de {nome.title()}\\{default[mus-1]}", f"lib\\opc\\mp3player\\{usrdir}\\{playlist}")
            except (FileExistsError):
                print('\033[1;32mA música escolhida já está adicionada na playlist\033[m')
            except:
                print("Ocorreu um erro ao adicionar a música na playlist")
                sleep(1.4)
            else:
                print(f"\033[1;32mMúsica \033[1;34m{default[mus-1]}\033[1;32m adicionada na playlist \033[1;35m{playlist}\033[1;33m, com SUCESSO!\033[m")
                default.remove(default[mus-1])
                sleep(1.7)


def removermus(usrdir,nome,playlist):
    from os import listdir,remove
    default = listdir(f'lib\\opc\\mp3player\\Playlists de {nome.title()}\\{playlist}')
    caminho = f"lib\\opc\\mp3player\\{usrdir}\\{playlist}"
    if playlist == f"Musicas de {nome.title()}":
        return None
    else:
        while True:
            for i,m in enumerate(default):
                print(f"\n\033[1;36m[ {i+1} ]\033[m \033[4m{m}\033[m")
                sleep(0.3)
            mus = int2("\nDigite a \033[1;36mposição\033[m da música para remover (Digite \033[1;34m0\033[m para voltar ao menu): ")
            if mus == 0:
                return None
            elif mus > len(default):
                print("\033[1;31mPosição Incorreta! Tente novamente.\033[m")
                sleep(0.4)
            else:
                break
        ch = verifSN("Tem certeza que quer remover está música? [\033[1;32mS\033[m/\033[1;31mN\033[m]")
        if ch == "N":
            return None
        else:
            try:
                remove(f"{caminho}\\{default[mus-1]}")
            except (FileNotFoundError):
                print(f"A música {default[mus-1]} não foi encontrada na playlist.")
            except:
                print("ERRO! Ocorreu um problema durante a remoção da música.")
            else:
                print(f"\033[1;32mA música \033[4;33m{default[mus-1]}\033[m\033[1;32m foi removida com sucesso!\033[m")


def playermp3(musica,nome,playlist=f"Musicas de DESCONHECIDO",opc=False):
    lib.interface.titulo_musica(f'TOCANDO AGORA ⇉ {musica.upper()}','Ciano')
    sleep(0.5)
    mixer.init()
    if opc == False:
        caminho = f'lib\\opc\\mp3player\\Playlists de {nome.title()}\\Musicas de {nome}'
        mixer.music.load(f'{caminho}\\{musica}')
    else:
        caminho = f'lib\\opc\\mp3player\\Playlists de {nome.title()}'
        mixer.music.load(f'{caminho}\\{playlist}\\{musica}')    
    mixer.music.play()
    while True:
        resp = lib.interface.playermenu(musica,nome)
        match resp:
            case 'Play' | 'Iniciar':
                mixer.music.unpause()
                print('\033[1;32mMÚSICA INICIADA\033[m')
            case 'Pausar' | 'Pause':
                mixer.music.pause()
                print('\033[1;32mMÚSICA PAUSADA!\033[m')
            case 'Volume' | 'Sound':
                while True:
                    v = input('\033[1;34mDigite a \033[1;33m\" % \"\033[1;34m do volume: \033[m')
                    if v.isalpha():
                        print('\033[mLETRAS NÃO SÃO VÁLIDAS! Tente Novamente.\033[m')
                    else:
                        v = float(v)
                        break
                if v < 0:
                    v * -1
                vol = v / 100
                mixer.music.set_volume(vol)
            case 'Pular' | 'Skip':
                mixer.music.stop()
                mixer.music.play() # Fazer a lógica do skip button
                print('\033[1;32mMÚSICA PULADA!\033[m')
            case 'Voltar' | 'Back':
                print('\033[1;32mVOLTANDO A MÚSICA!\033[m')
                mixer.music.stop()
                mixer.music.play() # Fazer a lógica do back button
            case 'Loop' | 'Looping':
                mixer.music.play(-1)
                print('\033[1;32mA MÚSICA ESTÁ EM LOOPING!\033[m')
                sleep(1.3)
            case 'Reiniciar' | 'Restart':
                print('\033[1;32mREINICIANDO A MÚSICA!\033[m')
                sleep(1.3)
                mixer.music.rewind()
            case 'Parar' | 'Stop':
                mixer.music.stop()
                print('\033[1;31mMÚSICA ENCERRADA.\033[m')
                sleep(1)
                print("\033c", end="") # Limpa Terminal
                break
            case _:
                print('\033[1;31mDIGITE UMA OPÇÃO CORRETA.\033[m')
                continue
    quit()


def lensong(musica,nome):
    lensong = mixer.Sound(f'lib\\opc\\mp3player\\Playlists de {nome}\\Musicas de {nome}\\{musica}').get_length()
    song_time = lensong
    song_min = int(song_time // 60)
    song_sec = int(song_time % 60)
    song_fmt = "{:02d}:{:02d}".format(song_min, song_sec)
    
    return song_fmt


def downloadyt(nome='DESCONHECIDO',code="1010"):
    from pytube import YouTube
    from googleapiclient.discovery import build
    import os
    caminho = f'lib\\opc\\mp3player\\Playlists de {nome.title()}\\Musicas de {nome.title()}'

    try:
        os.mkdir(caminho)
    except (FileExistsError):
        print(f'Diretório para Download de músicas: \033[1;34mMusicas de {nome.title()}\033[m')
    except:
        print('\033[1;31mOcorreu um ERRO ao criar o diretório de download! Tente novamente.\033[m')
    else:
        print('\033[1;32mO diretório de downloads foi criado com SUCESSO!\033[m')

    def videoid(video_nome):
        API_KEY = 'AIzaSyByXO11YY42NkRt6zvpjLzCLwozL7KV2-A'
        ytapi = build('youtube', 'v3', developerKey=API_KEY)
        busca = ytapi.search().list(q=video_nome,part='id',maxResults=1)
        
        resp = busca.execute()
        if 'items' in resp:
            for i in resp['items']:
                if i['id']['kind'] == 'youtube#video':
                    return i['id']['videoId']
        return None

    def mp4tomp3(mp4,mp3):
        fconvert = AudioFileClip(mp4)
        fconvert.write_audiofile(f'{caminho}\\{mp3}')
        fconvert.close()

    while True:
        sleep(1)
        print("\033[1;31mDigite \033[4;31m\"0\"\033[1;31m para voltar ao menu.\033[m")
        video = input('Digite o \033[1;36mnome da música\033[m que deseja baixar: ')
        if video == "0":
            break
        elif video == code:
            video = int(video)
            seguranca(video)
        else:
            ytid = videoid(video)
            if ytid:
                try:
                    yt = YouTube(f'https://www.youtube.com/watch?v={ytid}')
                    yt.streams.filter(only_audio=True).first()
                    play = yt.streams.get_by_itag(140)
                    print('\033[1;33mEstamos fazendo o DOWNLOAD da sua música, agurde um momento...\033[m') 
                    v = play.download(caminho)
                    mp4 = v.split('\\')
                    mp4tomp3(v,f'{video}.mp3')
                    removermp4(mp4[10],caminho)                 
                except Exception as e:
                    print('\033[1;31mOcorreu um ERRO durante o download do vídeo.\033[m')
                    # print(f'Erro encontrado: {e}')
                else:
                    print(f'\033[1;32mO Download do vídeo \033[4;33m{video}\033[m\033[1;32m teve SUCESSO!\033[m')
                    r = verifSN('Quer baixar outra música [\033[32mS\033[m/\033[31mN\033[m]? ')
                    if r == 'N':
                        break
            else:
                print('\033[1;31mVÍDEO NÃO ENCONTRADO.\033[m')
    

def random_musica(nome='Desconhecido'):
    from random import choice
    import os
    musicas = os.listdir(f'lib\\opc\\mp3player\\Playlists de {nome}\\Musicas de {nome}')
    sleep(1.2)
    print('\033[1;33mEstamos escolhendo a música \033[4maleatoriamente\033[m\033[1;33m entre as playlists...\033[m')
    play = choice(musicas)
    sleep(3)
    print('\033[1;33mMÚSICA ESCOLHIDA!!\033[m')
    sleep(1)
    playermp3(play,nome,opc=False)


def mp3playlist(usrdir,nome,code="1010"):
    from os import mkdir,listdir
    from shutil import copy2
    while True:
        playlist = input("Digite o \033[1;36mnome\033[m da sua nova playlist (Digite \033[1;31m0\033[m para voltar ao menu): ")
        if playlist == "0":
            break
        elif playlist == code:
            playlist = int(playlist)
            seguranca(playlist)
        else:
            try:
                mkdir(f"lib\\opc\\mp3player\\{usrdir}\\{playlist}")
            except FileExistsError:
                print("\033[1;31mERRO: Existe uma playlist com o mesmo nome digitado! Tente novamente.\033[m")
                sleep(0.4)
            except:
                print("\033[1;31mOcorreu um erro ao criar sua playlist!\033[m")
                break
            else:
                print("\033[1;32mA playlist foi criada com SUCESSO!\033[m")
                sleep(1.3)
                break
    if playlist != "0":
        try:
            totalm = listdir(f"lib\\opc\\mp3player\\{usrdir}\\Musicas de {nome}")
        except (FileNotFoundError):
            print("\033[1;33mVocê ainda não possuí músicas baixadas! Vá na opção \033[1;31m4\033[1;33m para baixar.\033[m")
            sleep(1.2)
        else:
            while True:
                print("\033c", end="") # Limpa Terminal
                lib.interface.titulo_musica("MUSICAS BAIXADAS","Azul")
                for i,m in enumerate(totalm):
                    print(f"\033[1;36m[ {i+1} ]\033[m \033[4m{m}\033[m")
                    sleep(0.3)
                mus = int2("\nDigite a \033[1;36mposição\033[m da música para adicionar (Digite \033[1;34m0\033[m para voltar ao menu): ")
                if mus == 0:
                    break
                if mus > len(totalm):
                    print("\033[1;31mPosição Incorreta! Tente novamente.\033[m")
                    sleep(0.4)
                else:
                    try:
                        copy2(f"lib\\opc\\mp3player\\{usrdir}\\Musicas de {nome}\\{totalm[mus-1]}", f"lib\\opc\\mp3player\\{usrdir}\\{playlist}")
                    except Exception as e:
                        print("Ocorreu um erro ao adicionar a música na playlist")
                        # print(f"Erro: {e}")
                        sleep(1.4)
                    else:
                        print(f"\033[1;32mMúsica \033[1;34m{totalm[mus-1]}\033[1;32m adicionada na playlist \033[1;35m{playlist}\033[1;33m, com SUCESSO!\033[m")
                        totalm.remove(totalm[mus-1])
                        sleep(1.7)
    

def verplaylist(nome):
    from os import listdir
    from shutil import rmtree
    usrdir = f'Playlists de {nome.title()}'
    caminho = f'lib\\opc\\mp3player\\{usrdir}'
    try:
        lstplay = listdir(caminho)
    except (FileNotFoundError):
        print('\033[1;31mNão foi criado nenhuma playlist no momento, tente criar uma na \033[1;36m1° opção\033[m.')
        sleep(1.2)
    except:
        print('\033[1;31mOcorreu um ERRO no sistema ao tentar abrir o arquivo\033[m')
    else:
        while True:
            print("\033c", end="") # Limpa Terminal
            lib.interface.titulo_musica("PLAYLISTS CRIADAS","Roxo")
            for i,e in enumerate(lstplay):
                print(f'\033[1;36m[ {i+1} ]\033[m {e}')
                sleep(0.5)
            print("\n\033[1;31mDigite \033[1;33m\"-1\"\033[1;31m para entrar no menu de remoção\033[m")
            play = int2('Digite a \033[1;36mposição\033[m da playlist para visualizar (Digite \033[1;31m0\033[m para voltar ao menu): ')
            if play == 0:
                break
            if play == -1:
                while True:
                    print("\033c", end="") # Limpa Terminal
                    lib.interface.titulo_musica("PLAYLISTS DISPONÍVEIS","Amarelo")
                    for i,e in enumerate(lstplay):
                        print(f'\033[1;36m[ {i+1} ]\033[m {e}')
                        sleep(0.45)
                    print('-'*40)
                    while True:
                        rem = int2("Digite a \033[1;36mposição\033[m da playlist que deseja remover (Digite \033[4;31m0\033[m para sair): ")
                        if rem == 0:
                            return None
                        elif rem > len(lstplay) or rem < 1:
                            print("\033[1;31mERRO: Posição inexistente. Tente Novamente\033[m\n")
                        elif lstplay[rem-1] == f"Musicas de {nome.title()}":
                            print("\033[1;31mEssa playlist não pode ser excluída.\033[m\n")
                        else:
                            break
                    try:
                        rmtree(f"{caminho}\\{lstplay[rem-1]}")
                    except (FileNotFoundError) :
                        print("\033[1;31mA playlist escolhida não foi encontrada no sistema\033[m")
                    except Exception:
                        print("\033[1;31mERRO! Ocorreu um erro ao tentar remover a playlist. Tente Novamente.\033[m")
                    else:
                        print(f"\033[1;32mPLAYLIST {lstplay[rem-1]} excluída com \033[4;32mSUCESSO.\033[m")
                        sleep(1.2)
                        print('\033[4;35mVoltando ao Menu principal\033[m')
                        sleep(0.5)
                        return None

            if play > len(lstplay) or play < 1:
                print('\033[1;31mERRO. Digite uma posição existente!\033[m')
            else:
                playlist = lstplay[play-1]
                try:
                    mus = listdir(f'{caminho}\\{playlist}')
                except:
                    print('\033[1;31mOcorreu um ERRO no sistema ao tentar entrar na playlist\033[m')
                else:
                    print("\033c", end="") # Limpa Terminal
                    lib.interface.titulo_musica(f"      MÚSICAS DA PLAYLIST \033[4m{playlist.upper()}\033[m\033[1;34m","Azul")
                    if len(mus) == 0:
                        print('\033[4;31mPLAYLIST VAZIA!\n\033[m')
                        sleep(1.2)
                    else:
                        for i,e in enumerate(mus):
                            print(f'\033[1;36m[ {i+1} ]\033[m {e}')
                            sleep(0.4)
                        print(f'{'─'*40}\n\033[1;34m OPÇÕES DA PLAYLIST:\033[m')
                    ch = lib.interface.menu(['Adicionar música','Remover música','Escutar música','Escolher outra playlist'],'Amarelo')
                    match ch:
                        case 1:
                            print("\033c", end="") # Limpa Terminal
                            lib.interface.titulo_musica(f'ADICIONE MÚSICAS NA PLAYLIST {playlist}','Roxo')
                            if addmusica(usrdir,nome,playlist) == "ofc":
                                print(f'A playlist \"{playlist}\" já tem todas as músicas do sistema.')
                                sleep(1.5)
                        case 2:
                            print("\033c", end="") # Limpa Terminal
                            lib.interface.titulo_musica(f' REMOVER MÚSICA DA PLAYLIST ','Vermelho')
                            removermus(usrdir,nome,playlist)
                            sleep(1.2)
                        case 3:
                            print("\033c", end="") # Limpa Terminal
                            lib.interface.titulo_musica(' PLAYER MP3... ','Ciano')
                            for i,e in enumerate(mus):
                                print(f'\033[1;36m[ {i+1} ]\033[m {e}')
                                sleep(0.4)
                            posm = int2("Digite a \033[1;36mposição\033[m da música para tocar: ")
                            song = mus[posm-1]
                            playermp3(song,nome,playlist,opc=True)
                            sleep(1.2)
                        case 4:
                            lib.interface.titulo_musica(' VOLTANDO PARA O MENU DE PLAYLIST ','Vermelho')
                            sleep(1.2)
