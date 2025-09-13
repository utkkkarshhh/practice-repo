class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level = 0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)

def n_ary_tree():
    root = TreeNode("Root")
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    child3 = TreeNode("Child3")

    root.add_child(child1)
    root.add_child(child2)
    child2.add_child(child3)

    root.display()


if __name__ == "__main__":
    n_ary_tree()
