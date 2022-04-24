# System of Equations-(2)

!!! question
    How do we solve for $x$ in the equation $Ax = b$?



## Column space

Now we come to the general form of the equation, $Ax = b$. First, we need to know if the equation admits any solution at all. For this, we have to take a closer look at this equation and see what it means:


$$
\begin{bmatrix}
\vdots & \vdots & \vdots\\
a_1 & \cdots & a_n\\
\vdots & \vdots & \vdots
\end{bmatrix} \begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix} = \begin{bmatrix}
b_1\\
\vdots\\
b_m
\end{bmatrix}
$$


Here, $a_1, \cdots, a_n$ are the columns of $A$. Recall that the product of a matrix and a vector can be interpreted as a linear combination of the columns of the matrix:


$$
x_1 a_1 + \cdots x_na_n=b
$$

$Ax = b$ has a solution if and only if $b$ can be expressed as a linear combination of the columns of $A$. Since the set of all linear combination of $A$ is given by the $\text{span}(\{a_1, \cdots, a_n\})$, the equation is solvable if and only if $b \in \text{span}(\{a_1, \cdots, a_n\})$. The span of the columns of $A$ is a subspace and is called the column space of the matrix $A$. Thus, $C(A)=\text{span}(\{a_1, \cdots, a_n\})$. We have now answered the question of when $Ax = b$ is solvable. 

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
x_1\\
x_2\\
x_3\\
x_4
\end{bmatrix} = \begin{bmatrix}
b_1\\
b_2\\
b_3
\end{bmatrix}
$$



We are back to the row-echelon form, but with the augmented matrix:




$$
\begin{bmatrix}
1 & 0 & -1 & 0 & \vert &  b_1\\
2 & 1 & 0 & 1 & \vert & b_2 \\
3 & 1 & -1 & 1 & \vert & b_3
\end{bmatrix}
$$




If we apply the same sequence of row operations as in the previous case, we get:


$$
\begin{bmatrix}
1 & 0 & -1 & 0 & \vert &  b_1\\
0 & 1 & 2 & 1 & \vert & b_2 - 2b_1 \\
0 & 0 & 0 & 0 & \vert & b_3 - b_1 - b_2
\end{bmatrix}
$$


We can immediately see that the system has a solution if and only if the following condition is met:


$$
b_3 - b_1 - b_2 = 0
$$



Now that we have the row-echelon matrix, let us rephrase the equation as follows:



$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 0 & 0 & 0
\end{bmatrix} \begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{bmatrix} = \begin{bmatrix}
b_1\\
b_2 - 2b_1\\
b_3 - b_1 - b_2
\end{bmatrix}
$$


Let us call this system $Bx = c$.



!!! note
    $x$ is a solution to $Ax = b$ if and only if $x$ is a solution to $Bx = c$



## General Solution

If a solution exists, how do we find it? And what about all possible solutions? First note that the set of pivot columns are linearly independent and form a basis for the column space of $B$. In the example we are working with, this is quite clear:



$$
C(B) = \text{span}\left( \left\{\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}, \begin{bmatrix}
0\\
1\\
0
\end{bmatrix} \right\} \right)
$$



So, $b$ can be uniquely expressed as a linear combination of the columns of this basis. Let us call this particular solution $x_p$. If $x_n$ is some vector in the nullspace of $A$, then every general solution $x_g$ to the equation can be expressed in this form:
$$
x_g = x_p + x_n
$$
To see why this might be true, just pre-multiply both sides by $A$:



$$
Ax_g = A(x_p + x_n) = Ax_p + Ax_n = b
$$



This not a complete proof. We have only shown that $x_p + x_n$ is a solution. It may still not be clear why every solution should be of this form. But we will skip this argument in this course. Coming back to the example we are working with, how do we find the particular solution $x_p$? We set all independent variables to zero and solve for the dependent variables:


$$
x_p = \begin{bmatrix}
b_1\\
b_2 - 2b_1\\
0\\
0
\end{bmatrix}
$$


We already know how to get $x_n$. Refer to the previous unit on computing a basis for the nullspace of the matrix.

## Summary

$Ax = b$ is solvable if and only if $b$ is an element of the column space of $A$. If this is true, then the general solution to the equation can be expressed as $x_p + x_n$, where $x_p$ is a particular solution and $x_n$ is some vector in the nullspace of $A$.
