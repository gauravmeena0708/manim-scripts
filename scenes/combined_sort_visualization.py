from manim import *
from src.manim_utils import create_sortable_bars, animate_bar_swap
import random
import copy

class CombinedSortScene(Scene):
    BUBBLE_SORT_COLOR = BLUE_D
    BUBBLE_SORT_HIGHLIGHT_COMPARE = YELLOW_C
    BUBBLE_SORT_SORTED_COLOR = ORANGE_C

    INSERTION_SORT_COLOR = GREEN_D
    INSERTION_SORT_HIGHLIGHT_KEY = YELLOW_C
    INSERTION_SORT_HIGHLIGHT_COMPARE = RED_C
    INSERTION_SORT_SORTED_COLOR = PURPLE_C

    def construct(self):
        # 0. Configuration
        # unsorted_data = [random.randint(1, 10) for _ in range(8)]
        unsorted_data = [7, 2, 8, 1, 4, 5, 9, 3] # Fixed data for consistent testing
        data_bubble = copy.deepcopy(unsorted_data)
        data_insertion = copy.deepcopy(unsorted_data)

        # 1. Title
        scene_title = Text("Comparing Sorting Algorithms", font_size=40).to_edge(UP)
        self.play(Write(scene_title))
        self.wait(0.5)

        # 2. Create and position bars and labels for Bubble Sort (Left side)
        bubble_title = Text("Bubble Sort", font_size=32).next_to(scene_title, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)
        bars_bubble = create_sortable_bars(data_bubble, initial_color=self.BUBBLE_SORT_COLOR, initial_opacity=0.8)
        bars_bubble.scale(0.75).next_to(bubble_title, DOWN, buff=0.3)
        bubble_status = Text("", font_size=24).next_to(bars_bubble, DOWN, buff=0.3)

        self.play(Write(bubble_title))
        self.play(FadeIn(bars_bubble), Write(bubble_status))
        self.wait(0.5)

        # 3. Create and position bars and labels for Insertion Sort (Right side)
        insertion_title = Text("Insertion Sort", font_size=32).align_to(bubble_title, UP).to_edge(RIGHT, buff=0.7)
        bars_insertion = create_sortable_bars(data_insertion, initial_color=self.INSERTION_SORT_COLOR, initial_opacity=0.8)
        bars_insertion.scale(0.75).next_to(insertion_title, DOWN, buff=0.3)
        insertion_status = Text("", font_size=24).next_to(bars_insertion, DOWN, buff=0.3)
        
        self.play(Write(insertion_title))
        self.play(FadeIn(bars_insertion), Write(insertion_status))
        self.wait(1)

        # 4. Run Bubble Sort Animation
        self.play(bubble_status.animate.set_text("Sorting..."))
        self.bubble_sort_animation(bars_bubble)
        self.play(bubble_status.animate.set_text("Sorted!").set_color(self.BUBBLE_SORT_SORTED_COLOR))
        self.wait(0.5)

        # 5. Run Insertion Sort Animation
        self.play(insertion_status.animate.set_text("Sorting..."))
        self.insertion_sort_animation(bars_insertion)
        self.play(insertion_status.animate.set_text("Sorted!").set_color(self.INSERTION_SORT_SORTED_COLOR))
        self.wait(3)

    def bubble_sort_animation(self, bars):
        n = len(bars)
        for i in range(n - 1):
            swapped_in_pass = False
            for j in range(0, n - i - 1):
                # Highlight bars being compared
                self.play(bars[j].animate.set_fill(self.BUBBLE_SORT_HIGHLIGHT_COMPARE, opacity=1),
                          bars[j+1].animate.set_fill(self.BUBBLE_SORT_HIGHLIGHT_COMPARE, opacity=1), run_time=0.2)
                
                if bars[j].height > bars[j+1].height:
                    animate_bar_swap(self, bars, j, j + 1, run_time=0.4)
                    swapped_in_pass = True
                
                # Unhighlight bars (that are not yet sorted)
                # bars[n-1-i] is the one that will be marked sorted in this pass.
                # So bars[j] and bars[j+1] (if not n-1-i) should revert to BUBBLE_SORT_COLOR
                if (n-1-i) != j : # if bar at j is not the one about to be marked sorted
                     self.play(bars[j].animate.set_fill(self.BUBBLE_SORT_COLOR, opacity=0.8), run_time=0.2)
                if (n-1-i) != (j+1): # if bar at j+1 is not the one about to be marked sorted
                     self.play(bars[j+1].animate.set_fill(self.BUBBLE_SORT_COLOR, opacity=0.8), run_time=0.2)

            # After each pass, the largest element is in its sorted position
            self.play(bars[n-1-i].animate.set_fill(self.BUBBLE_SORT_SORTED_COLOR, opacity=0.8), run_time=0.1)
            
            if not swapped_in_pass: # Optimization: if no swaps in a pass, list is sorted
                for k in range(n-1-i): # Mark remaining as sorted
                     self.play(bars[k].animate.set_fill(self.BUBBLE_SORT_SORTED_COLOR, opacity=0.8), run_time=0.1)
                break 
        
        # Ensure all bars are marked as sorted color in the end
        all_sorted_anims = []
        for bar_idx in range(n):
            if bars[bar_idx].get_fill_color() != self.BUBBLE_SORT_SORTED_COLOR:
                all_sorted_anims.append(bars[bar_idx].animate.set_fill(self.BUBBLE_SORT_SORTED_COLOR, opacity=0.8))
        if all_sorted_anims:
            self.play(*all_sorted_anims, run_time=0.3)


    def insertion_sort_animation(self, bars):
        n = len(bars)
        self.play(bars[0].animate.set_fill(self.INSERTION_SORT_SORTED_COLOR, opacity=0.8), run_time=0.1) # Mark the first element as sorted

        for i in range(1, n):
            # Current element to be inserted is at bars[i]
            self.play(bars[i].animate.set_fill(self.INSERTION_SORT_HIGHLIGHT_KEY, opacity=1), run_time=0.2)
            self.wait(0.1)

            j = i
            while j > 0 and bars[j].height < bars[j-1].height:
                self.play(bars[j-1].animate.set_fill(self.INSERTION_SORT_HIGHLIGHT_COMPARE, opacity=1), run_time=0.2)
                self.wait(0.1)
                
                # Swap current (key element, at bars[j]) with previous (bars[j-1])
                animate_bar_swap(self, bars, j-1, j, run_time=0.4) 
                
                # After swap:
                # bars[j] was bars[j-1] (the compared element from sorted part). Mark it as sorted.
                self.play(bars[j].animate.set_fill(self.INSERTION_SORT_SORTED_COLOR, opacity=0.8), run_time=0.2)
                # bars[j-1] is the key element, now shifted left. Keep it/Re-mark it as KEY_HIGHLIGHT.
                self.play(bars[j-1].animate.set_fill(self.INSERTION_SORT_HIGHLIGHT_KEY, opacity=1), run_time=0.1)
                j -= 1
            
            # Element at bars[j] (which was originally bars[i] or has been moved there) is now in its sorted position.
            self.play(bars[j].animate.set_fill(self.INSERTION_SORT_SORTED_COLOR, opacity=0.8), run_time=0.2)
            self.wait(0.3)
        
        all_sorted_anims = []
        for bar_idx in range(n):
            if bars[bar_idx].get_fill_color() != self.INSERTION_SORT_SORTED_COLOR:
                all_sorted_anims.append(bars[bar_idx].animate.set_fill(self.INSERTION_SORT_SORTED_COLOR, opacity=0.8))
        if all_sorted_anims:
            self.play(*all_sorted_anims, run_time=0.3)


if __name__ == "__main__":
    # To render, save this script and run from terminal:
    # manim -pql combined_sort_visualization.py CombinedSortScene
    pass
