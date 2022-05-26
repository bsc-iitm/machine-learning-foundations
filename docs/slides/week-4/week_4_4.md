---
title: MLF | Lecture | Week-4
---

# Lecture Outline

::: incremental

- Linear Transformations
- Eigenvectors and Eigenvalues
- Characteristic Polynomial
- **Computing Eigenvectors**
- Diagonalization
- Tests for Diagonalizability
- Fibonacci
- Orthogonally Diagonalizable Matrices

:::



# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>
$$
\begin{aligned}
(A - 2I) x &= 0\\\\
\end{aligned}
$$
:::

:::





# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>
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
:::

:::



# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>
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
\end{bmatrix}\\\\
x_1 + x_2 &= 0
\end{aligned}
$$
:::

:::



# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>
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
\end{bmatrix}\\\\
x_1 + x_2 &= 0
\end{aligned}
$$
$\begin{bmatrix}-1\\1\end{bmatrix}$ is an eigenvector of $A$ with eigenvalue $2$

:::

:::



# Computing Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br><br>
$$
A = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$

<br>

$\lambda = 2$ is an eigenvalue. What are the corresponding eigenvectors?

:::

::: {.column width="50%"}

<br>
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
\end{bmatrix}\\\\
x_1 + x_2 &= 0
\end{aligned}
$$
$\begin{bmatrix}-1\\1\end{bmatrix}$ is an eigenvector of $A$ with eigenvalue $2$

<br>

$\text{span} \left ( \begin{bmatrix}-1\\1\end{bmatrix}  \right)$ is the the eigenspace corresponding to $\lambda = 2$

:::

:::





# Eigenspace and Nullspace

<br>

<br>

::: {.columns align=center}

::: {.column width="50%"}

::: incremental

- If $(\lambda, v)$ is an eigenpair, then $(A - \lambda I) v = 0$
- Then, $v$ belongs to the nullspace of $A - \lambda I$ 
- Every non-zero vector in $N(A - \lambda I)$ is an eigenvector for $\lambda$

- Find a basis $B$ for the nullspace of $A - \lambda I$
- $\text{span}(B)$ is nothing but the eigenspace corresponding to $\lambda$

:::

:::

::: {.column width="0%"}

:::

:::
