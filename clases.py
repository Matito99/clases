print("Bienvenido a caluladora matito")
import time 
time.sleep(2) 

print("1.- Sumar") 
print("2.- Restar")
print("3- Dividir")
print("4.- Multiplicar ")

opcion=int(input("Escoge la opcion que deseas"))

if opcion==1:
    a=int(input("Escribe un numero"))
    b=int(input("Escribe un numero"))
    def sumar(a,b):
        return a+b
    print("La suma de dos numeres es", sumar(a,b))

if opcion==2:
    a=int(input("Escribe un numero"))
    b=int(input("Escribe un numero"))
    def sumar(a,b):
        return a-b
    print("La suma de dos numeres es", sumar(a,b))    
    
if opcion==3:
    a=int(input("Escribe un numero"))
    b=int(input("Escribe un numero"))
    def sumar(a,b):
        return a/b
    print("La suma de dos numeres es", sumar(a,b))    
        
if opcion==4:
    a=int(input("Escribe un numero"))
    b=int(input("Escribe un numero"))
    def sumar(a,b):
        return a*b
    print("La suma de dos numeres es", sumar(a,b))
    



      
        
    


