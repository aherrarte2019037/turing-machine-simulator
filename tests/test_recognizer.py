import unittest
from turing_machine import TuringMachine
from parser import parse_yaml
from colorama import Fore, Style

class TestRecognizer(unittest.TestCase):
    def setUp(self):
        self.config = parse_yaml('configurations/recognizer.yaml')
        self.tm = TuringMachine(self.config)

    def run_machine(self, input_string):
        self.tm.tape = list(input_string) + ['_']
        self.tm.head_position = 0
        self.tm.current_state = self.tm.initial_state
        result = self.tm.simulate()
        return ''.join(self.tm.tape).strip('_'), result.strip()

    def test_aaabbb(self):
        input_string = "aaabbb"
        final_tape, result = self.run_machine(input_string)
        print(Fore.CYAN + f"Probando cadena: '{input_string}'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Aceptada", result)
        print(Fore.GREEN + "Test PASADO: 'aaabbb' fue aceptada correctamente." + Style.RESET_ALL)

    def test_aabbbb(self):
        input_string = "aaaabbbb"
        final_tape, result = self.run_machine(input_string)
        print(Fore.CYAN + f"Probando cadena: '{input_string}'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Aceptada", result)
        print(Fore.GREEN + "Test PASADO: 'aaaabbbb' fue aceptada correctamente." + Style.RESET_ALL)

    def test_aaaabb(self):
        input_string = "aaaaabb"
        final_tape, result = self.run_machine(input_string)
        print(Fore.CYAN + f"Probando cadena: '{input_string}'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Rechazada", result)
        print(Fore.RED + "Test PASADO: 'aaaabb' fue rechazada correctamente." + Style.RESET_ALL)

    def test_aabbb(self):
        input_string = "aabbb"
        final_tape, result = self.run_machine(input_string)
        print(Fore.CYAN + f"Probando cadena: '{input_string}'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Rechazada", result)
        print(Fore.RED + "Test PASADO: 'aabbb' fue rechazada correctamente." + Style.RESET_ALL)

if __name__ == '__main__':
    unittest.main()
