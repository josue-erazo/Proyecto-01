val1=int(input("Ingrese un número: "));
val2=int(input("Ingrese otro número: "));
val3=int(input("Ingrese otro número: "));
suma=int((val1+val2+val3)/3);
if suma % 2==0:
    print(suma,"es el promedio y es par.");
else:
    print(suma,"es el promedio y es impar.");