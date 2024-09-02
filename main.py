import jappalib.visual
from time import sleep


base_emprestimo = 500
base_juros = 15

# CALCULANDO
saldo_anterior = base_emprestimo
vlr_pago = 100
vlr_juros = saldo_anterior * 0.15
vlr_capital = vlr_pago - vlr_juros
saldo_atual = saldo_anterior - vlr_capital

# MENU PRINCIPAL
while True:
	resp = jappalib.visual.menu(['Dados do emprestimo', 'Adicionar pagamento',
								 'Extrato detalhado', 'Configurar', 'Sair...'])

	if resp == 1:
		jappalib.visual.titulo('DADOS DO EMPRÉSTIMO')
		print('Valor: R$ {} reais\nJuros: {}%\n'.format(base_emprestimo, base_juros))
		sleep(2)
	
	elif resp == 2:
		jappalib.visual.titulo('ADICIONAR PAGAMENTO')
		sleep(2)
	
	elif resp == 3:
		jappalib.visual.titulo('EXTRATO DETALHADO')
		sleep(2)
	
	elif resp == 4:
		jappalib.visual.titulo('CONFIGURAR EMPRESTIMO')
		sleep(2)
	
	elif resp == 5:
		print('Encerrando o sistema, aguarde!')
		sleep(2)
		print('Finalizado com sucesso!')
		break

	else:
		print('ERRO: Opção inválida! Tente novamente.')
