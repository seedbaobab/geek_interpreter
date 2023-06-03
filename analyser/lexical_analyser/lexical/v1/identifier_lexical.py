from abc import ABC

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition


class IdentifierLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("IDENTIFIER")

    def _initialize(self):
        final: AutomatonState = AutomatonState(True)
        source: AutomatonState = AutomatonState(False)

        source.add_transition(AutomatonTransition(final, "[a-zA-Z0-9]"))
        final.add_transition(AutomatonTransition(final, "[a-zA-Z0-9]"))

        self._source_state = source
