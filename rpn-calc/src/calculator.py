from stack import Stack


class Calculator:
    '''
    A simple RPN calculator
    '''

    def __init__(self):
        self.theStack = Stack()

    def parse(self, token: str):
        '''
        Process the token.
        Operands pop the required number of tokens from the self.theStack and
        push the operand result.
        "p" or "" (empty string) pop and print the top-most self.theStack
        element.
        Anything else is assumed to be a float, and is pushed.
        '''
        match token:
            case "+":
                self.theStack.push(
                    self.theStack.pop() + self.theStack.pop()
                )
            case "-":
                self.theStack.push(
                    self.theStack.pop() - self.theStack.pop()
                )
            case "*":
                self.theStack.push(
                    self.theStack.pop() * self.theStack.pop()
                )
            case "/":
                self.theStack.push(
                    self.theStack.pop() / self.theStack.pop()
                )
            case "%":
                self.theStack.push(
                    self.theStack.pop() % self.theStack.pop()
                )
            case "p":
                token = self.theStack.pop()
                print(token)
                return token
            case _:
                self.theStack.push(float(token))
