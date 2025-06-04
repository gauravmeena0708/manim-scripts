from manim import *
import numpy as np

class expandPart(Scene):
  def construct(self):
    # Expressions
    term1 = MathTex(r"x^2")
    term2 = MathTex(r"- x")
    term3 = MathTex(r"+ 1")  # Initial term
    exp1 = VGroup(term1, term2, term3).arrange(RIGHT, buff=0.3)
    exp1.to_edge(LEFT)


    exp1_copy = exp1.copy()
    exp1_copy.to_corner(UL)
    self.play(Write(exp1_copy))

    # Animation
    self.play(Write(exp1))
    self.wait(1)  # Wait for 1 second
    term4 = MathTex(r"+\frac{1}{4} + \frac{3}{4}")
    term4.next_to(exp1[1],RIGHT)
    self.play(Transform(exp1[2], term4))
    self.wait(1)


class Plot(Scene):
    def construct(self):
        plot = VGroup()
        ax = Axes(
            x_range=[0, np.pi + 0.1, 1],
            y_range=[0, 1.1, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            x_length=7,
            y_length=5,
        ).add_coordinates()
        
        plot.add(ax)

        x = np.array([0., 0.16534698, 0.33069396, 0.49604095, 0.66138793,
                       0.82673491, 0.99208189, 1.15742887, 1.32277585, 1.48812284,
                       1.65346982, 1.8188168, 1.98416378, 2.14951076, 2.31485774,
                       2.48020473, 2.64555171, 2.81089869, 2.97624567, 3.14159265])

        y = np.array([0.01313289,  0.9531357,  0.27303831,  0.56426336,  0.69446266,
                         0.79658221,  0.72262249,  1.0565153,  0.90835232,  1.01992807,
                         1.11962864,  0.85117504,  1.01662771,  0.91446878,  0.67722208,
                         0.6222458,  0.511015,  0.39366855,  0.18442382, 0.03879388])

        plr = np.poly1d(np.polyfit(x, y, 50))

        graph = ax.plot(plr, x_range=[0, np.pi, 0.165346982],
                           use_smoothing=False, color=ORANGE)

        self.play(FadeIn(ax))
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.play(graph.animate.set_opacity(0.3))
        self.wait(5)

from manim import *  # manimCE v1.16
import numpy as np
import math as math

class  MaclaurinSine(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(0.6)
        
        def nth_series (n,x):
            terms = [(((-1) ** m) * (x ** (2 * m + 1)) / (math.factorial(2 * m + 1))) for m in range(n)]
            return sum(terms)
        
        coords = NumberPlane()
        transformations = []
        
        previous_graph = coords.plot_parametric_curve(
            lambda t:np.array([t, nth_series(0, t)]), t_range=[-17,17]
            )
        for i in range(1,20):
            new_graph = coords.plot_parametric_curve(
                lambda t:np.array([t, nth_series(i, t)]), t_range=[-17,17]
                )
            # just replacing ReplacementTransform with Transform
            trans = Transform(previous_graph, new_graph, run_time=0.4, rate_func=rate_functions.smooth)
            transformations.append(trans)
            
        self.wait(0.4)
        self.play(Succession(*transformations,lag_ratio=1), self.camera.frame.animate.scale(3))
        self.wait(1.5)

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()



class MatchingEquationParts(Scene):
    def construct(self):


        eq1 = MathTex("x^2", "-", "x", "+", "1")
        eq2 = MathTex("x^2", "-", r"2 \cdot \frac {1}{2} \cdot x", "+", "1")
        eq3 = MathTex("x^2", "-", r"2 \cdot \frac {1}{2} \cdot x", "+", r"\frac {1}{4}", "+", r"\frac {3}{4}")
        eq4 = MathTex(r"\left( x^2 - 2 \cdot \frac{1}{2} \cdot x + \frac{1}{4} \right) + \frac{3}{4}")
        eq3.next_to(eq2, DOWN)
        self.add(eq1)
        self.wait(2)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(2)

from manim import *

class solvingEquation(Scene):
    def construct(self):
        # Expressions
        from itertools import cycle
        colors = cycle([RED, TEAL, ORANGE, PINK])
        grp = VGroup(*[
            Text(n, color=next(colors))
            .scale(0.2)
            for n in "Enstoic"
        ])
        grp.arrange(RIGHT, buff=0.05, aligned_edge=DOWN).to_corner(UR)

        self.add(grp)

        exp1 = MathTex(r"x^2 - x + 1").to_corner(UL)
        exp2 = MathTex(r"\Downarrow").next_to(exp1, DOWN, buff=0.2)  # Adjusted position and buff
        exp3 = MathTex(r"x^2 - x + \frac{1}{4} + \frac{3}{4}").next_to(exp2, DOWN, buff=0.2, aligned_edge=LEFT)  # Adjusted position and buff
        exp4 = MathTex(r"\Rightarrow\left(x^2 - x + \frac{1}{4}\right) + \frac{3}{4}").next_to(exp3, DOWN, buff=0.2, aligned_edge=LEFT)  # Adjusted position and buff
        exp5 = MathTex(r"\Rightarrow\left(x - \frac{1}{2}\right)^2 + \left(\frac{\sqrt(3)}{2}\right)^2").next_to(exp4, DOWN, buff=0.2, aligned_edge=LEFT)  # Adjusted position and buff

        self.play(Write(exp1))
        self.wait(1)

        self.play(Write(exp2))
        self.wait(1)

        self.play(Write(exp3))
        self.wait(1)

        self.play(Write(exp4))
        self.wait(1)

        self.play(Write(exp5))
        self.wait(1)


