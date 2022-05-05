from manim import *

# Visualize linear transformations
class Transform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates = True,
            leave_ghost_vectors = True,
            show_basis_vectors = True
        )

    def construct(self):
        matrix = [[2, 0], [0, 2]]
        matrix_tex = MathTex(r"A = \begin{bmatrix} 2 & 0\\0 & 2 \end{bmatrix}").to_edge(UL).add_background_rectangle()
        self.add_background_mobject(matrix_tex)
        self.apply_matrix(matrix)
        self.wait()