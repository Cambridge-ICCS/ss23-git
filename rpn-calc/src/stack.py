from typing import Any, List

# This might be too trivial, since python's `list` builtin lends itself very
# nicely to a stack.  However, we could instruct on separation of concerns, and
# suggest other implementations of Stack could be slotted in here without
# changing the rest of the code.


class Stack:
    '''
    A simple stack class.
    '''
    def __init__(self):
        '''
        Initialise the stack.
        '''
        self.the_stack: List[Any] = []

    def push(self, item: Any) -> None:
        '''
        Push an item onto the stack.
        '''
        self.the_stack.append(item)

    def pop(self) -> Any:
        '''
        Pop an item off the stack.
        '''
        return self.the_stack.pop()
