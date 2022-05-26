---
title: MLF | Lecture | Week-4
---

# Lecture Outline

::: incremental

- Linear Transformations
- Eigenvectors and Eigenvalues
- **Characteristic Polynomial**
- Computing Eigenvectors
- Diagonalization
- Tests for Diagonalizability
- Fibonacci
- Orthogonally Diagonalizable Matrices

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

How do we find the eigenvalues of a matrix $A$?


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
Ax &= \lambda x
\end{aligned}
$$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
Ax &= \lambda x\\\\
Ax &= \lambda Ix\\\\
\end{aligned}
$$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
Ax &= \lambda x\\\\
Ax &= \lambda Ix\\\\
Ax - \lambda I x &= 0
\end{aligned}
$$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
Ax &= \lambda x\\\\
Ax &= \lambda Ix\\\\
Ax - \lambda I x &= 0\\\\
(A - \lambda I)x &= 0
\end{aligned}
$$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Characteristic Polynomial

::: {.columns align=left}

::: {.column width="100%"}

<br><br>

::: incremental

- Let $x$ be an eigenvector with eigenvalue $\lambda$	
- Then $(A - \lambda I)x = 0$

- $x$ is in the nullspace of $A - \lambda I$ 
- The linear transformation corresponding to $A - \lambda I$ is not one-one
- The linear transformation is not invertible
- $|A - \lambda I| = 0$

:::


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Example

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Example

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= 0\\\\
\end{aligned}
$$


:::

:::



# Example

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= 0\\\\
\begin{vmatrix}
3 - \lambda & 1\\
0 & 2 - \lambda
\end{vmatrix} &= 0
\end{aligned}
$$


:::

:::



# Example

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= 0\\\\
\begin{vmatrix}
3 - \lambda & 1\\
0 & 2 - \lambda
\end{vmatrix} &= 0\\\\
(3 - \lambda)(2 - \lambda) &= 0
\end{aligned}
$$


:::

:::



# Example

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= 0\\\\
\begin{vmatrix}
3 - \lambda & 1\\
0 & 2 - \lambda
\end{vmatrix} &= 0\\\\
(3 - \lambda)(2 - \lambda) &= 0\\\\
\lambda &= 2, 3
\end{aligned}
$$


:::

:::



# Characteristic Polynomial

::: {.columns align=center}

::: {.column width="100%"}

<br><br>
$$
|A - \lambda I| = (\lambda_1 - \lambda) \cdots (\lambda_n - \lambda)
$$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Properties

::: {.columns align=left}

::: {.column width="50%"}

<br>

<br>

::: incremental

- The sum of the eigenvalues is equal to the trace of the matrix.
- The product of the eigenvalues is equal to the determinant of the matrix.

:::

:::

::: {.column width="50%"}

<br>

<br>

<br>

<br>

:::

:::



# Properties

::: {.columns align=left}

::: {.column width="50%"}

<br>

<br>

- The sum of the eigenvalues is equal to the trace of the matrix.
- The product of the eigenvalues is equal to the determinant of the matrix.

:::

::: {.column width="50%"}

<br>

<br>

::: incremental

- $\lambda_1 + \cdots + \lambda_n = \text{tr}(A)$
- $\lambda_1 \cdots \lambda_n = |A|$

:::

:::

:::



# Properties

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
|A - \lambda I| = (\lambda_1 - \lambda) \cdots (\lambda_n - \lambda)
$$

:::

::: {.column width="50%"}

<br>

<br>

If we set $\lambda = 0$, we have:

<br>

<br>

:::

:::





# Properties

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
|A - \lambda I| = (\lambda_1 - \lambda) \cdots (\lambda_n - \lambda)
$$

:::

::: {.column width="50%"}

<br>

<br>

If we set $\lambda = 0$, we have:

<br>


$$
|A| = \lambda_1 \cdots \lambda_n
$$
<br>



:::

:::

# Properties

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
|A - \lambda I| = (\lambda_1 - \lambda) \cdots (\lambda_n - \lambda)
$$

:::

::: {.column width="50%"}

<br>

<br>

If we set $\lambda = 0$, we have:

<br>


$$
|A| = \lambda_1 \cdots \lambda_n
$$
<br>

The determinant of a matrix is equal to the product of its eigenvalues.

:::

:::

