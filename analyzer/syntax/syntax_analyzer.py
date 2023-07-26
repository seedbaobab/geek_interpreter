from typing import Optional

from analyzer.lexical.token.target import Target
from analyzer.syntax.core.grammar.core.grammar import Grammar
from analyzer.syntax.core.tree.abstract_tree import AbstractTree


class SyntaxAnalyzer:
    """
    Syntax analyser class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'SyntaxAnalyzer' class.
        """
        pass

    def analyse(self, grammar_axiom: Grammar, target: Target) -> Optional[AbstractTree]:
        """
        Analyze the target.
        :param grammar_axiom: The axiom of the grammar.
        :param target: The target pt 
        :return:
        """
        return grammar_axiom.extract_leaf(target)
