def verificar_numero():
    numero = int(input("digite um numero inteiro: "))
    if numero > 0:
        print("o numero é positivo.")
    elif numero < 0:
        print("numero é negativo.")
    else:
        print("o numero é nulo(zero).")
    
    verificar_numero()