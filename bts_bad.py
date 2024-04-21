from manim import *

class TreeNode(VGroup):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.circle = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        self.text = Text(str(value)).scale(0.5)
        self.add(self.circle, self.text)

class BinaryTreeScene(Scene):
    def construct(self):
        tree = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [8, 9],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }
        root = TreeNode(1)
        root.move_to(ORIGIN)
        self.add(root)

        stack = [root]
        visited = set()

        while stack:
            node = stack[-1]
            if node.value not in visited:
                visited.add(node.value)
                self.play(Indicate(node))
                self.wait(0.5)
            stack.pop()

            for child_value in tree[node.value]:
                child = TreeNode(child_value)
                child.move_to(node.get_center() + DOWN)
                stack.append(child)
                self.play(Create(child))
                self.wait(0.5)