num1=int(input("Ingrese un número: "));
num2=int(input("Ingrese otro número: "));
num3=int(input("Ingrese otro número: "));
#mayor=int();
if num1 > num2 and num1 > num3:
    mayor = num1;
    print("El mayor valor es:", mayor);
elif num2 > num1 and num2 > num3:
    mayor = num2;
    print("El mayor valor es:", mayor);
elif num3>num2 and num3>num1:
    mayor=num3;
    print("El mayor valor es:", mayor);
else:
    print("los numeros son neutros");
#elif num1==0 and num2==0 and num3==0:
    #print("El número cero (0) es neutro")
#else:
    #mayor = num3;