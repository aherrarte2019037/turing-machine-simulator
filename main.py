import unittest
from colorama import Fore, Style, init
import os

# Inicializar Colorama
init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n|Bienvenido al sistema de pruebas para la Máquina de Turing|")
    print(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una de las siguientes opciones:")
    print(Fore.GREEN + "1 →" + Fore.WHITE + " Correr pruebas de Alterator")
    print(Fore.GREEN + "2 →" + Fore.WHITE + " Correr pruebas de Recognizer")
    print(Fore.RED + "0 →" + Fore.WHITE + " Salir\n")

def run_alterator_tests():
    print(Fore.CYAN + "\nEjecutando pruebas para el Alterator...")
    print(Fore.YELLOW + "(Estas pruebas verifican si las cadenas son alteradas correctamente, marcando los símbolos desde el inicio y el final.)")
    print(Fore.YELLOW + "Incluyendo casos aceptados y rechazados.")

    # Correr tests de Alterator
    os.system("python3 -m unittest tests/test_alterator.py")

def run_recognizer_tests():
    print(Fore.CYAN + "\nEjecutando pruebas para el Recognizer...")
    print(Fore.YELLOW + "(Estas pruebas verifican si las cadenas tienen un número balanceado de 'a' y 'b' según las reglas de la máquina.)")
    print(Fore.YELLOW + "Incluyendo casos aceptados y rechazados.")

    # Correr tests de Recognizer
    os.system("python3 -m unittest tests/test_recognizer.py")

def main():
    while True:
        display_menu()
        choice = input(Fore.GREEN + "Seleccione una opción: " + Fore.WHITE)

        if choice == "1":
            clear_console()
            run_alterator_tests()
        elif choice == "2":
            clear_console()
            run_recognizer_tests()
        elif choice == "0":
            print(Fore.MAGENTA + "\nGracias por utilizar el sistema de pruebas para la Máquina de Turing.")
            break
        else:
            print(Fore.RED + "Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
