from abc import ABC

from analyzer.core.typology.typology import Typology
from analyzer.lexical.token.target import Target
from analyzer.syntax.core.exception.syntax_analyser_exception import SyntaxAnalyzerException
from analyzer.syntax.core.grammar.core.grammar import Grammar
from analyzer.syntax.core.grammar.core.transition_grammar import TransitionGrammar


class NonTerminalGrammar(Grammar, ABC):
    """
    An grammar nan terminal.
    """

    def __init__(self, typology: Typology):
        """
        Initialize a new instance of 'NonTerminalGrammar' class.
        :param typology: The grammar type.
        """
        super().__init__(typology)
        self._sequence: list[TransitionGrammar] = []

    def _check_precondition_extraction(self, target: Target):
        """
        Check the precondition for the extraction.
        :param target:
        :return:
        """
        if target.is_finish:
            message: str = "Your command is incorrect here: "
            space: str = "{0}^".format("".ljust(len(message) + target.token.end, " "))
            raise SyntaxAnalyzerException("{0}{1}\n{2}\nThe command is terminated but {3} is expected."
                                          .format(message, target.command, space, self.typology.lower()))
