print('ANALISADOR DE CORRIDAS')
print('Veja se uma corrida atende sua meta')
valorC = float(input('Qual o valor da corrida? R$'))
PontoA = float(input('Quantos Km ate buscar o passageiro(embarque)? '))
PontoB = float(input('Quantos Km tera a viagem com o passageiro(destino)? '))
AutCarro = float(input('Quantos Km seu carro faz por litro? '))
Custocombu = float(input('Quantos voce paga o litro do combustivel?R$ '))
meta = float(input('Qual a meta de ganho por Km tirando os custos? '))
distancia = PontoA + PontoB

if AutCarro <= 0 or distancia <= 0:
    print('ERRO: Consumo e distância devem ser maiores que zero!')
else:
    combunece = distancia / AutCarro
    Gastocombu = combunece * Custocombu
    liquidoCorrida = valorC - Gastocombu
    sobra = liquidoCorrida / distancia
print('Distancia ate o passageiro: {:.2f}Km'.format(PontoA))
print('Distancia da viagem: {:.2f}Km'.format(PontoB))
print('Distancia total percorrida: {:.2f}Km'.format(PontoA+PontoB))
print('Valor da corrida: R${:.2f}'.format(valorC))
print('Combustivel necessario: {:.2f} litros'.format(combunece))
print('Gasto com combustivel: R${:.2f}'.format(Gastocombu))
print('Valor liquido tirando o combustivel: R${:.2f}'.format(liquidoCorrida))
print('Sua meta é: R${:.2f} por Km'.format(meta))
print('Sobra estimada R$: {:.2f} por km'.format(sobra))
if sobra >= meta:
    print('Essa corrida esta dentro da sua meta!!')
else:
    print('Essa corrida esta abaixo da sua meta!!')



