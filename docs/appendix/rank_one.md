# Rank-1 matrices

## Outer product

Consider the following matrix product:


$$
\begin{bmatrix}
a\\
b\\
c\\
\end{bmatrix} \begin{bmatrix}
x & y & z
\end{bmatrix} = \begin{bmatrix}
ax & ay & az\\
bx & by & bz\\
cx & cy & cz
\end{bmatrix}
$$


If we notice the matrix on the right, each row is a multiple of the row vector $\begin{bmatrix}x\\ y \\z\end{bmatrix}^T$ and each column is a multiple of the column vector $\begin{bmatrix}a\\b\\c\end{bmatrix}$. From this we can deduce that this matrix has rank $1$. The product of the two vectors on the left is called the **outer product**. We can go the other way and claim that every matrix of unit rank can be expressed as the outer product of two vectors:


$$
\huge \boxed{uv^T}
$$


To see why this is true, start with any $m \times n$ matrix $A$ of unit rank. If the rank is $1$, then every vector in the column space of $A$ is of the form $ku$, where $u = \begin{bmatrix}u_1 & \cdots & u_m\end{bmatrix}^T$ . Then, for each vector in the standard basis, we have scalars $v_1, \cdots, v_n$ such that $Ae_i = v_i u$. Note that $Ae_i$ is nothing but the $i^{th}$ column of the matrix $A$. Therefore, we have:


$$
A = \begin{bmatrix}
u_1\\
\vdots\\
u_m
\end{bmatrix} \begin{bmatrix}
v_1 & \cdots v_n
\end{bmatrix} = uv^T
$$



!!! note
    Every $m \times n$ matrix of unit rank is of the form $uv^T$ where $u \in \mathbb{R}^m$ and $v \in \mathbb{R}^n$.
    

