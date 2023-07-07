from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class CloseParenthesisLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("CLOSE_PARENTHESIS")

    def _init(self):
        self.source_state = AutomatonStateLexical(False)
        self.source_state.add_transition(AutomatonTransitionLexical(AutomatonStateLexical(True), "\\)"))
