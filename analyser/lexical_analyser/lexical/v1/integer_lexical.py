from abc import ABC

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition


class IntegerLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("INTEGER")

    def _initialize(self):
        final: AutomatonState = AutomatonState(True)
        final.add_transition(AutomatonTransition(final, "\\d"))
        self._source_state = final
