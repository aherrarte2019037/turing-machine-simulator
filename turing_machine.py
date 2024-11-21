class TuringMachine:
    # funcion inicial
    def __init__(self, config):
        self.states = config['states']
        self.input_alphabet = config['input_alphabet']
        self.tape_alphabet = config['tape_alphabet']
        self.transitions = {
            tuple(k.strip("()").split(", ")): v for k, v in config['transitions'].items()
        }
        self.initial_state = config['initial_state']
        self.accept_state = config['accept_state']
        self.reject_state = config['reject_state']
        self.tape = list(config['input']) + ['_']
        self.head_position = 0
        self.current_state = self.initial_state

    # funcion para mover la cinta
    def step(self):
        symbol = self.tape[self.head_position]
        transition_key = (self.current_state, symbol)

        if transition_key in self.transitions:
            next_state, write_symbol, move = self.transitions[transition_key]
            self.tape[self.head_position] = write_symbol
            self.head_position += 1 if move == 'R' else -1

            if self.head_position < 0:
                self.tape.insert(0, '_')
                self.head_position = 0
            elif self.head_position >= len(self.tape):
                self.tape.append('_')

            self.current_state = next_state
        else:
            print(f"No se encontro la transición: {transition_key}")
            self.current_state = self.reject_state


    # funcion para simular la maquina de turing
    def simulate(self):
        result = f"Estado inicial: {self.current_state}\n"
        while self.current_state not in {self.accept_state, self.reject_state}:
            result += f"Estado actual: {self.current_state}, Cinta: {''.join(self.tape)}\n"
            self.step()
        result += f"Resultado final: {'Aceptada' if self.current_state == self.accept_state else 'Rechazada'}\n"
        return result
