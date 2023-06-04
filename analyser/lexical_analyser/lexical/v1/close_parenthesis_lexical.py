from analyser.lexical_analyser.core.automaton.automaton_lexical import AutomatonLexical
from analyser.lexical_analyser.core.automaton.automaton_state_lexical import AutomatonStateLexical
from analyser.lexical_analyser.core.automaton.automaton_transition_lexical import AutomatonTransitionLexical


class CloseParenthesisLexical(AutomatonLexical):

    def __init__(self):
        super().__init__()

        self._source = AutomatonStateLexical(False)
        self._source.add_transition(AutomatonTransitionLexical(AutomatonStateLexical(True), "\\)"))
