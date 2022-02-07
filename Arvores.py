"""
Árvores, como listas encadeadas, fazem refência a subárvores,sendo a árvore binária: a que aponta para
outras duas, a mais comum.
O primeiro "nó" é chamado raiz
o resto são galhos e os últimos, que apontam para vazio, são folhas
Logo, árvores são estruturas de dados recursivas.
"""


def percorre_arvore(tree):
    if tree is None: return 0
    return tree.carga + percorre_arvore(tree.left) + percorre_arvore(tree.right)


class Tree:
    def __init__(self, carga=None, left=None, right=None):
        self.carga = carga
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.carga)

    def print(self):
        print(f"{self.carga}".center(6))
        print(f"{self.left}".ljust(3), end="")
        print(f"{self.right}".rjust(2))


if __name__ == '__main__':
    left = Tree(4)
    right = Tree(5)
    tree = Tree(0, left, right)
    tree.print()
    print(percorre_arvore(tree))
