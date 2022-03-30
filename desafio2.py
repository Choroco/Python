print("Calcule sua media:")
a = float(input("primeira nota:\n"))
b = float(input("segunda nota:\n"))
c = float(input("terceira nota:\n"))
d = float(input("quarta nota:\n"))

valores = [a,b,c,d]
valortotal = 0
for x in valores:
    valortotal = (valortotal + x) 
y = len(valores)

media = valortotal/y
if media >=0 and media <=5:
    print("Voce precisa estudar, sua media e: ", valortotal/y)
elif media >=5.1 and media <=7:
    print("Ta bom, mas podia ta melhor, sua media e:", valortotal/y)
elif media >=7.1 and media <=10:
    print("Que cara bom, sua media e:", valortotal/y)
else:
    print("Media invalida!")