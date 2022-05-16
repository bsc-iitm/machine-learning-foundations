# Diagonalization

!!! question
	What is diagonalization?

## Diagonal matrices

Recall that diagonal matrices are quite interesting to study from the point of view of eigenvectors and eigenvalues. So let us first explore some properties of the same. Let $D$ be an arbitrary diagonal matrix:




$$
D = \begin{bmatrix}
a_1 & \\
& \ddots &\\
& & a_n
\end{bmatrix} = \text{diag}(a_1, \cdots, a_n)
$$


### Determinant

The determinant of a diagonal matrix is given by the product of the values along the diagonal:


$$
|D| = a_1 \cdots a_n
$$


### Invertibility

From the above equation, it follows that a diagonal matrix is invertible if and only if none of the diagonal elements are zero. 



### Matrix power

Consider the product $D^k$. This is extremely simple in the case of a diagonal matrix:


$$
D^k = \text{diag}(a_1^k, \cdots, a_n^k)
$$
We won't prove this statement now. But this is quite easy to see.



### Eigenvalues

This is something that we have already seen. The eigenvalues of a diagonal matrix are the diagonal elements. For the next two properties, let us express the diagonal matrix in terms of its eigenvalues:


$$
D = \text{diag}(\lambda_1, \cdots, \lambda_n)
$$
A diagonal matrix has $n$ eigenvalues, not necessarily distinct. The characteristic polynomial corresponding to it is:



$$
(\lambda  - \lambda_1) \cdots (\lambda - \lambda_n)
$$



### Eigenvectors

It is easy to see that the elements of the standard basis $\beta = \{e_1, \cdots, e_n\}$ are the eigenvectors of $D$. Specifically, $e_i$ is an eigenvector of $D$ corresponding to the eigenvalue $\lambda_i$ as $De_i = \lambda_i e_i$. Can we characterize every possible eigenvector corresponding to eigenvalue $\lambda_i$? For this particular case, let us assume that the eigenvalues are all distinct. Now, let $v$ be some eigenvector of $D$ corresponding to $\lambda_i$:


$$
\begin{bmatrix}
\lambda_1 & &\\
& \ddots & &\\
& & \lambda_n
\end{bmatrix} \begin{bmatrix}
v_1\\
\vdots\\
v_n
\end{bmatrix} = \begin{bmatrix}
\lambda_i v_1\\
\vdots\\
\lambda_iv_n
\end{bmatrix}
$$


This can be further simplified as:


$$
\begin{bmatrix}
(\lambda_1 - \lambda_i) v_1\\
\vdots\\
(\lambda_n - \lambda_i) v_n
\end{bmatrix} = \begin{bmatrix}
0\\
\vdots\\
0
\end{bmatrix}
$$


Since, $\lambda_i \neq \lambda_j$ for $i \neq j$, we have, $v_j = 0$ for $j \neq i$. Thus, the eigenvector corresponding to $\lambda_i$ is some non-zero vector in $\text{span}(\{e_i\})$.



## Diagonalizability

Now that we have seen some interesting properties concerning diagonal matrices, we shall study a special kind of matrices called **diagonalizable matrices**. These matrices are not necessarily diagonal, yet share a close kinship with them. Even if a matrix is not diagonal, can we hope that it is related in some way to a diagonal matrix?

In the last section, we noted that the vectors in the standard basis are eigenvectors of a diagonal matrix. We will generalize this property. Assume that an $n \times n$ matrix has a set of $n$ linearly independent eigenvectors: $\beta = \{v_1, \cdots, v_n\}$. Then $\beta$ is a basis for $\mathbb{R}^n$. From this, we have a definition for diagonalizable matrices:



!!! note "Definition-1"
	An $n \times n$ matrix $A$ is diagonalizable if there is a basis of eigenvectors for $\mathbb{R}^n$.



Taking off from this definition, for $1 \leq i \leq n$, we have:



$$
Av_i = \lambda_i v_i
$$



We can rearrange all these $n$ equations as follows:

