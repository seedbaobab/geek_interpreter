from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class IdentifierLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("IDENTIFIER")

    def _init(self):
        self.source_state = AutomatonStateLexical(False)
        final: AutomatonStateLexical = AutomatonStateLexical(True)

        final.add_transition(AutomatonTransitionLexical(final, "[_a-zA-Z0-9]"))
        self.source_state.add_transition(AutomatonTransitionLexical(final, "[a-zA-Z]"))
