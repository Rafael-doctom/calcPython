print("------ Executado operadores aritméticos ------")
print("Operações disponíveis: ")
print("1) Soma(+)")
print("2) Subtração(-)")
print("3) Multiplicação(x)")
print("4) Divisão(/)")

numberOne = int(input("Digite um número:"))
numberTwo = int(input("Digite outro número:"))

calcOperation = input("Deseja realizar a operação? (S/N):")

if calcOperation != 'S':
    print(f'{calcOperation} é uma opção inválida. Tente novamente!')
else:
    valueTotSum = numberOne + numberTwo
    print(f'Resultado:{numberOne} + {numberTwo} = {valueTotSum}')

    valueTotSubtract = numberOne - numberTwo
    print(f'Resultado:{numberOne} - {numberTwo} = {valueTotSubtract}')

    valueTotMulti = numberOne * numberTwo
    print(f'Resultado:{numberOne} * {numberTwo} = {valueTotMulti}')

    valueTotDiv = numberOne / numberTwo
    print(f'Resultado:{numberOne} / {numberTwo} = {valueTotDiv}')
    
    valueTotMedia = (valueTotSum + valueTotSubtract + valueTotMulti + valueTotSum) /4
    
print(f'A média geral é: {valueTotMedia}')