def soma(a, b):
    """Função simples para somar dois números"""
    return a + b


if __name__ == "__main__":
    print("Resultado:", soma(3, 5))



#testes abaixo, caso queira testar o validador ou um erro de segurança, descomente um dos respectivos blocos abaixo

"""Função com erro proposital"""

#def soma(a, b):
#    return a - b  # <- deveria ser +, mas colocamos - de propósito


""" Linha insegura de propósito"""

#def soma(a, b):
#    return a + b

#eval("print('Executando código inseguro!')")
