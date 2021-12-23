print("Executado operadores aritméticos")

numberOne = int(input("Digite um número:"))
numberTwo = int(input("Digite um 2° números:"))

print("Operações disponíveis: ")
print("Soma(+)")
print("Subtração(-)")
print("Multiplicação(x)")
print("Divisão(/)")

calcOperation = input("Qual operação deseja realizar:")

if calcOperation == '+':
    valueTot = numberOne + numberTwo
    print(valueTot)
elif calcOperation == '-':
    print("erro")
elif calcOperation == 'x':
    valueTot = numberOne * numberTwo
    print(valueTot)
elif calcOperation == '/':
    valueTot = numberOne / numberTwo
    print(valueTot)
elif calcOperation == '':
    print("[ERRO] - talvez você tenha errado em algo...")

print(f'[FIM]- Resultado final foi: {valueTot}')    
