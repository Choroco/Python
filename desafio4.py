print("APENAS HOJE! Promocao na casa:")
print(" ÁLCOOL:\n -Até 20 litros, desconto de 3% por litro\n -Acima de 20 litros, desconto de 5% por litro")
print(" GASOLINA:\n -Até 20 litros, desconto de 4% por litro\n -Acima de 20 litros, desconto de 6% por litro") 
print("Vai querer o que?\n1. A-alcool(R$3,30 O LITRO)\n2. G-gasolina(R$2,90 O LITRO)")

combustivel = int(input("Digite o número corresponde ao combustível desejado\n"))

litros = float(input("Vai querer quantos litros meu rei?\n"))

if combustivel == 1: 
    if litros >0 and litros <= 20:
        print("Preco a pagar: {:.2f}".format(litros*2.9*0.97),"R$")
        
    elif litros >20:
        print("Vai ficar: {:.2f}".format(litros*2.9*0.95),"R$")
    else:
        print("Quantidade invalida!")
elif combustivel == 2: 
    if litros >0 and litros <= 20:
        print("Preco a pagar: {:.2f}".format(litros*3.3*0.96),"R$")
        
    elif litros >20:
        print("Vai ficar: {:.2f}".format(litros*3.3*0.94),"R$")
    else:
        print("Quantidade invalida!")
else:
    print("Valor errado!")
#test