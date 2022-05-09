# Matrix product

There are several ways to understand the product of two matrices $A$ and $B$ of compatible dimensions. We will look at four different ways to do the same. Specifically, let $A$ be an $m \times n$ matrix and $B$ be a $n \times p$ matrix. Let $C = AB$.



## Row-column picture

$A$ is expressed in terms of $m$ row vectors. $B$ is expressed in terms of $p$ column vectors.



$$
\begin{bmatrix}
\cdots & u_1^T & \cdots\\
 & \vdots & \\
\cdots & u_m^T & \cdots
\end{bmatrix} \begin{bmatrix}
\vdots &  & \vdots\\
v_1 & \cdots & v_p\\
\vdots &  & \vdots
\end{bmatrix}
$$



The $ij^{th}$ element of the matrix $C$ is:



$$
C_{ij} = u_i^Tv_j
$$



This is by far the most popular form of matrix multiplication and is the first thing that we learn in high school. Each element of the matrix is represented as the inner product of two vectors.



## Matrix-column picture

$B$ is expressed as a sequence of $p$ column vectors.



$$
A \begin{bmatrix}
\vdots &  & \vdots\\
v_1 & \cdots & v_p\\
\vdots &  & \vdots
\end{bmatrix}
$$



Each column of $C$ can be represented as $Av_i$, a linear combination of the columns of $A$, where the coefficients of the combination are given by the columns of $B$:



$$
C = \begin{bmatrix}
\vdots &  & \vdots\\
Av_1 & \cdots & Av_p\\
\vdots &  & \vdots
\end{bmatrix}
$$



## Row-matrix picture

$A$ is expressed as a sequence of $m$ row vectors:


$$
\begin{bmatrix}
\cdots & u_1^T & \cdots\\
 & \vdots & \\
\cdots & u_m^T & \cdots
\end{bmatrix} B
$$




Each row of the matrix $C$ is of the form $u_i^TB$, a linear combination of the rows of $B$, where the coefficients of the combination are given by the rows of $A$:


$$
C = \begin{bmatrix}
\cdots & u_1^TB & \cdots\\
& \vdots & \\
\cdots & u_m^TB & \cdots\\
\end{bmatrix}
$$


## Column-row picture

$A$ is expressed in terms of $n$ column vectors. $B$ is expressed in terms of $n$ row vectors.



$$
\begin{bmatrix}
\vdots &  & \vdots\\
u_1 & \cdots & u_n\\
\vdots &  & \vdots\\
\end{bmatrix}
\begin{bmatrix}
\cdots & v_1^T & \cdots\\
 & \vdots & \\
\cdots & v_n^T & \cdots
\end{bmatrix}
$$



Here is another way to multiply two matrices:



$$
C = \sum \limits_{i = 1}^{n} u_i v_i^T
$$



Matrix $C$ is expressed as the sum of $n$ matrices of [unit rank](../appendix/rank_one.md). Alternatively, the matrix is represented as the sum of $n$ outer products. To see why this is true, consider an unit vector $e_k$ in the standard basis for $\mathbb{R}^{p}$. Now, let us look the product of the RHS with $e_k$. This is nothing but the $k^{th}$ column of this matrix:


$$
\sum \limits_{i = 1}^{n} u_i v_i^T e_k = \sum \limits_{i = 1}^{n} (v_i^Te_k) u_i
$$


The RHS of the above expression is a linear combinations of the columns of the matrix $A$. The coefficients of the combination are the columns of the matrix $B$. This is the same as the matrix-column picture.

