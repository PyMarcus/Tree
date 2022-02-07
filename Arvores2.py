class Tree:
    def __init__(self, root=None, left=None, right=None):
        self.payload = root
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.__payload)

    def Centerprint(self):
        contador = 25
        print(f"{self.payload}".center(contador), flush=True)
        contador = 10
        contador1 = 5
        while self.right and self.left:
            print(f"{self.left.payload}".rjust(contador), flush=True, end="")
            print(f"{self.right.payload}".rjust(contador1), flush=True)
            contador -= 2
            contador1 += 4
            self.left = self.left.left
            self.right = self.right.right


class Left:
    def __init__(self, payload=None, left=None, right=None):
        self.payload = payload
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.payload)


class Right:
    def __init__(self, payload=None, left=None, right=None):
        self.payload = payload
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.payload)


if __name__ == '__main__':
    galho3 = Left(3)
    galho4 = Right(4)
    galho5 = Left(5)
    galho6 = Right(6)
    galho1 = Left(1, galho3, galho4)
    galho2 = Right(2, galho5, galho6)
    raiz = Tree(0, galho1, galho2)
    raiz.Centerprint()
