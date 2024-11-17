import unittest
from turing_machine import TuringMachine
from parser import parse_yaml
from colorama import Fore, Style

class TestAlterator(unittest.TestCase):
    def setUp(self):
        self.config = parse_yaml('configurations/alterator.yaml')
        self.tm = TuringMachine(self.config)

    def run_machine(self, input_string):
        self.tm.tape = list(input_string) + ['_']
        self.tm.head_position = 0
        self.tm.current_state = self.tm.initial_state
        result = self.tm.simulate()
        return ''.join(self.tm.tape).strip('_'), result.strip()

    def test_accept_aaabbb(self):
        final_tape, result = self.run_machine("aaabbb")
        print(Fore.CYAN + f"Probando cadena: 'aaabbb'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Aceptada", result)
        print(Fore.GREEN + "Test PASADO: 'aaabbb' fue aceptada correctamente." + Style.RESET_ALL)

    def test_accept_aaaabbbb(self):
        final_tape, result = self.run_machine("aaabbb")
        print(Fore.CYAN + f"Probando cadena: 'aaabbb'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Aceptada", result)
        print(Fore.GREEN + "Test PASADO: 'aaaabbbb' fue aceptada correctamente." + Style.RESET_ALL)

    def test_reject_aabaa(self):
        final_tape, result = self.run_machine("aabaa")
        print(Fore.CYAN + f"Probando cadena: 'aabaa'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Rechazada", result)
        print(Fore.RED + "Test PASADO: 'aabaa' fue rechazada correctamente." + Style.RESET_ALL)

    def test_reject_bbaaa(self):
        final_tape, result = self.run_machine("bbaaa")
        print(Fore.CYAN + f"Probando cadena: 'bbaaa'")
        print(f"Tape final: {final_tape}")
        print(f"Resultado: {result}" + Style.RESET_ALL)
        self.assertIn("Rechazada", result)
        print(Fore.RED + "Test PASADO: 'bbaaa' fue rechazada correctamente." + Style.RESET_ALL)

if __name__ == "__main__":
    unittest.main()
