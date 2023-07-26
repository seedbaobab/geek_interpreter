from abc import ABC

from analyzer.core.typology.typology_v1 import TypologyV1
from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class IdentifierLexical(AutomatonLexical, ABC):
    """
    Identifier lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'IdentifierLexical' class.
        """
        super().__init__(TypologyV1.IDENTIFIER)

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(False)
        final: AutomatonStateLexical = AutomatonStateLexical(True)

        final.add_transition(AutomatonTransitionLexical(final, "[a-zAZ0-9]"))
        self.source_state.add_transition(AutomatonTransitionLexical(final, "[a-zA-Z]"))
