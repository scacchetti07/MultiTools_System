from time import sleep
from lib.skills import *
from lib.interface import *

def calculadora(nome="Desconhecido"):
    from math import factorial,sqrt,log
    numeros = list()
    cont = 1
    titulo('REGISTRANDO OS VALORES PARA CALCULAR','Verde')
    sleep(1)
    while True:
        num = int2(f'Digite o \033[1;31m{cont}°\033[m valor: ')
        numeros.append(num)
        cont+=1
        c = verifSN('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]? ')
        if c == 'N':
            break
    sleep(1.5)
    while True:
        print("\033c", end="") # Limpa Terminal
        titulo('    🔢 MENU DE CÁLCULOS 🔢     ','Roxo')
        print(f' \033[1;35mNúmeros registrados:\033[m \033[1;31m{numeros}\033[m')
        sleep(1)
        print(f""" \033[1;35m[ 1 ]\033[m Soma                           \033[1;35m[ 6 ]\033[m  Verificando se o número é divísivel
 \033[1;35m[ 2 ]\033[m Subtração                      \033[1;35m[ 7 ]\033[m  Raiz Quadrada
 \033[1;35m[ 3 ]\033[m Multiplicação                  \033[1;35m[ 8 ]\033[m  Logaritmo
 \033[1;35m[ 4 ]\033[m Divisão                        \033[1;35m[ 9 ]\033[m  Alterar Números
 \033[1;35m[ 5 ]\033[m Fatorial                       \033[1;35m[ 10 ]\033[m Voltar para \033[1;36m{nome.upper()} MULTI TOOLS\033[m          
    """)
        resp = int2(' \033[1;35mEscolha uma das Opções:\033[m ')
        t = len(numeros)
        match resp:
            case 1:
                print("\033c", end="") # Limpa Terminal  
                print('\n\033[1;33m══════| CALCULANDO A \033[1;32mSOMA\033[m \033[1;33mENTRE OS NÚMEROS |══════\033[m\n')
                sleep(1.5)
                c = 0
                print('➯  ',end='')
                while t > 0:
                    print(numeros[c],end='',flush=True)
                    sleep(0.5)
                    print(' + ' if t > 1 else ' = ',end='')
                    c+=1
                    t-=1
                print(f'\033[1;33m{sum(numeros)}\033[m')
                print('\033[1;32m══════════|\033[m'*5)
                sleep(3.5)
            case 2:
                print("\033c", end="") # Limpa Terminal
                print('\n\033[1;33m══════| CALCULANDO A \033[1;32mSUBTRAÇÃO\033[m \033[1;33mENTRE OS NÚMEROS |══════\033[m\n')
                sleep(1.5)
                c = sub = 0
                print('➯  ',end='')
                while t > 0:
                    print(numeros[c],end='',flush=True)
                    sleep(0.5)
                    print(' - ' if t > 1 else ' = ',end='')
                    c+=1
                    t-=1
                for i in range(len(numeros)):
                    if i == 0:
                        sub = numeros[i]
                    else:
                        sub -= numeros[i]
                print(f'\033[1;33m{sub}\033[m')
                print('\033[1;32m══════════|\033[m'*5)
                sleep(3.5) 
            case 3:
                print("\033c", end="") # Limpa Terminal
                print('\n\033[1;33m══════| CALCULANDO A \033[1;32mMULTIPLICAÇÃO\033[m \033[1;33mENTRE OS NÚMEROS |══════\033[m\n')
                sleep(1.5)
                c = mult = 0
                print('➯  ',end='')
                while t > 0:
                    print(numeros[c],end='',flush=True)
                    sleep(0.5)
                    print(' x ' if t > 1 else ' = ',end='')
                    c+=1
                    t-=1
                for i in range(len(numeros)):
                    if i == 0:
                        mult = numeros[i]
                    else:
                        mult *= numeros[i]
                print(f'\033[1;33m{mult}\033[m')
                print('\033[1;32m══════════|\033[m'*5)
                sleep(1)
            case 4:
                print("\033c", end="") # Limpa Terminal
                print('\n\033[1;33m══════| CALCULANDO A \033[1;32mDIVISÃO\033[m \033[1;33mENTRE OS NÚMEROS |══════\033[m\n')
                sleep(1.5)
                c = div = 0
                print('➯  ',end='')
                while t > 0:
                    print(numeros[c],end='',flush=True)
                    sleep(0.5)
                    print(' ÷ ' if t > 1 else ' = ',end='')
                    c+=1
                    t-=1
                try:
                    for i in range(len(numeros)):
                        if i == 0:
                            div = numeros[i]
                        else:
                            div /= numeros[i]
                except (ZeroDivisionError):
                    print('\033[1;31mNÃO É POSSÍVEL DIVIDIR POR 0\033[m')
                    sleep(3.5)
                else:
                    print(f'\033[1;33m{div:.2f}\033[m')
                    print('\033[1;32m══════════|\033[m'*5)
                    sleep(3.5)
            case 5:
                print("\033c", end="") # Limpa Terminal
                print('\033[1;33m══════| CALCULO DE \033[1;32mFATORIAIS\033[m \033[1;33m(!) |══════\033[m')
                sleep(1)
                loop = 'S'
                while loop == 'S':
                    for p,v in enumerate(numeros): 
                        print(F'Número \033[31m{v}\033[m na posição \t\033[32m[ {p} ]\033[m')
                        sleep(0.85)
                    print('══════|══════|══════|══════|══════')    
                    while True:
                        pos = int2('Digite a \033[1;32mposição\033[m do número que deseja ver o cálculo: ')
                        if pos > len(numeros)-1:
                            print('ERRO! DIGITE UMA POSIÇÃO VÁLIDA!')
                        else:
                            if numeros[pos] >= 0:
                                 break
                            else:
                                 print('\033[1;31mNÃO EXISTE FATORIAL DE NÚMERO NEGATIVO!\033[m')
                    print(f'\n\033[1;33m══════| CALCULANDO O \033[1;32mFATORIAL\033[m \033[1;33mDO NÚMERO \033[1;32m{numeros[pos]}\033[m\033[1;33m |══════\033[m')
                    sleep(1.5)
                    fat = numeros[pos]
                    print(f'\n\033[1;32m{numeros[pos]}!\033[m ⇒ ',end='')
                    while fat > 0:
                        print(fat,end='')
                        sleep(0.5)
                        print(' x ' if fat > 1 else ' = ',end='')
                        fat-=1
                    print(f'\033[1;32m{factorial(numeros[pos])}\033[m')
                    sleep(1)
                    print('\033[1;32m══════════|\033[m'*5)
                    while True:
                        loop = input('\nQuer ver outro número [\033[32mS\033[m/\033[31mN\033[m]? ').strip().upper()
                        if loop not in 'SN' or loop == '':
                            print('\033[1;31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
                        else:
                            break
                    if loop == 'N':
                        titulo('VOLTANDO PARA O MENU DE CÁLCULOS','Vermelho')
                        sleep(2)
                        break
                    else:
                        print("\033c", end="") # Limpa Terminal
                        print('\033[1;33m══════| CALCULO DE \033[1;32mFATORIAIS\033[m \033[1;33m(!) |══════\033[m')
                    sleep(1)
            case 6:
                print("\033c", end="") # Limpa Terminal
                print('\033[1;33m══════| VERIFICANDO SE UM NÚMERO É DIVÍVISEL USANDO \033[1;32mMODS\033[m \033[1;33m(%) |══════\033[m')
                sleep(1)
                loop = 'S'
                while loop == 'S':
                    for p,v in enumerate(numeros):
                        print(F'Número \033[31m{v}\033[m na posição \t\033[32m[ {p} ]\033[m')
                        sleep(0.85)
                    print('══════|══════|══════|══════|══════')  
                    while True:
                        pos = int2('Digite a \033[1;32mposição\033[m do número que deseja ver o cálculo: ')
                        if pos > len(numeros)-1:
                            print('ERRO! Digite uma posição válida!')
                        else:
                            n = int2('Qual número deseja fazer a \033[1;33mdivisão\033[m? ')
                            break
                    print(f'\n\033[1;33m══════| VERIFICANDO SE O \033[1;32m{numeros[pos]}\033[m É DIVISÍVEL POR \033[1;32m{n}\033[1;33m |══════\033[m')
                    sleep(1.5)   
                    mod = numeros[pos] % n
                    print(f'{numeros[pos]} % {n} = \033[1;33m{mod:.2f}\033[m')
                    print(f"\nO número {numeros[pos]} é dívisivel por {n}? ",end='')
                    if mod == 0:
                        print("Verdade\n")
                    else:
                        print("Falso\n")
                    sleep(1)
                    print('\033[1;32m══════════|\033[m'*5)
                    loop = verifSN('\nQuer ver outro número [\033[32mS\033[m/\033[31mN\033[m]? ')
                    if loop == 'N':
                        titulo('VOLTANDO AO MENU DE CÁLCULO','Vermelho')
                        sleep(1.5)
                        break
                    else:
                        print("\033c", end="") # Limpa Terminal
                        print('\033[1;33m══════| VERIFICANDO SE UM NÚMERO É DIVÍVISEL USANDO \033[1;32mMODS\033[m \033[1;33m(%) |══════\033[m')
                    sleep(1)
            case 7:
                print("\033c", end="") # Limpa Terminal
                print('\033[1;33m══════| CALCULO DE \033[1;32mRAIZ QUADRADA\033[m \033[1;33m(²√) |══════\033[m')
                sleep(1)
                loop = 'S'
                while loop == 'S':
                    sleep(1.2)
                    for p,v in enumerate(numeros):
                        print(f'Número \033[31m{v}\033[m na posição \t\033[32m[ {p} ]\033[m')
                        sleep(0.85)
                    print('══════|══════|══════|══════|══════')    
                    while True:
                        pos = int2('Digite a \033[1;32mposição\033[m do número que deseja ver o cálculo: ')
                        if pos > len(numeros)-1:
                            print('\033[1;31mERRO! DIGITE UMA POSIÇÃO VÁLIDA\033[m')
                        else:
                             if numeros[pos] >= 0:
                                 break
                             else:
                                 print('\033[1;31mNÃO EXISTE RAIZ QUADRADA DE NÚMERO NEGATIVO!\033[m')

                    print(f'\n\033[1;33m══════| CALCULANDO A \033[1;32mRAIZ QUADRADA\033[m \033[1;33mDO NÚMERO \033[1;32m{numeros[pos]}\033[m\033[1;33m |══════\033[m')
                    sleep(1.5)
                    print(f'\033[1m²√{numeros[pos]} = \033[1;33m{sqrt(numeros[pos]):.2f}\033[m')
                    sleep(1)
                    print('\033[1;32m══════════|\033[m'*5)
                    loop = verifSN('\nQuer ver outro número [\033[32mS\033[m/\033[31mN\033[m]? ')
                    if loop == 'N':
                        titulo('VOLTANDO AO MENU DE CÁLCULO','Vermelho')
                        sleep(1.5)
                        break
                    else:
                        print("\033c", end="") # Limpa Terminal
                        print('\033[1;33m══════| CALCULO DE \033[1;32mRAIZ QUADRADA\033[m \033[1;33m(²√) |══════\033[m')                                                          
                sleep(1)
            case 8:
                print("\033c", end="") # Limpa Terminal
                print('\033[1;33m══════| CALCULO DE \033[1;32mLOGARTIMO\033[m \033[1;33m(log) |══════\033[m')
                sleep(1)
                loop = 'S'
                while loop == 'S':
                    sleep(1.5)
                    print()
                    for p,v in enumerate(numeros):
                        print(F'Número \033[31m{v}\033[m na posição \t\033[32m[ {p} ]\033[m')
                        sleep(0.85)
                    print('══════|══════|══════|══════|══════')    
                    while True:
                        pos = int2('Digite a \033[1;32mposição\033[m do número que deseja ver o cálculo: ')
                        if pos > len(numeros)-1:
                            print('\033[1;31mERRO: DIGITE UMA POSIÇÃO VÁLIDA\033[m')
                        else:
                            if numeros[pos] < 0:
                                print('\033[1;31mNÃO EXISTE LOGARITMO DE NÚMERO NEGATIVO!\033[m')
                            else:
                                break
                    while True:
                        e = int(input('Qual será a \033[1;33mbase\033[m do logaritmo? '))
                        if e > 0:
                            break
                        else:
                            print('\033[1;31mERRO: NÃO EXISTE LOGARITMO DE BASE 0 OU NEGATIVA, DIGITE NOVAMENTE!\033[m')

                    print(f'\n\033[1;33m══════| CALCULANDO O \033[1;32mLOGARITMO \033[1;33mDO NÚMERO \033[1;32m{numeros[pos]}\033[1;33m |══════\033[m')
                    sleep(1.5)
                    if e == 1:
                        print(f'\033[1mlog {numeros[pos]} na base {e} = 0\033[m')
                    else:
                        print(f'\033[1mlog {numeros[pos]} na base {e} = {log(numeros[pos],e):.2f}\033[m')
                    print('\033[1;32m══════════|\033[m'*5)
                    sleep(3.5)
                    loop = verifSN('\nQuer ver outro número [\033[32mS\033[m/\033[31mN\033[m]? ')
                    if loop == 'N':
                        titulo('VOLTANDO AO MENU DE CÁLCULO','Vermelho')
                        sleep(1.5)
                        break
                    else:
                        print("\033c", end="") # Limpa Terminal
                        print('\033[1;33m══════| CALCULO DE \033[1;32mLOGARTIMO\033[m \033[1;33m(log) |══════\033[m')    
                sleep(1)
            case 9:
                print("\033c", end="") # Limpa Terminal
                titulo('  🚯 REMOVENDO E CRIANDO NOVOS CAMPOS 🚯  ','Vermelho')
                sleep(2)
                cont = 1
                numeros.clear()
                while True:
                    num = int2(f'Digite o \033[1;31m{cont}°\033[m valor: ')
                    numeros.append(num)
                    cont+=1
                    c = verifSN('Quer continuar [\033[32mS\033[m/\033[31mN\033[m]? ')
                    if c == 'N':
                        break
            case 10:
                titulo(f'   🔄️ VOLTANDO AO \033[1;36m{nome.upper()} MULTI TOOLS\033[1;33m 🔄️','Amarelo')
                sleep(2)
                break
            case _:
                 print(' \033[1;31mDIGITE UMA OPÇÃO VÁLIDA\033[m')
