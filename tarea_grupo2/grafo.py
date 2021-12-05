# Python program to demonstrate searching operation
# in binary search tree without recursion
class newNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# A utility function to insert a new Node with given key in BST
def insert(Node, data):
    # If the tree is empty, return
    # a new Node
    if Node == None:
        return newNode(data)
    # Otherwise, recur down the tree
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)
    # return the (unchanged) Node pointer
    return Node


def get_path(root, key):
    # Base case
    if root is None:
        return "No existe", [None]

    # print wheter it turns left or right
    if root.data == key:
        return "", [root.data]

    if key > root.data:
        string_, path = get_path(root.right, key)
        return "Derecha " + string_, [root.data] + path
    elif key < root.data:
        string_, path = get_path(root.left, key)
        return "Izquierda " + string_, [root.data] + path

# Code used for prin_tree: https://stackoverflow.com/a/65865825
def print_tree(root, path, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        if root.left is None and root.right is None:
            line = f"{root.data}"
            width = len(line)
            if root.data in path:
                line = f"\033[1;31m{root.data}\033[1;m"
            height = 1
            middle = width // 2
            return [line], width, height, middle
        if root.right is None:
            lines, n, p, x = display(root.left)
            s = f"{root.data}"
            u = len(s)
            if root.data in path:
                s = f"\033[1;31m{root.data}\033[1;m"
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if root.left is None:
            lines, n, p, x = display(root.right)
            s = f"{root.data}"
            u = len(s)
            if root.data in path:
                s = f"\033[1;31m{root.data}\033[1;m"
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = display(root.left)
        right, m, q, y = display(root.right)

        s = f"{root.data}"
        u = len(s)
        if root.data in path:
            s = f"\033[1;31m{root.data}\033[1;m"
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, max(n, m, n + u + y), max(p, q, p + 2 + y), n + u // 2

    lines, _, _, _ = display(root)
    for line in lines:
        print(line)


if __name__ == '__main__':
    root = newNode(int(input("Ingrese el valor raiz para la generación del arbol binario: ")))
    n = int(input("Cantidad nodos para la generación del arbol binario: "))
    for i in range(1, n):
        insert(root, int(input(f"Ingrese el valor ({i}): ")))

    val = int(input("diga cual valor desea buscar en el arbol: "))

    print("La ruta del valor buscado desde el origen es:")
    string_, path = get_path(root, val)
    print(string_)

    print_tree(root, path)

# This code is contributed by PranchalK