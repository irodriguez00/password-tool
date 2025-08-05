import random
import string

def generar_password(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Genera una contraseña segura con las opciones indicadas.

    Parámetros:
        longitud (int): Longitud de la contraseña (mínimo 4 caracteres recomendado).
        usar_mayusculas (bool): Incluir letras mayúsculas.
        usar_numeros (bool): Incluir dígitos numéricos.
        usar_simbolos (bool): Incluir símbolos especiales.

    Retorna:
        str: La contraseña generada.
    """
    if longitud < 4:
        raise ValueError("La longitud mínima recomendada es 4 caracteres")

    caracteres = string.ascii_lowercase

    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%^&*()_+-=<>?/"

    if not caracteres:
        raise ValueError("Debe incluir al menos un tipo de carácter.")

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password


# Test
if __name__ == "__main__":
    print("Generador de contraseñas")
    resultado = generar_password(16, True, True, True)
    print("Contraseña generada:", resultado)



    