dia = input('Que dia você nasceu?')
mes = input('Que mês você nasceu?')
ano = input('Que ano você nasceu?')

rules = [dia.isnumeric(),
         mes.isnumeric(),
         ano.isnumeric()]
if all(rules):
    print('{}/{}/{}'.format(dia,mes,ano))

else:
    print("por favor inserir somente números")