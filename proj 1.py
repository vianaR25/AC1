a = float(input("Digite o valor de a : "))
b = float(input("Digite o valor de b : "))
c = float(input("Digite o valor de c : "))

delta = (b**2 - 4*a*c)
x1 = (-b - delta**(1/2)) / (2*a)
x2 = (-b + delta**(1/2)) / (2*a)
print ( " x1 é igual a : ", x1 ,"x2 é igual a: ", x2)



anoBi = int(input( " Digite o ano "))
bisexto = (anoBi % 4 == 0 and anoBi % 100 != 0) or (anoBi % 400 == 0)