$$
A \begin{bmatrix}
\vert & & \vert\\
v_1 & \cdots & v_n\\
\vert & & \vert
\end{bmatrix} = \begin{bmatrix}
\vert & & \vert\\
v_1 & \cdots & v_n\\
\vert & & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \ddots &\\
& & \lambda_n
\end{bmatrix}
$$


Let $Q$ be the matrix of eigenvectors and $D$ be the diagonal matrix of eigenvalues:


$$
Q = \begin{bmatrix}
\vert & & \vert\\
v_1 & \cdots & v_n\\
\vert & & \vert
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & & \\
& \ddots & \\
 & & \lambda_n
\end{bmatrix}
$$

We can now express the equation as:



$$
A Q = Q D
$$



$Q$ is invertible as the columns are linearly independent. With this, we can now rewrite the equation as:



$$
A = QDQ^{-1}
$$



We have managed to establish a bridge from the matrix $A$ to a diagonal matrix $D$. Matrices $A$ and $D$ are similar.



!!! note "Similar matrices"
    Two $n \times n$ matrices $A$ and $B$ are similar if there exists an invertible matrix $Q$ such that $A = QBQ^{-1}$.



This gives an alternative definition for diagonalizable matrices:



!!! note "Definition-2"
	A matrix $A$ is diagonalizable if it is similar to a diagonal matrix.



## Examples

All diagonal matrices are diagonalizable. These are trivial examples of diagonalizable matrices. Let us take up a slightly non-trivial example of a diaongalizable matrix:


$$
A = \begin{bmatrix}
4 & 3\\
1 & 2
\end{bmatrix}
$$


The eigenvalues are $1$ and $5$. The eigenvectors corresponding to these two eigenvalues are $[1, -1]^T$ and $[3, 1]^T$. If we let these two matrices be the columns of a matrix $Q$, then:




$$
Q = \begin{bmatrix}
1 & 3\\
-1 & 1
\end{bmatrix}, Q^{-1} = \begin{bmatrix}
\frac{1}{2} & -\frac{1}{2}\\
\frac{1}{6} & \frac{1}{6}
\end{bmatrix}, D = \begin{bmatrix}
1 & 0\\
0 & 5
\end{bmatrix}
$$


We have:


$$
A = Q D Q^{-1}
$$


## Properties

Let us look at two observations which exemplify the relationship between diagonalizable matrices and their diagonal counterparts.

### Eigenvalues

The following observation will be useful for the rest of the analysis:

!!! note
	If two matrices $A$ and $B$ are similar then they have the same eigenvalues.



There exists some invertible matrix $Q$ such that $A = QBQ^{-1}$. We can now look at the characteristic polynomial of $A$:


$$
\begin{aligned}
|A - \lambda I| &= |QBQ^{-1} - \lambda I|\\\\
&= |QBQ^{-1} - \lambda Q Q^{-1}|\\\\
&= |Q(B - \lambda I)Q^{-1}|\\\\
&= |Q| \cdot |B - \lambda I| \cdot |Q^{-1}|\\\\
&= |B - \lambda I|
\end{aligned}
$$


The two matrices have the same characteristic polynomial and hence the same eigenvalues. Thus, a diagonalizable matrix has $n$ eigenvalues, not necessarily distinct. These eigenvalues can be directly read off if we know the diagonal counterpart corresponding to $A$.

### Matrix power

If $A$ is a diagonalizable matrix, then:


$$
\begin{aligned}
A^k &= (QDQ^{-1})^k\\\\
&= \underbrace{(QDQ^{-1}) \cdots (QDQ^{-1})}_{k \text{ blocks}}\\\\
&= Q D^k Q^{-1}
\end{aligned}
$$


We see that $A^{k}$ is also diagonalizable. The eigenvlaues of $A^k$ are the $k^{th}$ powers of the eigenvalues of $A$.



## Summary

Diagonalizable matrices are those matrices that are not necessarily diagonal, yet share a close kinship with them. The following are equivalent definitions. An $n \times n$ matrix $A$ is diagonalizable if:

- $\mathbb{R}^n$ has a basis of eigenvectors of $A$.
- $A$ is similar to a diagonal matrix.

