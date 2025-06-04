from manim import *

class AtomAnimation(Scene):
    def construct(self):
        # Define atom components
        proton = Sphere(radius=0.2, color=RED).shift(ORIGIN)
        electron_path = Circle(radius=0.5)
        electron = Dot(radius=0.05, color=BLUE)

        # Place the proton
        self.play(Create(proton)) 

        # Animate the electron
        self.play(
            Rotate(electron, about_point=ORIGIN, angle=2*PI, rate_func=linear, run_time=3),
            MoveAlongPath(electron, electron_path), 
        )
        self.wait() 
