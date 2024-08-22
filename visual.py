def linha(tam=42, caracter='-'):
    print(tam * caracter)


def titulo(txt, tam=42, caracter='-'):
    linha(tam, caracter)
    print(txt.center(tam))
    linha(tam, caracter)
