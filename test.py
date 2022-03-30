x = float(input("digite o valor de x: "))
y = float(input("digite o valor de y: "))

a = input("ecolha a operacao entre + (soma), * (multiplicacao) e / (divisao): ")
b: float

if a == "+":
    b = (x + y)
    if b >=10:
        print(b, " perfeito")
    else :
        print(b, " mamaco")
elif a == "*":
    b = (x * y)
    if b >=10:
        print(b, " perfeito")
    else :
        print(b, " mamaco")
elif a == "/":
    b = (x / y)
    if b >=10:
        print(b, " perfeito")
    else :
        print(b, " mamaco")
else:
    print("operador invalido!")