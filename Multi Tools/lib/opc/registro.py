from time import sleep
from lib.skills import *
from lib.interface import *

def registro2(perfil='DESCONHECIDO'):
    arq = f'Cadastros de {perfil}.txt'
    pasta = 'Registros'
    criarCadastro(arq,pasta)
    while True:
        print("\033c", end="") # Limpa Terminal
        titulo(' 📓 REGISTRO DE PESSOAS 📓 ','Azul')
        sleep(0.8)
        resp = menu(['Novo Registro','Ver lista dos registrados','Remover Pessoas',f'Voltar ao \033[1;36m{perfil.upper()} MULTI TOOLS\033[m'],'Amarelo')
        match resp:
            case 1:
                print("\033c", end="") # Limpa Terminal
                titulo('     ✍️  CRIANDO CAMPOS PARA NOVO REGISTRO ✍️   ','Amarelo')
                dados = {}
                sleep(1.2)
                dados['Nome:'] = input('Digite um \033[33mnome\033[m: ').title()
                nome = dados['Nome:'].split(' ')
                dados['Idade:'] = int2(f'Digite a \033[33midade\033[m de {nome[0]}: ')
                dados['Nickname:'] = input(f'Digite o \033[33mnickname\033[m de {nome[0]}: ')
                while True:
                    rede = input(f'{nome[0]} tem \033[33mredes sociais\033[m [\033[32mS\033[m/\033[31mN\033[m]? ').strip().upper()
                    if rede not in 'SN' or rede == '':
                        print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
                    else:
                        break
                if rede == 'S':
                    dados['Twitter:'] = input('Digite o \033[33muser\033[m do \033[1;36mTwitter\033[m: @')
                    dados['Instagram:'] = input('Digite o \033[33muser\033[m do \033[1;35mInstagram\033[m: @')
                    dados['Discord:'] = input('Digite o \033[33muser\033[m do \033[1;34mDiscord\033[m: ')
                else:
                    dados['Redes:'] = 'NÃO TEM'
                save = verifSN('Deseja salvar os dados registrados [\033[32mS\033[m/\033[31mN\033[m]? ')
                print("\033c", end="") # Limpa Terminal
                if save == 'S':
                    titulo('  📋 SALVANDO E MOSTRANDO DADOS 📋  ','Verde')
                    sleep(1.8)
                    for k,v in dados.items():
                        print(f'\033[1;34m{k}\033[m ➯  \033[1;33m{v}\033[m')
                        sleep(0.8)
                    sleep(1)
                    registrar(dados,perfil)
                else:
                    titulo(' 📋 MOSTRANDO OS DADOS NÃO SALVOS 📋','Verde')
                    sleep(1.8)
                    for k,v in dados.items():
                        print(f'\033[1;34m{k}\033[m ➯  \033[1;33m{v}\033[m')
                        sleep(0.5)
            case 2:
                print("\033c", end="") # Limpa Terminal
                titulo('  🗃️  ABRINDO LISTA DE REGISTROS  🗃️  ','Amarelo')
                sleep(1.5)
                leiaregistros(perfil)
                while True:
                        b = int2('\n\033[1;33mDigite \033[4;31m\"0\"\033[m\033[1;33m para voltar ao menu: \033[m')
                        if b == 0:
                            titulo('VOLTANDO PARA O MENU','Amarelo')
                            sleep(2)
                            break
                        else:
                            print('\033[1;31mApenas o valor \033[1;33m0\033[1;31m é válido.\033[m')
            case 3:
                titulo('NÃO DISPONÍVEL NO MOMENTO')
            case 4:
                titulo(f'🔄️ VOLTANDO AO \033[1;36m{perfil.upper()} MULTI TOOLS\033[1;33m 🔄️','Amarelo')
                sleep(2)
                break
            case _:
                print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
