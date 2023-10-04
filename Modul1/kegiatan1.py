
def div(left_num, right_num):
    return left_num / right_num

def mult(left_num, right_num):
    return left_num * right_num

def minus(left_num, right_num):
    return left_num - right_num

def plus(left_num, right_num):
    return left_num + right_num

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_num, operator, right_num = node
        if operator == '+':
            return plus(tree(left_num), tree(right_num))
        elif operator == '-':
            return minus(tree(left_num), tree(right_num))
        elif operator == '*':
            return mult(tree(left_num), tree(right_num))
        elif operator == '/':
            return div(tree(left_num), tree(right_num))

expression_tree = ((2, '+', 3), '*', (5, '-', 1))

print("Result:", tree(expression_tree))