import random
import string

def gerador_senha_aleatoria():
    letras = string.ascii_letters
    digitos = string.digits
    caracteres = '!@#$%*._-'
    geral = letras + digitos + caracteres
    senha = "".join(random.choices(geral, k=20))

    return senha

print(gerador_senha_aleatoria())