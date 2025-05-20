from manim import VGroup, RoundedRectangle, Dot, ORIGIN, LEFT, RIGHT, UP, DOWN, UR, UL, DR, DL, GREEN, Rectangle, config

def get_diceface(num=1):
    dice_face = VGroup()

    # Create the rounded square base
    round_square = RoundedRectangle(corner_radius=0.3, height=2.0, width=2.0)
    dice_face.add(round_square)
    dot1 = Dot(radius=0.15, color=GREEN)
    dot2 = Dot(radius=0.15, color=GREEN)
    dot3 = Dot(radius=0.15, color=GREEN)
    dot4 = Dot(radius=0.15, color=GREEN)
    dot5 = Dot(radius=0.15, color=GREEN)
    dot6 = Dot(radius=0.15, color=GREEN)

    gap_factor = 0.6

    if num == 1:
        round_square.add(dot1.move_to(ORIGIN))
    elif num == 2:
        round_square.add(dot1.move_to(LEFT * gap_factor))
        round_square.add(dot2.move_to(RIGHT * gap_factor))
    elif num == 3:
        round_square.add(dot1.move_to(ORIGIN))
        round_square.add(dot2.move_to(UP * gap_factor))
        round_square.add(dot3.move_to(DOWN * gap_factor))
    elif num == 4:
        round_square.add(dot1.move_to(UR * gap_factor))
        round_square.add(dot2.move_to(UL * gap_factor))
        round_square.add(dot3.move_to(DR * gap_factor))
        round_square.add(dot4.move_to(DL * gap_factor))
    elif num == 5:
        round_square.add(dot1.move_to(ORIGIN))
        round_square.add(dot2.move_to(UP * gap_factor))
        round_square.add(dot3.move_to(DOWN * gap_factor))
        round_square.add(dot4.move_to(LEFT * gap_factor))
        round_square.add(dot5.move_to(RIGHT * gap_factor))
    elif num == 6:
        round_square.add(dot1.move_to(UR * gap_factor))
        round_square.add(dot2.move_to(UL * gap_factor))
        round_square.add(dot3.move_to(LEFT * gap_factor))
        round_square.add(dot4.move_to(RIGHT * gap_factor))
        round_square.add(dot5.move_to(DR * gap_factor))
        round_square.add(dot6.move_to(DL * gap_factor))
    return dice_face

def create_sortable_bars(data, bar_width=0.5, bar_buff=0.3, initial_color=None, initial_opacity=None):
    """
    Creates a VGroup of Rectangles for sorting visualizations.
    """
    bars = VGroup(*[
        Rectangle(width=bar_width, height=value) for value in data
    ]).arrange(RIGHT, buff=bar_buff)
    
    if initial_color:
        for bar in bars:
            bar.set_fill(color=initial_color, opacity=initial_opacity if initial_opacity is not None else 1.0)
            
    # Position bars to be visible, e.g., shift them down
    # This specific positioning might need adjustment depending on the scene's camera.
    # Using a fixed shift for now, similar to the original.
    bars.shift(DOWN * (config.frame_y_radius * 0.5)) # Adjusted to be less aggressive
    return bars

def animate_bar_swap(scene, bars, i, j, run_time=0.5):
    """
    Animates the swapping of two bars in a VGroup and updates the VGroup.
    'scene' is the Manim Scene instance (e.g., self from the calling Scene).
    """
    scene.play(bars[i].animate.move_to(bars[j].get_center()),
               bars[j].animate.move_to(bars[i].get_center()),
               run_time=run_time)

    # Manually swap elements within the VGroup
    bars[i], bars[j] = bars[j], bars[i]
