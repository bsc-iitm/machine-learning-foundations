from manim import *

# Visualize eigenvectors
class EigTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates = True,
            leave_ghost_vectors = True,
            show_basis_vectors = True
        )

    def construct(self):
        matrix = [[3, 1], [0, 2]]
        line = DashedLine([-5, -5, 0], [5, 5, 0])
        vect = Vector([1, 1], color = PURPLE_B)
        self.add_background_mobject(line)
        self.moving_vectors.append(vect)
        self.apply_matrix(matrix)
        self.wait()