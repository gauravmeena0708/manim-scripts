from manim import *

class StackNode(VGroup):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.box = Rectangle(height=0.5, width=1.5, stroke_color=BLUE, stroke_width=2, fill_color=BLUE, fill_opacity=0.3)
        self.text = Text(str(value)).move_to(self.box.get_center())
        self.add(self.box, self.text)

class StackScene(Scene):
    def construct(self):
        stack = VGroup() 
        top_pointer = Arrow(UP)
        top_label = Text("Top").next_to(top_pointer, UP)

        def push(value):
            nonlocal stack, top_pointer, top_label
            new_node = StackNode(value)
            if len(stack) == 0:
                new_node.move_to(ORIGIN)
            else:
                new_node.next_to(stack[-1], UP, buff=0)
            self.play(Create(new_node))
            stack.add(new_node)

            # Update top pointer
            top_pointer.next_to(stack[-1], UP) 
            self.play(FadeIn(top_pointer), FadeIn(top_label))
            push_label = Text("Push", font_size=36).next_to(stack, RIGHT)
            self.play(FadeIn(push_label))
            self.wait(0.5)
            self.play(FadeOut(push_label))

        def pop():
            nonlocal stack, top_pointer, top_label
            if len(stack) == 0:
                return None
            popped_node = stack[-1]
            self.play(FadeOut(popped_node))
            stack.remove(popped_node)

            # Update top pointer
            if len(stack) == 0:
                self.play(FadeOut(top_pointer), FadeOut(top_label))
            else:
                top_pointer.next_to(stack[-1], UP)
            pop_label = Text("Pop", font_size=36).next_to(stack, RIGHT)
            self.play(FadeIn(pop_label))
            self.wait(0.5)
            self.play(FadeOut(pop_label))


        # Demonstration
        self.play(Write(top_pointer), Write(top_label))  # Initial top pointer
        push(5)
        push(8)
        push(3)
        popped_value = pop()
        self.wait(1)
        push(2)
        popped_value = pop()
        popped_value = pop()
        self.wait(1)

class QueueNode(VGroup):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.box = Rectangle(height=0.5, width=1.5, stroke_color=GREEN, stroke_width=2, fill_color=GREEN, fill_opacity=0.3)
        self.text = Text(str(value)).move_to(self.box.get_center())
        self.add(self.box, self.text)

class QueueScene(Scene):
    def construct(self):
        queue = VGroup()
        front_pointer = Arrow(LEFT)
        front_label = Text("Front").next_to(front_pointer, LEFT)
        rear_pointer = Arrow(LEFT)
        rear_label = Text("Rear").next_to(rear_pointer, LEFT)

        def enqueue(value):
            nonlocal queue, front_pointer, front_label, rear_pointer, rear_label
            new_node = QueueNode(value)
            if len(queue) == 0:
                new_node.move_to(ORIGIN)
                rear_pointer.next_to(new_node, RIGHT)  # Initial rear pointer
                self.play(FadeIn(rear_pointer), FadeIn(rear_label))
            else:
                new_node.next_to(queue[-1], RIGHT, buff=0)

            self.play(Create(new_node))
            queue.add(new_node)

            # Update front pointer 
            if len(queue) == 1:
                front_pointer.next_to(queue[0], LEFT)
                self.play(FadeIn(front_pointer), FadeIn(front_label))

            self.play(Write(Text("Enqueue").next_to(queue, DOWN)))

        def dequeue():
            nonlocal queue, front_pointer, front_label, rear_pointer, rear_label
            if len(queue) == 0:
                return None

            removed_node = queue[0]  # Access the first element
            self.play(FadeOut(removed_node))
            queue.remove(removed_node)  # Remove from VGroup


            # Update rear pointer
            if len(queue) == 0:  # If queue becomes empty
                self.play(FadeOut(rear_pointer), FadeOut(rear_label))
                front_pointer.next_to(ORIGIN, LEFT)  # Move front pointer to start
                self.play(FadeOut(front_pointer), FadeOut(front_label))
            else:
                rear_pointer.next_to(queue[-1], RIGHT)

            self.play(Write(Text("Dequeue").next_to(queue, DOWN)))

        # Demonstration
        enqueue(3)
        enqueue(8)
        enqueue(1)
        dequeue()
        self.wait()
        enqueue(6)
        dequeue()
        dequeue()  # Dequeue from empty queue
        self.wait()