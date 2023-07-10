# Reverse Polish notation calculator in Python
Reverse Polish notation (RPN) is a postfix expression notation. Unlike the infix
notation taught in schools, RPN defines an unambiguous evaluation strategy
without brackets. This makes it especially simple to implement an RPN calculator
-- all you need is a small amount of parsing code, and a stack (a first in,
first out data structure).

## Usage
From the `rpn-calc/src` directory:

```
python rpn_calc.py
```

Expressions are read from `stdin`. Input strings are broken into space-separated
tokens.

  * Binary operators: `+`, `-`, `*`, `/`
  * Special functions: `p` (pops number on top of stack and prints)
  * Numbers are parsed as *floats*.

At input end, the top of the stack is popped and printed.

Binary operators work by popping two arguments off the stack, running a
calculation, and pushing the result. The top of the stack becomes the left
operand, and the element one below the top becomes the right operand, as in the
following illustration:

![Illustration of binary operator processing](/rpn-calc/docs/oper-order.png)

### Example
The input string `1 2 +` processed as follows:

  * `1`: push `1`
  * `2`: push `2`
  * `+`: pop `2`, pop `1`, push `2 + 1`

Here's an example shell session:

```
$ cd rpn-calc/src
$ python rpn_calc.py << EOM
1 2 +
EOM
3.0
```

## Installation (including running `pytest`)
```
git clone https://github.com/Cambridge-ICCS/ss23-git.git
cd ss23-git
python -m venv venv
source venv/bin/activate
pip install pytest
cd rpn-calc/src
pytest
```
