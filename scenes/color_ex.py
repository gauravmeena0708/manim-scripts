from manim import *

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1, color=RED, fill_opacity=0.5)
              for j in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time=2)
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t), # rate_func=linear
            Rotate(polys[1], PI, rate_func=smooth),  # default behavior for most animations
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t*PI)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1 - abs(1-2*t)),
            run_time=2
        )
        self.wait()

class ConflictingAnimations(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        self.play(Rotate(s, PI), Rotate(s, -PI), run_time=3)

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=RED, fill_opacity=0.05*j) for j in range(20)])
        squares.arrange_in_grid(4, 5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))

class NewColors(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        xkcd_color_mobjects = VMobject()
        xkcd_colors = [
            color for color_name, color in 
            inspect.getmembers(XKCD, lambda obj: isinstance(obj, ManimColor))
        ]
        
        for color in xkcd_colors:
            col_square = Square()
            col_square.set_fill(color, opacity=1)
            col_square.set_stroke(opacity=0)
            xkcd_color_mobjects.add(col_square)
            
        def color_sort(col):
            h, s, v = col.to_hsv()
            return h, v
            
        xkcd_sorted_ind = sorted(
            range(len(xkcd_colors)),
            key=lambda ind: xkcd_colors[ind].to_hsv()
        )
        
        xkcd_color_mobjects.arrange_in_grid(23, 41)
        xkcd_color_mobjects.width = config.frame_width
        
        for ind, col_square in enumerate(xkcd_color_mobjects):
            col_square.generate_target()
            target_ind = xkcd_sorted_ind.index(ind)
            col_square.target.move_to(xkcd_color_mobjects[target_ind])
        
        
        self.play(FadeIn(xkcd_color_mobjects, lag_ratio=0.001, run_time=5))
        self.wait()
        
        move_squares = AnimationGroup(*[
                MoveToTarget(col_square)
                for col_square in xkcd_color_mobjects
            ],
            lag_ratio=0.001,
            run_time=5,
        )
        self.play(move_squares)
        self.wait(1)
        
        self.play(FadeOut(xkcd_color_mobjects, lag_ratio=0.001, run_time=5))
