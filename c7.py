def converter_dolar_para_real(valor_dolar):
    taxa_convensão = 5.72
    valor_real = valor_dolar * taxa_convensão
    return valor_real
valor_dolar = 880
valor_em_real = converter_dolar_para_real(valor_dolar)
print(f"${valor_dolar} equivale a R${valor_em_real:.2}.")