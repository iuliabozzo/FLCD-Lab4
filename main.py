from finite_automaton import *

fa = FiniteAutomaton.read_from_file("FA.in")
print(fa.is_deterministic())
print(fa.is_accepted("abc1"))
