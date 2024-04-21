from manim import *

class InsertionSortScene(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        
        bars = self.create_bars(unsorted_list)

        # Implement insertion sort with animations
        self.insertion_sort(bars)

    def create_bars(self, data):
        bars = VGroup(*[
            Rectangle(width=0.5, height=value) for value in data
        ]).arrange(RIGHT, buff=0.3)
        #bars.arrange(DOWN)
        bottom_y = config.frame_y_radius * 1 
        bars.shift(DOWN * bottom_y)  # Shift the bars to the bottom
        return bars

    def insertion_sort(self, bars):
        for i in range(1, len(bars)):
            j = i
            while j > 0 and bars[j - 1].get_height() > bars[j].get_height():
                self.swap_bars(bars, j, j - 1)
                j -= 1

        # Optional: Indicate the array is sorted

    def swap_bars(self, bars, i, j):
        self.play(bars[i].animate.move_to(bars[j].get_center()),
                  bars[j].animate.move_to(bars[i].get_center()),
                  run_time=0.5)

        # Manually swap elements within the VGroup
        temp = bars[i]
        bars[i] = bars[j]
        bars[j] = temp 

class SelectionSortScene(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        bars = self.create_bars(unsorted_list)

        # Implement selection sort with animations
        self.selection_sort(bars)

    def create_bars(self, data):
        bars = VGroup(*[
            Rectangle(width=0.5, height=value) for value in data
        ]).arrange(RIGHT, buff=0.3)
        bottom_y = config.frame_y_radius * 1 
        bars.shift(DOWN * bottom_y)  # Shift the bars to the bottom
        return bars

    def selection_sort(self, bars):
        n = len(bars)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if bars[j].get_height() < bars[min_idx].get_height():
                    min_idx = j

            if min_idx != i:
                self.swap_bars(bars, i, min_idx)

        # Optional: Indicate the array is sorted

    def swap_bars(self, bars, i, j):
        self.play(bars[i].animate.move_to(bars[j].get_center()),
                  bars[j].animate.move_to(bars[i].get_center()),
                  run_time=0.5)

        # Manually swap elements within the VGroup
        temp = bars[i]
        bars[i] = bars[j]
        bars[j] = temp 

class SelectionSortScene2(Scene):
    def construct(self):
        # Data for the sorting visualization
        unsorted_list = [8, 3, 1, 6, 4, 7, 2, 5]  

        # Create visual representations (e.g., rectangles) 
        bars = self.create_bars(unsorted_list)

        # Implement selection sort with animations
        self.selection_sort(bars)

    def create_bars(self, data):
        bars = VGroup(*[
            Rectangle(width=0.5, height=value, fill_color=BLUE, fill_opacity=0.75) for value in data
        ]).arrange(RIGHT, buff=0.3)
        bottom_y = config.frame_y_radius * 1 
        bars.shift(DOWN * bottom_y)  # Shift the bars to the bottom
        return bars

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
                self.swap_bars(bars, i, min_idx)

            # Reset the colors
            for j in range(i + 1, n):
                bars[j].set_fill(color=BLUE, opacity=0.75)
            bars[i].set_fill(color=BLUE, opacity=0.75)

        # Optional: Indicate the array is sorted

    def swap_bars(self, bars, i, j):
        self.play(bars[i].animate.move_to(bars[j].get_center()),
                  bars[j].animate.move_to(bars[i].get_center()),
                  run_time=0.5)

        # Manually swap elements within the VGroup
        temp = bars[i]
        bars[i] = bars[j]
        bars[j] = temp 