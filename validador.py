import math
numeros_rut = []
run = (input("Ingresa tu rut: "))
for numero in run:
    numeros_rut.append(numero)
numeros_rut.reverse()
print(numeros_rut)
mul1 = (int(numeros_rut[0])) * 2
mul2 = (int(numeros_rut[1])) * 3
mul3 = (int(numeros_rut[2])) * 4
mul4 = (int(numeros_rut[3])) * 5
mul5 = (int(numeros_rut[4])) * 6
mul6 = (int(numeros_rut[5])) * 7
mul7 = (int(numeros_rut[6])) * 2
mul8 = (int(numeros_rut[7])) * 3
suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8
total = suma / 11
total = math.trunc(total)
total_multi = total * 11
valor_final = suma - total_multi
dv =  11 - valor_final
print("Tu dv es: ", dv)
print("11 = 0,  10 = K")
