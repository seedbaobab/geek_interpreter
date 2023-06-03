from analyser.syntax_analyzer.core.automaton.i_automaton_state_syntax import IAutomatonStateSyntax


class AutomatonTransitionSyntax:

    def __init__(self, destination: IAutomatonStateSyntax):
        self.__destination: IAutomatonStateSyntax = destination

    @property
    def destination(self):
        return self.__destination

    def is_valid(self):
