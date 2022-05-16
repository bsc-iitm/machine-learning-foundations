# Projections

!!! question
	Geometrically, what is the relationship between the approximation $X \hat{\theta}$ and the vector $y$?



## Setting

Recall that we are trying to solve the following:
$$
X\theta \approx y
$$
The best approximation is given by the solution to this equation:


$$
(X^TX)\hat{\theta} = X^Ty
$$


$X\hat{\theta}$ is therefore the best approximation for $y$. Now, how are these two vectors related? Specifically, note that both vectors reside in $\mathbb{R}^{m}$. To keep things simple, let us return to our favourite haunt, $\mathbb{R}^2$, with the following configuration:


$$
X = \begin{bmatrix}
2 & 6\\
1 & 3
\end{bmatrix}, y = \begin{bmatrix}
3\\
4
\end{bmatrix}
$$


## Back to Column space

We look for an approximation only when $y$ does not lie in the column space of $X$. So, first, we see what the column space is:


$$
C(X) = \text{span}\left( \left\{ \begin{bmatrix}2\\1\end{bmatrix} \right\} \right)
$$


The second column of $X$ is just three times the first column. The rank of the matrix is $1$. The column space of $X$ is a one-dimensional subspace of $\mathbb{R}^2$ . Geometrically, what does this mean?



![](../assets/images/img_005.svg){width="1000"}



The column space is a line passing through the origin and the point $(2, 1)$. Clearly, the vector $y$ does not lie in the column space of $X$. So, we are justified in looking for an approximation.



## Projections: 2-dimensions

The key idea to remember is that the approximation is going to lie in the column space of $X$. What vector in $C(X)$ is closest to to $y$?  First up, what do we mean by closest? Recall that the distance between the two vectors is our measure of distance. In our 2D case, this is nothing but the distance between the point $y$ and some point on the line $C(X)$. The point on the line which is going to have the shortest distance is the projection of $y$ onto the line! Why is that the case? Among all line segments from a point to a line, the perpendicular to it is the shortest.



![](../assets/images/img_006.svg){width="1000"}





Geometric intuition therefore suggests that $X\hat{\theta} = \begin{bmatrix}4\\2\end{bmatrix}$. 

## Back to Normal Equations

Let us see if algebra agrees with geometry:


$$
\begin{aligned}
(X^TX)\hat{\theta} &= X^Ty\\\\
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




We see that $X^TX$ is singular. But thankfully, the system is still solvable. One such solution is:


$$
\hat{\theta} = \begin{bmatrix}
-1\\
1
\end{bmatrix}
$$


Therefore, the approximation is:


$$
X\hat{\theta} = \begin{bmatrix}
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

The main takeaway from the 2D case is this: the vector closest to $y$ in the column space of $X$ is its projection onto the column space of $X$. This can be extended to any higher dimensional space. First, we note that for a projection, the error vector is orthogonal to the column space of $X$:



![](../assets/images/img_007.svg){width="1000"}



The error vector $e$ is:
$$
e = y - X\hat{\theta}
$$
This is orthogonal to the column space of $X$. This is the same as saying that it is orthogonal to each column of $X$. If we let $X$ be $[x_1, \cdots, x_n]$, where $x_i$ is the $i^{th}$ column of $X$. Then for $1 \leq i \leq n$:


$$
x_i^T e = 0
$$
This can be neatly expressed as:


$$
X^Te=0
$$


So, the error vector is in the nullspace of $X^T$! Replacing $e = y - X\hat{\theta}$, we get:


$$
\begin{aligned}
X^T(y - X\hat{\theta}) &= 0\\
\implies (X^TX)\hat{\theta} = X^Ty
\end{aligned}
$$
The normal equations again! 



## Summary

If the parameters of the linear model obtained by solving the normal equations is $\hat{\theta}$, then the vector $A\hat{\theta}$ is the projection of the vector $y$ onto the column space of $X$.
