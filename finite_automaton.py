class FiniteAutomaton:

    def __init__(self, Q, sigma, q0, F, transitions):
        self.Q = Q
        self.sigma = sigma
        self.q0 = q0
        self.F = F
        self.transitions = transitions

    @staticmethod
    def line_to_list(line):
        return line.strip().split(' ')

    @staticmethod
    def validate_q0(q0, Q):
        if q0 not in Q:
            raise Exception("Initial state is invalid")

    @staticmethod
    def validate_F(F, Q):
        for state in F:
            if state not in Q:
                raise Exception("Final states are invalid")

    @staticmethod
    def validate_transition(crt_state, input, next_state, sigma, Q):
        if crt_state not in Q or next_state not in Q or input not in sigma:
            raise Exception("Transition is invalid")

    @staticmethod
    def already_added_transition(crt_state, input, next_state, transitions):
        for t in transitions[(crt_state, input)]:
            if t == next_state:
                return True
        return False

    @staticmethod
    def read_from_file(file_name):
        with open(file_name) as file:
            Q = FiniteAutomaton.line_to_list(file.readline())
            sigma = FiniteAutomaton.line_to_list(file.readline())
            q0 = FiniteAutomaton.line_to_list(file.readline())[0]
            F = FiniteAutomaton.line_to_list(file.readline())

            FiniteAutomaton.validate_q0(q0, Q)
            FiniteAutomaton.validate_F(F, Q)

            transitions = {}

            for t in file:
                crt_state = t.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                input = t.strip().split('->')[0].strip().split(',')[1]
                next_state = t.strip().split('->')[1].strip()
                FiniteAutomaton.validate_transition(crt_state, input, next_state, sigma, Q)
                if (crt_state, input) in transitions.keys():
                    if FiniteAutomaton.already_added_transition(crt_state, input, next_state, transitions) is False:
                        transitions[(crt_state, input)].append(next_state)
                else:
                    transitions[(crt_state, input)] = [next_state]

            return FiniteAutomaton(Q, sigma, q0, F, transitions)

    def is_deterministic(self):
        for state in self.transitions.keys():
            if len(self.transitions[state]) != 1:
                return False
        return True

    def is_accepted(self, input):
        if self.is_deterministic():
            crt_state = self.q0
            for symbol in input:
                try:
                    crt_state = self.transitions[(crt_state, symbol)][0]
                except KeyError:
                    return False
            return crt_state in self.F
        return False

    def __str__(self):
        return "states = { " + ', '.join(self.Q) + " }\n" \
                "alphabet = { " + ', '.join(self.sigma) + " }\n" \
                "q0 = { " + self.q0 + " }\n" \
                "final_states = { " + ', '.join(self.F) + " }\n" \
                "transitions = { " + str(self.transitions) + " }"
