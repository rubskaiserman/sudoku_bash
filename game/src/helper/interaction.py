from helper import board_builder

def imprime_linha(LINHA_STRING:str)->None:
    # Imprime a linha do tabuleiro
    length = len(LINHA_STRING)
    for j in range(length):
        if (j + 1) % 9 == 0:
            print(LINHA_STRING[j])
        elif (j + 1) % 3 == 0:
            print(LINHA_STRING[j], end=' || ')
        else:
            print(LINHA_STRING[j], end=' | ')

def imprime_divisor(i:int)->None:
    # Imprime o divisor entre as linhas
    if (i + 1) % 3 == 0 and (i + 1) % 9 != 0:
        print('- '*18)
    elif (i + 1) % 3 != 0:
        print('= '* 18)

def imprime(T: list[list])->None:
    # Imprime o tabuleiro
    for i in range(len(T)):
        imprime_linha(T[i])
        imprime_divisor(i)
        

def verifica_posicao_fixa(F:list, L:int, C:int)->bool:
    return (L, C) in F

def marca(T:list, L:int, C:int, V:str):
    T = board_builder.cria_tabuleiro(T)
    T[L][C] = V
    string_appender = ''
    for line in T:
        string_appender += ' , '.join(line)
        string_appender += '\n'
    T = string_appender

    return T

