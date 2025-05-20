from manim import *
from manim_utils import get_diceface
import random

class DiceStatisticsScene(Scene):
    def construct(self):
        # Title
        title = Text("Dice Roll Statistics", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Initialize dice
        die1_value = random.randint(1, 6)
        die2_value = random.randint(1, 6)
        
        die1_mobject = get_diceface(die1_value).scale(0.8)
        die2_mobject = get_diceface(die2_value).scale(0.8)
        
        dice_group = VGroup(die1_mobject, die2_mobject).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(die1_mobject), FadeIn(die2_mobject))

        # Sum display
        current_sum = die1_value + die2_value
        sum_text = MathTex(f"Sum = {current_sum}", font_size=40).next_to(dice_group, DOWN, buff=0.5)
        self.play(Write(sum_text))

        # Sum frequencies
        sum_frequencies = {i: 0 for i in range(2, 13)}
        sum_frequencies[current_sum] += 1

        num_rolls = 15 # Number of rolls to animate

        for i in range(num_rolls):
            self.wait(0.5) # Pause before next roll

            # Roll new values
            new_die1_value = random.randint(1, 6)
            new_die2_value = random.randint(1, 6)

            # Create new dice mobjects
            new_die1_mobject = get_diceface(new_die1_value).scale(0.8).move_to(die1_mobject.get_center())
            new_die2_mobject = get_diceface(new_die2_value).scale(0.8).move_to(die2_mobject.get_center())

            # Animate dice roll (simple replacement for now, can add rotation later)
            self.play(
                Rotate(die1_mobject, angle=PI*2, axis=OUT, run_time=0.5),
                Rotate(die2_mobject, angle=PI*2, axis=OUT, run_time=0.5),
            )
            self.play(
                ReplacementTransform(die1_mobject, new_die1_mobject),
                ReplacementTransform(die2_mobject, new_die2_mobject)
            )
            die1_mobject = new_die1_mobject
            die2_mobject = new_die2_mobject
            
            # Update sum
            current_sum = new_die1_value + new_die2_value
            new_sum_text = MathTex(f"Sum = {current_sum}", font_size=40).move_to(sum_text.get_center())
            self.play(ReplacementTransform(sum_text, new_sum_text))
            sum_text = new_sum_text

            sum_frequencies[current_sum] += 1
            
            # Briefly indicate the sum by highlighting the text
            self.play(Indicate(sum_text, color=YELLOW, scale_factor=1.2), run_time=0.3)


        self.wait(1)

        # Hide dice and sum
        self.play(FadeOut(die1_mobject), FadeOut(die2_mobject), FadeOut(sum_text))
        
        # Display Bar Chart of Frequencies
        chart_title = Text("Sum Frequencies After " + str(num_rolls+1) + " Rolls", font_size=36).next_to(title, DOWN, buff=0.5)
        
        # Prepare data for BarChart
        bar_values = [sum_frequencies[s] for s in range(2, 13)]
        bar_names = [str(s) for s in range(2, 13)]
        
        max_freq = 0
        if any(bar_values): # Check if bar_values is not all zeros
            max_freq = max(bar_values)

        y_range_step = 1
        if max_freq > 10:
            y_range_step = 2 # Adjust step if frequencies are high

        bar_chart = BarChart(
            values=bar_values,
            bar_names=bar_names,
            y_range=[0, max_freq + y_range_step, y_range_step], # Ensure y_axis covers all values
            x_length=10,
            y_length=5,
            x_axis_config={"font_size": 24},
            y_axis_config={"font_size": 24},
            bar_colors=[BLUE, GREEN, YELLOW, ORANGE, RED] # Cycle through these colors
        ).next_to(chart_title, DOWN, buff=0.5)

        x_label = bar_chart.get_x_axis_label(
            Text("Sum of Dice", font_size=30), edge=DOWN, direction=DOWN, buff=0.4
        )
        y_label = bar_chart.get_y_axis_label(
            Text("Frequency", font_size=30).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.4
        )

        self.play(Write(chart_title))
        self.play(Create(bar_chart), Write(x_label), Write(y_label))

        self.wait(3)

if __name__ == "__main__":
    # This part is for local execution if needed, but the agent won't use it.
    # config.media_width = "75%"
    # config.verbosity = "INFO"
    # scene = DiceStatisticsScene()
    # scene.render()
    pass
