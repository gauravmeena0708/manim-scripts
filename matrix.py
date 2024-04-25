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
import random

def get_matrix(num = 0):
    base = []
    base.append(np.array([[1, 1, 0], [0, 0, 0], [0, 0, 0]]))
    base.append(np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    base.append(np.array([[1, 1, 0], [1, 0, 0], [0, 0, 0]]))
    base.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))
    base.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    base.append(np.array([[1, 1, 1], [0, 1, 0], [0, 0, 1]]))
    return base[num]

class MatrixMultiplication2(Scene):
    def construct(self):
        matrix_A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
        matrix_A_mn = Matrix(matrix_A).to_edge(UL)
        matrix_1 = get_matrix(0)
        matrix_1_mn = Matrix(matrix_1).to_edge(UL).next_to(matrix_A_mn, RIGHT)
        text_eq = Text(" = ").next_to(matrix_1_mn, RIGHT)
        result_1 = Matrix(np.dot(matrix_A, matrix_1)).next_to(text_eq, RIGHT)

        self.play(FadeIn(matrix_A_mn), FadeIn(matrix_1_mn), FadeIn(text_eq), FadeIn(result_1))
        self.wait(2)

        matrix_2 = get_matrix(2)
        matrix_2_mn = Matrix(matrix_2).to_edge(UL).next_to(matrix_A_mn, RIGHT)
        text_eq = Text(" = ").next_to(matrix_1_mn, RIGHT)
        result_2 = Matrix(np.dot(matrix_A, matrix_2)).next_to(text_eq, RIGHT)

        self.play(Transform(matrix_1_mn, matrix_2_mn), Transform(result_1, result_2))
        self.wait(2)




class MatrixMultiplication3(Scene):
    def construct(self):
        matrix_A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
        matrix_A_mn = Matrix(matrix_A).to_edge(UL)

        # Function to get the position of a specific element in the matrix
        def get_element_position(matrix, row, col):
            element = matrix.get_mob_matrix()[row][col]
            return element.get_center()
        
        def color_row(matrix, row_index, color=RED, opacity=0.5):
            elements = matrix.get_mob_matrix()[row_index]
            for element in elements:
                element.set_fill(color, opacity=opacity)

        def color_column(matrix, col_index, color=GREEN, opacity=0.5):
            elements = [row[col_index] for row in matrix.get_mob_matrix()]
            for element in elements:
                element.set_fill(color, opacity=opacity)

        # Function to draw surrounding box over a row or column of matrix
        def surround_row_or_column(matrix, row=None, column=None, color=YELLOW):
            if row is not None:
                elements = matrix.get_mob_matrix()[row]
            elif column is not None:
                num_rows = len(matrix.get_mob_matrix())
                elements = [matrix.get_mob_matrix()[i][column] for i in range(num_rows)]
            else:
                raise ValueError("Either row or column must be specified.")
            
            rectangle = SurroundingRectangle(VGroup(*elements), color=color, stroke_width=2)
            return rectangle

        row = 1
        col = 2
        element_x, element_y, _ = get_element_position(matrix_A_mn, 1, 2)

        # Create the surrounding rectangle
        rectangle1 = SurroundingRectangle(matrix_A_mn.get_mob_matrix()[row][col], color=YELLOW, stroke_width=2)
        rectangle2 = surround_row_or_column(matrix_A_mn, column=0)
        rectangle3 = surround_row_or_column(matrix_A_mn, row=1)

        matrix_1 = get_matrix(0)
        matrix_1_mn = Matrix(matrix_1).to_edge(UL).next_to(matrix_A_mn, RIGHT)
        text_eq = Text(" = ").next_to(matrix_1_mn, RIGHT)
        result_1 = Matrix(np.dot(matrix_A, matrix_1)).next_to(text_eq, RIGHT)

        self.play(FadeIn(matrix_A_mn), FadeIn(rectangle1), FadeIn(rectangle2), FadeIn(rectangle3), FadeIn(matrix_1_mn), FadeIn(text_eq), FadeIn(result_1))
        self.wait(2)

