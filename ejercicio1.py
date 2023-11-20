num1=int(input("Ingrese un número: "));
num2=int(input("Ingrese otro número: "));
if num1>num2:
    mensaje= str(num1) + " es mayor que " + str(num2);
else:
    mensaje=str(num1) + " es menor que " + str(num2);
print(mensaje);