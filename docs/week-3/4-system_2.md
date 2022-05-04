# Xθ = y

!!! question
    How do we solve for $\theta$ in the equation $X\theta = y$?



## Column space

Now we come to the general form of the equation, $X\theta = y$. First, we need to know if the equation admits any solution at all. For this, we have to take a closer look at this equation and see what it means:





$$
\begin{bmatrix}
\big\vert & \big\vert & \big\vert\\
x_1 & \cdots & x_n\\
\big\vert & \big\vert & \big\vert
\end{bmatrix} \begin{bmatrix}
\theta_1\\
\vdots\\
\theta_n
\end{bmatrix} = \begin{bmatrix}
y_1\\
\vdots\\
y_m
\end{bmatrix}
$$



Here, $x_1, \cdots, x_n$ are the columns of $X$. Recall that the product of a matrix and a vector can be interpreted as a linear combination of the columns of the matrix:

$$
\theta_1 x_1 + \cdots + \theta_n x_n = y
$$

$X \theta = y$ has a solution if and only if $y$ can be expressed as a linear combination of the columns of $X$. Since the set of all linear combination of $X$ is given by the $\text{span}(\{x_1, \cdots, x_n\})$, the equation is solvable if and only if $y \in \text{span}(\{x_1, \cdots, x_n\})$. The span of the columns of $X$ is a subspace and is called the column space of the matrix $X$. Thus, $C(X)=\text{span}(\{x_1, \cdots, x_n\})$. We have now answered the question of when $X\theta = y$ is solvable.

!!! note
    The dimension of the column space is called the rank. You must be aware of the rank-nullity theorem:
$$
            \text{rank} + \text{nullity} = n
$$


## Conditions for Solution

Let us reuse the example from the previous unit:


$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
2 & 1 & 0 & 1\\
3 & 1 & -1 & 1
\end{bmatrix} \begin{bmatrix}
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4
\end{bmatrix} = \begin{bmatrix}
y_1\\
y_2\\
y_3
\end{bmatrix}
$$



We are back to the row-echelon form, but with the augmented matrix:




$$
\begin{bmatrix}
1 & 0 & -1 & 0 & \big\vert &  y_1\\
2 & 1 & 0 & 1 & \big\vert & y_2 \\
3 & 1 & -1 & 1 & \big\vert & y_3
\end{bmatrix}
$$




If we apply the same sequence of row operations as in the previous case, we get:


$$
\begin{bmatrix}
1 & 0 & -1 & 0 & \vert &  y_1\\
0 & 1 & 2 & 1 & \vert & y_2 - 2y_1 \\
0 & 0 & 0 & 0 & \vert & y_3 - y_1 - y_2
\end{bmatrix}
$$


We can immediately see that the system has a solution if and only if the following condition is met:


$$
y_3 - y_1 - y_2 = 0
$$



Now that we have the row-echelon matrix, let us rephrase the equation as follows:



$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4
\end{bmatrix} = \begin{bmatrix}
y_1\\
y_2 - 2y_1\\
y_3 - y_1 - y_2
\end{bmatrix}
$$


Let us call this system $P\theta = z$.



!!! note
    $\theta$ is a solution to $X\theta = y$ if and only if $\theta$ is a solution to $P\theta = z$, where $P\ |\ z$ is the augmented matrix after Gaussian elimination.



## General Solution

If a solution exists, how do we find it? And what about all possible solutions? First note that the set of pivot columns are linearly independent and form a basis for the column space of $P$. In the example we are working with, this is quite clear:



$$
C(P) = \text{span}\left( \left\{\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}, \begin{bmatrix}
0\\
1\\
0
\end{bmatrix} \right\} \right)
$$



So, $y$ can be uniquely expressed as a linear combination of the columns of this basis. Let us call this particular solution $\theta_p$. If $\theta_n$ is some vector in the nullspace of $X$, then every general solution $\theta_g$ to the equation can be expressed in this form:
$$
\theta_g = \theta_p + \theta_n
$$
To see why this might be true, just pre-multiply both sides by $X$:



$$
X\theta_g = X(\theta_p + \theta_n) = X\theta_p + X\theta_n = y
$$



This not a complete proof. We have only shown that $\theta_p + \theta_n$ is a solution. It may still not be clear why every solution should be of this form. But we will skip this argument in this course. Coming back to the example we are working with, how do we find the particular solution $\theta_p$? We set all independent variables to zero and solve for the dependent variables:


$$
\theta_p = \begin{bmatrix}
y_1\\
y_2 - 2y_1\\
0\\
0
\end{bmatrix}
$$


We already know how to get $\theta_n$. Refer to the previous unit on computing a basis for the nullspace of the matrix.

## Summary

$X\theta = y$ is solvable if and only if $y$ is an element of the column space of $X$. If this is true, then the general solution to the equation can be expressed as $\theta_p + \theta_n$, where $\theta_p$ is a particular solution and $\theta_n$ is some vector in the nullspace of $X$.
