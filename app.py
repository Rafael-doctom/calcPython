print("Executado operadores aritméticos")

numberOne = int(input("Digite um número:"))
numberTwo = int(input("Digite outro número:"))

print("Operações disponíveis: ")
print("1) Soma(+)")
print("2) Subtração(-)")
print("3) Multiplicação(x)")
print("4) Divisão(/)")

calcOperation = int(input("Qual operação deseja realizar:"))


if calcOperation == '+' or '1' or 'soma' or 'Soma' or 'SOMA':
    valueTot = numberOne + numberTwo
    print(f'Resultado:{numberOne} + {numberTwo} = {valueTot}')

elif calcOperation == '-' or '2' or 'menos' or 'MENOS':
    valueTot = numberOne - numberTwo
    print(f'Resultado:{numberOne} - {numberTwo} = {valueTot}')

elif calcOperation == 'x' or '3' or 'vezes' or 'VEZES':
    valueTot = numberOne * numberTwo
    print(f'Resultado:{numberOne} * {numberTwo} = {valueTot}')

elif calcOperation == '/' or '4' or 'divisao' or 'divisão' or 'DIVISAO' or 'DIVISÃO':
    valueTot = numberOne / numberTwo
    print(f'Resultado:{numberOne} / {numberTwo} = {valueTot}')


print(f'[FIM]- Resultado final foi: {valueTot}.')
