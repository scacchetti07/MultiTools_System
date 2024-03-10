from time import sleep
from datetime import datetime
from lib.opc import *
import os.path


def perfil(nome):
    a = list()
    try:
        ler = open('lib\\opc\\Perfis\\Perfis_Sys.txt','r')
    except Exception:
        print('OCORREU UM ERRO AO CRIAR O SEU PERFIL!')
    else:
        try:
            file = open('lib\\opc\\Perfis\\Perfis_Sys.txt','a')
        except Exception:
            print('OCORREU UM ERRO AO CRIAR O SEU PERFIL!')
        else:
            if os.path.getsize('lib\\opc\\Perfis\\Perfis_Sys.txt') == 0:
                file.write(f'Perfil [ {nome.title()} ] criado em {datetime.now()}\n')
                return True 
            for i,l in enumerate(ler.readlines()):
                if nome not in l:
                    a.append('n')
                else:
                    if len(a) == 0:
                        a.append('s')
                        break
                    else:    
                        a.clear()
                        a.append('s')
                        break
            for i in range(len(a)):
                if a[i] == 'n':                        
                    file.write(f'Perfil [ {nome.title()} ] criado em {datetime.now()}\n')
                    return True
                if a[i] == 's':         
                    a.clear()
                    return False
    finally:
        file.close()
        ler.close()
    