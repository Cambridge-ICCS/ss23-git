"""
A Reverse Polish Notation calculator.
"""

import sys
from typing import Any, List, TYPE_CHECKING
from calculator import Calculator


if TYPE_CHECKING:
    from collections.abc import Iterable


def main(commands: "Iterable" = sys.stdin):
    '''
    Iterate through commands (default stdin)
    parsing each line.
    '''
    calculator = Calculator()
    for line in commands:
        parse_tokens(calculator, line.split(' '))
    return calculator.parse('p')


def parse_tokens(calculator: Calculator, tokens: List[Any]):
    '''
    Just feed the tokens into the calculator.
    FIXME: Could this be in Calculator?
    '''
    for token in tokens:
        calculator.parse(token.rstrip())


if __name__ == '__main__':
    calculator = Calculator()
    main()
