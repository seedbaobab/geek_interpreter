from abc import ABC

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition


class SpaceLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("SPACE")

    def _initialize(self):
        final: AutomatonState = AutomatonState(True)
        final.add_transition(AutomatonTransition(final, "\\s"))
        self._source_state = final
