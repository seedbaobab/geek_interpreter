from abc import ABC

from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state import AutomatonState
from analyser.lexical_analyser.core.automaton.automaton_transition import AutomatonTransition


class StringLexical(AutomatonLexical, ABC):

    def __init__(self):
        super().__init__("STRING")

    def _initialize(self):
        final: AutomatonState = AutomatonState(True)
        source: AutomatonState = AutomatonState(False)
        step_one: AutomatonState = AutomatonState(False)

        source.add_transition(AutomatonTransition(step_one, "\""))
        step_one.add_transition(AutomatonTransition(step_one, "[^\"]"))
        step_one.add_transition(AutomatonTransition(final, "\""))

        self._source_state = source
