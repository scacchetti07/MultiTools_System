from lib.skills import *
from lib.interface import *
from os import listdir

def bloco(nome='DESCONHECIDO'):
    pasta = 'Anotacoes'
    usrdir = f'Notas de {nome}'
    criarpasta(pasta,usrdir)
    while True:
        titulo(f' ANOTAÇÕES DE \033[1;36m{nome.upper()}\033[1;32m ','Verde')
        resp = menu(['Criar nova anotação','Menu de Edição',f'Voltar para \033[1;36m{nome.upper()} MULTI TOOLS\033[m'],'Verde')
        match resp:
            case 1:
                print("\033c", end="") # Limpa Terminal
                titulo(' CRIANDO NOVO ARQUIVO DE TEXTO ','Amarelo')
                sleep(1)
                print(f"Digite \"\033[4;31m0\033[m\" para sair")
                arq = input('Digite o \033[1;32mnome\033[m do seu arquivo .txt: ')
                if arq == "0":
                    break
                else:
                    arq = f'{arq}.txt'
                    print(f'\033[1;33mCRIANDO O ARQUIVO {arq}...\033[m')
                    sleep(3)
                    criarNotas(arq,pasta,usrdir)
            case 2:
                while True:
                    print("\033c", end="") # Limpa Terminal
                    caminho = listdir(f'lib\\opc\\Anotacoes\\Notas de {nome}')
                    titulo(' Menu de Edição de Arquivos', 'Verde')
                    r = menu(['Ver arquivos','Editar Arquivos','Remover Arquivos','Voltar para o Menu principal'],'Verde')
                    match r:
                        case 1:
                            while True:
                                print("\033c", end="") # Limpa Terminal
                                titulo(f' ANOTAÇÕES SALVAS DE \033[1;36m{nome.upper()}\033[1;32m ', 'Verde')
                                sleep(1)
                                for c,v in enumerate(caminho):
                                    print(f' \033[1;32m[ {c+1} ]\033[m {v}')
                                    sleep(0.5)
                                print('═'*40)
                                sleep(0.5)
                                pos = int2('Digite qual arquivo que deseja \033[1;32mvisualizar\033[m seu conteúdo (Digite \033[31m"0"\033[m para voltar ao menu): ')
                                if pos == 0:
                                    titulo(' VOLTANDO AO MENU ','Vermelho')
                                    sleep(3)
                                    break
                                elif 0 < pos <= len(caminho):
                                    ver = caminho[pos-1]
                                    print(f'\033[1;32mAbrindo arquivo \033[4m{ver}\033[m\033[1;32m para visualização.\033[m')
                                    sleep(1.5)
                                    veranot(ver,usrdir)
                                else:
                                    print('\033[1;31mERRO! Digite uma posição válida\033[m')
                        case 2:
                            while True:
                                print("\033c", end="") # Limpa Terminal
                                titulo(f' ANOTAÇÕES SALVAS DE \033[1;36m{nome.upper()}\033[1;32m ', 'Verde')
                                sleep(1)
                                for c,v in enumerate(caminho):
                                    print(f' \033[1;32m[ {c+1} ]\033[m {v}')
                                    sleep(0.5)
                                print('═'*40)
                                sleep(0.5)                                
                                pos = int2('Digite qual arquivo que deseja \033[1;32meditar\033[m (Digite \033[31m0\033[m para voltar ao menu): ')
                                if pos == 0:
                                    titulo(' VOLTANDO AO MENU ','Vermelho')
                                    sleep(2)
                                    break
                                elif 0 < pos <= len(caminho):
                                    editar = caminho[pos-1]
                                    print(f'\033[1;32mAbrindo arquivo \033[4m{editar}\033[m\033[1;32m para edição.\033[m')
                                    sleep(1)
                                    if veranot(editar,usrdir):
                                        edit = input('Digite o que deseja \033[32mnessa linha\033[m no arquivo: ')
                                        editaranot(edit,editar,usrdir)
                                    else:
                                        break
                                else:
                                    print('\033[1;31mERRO! Digite uma posição válida\033[m')
                        case 3:
                            print("\033c", end="") # Limpa Terminal
                            titulo(f' ANOTAÇÕES SALVAS DE \033[1;36m{nome.upper()}\033[1;32m ', 'Verde')
                            sleep(1)
                            for c,v in enumerate(caminho):
                                print(f' \033[1;32m[ {c+1} ]\033[m {v}')
                                sleep(0.5)
                            print('═'*40)
                            sleep(0.5)                                    
                            pos = int2('Digite o arquivo que deseja \033[1;32mremover\033[m (Digite \033[31m0\033[m para voltar ao menu): ')
                            if pos == 0:
                                titulo(' VOLTANDO AO MENU ','Vermelho')
                                sleep(2)
                                break
                            else:
                                trat = verifSN('Deseja mesmo remover esse arquivo? [\033[32mS\033[m/\033[31mN\033[m]? ')
                                if trat == 'S':
                                    remover = caminho[pos-1]
                                    if removerarquivo(remover,'Anotacoes',usrdir):
                                        print('\033[1;32mArquivo excluído com SUCESSO!!\033[m')
                                        sleep(1.5)
                                else:
                                    titulo(' VOLTANDO PARA O MENU ','Vermelho')
                                    sleep(1)
                                    break
                        case 4:
                            titulo(' VOLTANDO PARA O MENU ','Vermelho')
                            sleep(1.5)
                            break
            case 3:
                titulo(f' VOLTANDO PARA {nome.upper()} MULTI TOOLS ','Amarelo')
                sleep(1.5)
                break
