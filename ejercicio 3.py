num1=int(input("Ingrese un número: "));
num2=int(input("Ingrese otro número: "));
num3=int(input("Ingrese otro número: "));
total=num1+num2+num3;
if  total % 7==0:
    print(total," es la suma de los valores ingresados y sí es múltiplo de 7");
else:
    print(total," es la suma de los valores ingresados y no es múltiplo de 7");