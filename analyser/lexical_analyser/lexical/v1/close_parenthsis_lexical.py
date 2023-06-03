from abc import ABC

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition


class CloseParenthesisLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("CLOSE_PARENTHESIS")

    def _initialize(self):
        final: AutomatonState = AutomatonState(True)
        source: AutomatonState = AutomatonState(False)

        source.add_transition(AutomatonTransition(final, "\)"))

        self._source_state = source
