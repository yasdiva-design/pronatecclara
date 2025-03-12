usuario = ('clarinha')
senha =('070808')
teste = True
while teste:
    usuario_correto =input ('digite seu nome') 
    senha_correta =input ("digite sua senha")
    if usuario_correto == usuario and senha_correta == senha:
        print('acesso permitido')
else:
    print("usuario ou senha correta, tente novamente")
