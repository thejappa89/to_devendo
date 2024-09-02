def config_emprestimo(valor, juros, data):
    caminho = "to_devendo\\config.txt"
    with open(caminho, 'w') as arquivo:
        arquivo.write('Emprestimo: {}\n'.format(valor))
        arquivo.write('Juros: {}\n'.format(juros))
        arquivo.write('Data: {}'.format(data))
