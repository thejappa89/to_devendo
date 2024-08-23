def linha(tam=42, caracter='-'):
    print(tam * caracter)


def titulo(txt, tam=42, caracter='-'):
    linha(tam, caracter)
    print(txt.center(tam))
    linha(tam, caracter)


def leiaint(caracteres):
    while True:
        try:
            num = int(input(caracteres))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido!\33[m]]')
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de lib interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def menu(lista, msg='MENU PRINCIPAL'):
    titulo(msg)
    for e, i in enumerate(lista):
        print(f'{e + 1}. {i}')
    linha()
    opc = leiaint('Sua opção: ')
    return opc
