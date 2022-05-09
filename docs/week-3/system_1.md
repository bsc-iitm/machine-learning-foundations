# Xθ = 0

!!! question
    How do we solve for $\theta$ in the equation $X\theta = 0$?



## Setting

Before we tackle the general problem of $X\theta = y$, let us first see if we can solve the system when $y$ is the zero vector. In all the discussions that follow, this will be our setting:

- $X$ is a data-matrix of dimensions $m \times n$
- $y$ is a column-vector of size $m$
- $\theta \in \mathbb{R}^n$
- $X\theta \in \mathbb{R}^{m}$

The equation that we have taken up is:
$$
X\theta = 0
$$
!!! note
    We have to be careful with the use of $0$. Depending on the context, it could either mean a scalar or a vector.



## Nullspace

We can immediately see that $\theta = 0$ is a solution. However, this is a trivial solution and is not particularly interesting. We would like to search for non-trivial solutions. Let us begin optimistically by assuming that at least one such solution exists, say $\theta_1$. Then, we can see that $k \theta_1$ is also a solution. This is because $X (k\theta_1) = k \cdot X\theta_1 = 0$. Also, if $\theta_1$ and $\theta_2$ are two solutions to the equation, then $\theta_1 + \theta_2$ is also a solution, as $X(\theta_1 + \theta_2) = X\theta_1 + X\theta_2 = 0$. From these two observations, we see that the set of all solutions to the equation $X \theta = 0$ is a subspace of $\mathbb{R}^{n}$. We denote this by $N(X)$ and call it the nullspace of $X$. The dimension of the nullspace is called nullity.

All this is fine, but how does it help us find all the solutions? If we can find a basis for the nullspace, that will help us characterize all the solutions. If $B = \{v_1, \cdots, v_k\}$ is a basis for the nullspace, then the set of all solutions to the equation is given by $N(X) = \text{span}(B)$.



## Row-Echelon form

Let us take up an example and work with that:


$$
X = \begin{bmatrix}
1 & 0 & -1 & 0\\
2 & 1 & 0 & 1\\
3 & 1 & -1 & 1
\end{bmatrix}
$$


Recall that we can apply a sequence of any of these three row operations on a matrix:

- swap two rows
- scale a row by a non-zero constant
- add a scalar multiple of a row to another row



**Step-1**


$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
2 & 1 & 0 & 1\\
3 & 1 & -1 & 1
\end{bmatrix} \underrightarrow{R_2 \rightarrow R_2-2R_1} 
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
3 & 1 & -1 & 1
\end{bmatrix}
$$


**Step-2**


$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
3 & 1 & -1 & 1
\end{bmatrix} \underrightarrow{R_3 \rightarrow R_3-3R_1} 
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 1 & 2 & 1
\end{bmatrix}
$$


**Step-3**


$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 1 & 2 & 1
\end{bmatrix} \underrightarrow{R_3 \rightarrow R_3 - R_2} 
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 0 & 0 & 0
\end{bmatrix}
$$


The final matrix that we have is in row-echelon form. Here is a quick reminder of what the row-echelon matrix is:

- All rows that have only zeros are at the bottom.
- The first nonzero entry in a row is always to the right of the first nonzero entry in the row above it.

The first nonzero entry in a row is called a pivot. Let us call the row-echelon matrix of $X$ as $P$. We state the following result without a proof.

!!! note "Useful result"
	If $P$ is the row-echelon form of $X$, then $X\theta = 0$ if and only if $P\theta = 0$

Thus, the nullspace of a matrix and its row-echelon matrix are the same. This lets us forget about $X$ and deal with its row-echelon form directly.



## Recipe for a Basis

Now we have to solve the following equation:


$$
\begin{bmatrix}
1 & 0 & -1 & 0\\
0 & 1 & 2 & 1\\
0 & 0 & 0 & 0
\end{bmatrix}\begin{bmatrix}
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4
\end{bmatrix} = \begin{bmatrix}
0\\
0\\
0\\
0
\end{bmatrix}
$$


Columns $1$ and $2$ are called the **pivot columns** as they contain the pivots. The variables corresponding to the pivots are called "dependent variables", while the others are called "independent variables".

!!! note "Algorithm"
    $B = \{ \}$

    For each independent variable $\theta_i$:
    
    - Set $\theta_i = 1$ and $\theta_j = 0$ for all independent variables, $j \neq i$
    - Solve for the dependent variables        
    - Add $\theta$ to $B$



$B$ is the required basis. Let us try it out here. $\theta_1$ and $\theta_2$ are the dependent variables. $\theta_3$ and $\theta_4$ are the independent variables. First, let us set $\theta_3 = 1, \theta_4 = 0$. This gives us $\theta_1 = 1, \theta_2 = -2$. The first element of the basis is therefore $\begin{bmatrix}1 & -2 & 1 & 0\end{bmatrix}^T$. Next, we set $\theta_3 = 0, \theta_4 = 1$. This gives us $\theta_1 = 0, \theta_2 = -1$. The second element of the basis is $\begin{bmatrix}0 & -1 & 0 & 1\end{bmatrix}^T$. Thus, the basis for $N(X)$ is:


$$
B = \left \{ \begin{bmatrix}1\\
-2\\
1\\
0\end{bmatrix}, \begin{bmatrix}0\\
-1\\
0\\
1\end{bmatrix} \right \}
$$


The set of all solutions for the equation $X\theta = 0$ is $\text{span}(B)$.



## Summary

In order to solve the equation $X\theta = 0$, we first reduce the matrix $X$ to its row-echelon form. Then we use an iterative algorithm to construct a basis for the null space. The span of the basis is the set of all solutions to this equation.
