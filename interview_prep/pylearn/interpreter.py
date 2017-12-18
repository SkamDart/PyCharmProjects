from operator import add, sub, mul, truediv

ops = {
    'add': add,
    'mult': mul,
}
"""
https://leetcode.com/problems/parse-lisp-expression/description/
"""

def apply(op, *args):
    return op(list(map(int, args)))

def evaluate(expression):
    """
    :type expression: str
    :rtype: int
    """
    scope = expression[1:-1]

    if len(scope.split(" ")) == 3:
        split = scope.split(" ")
        op = ops[split[0]]
        return op(int(split[1]), int(split[2]))



print(evaluate("(mult 1 2)"))
print(evaluate("(add 1 2)"))

