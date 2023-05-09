'''
Introduction:
    Before running this program, reading the **README.md** first may helps you a lot
    Here is the core code of this program, you can run this file or call some other function at the bottom in the "if __name__=='__main__': "
    However, you are also recommended to run in **main.py**, it is much more user-friendly.
'''


import sys
import os
import pickle


# Create a binary tree class
class BiTreeNode:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


# This function receives an infix expression, turns it into a reverse Polish expression and returns it
def suffix(arr):
    Stack = []  # use stack to collect all the operators and brackets
    lst = []
    for value in arr:
        if value == '(':
            Stack.append(value)
        elif value == ')':
            S_n = len(Stack) - 1
            while S_n != -1 and Stack[S_n] != '(':
                lst.append(Stack.pop())
                S_n -= 1
            if Stack != []:
                Stack.pop()     # pop out the "("
        elif 48 <= ord(value) <= 57:  # ord() from 48 to 57 is exactly '0' to '9'
            lst.append(value)
        else:
            Stack.append(value)
    return lst


# This function turns the reverse Polish expression into a binary tree and returns it
def build_tree(li):
    ind = 0
    while True:
        if ind == len(li):
            break
        now = li[ind]
        if 48 <= ord(now) <= 57:
            ind += 1
        else:   # When finding an operator, convert it into a BiTreeNode class
            rt = BiTreeNode(now)
            li[ind] = rt
            if type(li[ind - 1]) == str:
                rt.lchild = BiTreeNode(li[ind - 1])
            else:
                rt.lchild = li[ind - 1]
            if type(li[ind - 2]) == str:
                rt.rchild = BiTreeNode(li[ind - 2])
            else:
                rt.rchild = li[ind - 2]
            li.pop(ind - 1)
            li.pop(ind - 2)
            ind -= 1
    return rt


# the function below is using for visualize the tree
def print_inorder(root, height = 0, length = 4):
    if not root:
        return
    print_inorder(root.rchild, height + 1, length)
    print(" " * height * length + root.data)
    print_inorder(root.lchild, height + 1, length)


# Using to detect whether the brackets are matched
def match_bracket(expr):
    # Check the two sides of the equation
    if expr[0] != "(" or expr[-1] != ")":
        # raise SyntaxError
        return "SyntaxError: Not a valid expression, brackets mismatched."
    Stack = []  # Used to carry brackets
    for i in expr:
        if i == '(':
            Stack.append(i)
        elif i == ')':
            if len(Stack) == 0:
                # raise SyntaxError
                return "SyntaxError: Not a valid expression, brackets mismatched."
            Stack.pop(-1)
    if len(Stack) != 0:
        # raise SyntaxError
        return "SyntaxError: Not a valid expression, brackets mismatched."
    else:
        return True


# checking whether the number of operands in equation are correct
def check_operands(expr):
    Stack = []  # used to carry "(" and operators
    operands = []
    ind = 0
    length = len(expr)
    # First make sure the equation has at least a pair of brackets at two sides, if do not have this part, this function can't deal with something like "(1+1)/2"
    if expr[0] != "(" or expr[-1] != ")":
        return "SyntaxError: Not a valid expression, brackets mismatched."
    for j, i in enumerate(expr):
        if 48 <= ord(i) <= 57 and expr[j-1] == '(' and expr[j+1] == ')':
            # raise SyntaxError
            return 'SyntaxError: Not a valid expression, wrong number of operands.'
        elif i in '+-*/':
            if (48 <= ord(expr[j-1]) <=57 and expr[j+1] == ")") or (48 <= ord(expr[j+1]) <=57 and expr[j+1] == "("):
                return 'SyntaxError: Not a valid expression, one number missing.'
            elif expr[j-1] == '(' and expr[j+1] == ')':
                return 'SyntaxError: Not a valid expression, two numbers missing.'
    while True:
        if expr[ind] == '(' or expr[ind] in ['+', '-', "*", '/']:
            Stack.append(expr[ind])
            ind += 1
        elif expr[ind] == ')':
            temp = []
            while Stack[-1] != '(':
                if Stack[-1] in ['+', '-', '*', '/']:
                    tp = Stack.pop(-1)
                    operands.append(tp)
                    temp.append(tp)
            Stack.pop(-1)
            # Finding if there are more than one operand in a pair of brackets
            if len(temp) > 1:
                # raise SyntaxError
                return 'SyntaxError: Not a valid expression, wrong number of operands.'
            # Finding if there has missed a operand in this pair of brackets
            if len(temp) == 0:
                # raise SyntaxError
                return 'SyntaxError: Not a valid expression, operator missing.'
            ind += 1
        else:
            ind += 1
        # This is how we check whether the equation has missed a pair of brackets at two sides eg: (1*2)-(1/2) [expected: ((1*2)-(1/2))]
        if len(Stack) == 0 and ind != length:
            # raise SyntaxError
            return 'SyntaxError: Not a valid expression, brackets mismatched.'
        if len(Stack) == 0 and ind == length:
            break
    return True


