from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class StringLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("STRING")

    def _init(self):
        self.source_state = AutomatonStateLexical(False)

        step: AutomatonStateLexical = AutomatonStateLexical(False)
        final: AutomatonStateLexical = AutomatonStateLexical(True)

        step.add_transition(AutomatonTransitionLexical(step, "[^\"]"))
        step.add_transition(AutomatonTransitionLexical(final, "\""))
        self.source_state.add_transition(AutomatonTransitionLexical(step, "\""))
