import requests

reais = float(input("Digite quando dinheiro voce tem na carteira: R$"))

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic["USDBRL"]["bid"]

conversao_BRL_USD = reais/float(cotacao_dolar)

print(f"Com R${reais} voce pode comprar US${conversao_BRL_USD}")
