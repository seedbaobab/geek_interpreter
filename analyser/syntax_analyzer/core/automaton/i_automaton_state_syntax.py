from analyser.syntax_analyzer.core.automaton.automaton_transition_syntax import AutomatonTransitionSyntax


class IAutomatonStateSyntax:

    def __init__(self):
        transitions: list[AutomatonTransitionSyntax]
