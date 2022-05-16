# Computing Eigenvectors

!!! question
	How do we find the eigenvectors of a matrix?



## Example

Once we have the eigenvalues of a matrix, the next logical step is to find the eigenvectors for each of these eigenvalues. Let us continue with the example that we have been working with so far:


$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$


We already know that the eigenvalues are $2$ and $3$. What are the eigenvectors corresponding to $\lambda = 2$? First, we note that if $x$ is an eigenvector corresponding to $\lambda = 2$, then:


$$
\begin{aligned}
(A - 2I) x &= 0\\\\
\begin{bmatrix}
1 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
x_1\\
x_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}
\end{aligned}
$$


From this, we have $x_1 + x_2 = 0$. $x_2$ is an independent variabe and $x_1$ is a dependent variable. The rank of this matrix is $1$, so every eigenvector is of the form:


$$
k\begin{bmatrix}
-1\\
1
\end{bmatrix}
$$


Therefore, the eigenspace corresponding to the eigenvalue $\lambda = 2$ is given by:


$$
\text{span}\left( \left\{ \begin{bmatrix}-1\\1\end{bmatrix} \right\} \right)
$$


If we repeat the same process for $\lambda = 3$, the eigenspace turns out to be:


$$
\text{span}\left( \left\{ \begin{bmatrix}1\\0\end{bmatrix} \right\} \right)
$$


What have we done so far? We have just computed the nullspace of $A - \lambda I$. So, this is the recipe to follow: compute a basis for the nullspace of the matrix $A - \lambda I$. The span of this basis (exculding the zero vector) is the set of all eigenvectors of the matrix $A$ corresponding to the eigenvalue $\lambda$. We have already discussed an [algorithm](../week-3/system_1.md) to compute the basis for the nullspace of a matrix.

!!! note
    For any matrix $A$, the nullspace of $A$ (excluding the vector $0$) has all the eigenvectors of $A$ with eigenvalue $0$. This is because $Ax = 0 = 0x$ if $x \in N(A)$.



## Special examples

Let us take up some special examples and see how the eigenvectors and eigenvalues look.



### Diagonal matrix

If $D$ is a diagonal matrix, then the eigenvalues are the diagonal entries of the matrix. We can express it as:
$$
D = \text{diag}(\lambda_1, \cdots, \lambda_n)
$$
The characteristic polynomial is $(\lambda - \lambda_1) \cdots (\lambda - \lambda_n)$. The eigenvectors of $D$ are going to be elements of the standard basis $\{e_1, \cdots, e_n\}$. Diagonal matrices are the most interesting when it comes to the study of eigenvalues and eigenvectors because of the ease with which we can read off the eigenvalues.



### Identity matrix

If $I$ is an identity matrix of size $n \times n$, then every vector in $\mathbb{R}^{n}$ is an eigenvector with eigenvalue $1$. The characteristic polynomial for the identity matrix is of the form $(\lambda - 1)^n$. There is exactly one eigenvalue that is repeated $n$ times. This is en extreme case of the diagonal matrix.



### Projection matrix

If $P$ is a projection matrix corresponding to a matrix $A$, then every vector that is in the column space of $A$ is  an eigenvector with eigenvalue $1$. To see why this is true, note that $Px = x$ for any vector in the column space of $A$. Also, every vector that is orthogonal to the column space of $A$ will be an eigenvector of $P$ with eigenvalue $0$. This is because $Px = 0$ for any vector in this space.



