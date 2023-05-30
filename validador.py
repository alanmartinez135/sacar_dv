import math
numeros_rut = []
numeros_rut.append(input("Ingresa tu rut: "))
numeros_rut.reverse()
print(numeros_rut)
for numero in numeros_rut:
    mul1 = int(numero[0]) * 2
    mul2 = int(numero[1]) * 3
    mul3 = int(numero[2]) * 4
    mul4 = int(numero[3]) * 5
    mul5 = int(numero[4]) * 6
    mul6 = int(numero[5]) * 7
    mul7 = int(numero[6]) * 2
    mul8 = int(numero[7]) * 3
suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8
print("suma =", suma)
total = suma / 11
total = math.trunc(total)
print("total = ", total)
total_multi = total * 11
print("total x 11 = ", total_multi)
valor_final = suma - total_multi
print("suma menos total x 11= ", valor_final)
dv = 11 - valor_final
print(dv)
#Incompleto, no da bien el dv