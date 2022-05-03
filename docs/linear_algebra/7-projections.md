# Projections

!!! question
	Geometrically, what is the relationship between the approximation $A \hat{x}$ and the vector $b$?



## Setting

Recall that we are trying to solve the following:
$$
Ax \approx b
$$
The best approximation is given by the solution to this equation:


$$
(A^TA)\hat{x} = A^Tb
$$


$A\hat{x}$ is therefore the best approximation for $b$. Now, how are these two vectors related? Specifically, note that both vectors reside in $\mathbb{R}^{m}$. To keep things simple, let us return to our favourite haunt, $\mathbb{R}^2$, with the following configuration:


$$
A = \begin{bmatrix}
2 & 6\\
1 & 3
\end{bmatrix}, b = \begin{bmatrix}
3\\
4
\end{bmatrix}
$$


## Back to Column space

We look for an approximation only when $b$ does not lie in the column space of $A$. So, first, we see what the column space is:


$$
C(A) = \text{span}\left( \left\{ \begin{bmatrix}2\\1\end{bmatrix} \right\} \right)
$$


The second column of $A$ is just three times the first column. The rank of the matrix is $1$. The column space of $A$ is a one-dimensional subspace of $\mathbb{R}^2$ . Geometrically, what does this mean?



![](../assets/images/img_005.svg){width="1000"}



The column space is a line passing through the origin and the point $(2, 1)$. Clearly, the vector $b$ does not lie in the column space of $A$. So, we are justified in looking for an approximation.



## Projections: 2-dimensions

The key idea to remember is that the approximation is going to lie in the column space of $A$. What vector in $C(A)$ is closest to to $b$?  First up, what do we mean by closest? Recall that the distance between the two vectors is our measure of distance. In our 2D case, this is nothing but the distance between the point $b$ and some point on the line $C(A)$. The point on the line which is going to have the shortest distance is the projection of $b$ onto the line! Why is that the case? Among all line segments from a point to a line, the perpendicular to it is the shortest.



![](../assets/images/img_006.svg){width="1000"}





Geometric intuition therefore suggests that $A\hat{x} = \begin{bmatrix}4\\2\end{bmatrix}$. 

## Back to Normal Equations

Let us see if algebra agrees with geometry:


$$
\begin{aligned}
(A^TA)\hat{x} &= A^Tb\\\\
\begin{bmatrix}
2 & 1\\
6 & 3
\end{bmatrix} \begin{bmatrix}
2 & 6\\
1 & 3
\end{bmatrix} \begin{bmatrix}
\hat{x}_1\\
\hat{x}_2
\end{bmatrix} &= \begin{bmatrix}
2 & 1\\
6 & 3
\end{bmatrix}\begin{bmatrix}
3\\
4
\end{bmatrix}\\\\
\begin{bmatrix}
5 & 15\\
15 & 45
\end{bmatrix} \begin{bmatrix}
\hat{x}_1\\
\hat{x}_2
\end{bmatrix} &= \begin{bmatrix}
10\\
30
\end{bmatrix}\\\\
\begin{bmatrix}
1 & 3\\
1 & 3
\end{bmatrix} \begin{bmatrix}
\hat{x}_1\\
\hat{x}_2
\end{bmatrix} &= \begin{bmatrix}
2\\
2
\end{bmatrix}\\
\end{aligned}
$$




We see that $A^TA$ is singular. But thankfully, the system is solvable. One such solution is:


$$
\hat{x} = \begin{bmatrix}
-1\\
1
\end{bmatrix}
$$


Therefore, the approximation is:


$$
A\hat{x} = \begin{bmatrix}
2 & 6\\
1 & 3
\end{bmatrix} \begin{bmatrix}
-1\\
1
\end{bmatrix} = \begin{bmatrix}
4\\
2
\end{bmatrix}
$$


Algebra does agree with geometry!



## Projections: m-dimensions

The main takeaway from the 2D case is this: the vector closest to $b$ in the column space of $A$ is its projection onto the column space of $A$. This can be extended to any higher dimensional space. First, we note that for a projection, the error vector is orthogonal to the column space of $A$:



![](../assets/images/img_007.svg){width="1000"}



The error vector $e$ is:
$$
e = b - A\hat{x}
$$
This is orthogonal to the column space of $A$. This is the same as saying that it is orthogonal to each column of $A$. If we let $A$ be $[a_1, \cdots, a_n]$, where $a_i$ is the $i^{th}$ column of $A$. Then for $1 \leq i \leq n$:


$$
a_i^T e = 0
$$
This can be neatly expressed as:


$$
A^Te=0
$$


So, the error vector is in the nullspace of $A^T$! Replacing $e = b - A\hat{x}$, we get:


$$
\begin{aligned}
A^T(b - A\hat{x}) &= 0\\
\implies (A^TA)\hat{x} = A^Tb
\end{aligned}
$$
The normal equations again! 



## Summary

If the parameters of the linear model obtained by solving the normal equations is $\hat{x}$, then the vector $A\hat{x}$ is the projection of the vector $b$ onto the column space of $A$.
