from manim import *
import random
from src.manim_utils import get_diceface

class Dice(Scene):
    def construct(self):
        face_size = 0.9  # Adjust based on your preference
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE, stroke_width=0.2)

        # Define the positions for the labels
        top_label_pos = cube.get_top() + UP * 0.5
        bottom_label_pos = cube.get_bottom() + DOWN * 0.5
        right_label_pos = cube.get_right() + RIGHT * 0.5
        left_label_pos = cube.get_left() + LEFT * 0.5
        front_label_pos = cube.get_center() + OUT * 1.5
        back_label_pos = cube.get_center() + IN * 1.5

        # Create text labels for each face
        face_labels = VGroup(
            Tex("1").move_to(top_label_pos),
            Tex("2").move_to(bottom_label_pos),
            Tex("3").move_to(right_label_pos),
            Tex("4").move_to(left_label_pos),
            Tex("5").move_to(front_label_pos),
            Tex("6").move_to(back_label_pos)
        )

        # Group all faces and labels together
        all_faces = VGroup(cube, face_labels)

        # Add all faces to the scene
        self.add(all_faces)
        
        title = Text("Dice Animation", font_size=48).move_to(UP)
        self.add(title)
        self.wait(2)
        # Animate the dice roll with random rotation
        axis = np.random.rand(3)
        self.play(Rotate(all_faces, axis=axis, angle=360 * DEGREES * random.random()))

# The get_diceface function has been moved to manim_utils.py

import random # random is still used by RoundSquareDots, DiceProbability, HundredDice, MatrixScene
# from manim import * # This is already imported at the top

class RoundSquareDots(Scene):
    def construct(self):
        round_square1 = get_diceface(1)
        round_square2 = get_diceface(2).to_edge(RIGHT)
        round_square3 = get_diceface(6).to_edge(LEFT) 
        round_square4 = get_diceface(4).to_edge(UP)
        round_square5 = get_diceface(random.randrange(5, 6)).to_edge(DOWN) # Get another random dice face

        # Add the VGroups to the scene
        self.add(round_square1)
        self.add(round_square2)
        self.add(round_square3)
        self.add(round_square4)
        self.add(round_square5)
        self.play(Rotate(round_square1,PI/3))
        self.play(Rotate(round_square2,PI/3))
        self.play(Rotate(round_square3,PI/3))
        self.play(Rotate(round_square4,PI/3))
        self.play(Rotate(round_square5,PI/3))

class DiceProbability(Scene):
    def construct(self):
        # Create dice with random faces
        dice1 = get_diceface(random.randrange(1, 6))
        dice2 = get_diceface(random.randrange(1, 6))

        probability_text1 = MathTex("P( ")  # Access number from dice VGroup
        probability_text2 = MathTex(") + P( ")
        probability_text3 = MathTex(r") = \frac{1}{3}") 
        probability_group = VGroup(probability_text1, dice1, probability_text2, dice2, probability_text3)
        probability_group.arrange(RIGHT, buff=0.5)

        self.play(Write(probability_group))


import random
from manim import *


class HundredDice(Scene):
    def construct(self):
        dice_grid = VGroup()
        rows, cols = 10, 10
        for i in range(rows):
            for j in range(cols):
                # Create a random dice face
                dice = get_diceface(random.randrange(1, 6))
                # Scale dice to fit in a 10x10 grid
                dice.scale(0.2)
                # Position the dice in a grid layout
                dice.move_to(LEFT * j - LEFT * 1 + UP * i - DOWN * 1)
                dice_grid.add(dice)

        # Fade in all dice faces simultaneously
        self.play(FadeIn(dice_grid))


class MatrixScene(Scene):
    def construct(self):
        # Define parameters
        rows = 10
        cols = 10
        spacing = 0.8 

        # Create objects
        objects = VGroup(*[get_diceface(random.randrange(1, 6)).scale(0.3) for _ in range(rows * cols)])

        # Position objects in a 10x10 grid
        for i, obj in enumerate(objects):
            row = i // cols
            col = i % cols
            obj.move_to(LEFT * 5 + UP * 4.5 + RIGHT * col * spacing + DOWN * row * spacing)

        self.play(Write(objects))