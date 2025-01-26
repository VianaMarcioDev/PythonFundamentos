# comentário


'''
comentário
de
múltiplas
linhas
'''

name = input('Digite o nome do jogo:\n')
yearLaunch = int(input('Digite o ano do lançamento do jogo:\n'))
gamePrice = float(input('Digite o valor do jogo:\n'))
planIncluded = input("Está incluso no plano:\n")

print(name)
print(yearLaunch)
print(gamePrice)
print(planIncluded)


#concatenação com fstring
print(f"===========Dados do jogo==========\nNome do jogo:\n{name}\nAno de Lançamento:\n{yearLaunch}\nPreço do jogo:\n{gamePrice}\nIncluído no plano?\n{planIncluded}")
