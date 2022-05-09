# Characteristic Polynomial

!!! question
	How do we find the eigenvalues of a matrix?



## Necessary condition

If $x$ is an eigenvector of a matrix $A$ with eigenvalue $\lambda$, then we have:


$$
Ax = \lambda x
$$


Let us rearrange this a bit. First, observe that if $I$ is the identity matrix, then:


$$
Ix = x
$$

Using this fact, we can express the eigenvalue equation as:



$$
\begin{aligned}
Ax &= \lambda Ix\\\\
Ax - \lambda I x &= 0\\\\
(A - \lambda I)x &= 0
\end{aligned}
$$



If $(\lambda, x)$ is an eigenpair, then $(A - \lambda I) x = 0$. Another way of expressing this is: 

!!! note "Necessary condition"
    $(A - \lambda I)x = 0$ is a necessary condition for $x$ to be an eigenvector of $A$ with eigenvalue $\lambda$.



## Sufficient condition

Let us try the other direction. What if $(A - \lambda I)x = 0$? We have:


$$
\begin{aligned}
(A - \lambda I)x &= 0\\\\
Ax - \lambda Ix &= 0\\\\
Ax &= \lambda x
\end{aligned}
$$


Thus we see that $x$ is an eigenvector of $A$ with eigenvalue $\lambda$. 



!!! note "Sufficient condition"
    $(A - \lambda I)x = 0$ is a sufficient condition for $x$ to be an eigenvector of $A$ with eigenvalue $\lambda$.



## Nullspace argument

Thus we see that $(\lambda, x)$ is an eigenpair of $A$ *if and only if* $(A - \lambda I)x = 0$. From this, we deduce that $x$ has to be in the nullspace of $A - \lambda I$. Thus the nullspace of $A - \lambda I$ is non-trivial. If the nullspace is non-trivial, we can conclude that the matrix is not invertible. To see why this is true, think about the linear transformation corresponding to this matrix. If the nullspace is non-trivial, then the transformation is not one-one. Therefore, it doesn't have an inverse. If the transformation doesn't have an inverse, the corresponding matrix is not invertible.

If the matrix is not invertible, then its determinant is zero. So, we have the following result:



!!! Important
	$\lambda$ is an eigenvalue of $A$ if and only if $|A - \lambda I| = 0$



Notice how we end up with a result that doesn't involve the eigenvector and only the matrix and its eigenvalue. 

!!! note
	The eigenspace corresponding to an eigenvalue $\lambda$ is the nullspace of $A - \lambda I$.



## The Polynomial

At this stage, let us take up an example:


$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$


For $\lambda$ to be an eigenvalue of the matrix $A$, $|A - \lambda I| = 0$. This translates to:


$$
\begin{vmatrix}
3 - \lambda & 1\\
0 & 2 - \lambda
\end{vmatrix} = 0
$$


Expanding the determinant, we get:


$$
\begin{aligned}
(3 - \lambda)(2 - \lambda) = 0
\end{aligned}
$$


The expression on the LHS is a polynomial of degree $2$ and is called the **characteristic polynomial** of $A$. We see that $\lambda = 2, 3$ are the eigenvalues of the matrix $A$. 



## Properties

In general, for an $n \times n$ matrix $A$, the characteristic polynomial has degree $n$. The roots of the characteristic polynomial are the eigenvalues of the matrix $A$. There are two properties of the polynomial that are worth knowing:

- the sum of the eigenvalues of the matrix is equal to its trace
- the product of the eigenvalues of the matrix is equal to its determinant

The second property is easy to see. Assume that the polynomial splits into $n$ factors corresponding to $n$ eigenvalues $\lambda_1, \cdots, \lambda_n$, then:


$$
|A - \lambda I| = (\lambda - \lambda_1) \cdots (\lambda - \lambda_n)
$$


If we set $\lambda = 0$, then:


$$
|A| = \lambda_1 \cdots \lambda_n
$$




## Summary

To find the eigenvalues of a matrix $A$, we first compute the characteristic polynomial $|A - \lambda I|$. The roots of this polynomial are the eigenvalues of the matrix $A$. There are two important properties:

- sum of the eigenvalues is equal to the trace of the matrix
- product of the eigenvalues is equal to the determinant of the matrix
