class BinaryTreenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    # Divide la expresión en tokens (operadores y operandos) utilizando el espacio como delimitador
    tokens = expression.split()
    stack = []
    
    for token in tokens:
        if token.isdigit():
            # Si el token es un operando (número), crea un árbol de un solo nodo con el operando y lo agrega a la pila
            operand_tree = BinaryTree(token)
            stack.append(operand_tree)
        else:
            # Si el token es un operador, saca dos árboles de la pila (que deben ser operandos) y combínalos en un nuevo árbol con el operador como nodo raíz
            if len(stack) < 2:
                raise ValueError("Invalid expression. Not enough operands.")
            right_tree = stack.pop()
            left_tree = stack.pop()
            operator_tree = BinaryTree(token)
            operator_tree.left = left_tree
            operator_tree.right = right_tree
            stack.append(operator_tree)

    # Al final, debe haber un solo árbol en la pila, que es el árbol binario completo que representa la expresión
    if len(stack) != 1:
        raise ValueError("Invalid expression. Too many operands.")
    
    return stack[0]

def inorder_traversal(tree):
    if tree is None:
        return ""
    
    if tree.left and tree.right:
        # Recorre en orden los subárboles izquierdo, el operador y el subárbol derecho, agregando paréntesis para mantener la precedencia del operador
        return f"({inorder_traversal(tree.left)} {tree.value} {inorder_traversal(tree.right)})"
    else:
        # Si el árbol es un nodo de un solo operando, simplemente devuelve el valor del nodo
        return str(tree.value)

def postfix_evaluation(tree):
    if tree is None:
        return 0
    
    if tree.left and tree.right:
        # Si el árbol tiene hijos izquierdo y derecho, evalúa recursivamente los valores de los subárboles y aplica el operador del nodo raíz
        left_val = postfix_evaluation(tree.left)
        right_val = postfix_evaluation(tree.right)
        return evaluate_operation(tree.value, left_val, right_val)
    else:
        # Si el árbol es un nodo de un solo operando, simplemente devuelve su valor
        return int(tree.value)

def evaluate_operation(operator, left_operand, right_operand):
    # Evalúa la operación utilizando el operador y los operandos proporcionados
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
    else:
        raise ValueError("Invalid operator.")

if __name__ == "__main__":
    try:
        expression_a = "91 95 15 19 4*"
        tree_a = build_expression_tree(expression_a)
        print("Expresión A:", expression_a)
        print("Árbol binario A:", inorder_traversal(tree_a))
        print("Resultado A:", postfix_evaluation(tree_a))

        expression_b = "B B * A C 4 * * -"
        tree_b = build_expression_tree(expression_b)
        print("\nExpresión B:", expression_b)
        print("Árbol binario B:", inorder_traversal(tree_b))
        print("Resultado B:", postfix_evaluation(tree_b))

        expression_c = "42"
        tree_c = build_expression_tree(expression_c)
        print("\nExpresión C:", expression_c)
        print("Árbol binario C:", inorder_traversal(tree_c))
        print("Resultado C:", postfix_evaluation(tree_c))

        expression_d = "A 57 #"
        tree_d = build_expression_tree(expression_d)
        print("\nExpresión D:", expression_d)
        print("Árbol binario D:", inorder_traversal(tree_d))
        print("Resultado D:", postfix_evaluation(tree_d))
    except Exception as e:
        print("Error:", str(e))