from manim import *


class PlayingCardExample(Scene):
    def construct(self):
        clubs_2 = ImageMobject("cards/clubs_2.png").scale(0.5)

        hearts_3 = ImageMobject("cards/hearts_3.png").scale(0.5).next_to(clubs_2,RIGHT)

        # Add the cards to the scene
        self.add(clubs_2, hearts_3)
