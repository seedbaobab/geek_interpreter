from analyzer.lexical.lexical_analyzer import LexicalAnalyzer
from analyzer.lexical.token.target import Target
from analyzer.lexical.token.token import TokenModel
from analyzer.syntax.core.tree.abstract_tree import AbstractTree
from analyzer.syntax.syntax.v1.axiom_v1 import AxiomV1

from analyzer.syntax.syntax_analyzer import SyntaxAnalyzer
from model.symbol.core.table.symbol_table import SymbolTable


class Interpreter:
    """
    The Geek interpreter class.
    """

    def __init__(self):
        """
        Initialize a new instance of 'Interpreter' class.
        """
        self.__symbol_table: SymbolTable = SymbolTable()
        self.__lexical_analyser: LexicalAnalyzer = LexicalAnalyzer()
        self.__syntax_analyser: SyntaxAnalyzer = SyntaxAnalyzer()

    def interpret(self, command: str):
        """
        Interpret the command.
        :param command: The command to interpret.
        """
        print(command)
        tokens: list[TokenModel] = self.__lexical_analyser.analyse(command)
        for token in tokens:
            print(token.to_str())

        root: AbstractTree = self.__syntax_analyser.analyse(AxiomV1(), Target(command, tokens))
        print("\nPRINT TREE")
        print(command)
        print(root.to_str())
