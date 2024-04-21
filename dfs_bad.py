from manim import *

class Node(Circle):
    def __init__(self, val, left=None, right=None, **kwargs):
        super().__init__(**kwargs)
        self.val = val
        self.left = left
        self.right = right
        self.label = Text(str(val)).scale(0.75)
        self.label.move_to(self)

class BinaryTree(VGroup):
    CONFIG = { 
        "radius": 0.5,
        "buff": 1,
        "root_to_child_stroke_width": 2,
    }

    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.add(self.root) 
        self.layout_tree(self.root)

    def layout_tree(self, node, parent=None, direction=None):
        if node is not None:
            dx = self.CONFIG["buff"] * (2 if direction == "RIGHT" else -2)  # Ensure direction is a string
            dy = self.CONFIG["buff"]  # Downwards spacing
            if parent:
                node.move_to(parent.get_center() + np.array([dx, -dy, 0]))
                self.add(Line(parent, node, stroke_width=self.CONFIG["root_to_child_stroke_width"]))

            self.layout_tree(node.left, node, "LEFT")
            self.layout_tree(node.right, node, "RIGHT")

class DFSScene(Scene):
    def construct(self):
        # Create the binary tree (replace with your tree data)
        root = Node(1, radius=0.8)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        tree = BinaryTree(root)
        tree.arrange_submobjects(DOWN) 

        # Visualize the stack
        stack_text = Text("Stack").shift(RIGHT * 3 + UP * 2)
        stack = VGroup(*[Rectangle(width=1, height=0.5) for _ in range(5)]).arrange(DOWN, buff=0.2).next_to(stack_text, DOWN)

        self.play(FadeIn(tree), Write(stack_text), Create(stack))

        visited = set()  # Track visited nodes
        search_value = 5  # Adjust search as needed
        self.dfs(tree.root, stack, visited, search_value) 

    def dfs(self, node, stack, visited, search_value):
        if node is None:
            return 

        visited.add(node)
        self.highlight_node(node) 
        self.update_stack(stack, node, "push") 

        if node.val == search_value:
            self.indicate_found(node)
            return

        for child in (node.left, node.right):
            if child and child not in visited:
                self.dfs(child, stack, visited, search_value)

        self.update_stack(stack, node, "pop") 
        self.unhighlight_node(node) 

    def highlight_node(self, node):
        self.play(node.animate.set_color(YELLOW), node.label.animate.set_color(YELLOW))

    def unhighlight_node(self, node):
        self.play(node.animate.set_color(WHITE), node.label.animate.set_color(WHITE))

    def indicate_found(self, node):
        circle = Circle(color=GREEN, radius=node.radius + 0.1, stroke_width=3)
        circle.move_to(node)
        self.play(FadeIn(circle), run_time=0.5)

    def update_stack(self, stack, node, action):
        if action == "push":
            new_rect = stack[0].copy()  # Placeholder, adjust as needed
            self.play(new_rect.animate.shift(DOWN * 0.5)) 
        elif action == "pop":
            if len(stack) > 0:
                top_rect = stack[-1]  # Get the top element
                stack.remove(top_rect)  # Remove the top element from the stack
                self.play(FadeOut(top_rect.shift(UP * 0.5))) 