from manim import *

class SelectionSortAnimation(Scene):
    def construct(self):
        array = [8, 3, 5, 1, 6, 4]
        bars = self.create_bars(array)

        for i in range(len(array) - 1):  # Outer loop for passes
            min_index = i
            for j in range(i + 1, len(array)):  # Finding minimum
                self.highlight_search(bars, j)
                if bars[j].get_height() < bars[min_index].get_height():
                    min_index = j
                self.unhighlight_search(bars, j)

            self.swap_bars(bars, i, min_index)
            self.mark_sorted(bars, i)

        self.wait()  # Pause at the end

    def create_bars(self, array):
        bars = VGroup(*[
            Rectangle(width=0.5, height=value)
            for value in array
        ]).arrange(buff=0.2)
        bars.shift(DOWN)  # Adjust positioning as needed
        return bars

    def highlight_search(self, bars, index):
        bars[index].set_color(YELLOW)
        self.wait(0.2)

    def unhighlight_search(self, bars, index):
        bars[index].set_color(WHITE)  # Or your default bar color
        self.wait(0.1)

    def swap_bars(self, bars, index1, index2):
        self.play(
            bars[index1].animate.set_width(bars[index2].get_width()),
            bars[index2].animate.set_width(bars[index1].get_width()),
            rate_func=linear,
            run_time=0.5
        )
        bars[index1], bars[index2] = bars[index2], bars[index1]  # Swap

    def mark_sorted(self, bars, end_index):
        self.play(
            *[bar.animate.set_color(GREEN) for bar in bars[:end_index + 1]],
            run_time=0.5
        )