import numpy as np
from manim import *

class MatrixMultiplication(Scene):
    def construct(self):
        # Define matrices
        text_A = Tex("A = ").to_edge(UL) 
        matrix_A = Matrix([[1, 2], [3, 4]]).next_to(text_A, RIGHT) # Use Manim's Matrix class
        text_B = Tex("B").next_to(matrix_A, RIGHT)
        matrix_B = Matrix([[5, 6], [7, 8]]).next_to(text_B, RIGHT)  # Use Manim's Matrix class

        matrix_C = Matrix(np.matmul(matrix_A.get_matrix(), matrix_A.get_matrix()))

        self.play(Write(text_A))
        self.play(FadeIn(matrix_A))
        self.play(Write(text_B))
        self.play(FadeIn(matrix_B))
        self.play(FadeIn(matrix_C))

import numpy as np
from manim import *

class MatrixMultiplication2(Scene):
    def construct(self):
        # Define the original matrix
        matrix_A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
        matrix_B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        # Create the original matrix in Manim
        matrix_A_mn = Matrix(matrix_A).to_edge(UL)
        matrix_B_mn = Matrix(matrix_B).next_to(matrix_A_mn, RIGHT)
        text_eq = Text(" = ").next_to(matrix_B_mn, RIGHT)

        self.play(Write(matrix_A_mn), Write(matrix_B_mn))
        self.play(Write(text_eq))

        # Perform matrix multiplication
        result = np.dot(matrix_A, matrix_B)
        result_mn = Matrix(result).move_to(DOWN)
        #result_mn.move_to(2 * DOWN)

        # Display the result matrix
        self.play(Write(result_mn))
        self.wait()
