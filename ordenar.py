# INPUT

print("------------------------------------------------")
print("--------ORDENAR DE MENOR A MAYOR----------------")
print("------------------------------------------------")

a = int (input("ingrese el primer digito: "))
b = int (input("ingrese el segundo digito: "))
c = int (input("ingrese el tercer  digito: "))

# PROCESSING

if a < b < c :
    rt= (a , b , c)
else:
    if c < b < a :
        rt= (c , b, a)
    else:
        if a < c < b:
            rt=  (a  , c , b)
        else:
            rt = (b , a , c)

#OUTPUT

print("------------------------------------------")
print("------------EL RESULTADO ES---------------")
print("------------------------------------------")

print("Los números en forma ascendente son: " + str (rt))


print("------------------------------------------")
print("-----------------FIN----------------------")
print("------------------------------------------")