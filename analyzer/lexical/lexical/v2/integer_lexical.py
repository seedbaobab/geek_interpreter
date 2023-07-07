from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class IntegerLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("INTEGER")

    def _init(self):
        self.source_state = AutomatonStateLexical(True)
        self.source_state.add_transition(AutomatonTransitionLexical(self.source_state, "\\d"))