def check_valid(expr):
    for i in expr:
        if not (48 <= ord(i) <= 57 or i in ['+', '-', '*', '/', '(', ')']):
            # raise TypeError
            return "TypeError: Not a valid expression, invalid symbol was entered."
    return True


# Exception Handling
def test(expr):
    # Here using set to carry all the Exception
    Set = set()
    valid, bracket, operands = check_valid(expr), match_bracket(expr), check_operands(expr)
    if type(valid) != bool:
        Set.add(valid)
    if type(bracket) != bool:
        Set.add(bracket)
    if type(operands) != bool:
        Set.add(operands)
    if len(Set) == 0:
        return True
    print(f"{len(Set)} Error")
    for i in Set:
        print(i)
    return False

'''
# finding the height of the tree, for print_tree(). (Not required)
def depth(root):
    if not root:
        return 0
    leftDepth = depth(root.lchild) + 1
    rightDepth = depth(root.rchild) + 1
    height = max(rightDepth, leftDepth)
    return height
    

# another way to print the tree, not required in the assignment
def print_tree(root):
    current = depth(root)
    max_word = 3 * (2**(current - 1)) - 1
    node_space = max_word // 2
    queue1 = [[root, node_space + 1]]
    queue2 = []
    while queue1:
        position = []
        for i in range(len(queue1)):
            node = queue1[i][0]
            space = queue1[i][1] - 1
            if node.data == root.data:
                space -= 2
            if node.lchild is not None:
                position.append([space, '/'])
                queue2.append([node.lchild, space - 1])
            space += 2
            if node.data == root.data:
                space += 4
            if node.rchild is not None:
                position.append([space, '\\'])
                queue2.append([node.rchild, space + 1])
        if len(queue1) > 0:
            last_node = queue1[len(queue1) - 1][1]
            index = 0
            for i in range(last_node + 1):
                if index < len(queue1) and i == queue1[index][1]:
                    print(queue1[index][0].data, end='')
                    index += 1
                else:
                    print(' ', end='')
        print()
        index = 0
        if len(position) > 0:
            for i in range(position[len(position) - 1][0] + 1):
                if i == position[index][0]:
                    print(position[index][1], end='')
                    index += 1
                else:
                    print(' ', end='')
        print()
        queue1 = []
        while queue2:
            queue1.append(queue2.pop(0))
        node_space -= 2
'''

def save_tree(root, file_name='default_save.pkl', path="tree_files/"):
    with open(os.path.join(path, file_name), 'wb') as f:
        pickle.dump(root, f)


def read_tree(file_name='default_read.pkl', path="tree_files/"):
    with open(os.path.join(path, file_name), 'rb') as f:
        root = pickle.load(f)
        print('==================== read from document ====================')
        print_inorder(root)
        return root


def main_function():
    formula = input('please type in your equation\n')
    # test the equation first, if the equation has something wrong, exit the program now
    if not test(formula):
        sys.exit()
    try:
        res = eval(formula)
    except (Exception) as e:
        print(repr(e))
        sys.exit()
    # turn the equation into suffix expression
    suffix_expr = suffix(formula)
    root = build_tree(suffix_expr)
    print()
    print(f"the result is: {res}")
    print('=' * 60)
    print_inorder(root)
    # the following two rows are using for the function print_tree() that can print the tree in another way
    # print('=' * 60)
    # print_tree(root)
    return root


#  you can directly run this file, or run in main.py
if __name__ == '__main__':
    # You can do some changes or call some funcions here
    root = main_function()
    # The following two functions can both recieve one more parameter -- path
    save_tree(root, file_name = "default_save.pkl")
    read_tree(file_name = "default_read.pkl") 