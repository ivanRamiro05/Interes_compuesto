#INTERES COMPUESTO

C= int(input("Ingrese el valor de dinero ingresado: "))

#processing
B=2*C
sum=0

while C < B:
    C= C*0.05 +C
    sum = sum + 1
    
 #output

print("Su dinero se duplicara en " , sum ,"Meses" )