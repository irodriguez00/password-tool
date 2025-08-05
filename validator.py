import re

def validar_password(password: str) -> str:
    """
    Verificación de si una contraseña es segura.

    Reglas aplicadas:
    - Mínimo 8 caracteres.
    - Al menos una letra mayúscula.
    - Al menos una letra minúscula.
    - Al menos un número.
    - Al menos un símbolo especial.

    Parámetros:
        password (str): Contraseña a validar.

    Retorna:
        str: Mensaje indicada si es segura o indicando que le falta.
    """

    if len(password) < 8:
        return "Contraseña muy corta (mínimo 8 caracteres)."
    if not re.search(r"[A-Z]", password):
        return "Falta al menos una letra mayúscula."
    if not re.search(r"[a-z]", password):
        return "Falta al menos una letra minúscula."
    if not re.search(r"\d", password):
        return "Falta al menos un número."
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]",password):
        return "Falta al menos un símbolo."
    
    return "Contraseña segura."

#Test 

if __name__ == "__main__":
    prueba = input("Ingresá una contraseña para validar:")
    resultado = validar_password(prueba)
    print(resultado)