from manim import *

class Transform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates = True,
            leave_ghost_vectors = True,
        )

    def construct(self):
        matrix = [[0, -2], [2, 0]]
        self.apply_matrix(matrix)
        self.wait()