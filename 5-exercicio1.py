# antecessor e sucessor

numDigitado = input("Digite um número e vou devolver a informação do sucessor e antecessor dele:\n")
antecessor = int(numDigitado) - 1
sucessor = int(numDigitado) + 1
print(f"O número digitado foi {numDigitado}, o antecessor é {antecessor} e o sucessor é {sucessor}")

# média de quatro notas

nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))
nota3 = float(input("Digite a terceira nota:\n"))
nota4 = float(input("Digite a quarta nota:\n"))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média dessas quatro notas é {media}")
