class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.inorder()

    def inorder(self):
        if self.left and self.right:
            return f"({self.left.inorder()} {self.value} {self.right.inorder()})"
        else:
            return str(self.value)

def build_expression_tree(expression):
    tokens = expression.split()  # Divide la expresión en tokens
    stack = []

    for token in tokens:
        if token.isdigit() or token.isalpha():
            operand_tree = BinaryTree(token)  # Crea un árbol para el operando
            stack.append(operand_tree)
        elif token in "+-*/#&":
            if len(stack) < 2:
                raise ValueError("Invalid expression. Not enough operands.")
            right_tree = stack.pop()
            left_tree = stack.pop()
            operator_tree = BinaryTree(token)  # Crea un árbol para el operador
            operator_tree.left = left_tree
            operator_tree.right = right_tree
            stack.append(operator_tree)
        elif token == "#":
            stack.append(BinaryTree("#"))  # Agrega un nodo de marcador "#" como operando
        else:
            raise ValueError("Invalid token: " + token)

    if len(stack) != 1:
        raise ValueError("Invalid expression. Too many operators.")

    return stack[0]

# Ejemplo de uso:
if __name__ == "__main__":
    expressions = [
        ("91 95 + 15 + 19 + 4 *", "Expression A"),
        ("B B * A C 4 * * -", "Expression B"),
        ("42", "Expression C"),
        ("A 57 &", "Expression D"),
        ("+ / &", "Expression E")
    ]

    for expression, label in expressions:
        try:
            tree = build_expression_tree(expression)
            print(label)
            print("Expression:", expression)
            print("Binary Tree:", tree)
            print("Inorder Traversal:", tree.inorder())  # Agrega la impresión de recorrido en orden
        except Exception as e:
            print(label)
            print("Error:", str(e))

        print()
