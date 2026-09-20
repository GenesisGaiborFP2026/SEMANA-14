def determinar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "El número es par"
    else:
        resultado = "El número es impar"
    return resultado
numero = 7
resultado = determinar_par_impar(numero)
print(resultado)