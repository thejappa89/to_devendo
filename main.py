base_emprestimo = 500
base_juros = 15

# INFORMAÇÕES INICIAIS
print('''
DADOS GERAIS DO EMPRÉSTIMO PESSOAL
      Valor: R$ {} reais
      Juros: {}%
      '''.format(base_emprestimo, base_juros))

# CALCULANDO
saldo_anterior = base_emprestimo
vlr_pago = 100
vlr_juros = saldo_anterior * 0.15
vlr_capital = vlr_pago - vlr_juros
saldo_atual = saldo_anterior - vlr_capital

# INFORMAÇÕES GERAIS
print('''
DETALHAMENTO MENSAL DE PAGAMENTOS
      Saldo anterior: {}

      Valor pago: R$ {}
        {} juros
        {} capital
     
      Saldo atualizado: {}
      '''.format(saldo_anterior,
                 vlr_pago,
                 vlr_juros,
                 vlr_capital,
                 saldo_atual
                 ))
