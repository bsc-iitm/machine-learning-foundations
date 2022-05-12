# Test for Diagonalizability

!!! question
	How do we know if a matrix is diagonalizable?
	

## Negative test

Are all matrices diagonalizable[^1]? Not really. As a counterexample, consider the following matrix:

[^1]: In all the discussions in this unit, we will be only concerned with real vector spaces. The matrices and their eigenvalues, if they exist, will be real.


$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$



The characteristic polynomial for $A$ is:



$$
\begin{aligned}
|A - \lambda I| &= \begin{vmatrix}
-\lambda & 1\\
-1 & -\lambda
\end{vmatrix}\\\\
&= \lambda^2 + 1
\end{aligned}
$$



We see that the polynomial has no real roots. Thus the matrix $A$ has no real eigenvalues. Using this example, we can formulate the following negative test for diagonalizability:



!!! note "Negative test"
	If the characteristic polynomial of a matrix $A$ does not have $n$ eigenvalues, then the matrix is not diagonalizable.



## Positive test

Now that we know that not all matrices are diagonalizable, is there a way to find out which matrices are? We will look at one such test which is based on the following observation.

!!! note
    The eigenvectors corresponding to distinct eigenvalues of $A$ are linearly independent.

We shall prove this for the case of two eigenvlaues. Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$ such that $\lambda_1 \neq \lambda_2$. Consider any linear combination of $v_1$ and $v_2$:


$$
\alpha_1v_1 + \alpha_2 v_2 = 0
$$


Pre-multiplying by $A - \lambda_1 I$ on both sides:


$$
\begin{aligned}
(A - \lambda_1I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_2(\lambda_2 - \lambda_1) &= 0
\end{aligned}
$$


Since $\lambda_1 \neq \lambda_2$, we have $\alpha_2 = 0$. From this it follows that $\alpha_1 = 0$. So, $v_1$ and $v_2$ are linearly independent. So, one positive test for diagonalizability is this:



!!! note "Positive test"
    If an $n \times n$ matrix $A$ has $n$ distinct eigenvalues, then it is diagonalizable.



## No man's land

A natural question now arises. What about the case where a matrix has $n$​ eigenvalues, but in which some eigenvalues repeat. Is it always diagonalizable? Even if a matrix has eigenvalues, there is no guarantee that it will have a basis of eigenvectors. For example, consider the matrix:



$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$



The characteristic polynomial is $(\lambda - 2)^2$. So, $\lambda = 2$ is the only eigenvalue, but repeated twice. To get the eigenvectors, we solve $(A - 2I)v = 0$:



$$
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
v_1\\v_2
\end{bmatrix} = \begin{bmatrix}
0\\
0
\end{bmatrix}
$$



This gives us $v_2 = 0$ and $v_1 = k$, where $k$ is some non-zero real number. Thus, every eigenvector of $A$ is some non-zero vector in $\text{span}\left( \left\{ \begin{bmatrix}1\\0 \end{bmatrix} \right\} \right)$. Since we don't have two linearly independent eigenvectors, $A$ is not diagonalizable.



## Summary

Not all matrices are diagonalizable. There are two tests for diagonlizability:

- Negative test: if a matrix doesn't have $n$ eigenvalues, it is not diagonalizable.
- Positive test: if a matrix has $n$ distinct eigenvalues, then it is diagonalizable.

If a matrix has $n$ eigenvalues, but with repetitions, then the test is inconclusive.

