def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def division(a,b):
    if b==0:
        print("No se puede dividir con 0 ")
    else:
        return a/b

def multiplicacion(a,b):
    return a*b

def validacion_num(numero):
    try:
        numeroFloat=float(numero)
    except ValueError:
        return 
    else:
        return numeroFloat

while True:
    num1=int(input("Escriba el primer número >"))
    num2=int(input("Escriba el segundo número >"))
    if validacion_num(num1)==None or validacion_num(num2)==None:
        print("Debe ingresar valores númericos")
    else:
        sum=suma(num1, num2)
        rest=resta(num1, num2)
        div=division(num1, num2)
        mult=multiplicacion(num1, num2)

        print(f"La suma es de: ",sum)
        print(f"La resta es de: ",rest)
        print(f"La división es de: ",div)
        print(f"La multiplicación es de:",mult)
            