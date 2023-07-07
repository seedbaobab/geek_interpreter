from abc import ABC

from analyzer.lexical.core.automaton.automaton_lexical import AutomatonLexical
from analyzer.lexical.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyzer.lexical.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class UnderscoreLexical(AutomatonLexical, ABC):
    """
    Underscore lexical unit class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'UnderscoreLexical' class.
        """
        super().__init__("UNDERSCORE")

    def _init(self):
        """
        Initialize the lexical unit.
        """
        self.source_state = AutomatonStateLexical(False)
        self.source_state.add_transition(AutomatonTransitionLexical(AutomatonStateLexical(True), "_"))
