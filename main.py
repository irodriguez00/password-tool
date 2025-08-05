from generator import generar_password
from validator import validar_password

def menu():
    while True:
        print("\n=== Herramienta de Contraseñas ===")
        print("1. Generar contraseña segura")
        print("2. Validar contraseña")
        print("3. Salir")

        opcion = input("Seleccioná una opción (1/2/3): ")

        if opcion == "1":
            try:
                longitud = int(input("Longitud de la contraseña: "))
                usar_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
                usar_nums = input("¿Incluir números? (s/n): ").lower() == "s"
                usar_syms = input("¿Incluir símbolos? (s/n): ").lower() == "s"

                password = generar_password(longitud, usar_mayus, usar_nums, usar_syms)
                print(f"Contraseña generada: {password}")
            except ValueError:
                print("Ingresá un número válido para la longitud.")

        elif opcion == "2":
            pwd = input("Ingresá la contraseña a validar: ")
            resultado = validar_password(pwd)
            print(resultado)

        elif opcion == "3":
            print("Hasta luego")
            break

        else:
            print("Opción no válida. Elegí 1, 2 o 3.")

if __name__ == "__main__":
    menu()
