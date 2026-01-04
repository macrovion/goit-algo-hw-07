class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# функція суми всіх значень у дереві
def sum_values(root):
   
    if root is None:
        return 0
   
    return root.key + sum_values(root.left) + sum_values(root.right)


def pre_order(root):
    if not root:
        return
    print(f"{root.key} ", end="")
    pre_order(root.left)
    pre_order(root.right)

if __name__ == "__main__":
    root = None
    
    # тестові дані
    keys = [10, 20, 30, 40, 50, 25]
    
    for key in keys:
        root = insert(root, key)

    print("\nPre-order обхід побудованого AVL-дерева:")
    pre_order(root)
    
    
    total_sum = sum_values(root)
    print(f"\n\nСума всіх значень у дереві: {total_sum}")    
