from finite_automaton import *

class Main:
    def __init__(self):
        self._fa = FiniteAutomaton.read_from_file('FA.in')

    def print_all(self):
        print(self._fa)

    def print_states(self):
        print(self._fa.Q)

    def print_alphabet(self):
        print(self._fa.sigma)

    def print_initial_state(self):
        print(self._fa.q0)

    def print_final_states(self):
        print(self._fa.F)

    def print_transitions(self):
        print(self._fa.transitions)

    def print_dfa_check(self):
        print("Yes, it is DFA") if self._fa.is_deterministic() else print("No, it is not DFA")

    def check_sequence(self):
        seq = input()
        print(self._fa.is_accepted(seq))

    def run(self):
        commands = {
                    '1': self.print_all,
                    '2': self.print_states,
                    '3': self.print_alphabet,
                    '4': self.print_initial_state,
                    '5': self.print_final_states,
                    '6': self.print_transitions,
                    '7': self.print_dfa_check,
                    '8': self.check_sequence
                    }
        ok = False
        while not ok:
            print("0. Exit")
            print("1. Display the finite automata")
            print("2. Display all states")
            print("3. Display the alphabet")
            print("4. Display the initial state/q0")
            print("5. Display the final states")
            print("6. Display all transitions")
            print("7. Check if FA is DFA")
            print("8. Check sequence")
            print(">>")
            cmd = input()
            if cmd in commands.keys():
                commands[cmd]()
            elif cmd == "0":
                ok = True
            else:
                continue

main = Main()
main.run()
