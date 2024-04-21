from manim import *
import random 

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


