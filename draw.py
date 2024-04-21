from manim import *

class plotSmooth(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.play(Create(ax, run_time=2), Create(curve, run_time=5))
        self.play(FadeIn(area))
        self.wait(2)

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))

class ComplexExp(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(-0.1, 4.25), y_range=(-1.5, 1.5), z_range=(-1.5, 1.5), y_length=5, z_length=5)
        curve = ParametricFunction(
            lambda p: axes.coords_to_point(p, np.exp(complex(0, PI*p)).real, np.exp(complex(0, PI*p)).imag),
            t_range=(0, 2, 0.1)
        )
        curve_extension = ParametricFunction(
            lambda p: axes.coords_to_point(p, np.exp(complex(0, PI*p)).real, np.exp(complex(0, PI*p)).imag),
            t_range=(2, 4, 0.1)
        )
        t = MathTex("z = e^{t \pi i}, \quad t\in [0, 2]")
        t.rotate(axis=OUT, angle=90*DEGREES).rotate(axis=UP, angle=90*DEGREES)
        t.next_to(curve, UP + OUT)
        self.set_camera_orientation(phi=90*DEGREES, theta=0, focal_distance=10000)
        self.add(axes)
        self.play(Create(curve, run_time=2), Write(t))
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        four = MathTex("4").rotate(axis=OUT, angle=90*DEGREES).rotate(axis=UP, angle=90*DEGREES)
        four.move_to(t[0][12])
        self.play(Create(curve_extension, run_time=2), t[0][12].animate.become(four))
        self.wait()
        self.move_camera(phi=90*DEGREES, theta=-90*DEGREES, focal_distance=10000)
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        self.move_camera(phi=0, theta=-90*DEGREES, focal_distance=10000)
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        self.play(FadeOut(axes, curve, curve_extension, t, shift=IN))
        self.wait()

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next_to from episode 1
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)  # RIGHT == [1, 0, 0]
        self.add(red_dot, green_dot)

        # shift
        s = Square(color=ORANGE)
        s.shift(2*UP + 4*RIGHT)
        self.add(s)

        # move_to
        c = Circle(color=PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c)

        # align_to
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2, c3, c4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1,0,0], aligned_edge=LEFT)
        self.add(s)

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5, 51, 5):
            self.add(Circle(radius=perc * Percent(X_AXIS)))
            self.add(Square(side_length=2*perc*Percent(Y_AXIS), color=YELLOW))

        d = Dot()
        d.shift(100 * Pixels * RIGHT)
        self.add(d)

class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP, buff=0.5)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.2)
        self.add(stars)

class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s, c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s, c).animate.arrange(RIGHT))
        self.play(c.animate(rate_func=linear).shift(RIGHT).scale(2))
        self.wait()

class AnimateProblem(Scene):
    def construct(self):
        left_square = Square()
        right_square = Square()
        VGroup(left_square, right_square).arrange(RIGHT, buff=1)
        self.add(left_square, right_square)
        self.play(left_square.animate.rotate(PI), Rotate(right_square, PI), run_time=2)

class AnimationMechanisms(Scene):
    def construct(self):
        c = Circle()
        
        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)
        
        self.add(c)
        self.wait()
        self.play(MoveToTarget(c))
        
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

        self.wait()

class SimpleCustomAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 4 * t
            angle = 2*t * 2*PI
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(Color(hue=t, saturation=1, luminance=0.5))
            mobject.set_opacity(1-t)
        
        d = Dot(color=YELLOW)
        self.add(d)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))

class Disperse(Animation):
    def __init__(self, mobject, dot_radius=0.05, dot_number=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_number = dot_number
    
    def begin(self):
        dots = VGroup(
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_number)]
        )
        for dot in dots:
            dot.initial_position = dot.get_center()
            dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())
        dots.set_opacity(0)
        self.mobject.add(dots)
        self.dots = dots
        super().begin()
        
    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.dots)

    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)  # manually apply rate function
        if alpha <= 0.5:
            self.mobject.set_opacity(1 - 2*alpha, family=False)
            self.dots.set_opacity(2*alpha)
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1 - alpha))
            for dot in self.dots:
                dot.move_to(dot.initial_position + 2*(alpha-0.5)*dot.shift_vector)
            
            

class CustomAnimationExample(Scene):
    def construct(self):
        st = Star(color=YELLOW, fill_opacity=1).scale(3)
        self.add(st)
        self.wait()
        self.play(Disperse(st, dot_number=200, run_time=4))

class MovingLabel(Scene):
    def construct(self):
        blue_dot = Dot(color=BLUE)
        dot_label = Text("Hello dot!").next_to(blue_dot, UP)
        dot_label.add_updater(
            lambda mobject: mobject.next_to(blue_dot, UP)
        )
        self.add(blue_dot, dot_label)
        self.play(blue_dot.animate.shift(RIGHT))
        self.play(blue_dot.animate.scale(10))
        self.play(blue_dot.animate.move_to([-2, -2, 0]))

class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater( # place arrow left of dot
            lambda mob: mob.next_to(red_dot, LEFT)
        )
        
        def shifter(mob, dt): # make dot move 2 units RIGHT/sec
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)
        
        def scene_scaler(dt): # scale mobjects depending on distance to origin
            for mob in self.mobjects:
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)
        
        self.add(red_dot, pointer)
        # scene has to update initially to fix first frame:
        # first mobject updaters are called, then scene updaters
        self.update_self(0)
        self.wait(5)

class UpdaterAndAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(lambda mob, dt: mob.rotate(dt*PI))
        
        def shifter(mob, dt): # make dot move 2 units RIGHT/sec
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)
        
        self.add(red_dot, rotating_square)
        self.wait(1)
        red_dot.suspend_updating()
        self.wait(1)
        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2, -2, 0])
        )
        self.wait(1)

class ValueTrackerMove(Scene):
    def construct(self):
        line = NumberLine(x_range=[-5, 5])
        position = ValueTracker(0)
        pointer = Vector(DOWN)
        pointer.add_updater(
            lambda mob: mob.next_to(
                line.number_to_point(position.get_value()), UP
            )
        )
        pointer.update()
        self.add(line, pointer)
        self.wait()
        self.play(position.animate.set_value(4))
        self.play(position.animate.set_value(-2))

class ValueTrackerPlot(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        parabola = ax.plot(lambda x: a.get_value() * x**2, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color=RED))
        )
        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))