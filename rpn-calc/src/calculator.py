from stack import Stack


class Calculator:
    '''
    A simple RPN calculator
    '''

    def __init__(self):
        self.the_stack = Stack()

    def parse(self, token: str):
        '''
        Process the token.
        Operands pop the required number of tokens from the self.the_stack and
        push the operand result.
        "p" or "" (empty string) pop and print the top-most self.the_stack
        element.
        Anything else is assumed to be a float, and is pushed.
        '''
        match token:
            case "+":
                self.the_stack.push(
                    self.the_stack.pop() + self.the_stack.pop()
                )
            case "-":
                self.the_stack.push(
                    self.the_stack.pop() - self.the_stack.pop()
                )
            case "*":
                self.the_stack.push(
                    self.the_stack.pop() * self.the_stack.pop()
                )
            case "/":
                self.the_stack.push(
                    self.the_stack.pop() / self.the_stack.pop()
                )
            case "p":
                token = self.the_stack.pop()
                print(token)
                return token
            case _:
                self.the_stack.push(float(token))
