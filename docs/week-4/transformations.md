# Linear Transformations

!!! question
	Geometrically, what does a linear transformation do to vectors?



## Algebraic view

Recall that a linear transformation is a linear mapping between two vector spaces $V$ and $W$:
$$
T: V \rightarrow W
$$
In this course, we will be dealing with $\mathbb{R}^n$. So, our transformations will be of the form:
$$
T: \mathbb{R}^n \rightarrow \mathbb{R}^m
$$
To get a better idea about what a linear transformation does, let us restrict our attention to a map from $\mathbb{R}^{2}$ to itself. If $u$ is a vector in $\mathbb{R}^{2}$, then the transformation returns another vector in the same space. We can associated a matrix for every linear transformation. Assuming that we use the standard basis $\beta = \{e_1, e_2\}$ for $\mathbb{R}^2$:


$$
[T]_{\beta}^{\beta} = \begin{bmatrix}
\big\vert & \big\vert\\
T(e_1) & T(e_2)\\
\big\vert & \big\vert
\end{bmatrix}
$$


The basis vectors $e_1$ and $e_2$ are mapped to $T(e_1)$ and $T(e_2)$ respectively. The action of the linear transformation on the basis vectors gives us complete information on what happens to any vector in $\mathbb{R}^{2}$.



## Geometric view

 Geometrically, what does all this mean? Let us begin with a simple example:



$$
T = \begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
$$



This is the identity transformation. It doesn't disturb the vectors and leaves them as they are. This is not all that interesting. Next:



$$
T = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}
$$



Let us see what this does to the basis vectors[^1]:



![type:video](../assets/videos/mat_1.mp4)



Notice the effect it has. Each vector is scaled. In this case, it is stretched. It becomes twice as long as the input. To see why this is true algebraically, consider an arbitrary vector $x = \begin{bmatrix}x_1 & x_2\end{bmatrix}^T$:


$$
Tx = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix} \begin{bmatrix}
x_1\\
x_2
\end{bmatrix} = 2 \begin{bmatrix}
x_1\\
x_2
\end{bmatrix} = 2x
$$


Let us now consider another matrix:


$$
T = \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$


![type:video](../assets/videos/mat_2.mp4)



This is a rotation matrix. That is, it rotates the input vector without changing its magnitude. Moving on, let us take up another matrix. This time, let us compose the two linear transformations that we have seen. Composition of linear transformations is equivalent to matrix multiplication:




$$
T = \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix} \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix} = \begin{bmatrix}
0 & -2\\
2 & 0
\end{bmatrix}
$$


What do you expect this matrix to do?



![type:video](../assets/videos/mat_3.mp4)



It stretches the vectors and rotates them by $90^{\circ}$. Note that the two matrices involved in the product are commutative. That is, $T_1 T_2 = T_2 T_1$. Intuitively, we can see why this is true. We could either stretch a vector and then rotate it (OR) we could rotate it and then stretch it. Let us now move to a more complex linear transformation:




$$
T = \begin{bmatrix}
2 & 1\\
1 & 2
\end{bmatrix}
$$




![type:video](../assets/videos/mat_4.mp4)



Now that we have a good idea of what linear transformations do, we are ready to explore the idea of eigenvalues and eigenvectors.

[^1]: The library [Manim Community](https://www.manim.community/) was used to render these animations. The code for this can be found in the GitHub repository.