class MatrixMultiplication4(Scene):
    def construct(self):
        matrix_A = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
        matrix_A_mn = Matrix(matrix_A).to_edge(UL)

        # Function to get the position of a specific element in the matrix
        def get_element_position(matrix, row, col):
            element = matrix.get_mob_matrix()[row][col]
            return element.get_center()
        
        def color_row(matrix, row_index, color=RED, opacity=0.5):
            elements = matrix.get_mob_matrix()[row_index]
            for element in elements:
                element.set_fill(color, opacity=opacity)

        def color_column(matrix, col_index, color=GREEN, opacity=0.5):
            elements = [row[col_index] for row in matrix.get_mob_matrix()]
            for element in elements:
                element.set_fill(color, opacity=opacity)

        # Function to draw surrounding box over a row or column of matrix
        def surround_row_or_column(matrix, row=None, column=None, color=YELLOW):
            if row is not None:
                elements = matrix.get_mob_matrix()[row]
            elif column is not None:
                num_rows = len(matrix.get_mob_matrix())
                elements = [matrix.get_mob_matrix()[i][column] for i in range(num_rows)]
            else:
                raise ValueError("Either row or column must be specified.")
            
            rectangle = SurroundingRectangle(VGroup(*elements), color=color, stroke_width=2)
            return rectangle


        rectangle1 = surround_row_or_column(matrix_A_mn, column=0)


        matrix_1 = get_matrix(0)
        matrix_1_mn = Matrix(matrix_1).to_edge(UL).next_to(matrix_A_mn, RIGHT)
        rectangle2 = surround_row_or_column(matrix_1_mn, column=0)
        text_eq = Text(" = ").next_to(matrix_1_mn, RIGHT)
        result_1 = Matrix(np.dot(matrix_A, matrix_1)).next_to(text_eq, RIGHT)
        rectangle3 = surround_row_or_column(result_1, column=0)

        self.play(FadeIn(matrix_A_mn), FadeIn(rectangle1), FadeIn(rectangle2), FadeIn(matrix_1_mn), FadeIn(text_eq), FadeIn(result_1),FadeIn(rectangle3))
        self.wait(2)

        matrix_2 = get_matrix(2)
        matrix_2_mn = Matrix(matrix_2).to_edge(UL).next_to(matrix_A_mn, RIGHT)
        result_2 = Matrix(np.dot(matrix_A, matrix_2)).next_to(text_eq, RIGHT)
        rectangle4 = surround_row_or_column(result_2, column=0)

        self.play(Transform(matrix_1_mn, matrix_2_mn), Transform(result_1, result_2), Transform(rectangle3, rectangle4))
        self.wait(2)


        matrix_B = np.array([[1, 2, 1], [3, 8, 1], [0, 4, 1]])
        matrix_B_mn = Matrix(matrix_B).to_edge(DL)
        
        rectangle5 = surround_row_or_column(matrix_B_mn, column=2) 
        matrix_3 = get_matrix(3)
        matrix_3_mn = Matrix(matrix_3).to_edge(UL).next_to(matrix_B_mn, RIGHT)
        rectangle6 = surround_row_or_column(matrix_3_mn, column=2)
        text_eq_1 = Text(" = ").next_to(matrix_3_mn, RIGHT)
        result_3 = Matrix(np.dot(matrix_B, matrix_3)).next_to(text_eq_1, RIGHT)
        rectangle7 = surround_row_or_column(result_3, column=2)

        self.play(FadeIn(matrix_B_mn), FadeIn(rectangle5), FadeIn(rectangle6), FadeIn(matrix_3_mn), FadeIn(text_eq_1), FadeIn(result_3),FadeIn(rectangle7))
        self.wait(2)

        matrix_4 = get_matrix(4)
        matrix_4_mn = Matrix(matrix_4).to_edge(UL).next_to(matrix_B_mn, RIGHT)
        result_4 = Matrix(np.dot(matrix_B, matrix_4)).next_to(text_eq_1, RIGHT)
        rectangle8 = surround_row_or_column(result_4, column=2)

        self.play(Transform(matrix_3_mn, matrix_4_mn), Transform(result_3, result_4), Transform(rectangle7, rectangle8))
        self.wait(2)