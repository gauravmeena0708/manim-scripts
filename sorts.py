from manim import *
from manim_utils import create_sortable_bars, animate_bar_swap

class InsertionSortScene(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        bars = create_sortable_bars(unsorted_list)
        # Ensure bars have a default color if not set by create_sortable_bars
        for bar in bars:
            if bar.get_fill_opacity() == 0: # Check if color not set
                 bar.set_fill(color=BLUE, opacity=0.75) # Default color
        self.add(bars) # Add bars to the scene


        # Implement insertion sort with animations
        self.insertion_sort(bars)

    def insertion_sort(self, bars):
        for i in range(1, len(bars)):
            j = i
            while j > 0 and bars[j - 1].get_height() > bars[j].get_height():
                animate_bar_swap(self, bars, j, j - 1)
                j -= 1

        # Optional: Indicate the array is sorted

class SelectionSortScene(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        bars = create_sortable_bars(unsorted_list)
        # Ensure bars have a default color if not set by create_sortable_bars
        for bar in bars:
            if bar.get_fill_opacity() == 0: # Check if color not set
                bar.set_fill(color=BLUE, opacity=0.75) # Default color
        self.add(bars) # Add bars to the scene

        # Implement selection sort with animations
        self.selection_sort(bars)

    def selection_sort(self, bars):
        n = len(bars)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if bars[j].get_height() < bars[min_idx].get_height():
                    min_idx = j

            if min_idx != i:
                animate_bar_swap(self, bars, i, min_idx)

        # Optional: Indicate the array is sorted

class SelectionSortScene2(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        bars = create_sortable_bars(unsorted_list, initial_color=BLUE, initial_opacity=0.75)
        self.add(bars) # Add bars to the scene

        # Implement selection sort with animations
        self.selection_sort(bars)

    def selection_sort(self, bars):
        n = len(bars)
        for i in range(n - 1):
            min_idx = i
            bars[i].set_fill(color=RED, opacity=0.75)  # Highlight the current comparison
            for j in range(i + 1, n):
                bars[j].set_fill(color=ORANGE, opacity=0.75)  # Highlight the element being compared
                self.wait(0.5)
                if bars[j].get_height() < bars[min_idx].get_height():
                    min_idx = j

            if min_idx != i:
                animate_bar_swap(self, bars, i, min_idx)

            # Reset the colors
            bars[i].set_fill(color=BLUE, opacity=0.75) # Final color for the sorted bar (now at index i)
            for k in range(i + 1, n): # Reset remaining bars in the unsorted part
                bars[k].set_fill(color=BLUE, opacity=0.75)

        # Optional: Indicate the array is sorted

class BubbleSortBoxes(Scene):
    def construct(self):
        # Define box heights
        box_heights = [2, 6, 7, 3, 5, 9, 1]
        
        # Create boxes
        boxes = VGroup(*[
            Square(side_length=1, fill_color=WHITE, stroke_width=2)
            for _ in range(len(box_heights))
        ])
        
        # Set heights and colors of the boxes based on input
        for box, height in zip(boxes, box_heights):
            box.stretch_to_fit_height(height)
            box.set_fill(color=BLUE, opacity=0.8)
        
        # Arrange boxes in a row
        boxes.arrange(RIGHT, buff=0.2)
        boxes.move_to(ORIGIN)
        
        # Display boxes
        self.play(Create(boxes))
        self.wait()
        
        # Bubble sort algorithm
        n = len(box_heights)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if box_heights[j] > box_heights[j + 1]:
                    # Swap heights
                    box_heights[j], box_heights[j + 1] = box_heights[j + 1], box_heights[j]
                    # Swap positions of boxes
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    # Move boxes to new positions
                    self.play(Swap(boxes[j], boxes[j + 1]))
        
        self.wait()

