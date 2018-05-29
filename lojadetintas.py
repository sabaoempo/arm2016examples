m=int(input("Informe, em metros quadrados, a área a ser pintada:"))

litros=m//3
if m%3>0:
    litros=litros+1

latas=litros//18
if litros%18>0:
    latas=latas+1

print("Você irá precisar de",litros,"litros de tinta,",latas,"latas e gastará",latas*80,"reais.")

