print ("Ingrese un valor")
suma=0
num = int(input())
while(num>0):
    num2= num%10
    suma= suma+num2
    num= num//10

    print(suma)
