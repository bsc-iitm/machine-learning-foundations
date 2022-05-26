---
title: MLF | Lecture | Week-4
---

# Lecture Outline

::: incremental

- Linear Transformations
- Eigenvectors and Eigenvalues
- Characteristic Polynomial
- Computing Eigenvectors
- **Diagonalization**
- Tests for Diagonalizability
- Fibonacci
- Orthogonally Diagonalizable Matrices

:::

# Tests for Diagonalizability

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

Are all matrices diagonalizable?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

$$
\begin{aligned}
|A - \lambda I| &=
\end{aligned}
$$
:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

$$
\begin{aligned}
|A - \lambda I| &= \begin{vmatrix}
-\lambda & 1\\
-1 & -\lambda
\end{vmatrix}
\end{aligned}
$$
:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

$$
\begin{aligned}
|A - \lambda I| &= \begin{vmatrix}
-\lambda & 1\\
-1 & -\lambda
\end{vmatrix}\\\\
&= \lambda^2 + 1
\end{aligned}
$$
:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

$$
\begin{aligned}
|A - \lambda I| &= \begin{vmatrix}
-\lambda & 1\\
-1 & -\lambda
\end{vmatrix}\\\\
&= \lambda^2 + 1
\end{aligned}
$$
<br>

This polynomial doesn't have real roots

:::

:::



# Negative test

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
A = \begin{bmatrix}
0 & 1\\
-1 & 0
\end{bmatrix}
$$
:::

::: {.column width="50%"}

$$
\begin{aligned}
|A - \lambda I| &= \begin{vmatrix}
-\lambda & 1\\
-1 & -\lambda
\end{vmatrix}\\\\
&= \lambda^2 + 1
\end{aligned}
$$
<br>

This polynomial doesn't have real roots

<br>

No eigenvalues $\implies$ no eigenvectors

:::

:::





# Negative test

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If the characteristic polynomial of a matrix $A$ does not have $n$ eigenvalues, then the matrix is not diagonalizable.

<br>

:::

::: {.column width="0%"}

<br>

<br>

:::

:::

# Negative test

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If the characteristic polynomial of a matrix $A$ does not have $n$ eigenvalues, then the matrix is not diagonalizable.

<br>

:::

::: {.column width="0%"}

<br>

<br>

:::

:::

**Note-1**: the $n$ eigenvalues need not be distinct

**Note-2**: this is true only for real vector spaces



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

<br>

<br>

Are $v_1$ and $v_2$ linearly independent?

:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\quad \quad \quad \quad \quad \quad \quad \quad \alpha_1 v_1 + \alpha_2 v_2 &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\quad \quad \quad \quad \quad \quad \quad \quad  \alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_1 (A - \lambda_1 I)v_1 + \alpha_2 (A - \lambda_1 I)v_2 &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_1 (A - \lambda_1 I)v_1 + \alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (A - \lambda_1 I)v_2 &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_1 (A - \lambda_1 I)v_1 + \alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (\lambda_2 v_2 - \lambda_1v_2) &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_1 (A - \lambda_1 I)v_1 + \alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (\lambda_2 v_2 - \lambda_1v_2) &= 0\\\\
\alpha_2 (\lambda_2 - \lambda_1) v_2 &= 0\\\\
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Let $(\lambda_1, v_1)$ and $(\lambda_2, v_2)$ be two eigenpairs of $A$

<br>

$\lambda_1 \neq \lambda_2$

:::

::: {.column width="50%"}

$$
\begin{aligned}
\alpha_1 v_1 + \alpha_2 v_2 &= 0\\\\
(A - \lambda_1 I)(\alpha_1 v_1 + \alpha_2 v_2) &= 0\\\\
\alpha_1 (A - \lambda_1 I)v_1 + \alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (A - \lambda_1 I)v_2 &= 0\\\\
\alpha_2 (\lambda_2 v_2 - \lambda_1v_2) &= 0\\\\
\alpha_2 (\lambda_2 - \lambda_1) v_2 &= 0\\\\
\implies \alpha_2 = \alpha_1 &= 0
\end{aligned}
$$


:::

:::



# Positive Test

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If an $n \times n$ matrix $A$ has $n$ distinct distinct eigenvalues, then it is diagonalizable.

<br>

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

What if a matrix has $n$ eigenvalues but some of them repeat?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
|A - \lambda I| = (\lambda - 2)^2
$$
<br>

$\lambda = 2$ is the only eigenvalue

:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="30%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
$\lambda = 2$ is the only eigenvalue of $A$

:::

::: {.column width="70%"}


$$
\begin{aligned}
(A - 2I)\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= 0 \quad \quad\\\\
\end{aligned}
$$
:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="30%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
$\lambda = 2$ is the only eigenvalue of $A$

:::

::: {.column width="70%"}


$$
\begin{aligned}
(A - 2I)\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= 0\\\\
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
v_1\\v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}
\end{aligned}
$$
:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="30%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
$\lambda = 2$ is the only eigenvalue of $A$

:::

::: {.column width="70%"}


$$
\begin{aligned}
(A - 2I)\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= 0\\\\
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
v_1\\v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
v_2 &= 0
\end{aligned}
$$
:::

:::





# No man's land

::: {.columns align=center}

::: {.column width="30%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
$\lambda = 2$ is the only eigenvalue of $A$

:::

::: {.column width="70%"}


$$
\begin{aligned}
(A - 2I)\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= 0\\\\
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
v_1\\v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
v_2 &= 0
\end{aligned}
$$
$\text{span} \left( \begin{bmatrix}1\\0\end{bmatrix} \right)$ is the eigenspace corresponding to $\lambda = 2$

:::

:::



# No man's land

::: {.columns align=center}

::: {.column width="30%"}

<br>

<br>
$$
A = \begin{bmatrix}
2 & 1\\
0 & 2
\end{bmatrix}
$$
$\lambda = 2$ is the only eigenvalue of $A$

:::

::: {.column width="70%"}


$$
\begin{aligned}
(A - 2I)\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= 0\\\\
\begin{bmatrix}
0 & 1\\
0 & 0
\end{bmatrix} \begin{bmatrix}
v_1\\v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
v_2 &= 0
\end{aligned}
$$
$\text{span} \left( \begin{bmatrix}1\\0\end{bmatrix} \right)$ is the eigenspace corresponding to $\lambda = 2$

Since we don't have two linearly independent eigenvectors, $A$ is not diagonalizable

:::

:::



# Summary

::: {.columns align=left}

::: {.column width="100%"}

<br>

::: incremental

Tests for diagonalizability:

- Negative test: if a matrix doesn't have $n$ eigenvalues, it is not diagonalizable.
- Positive test: if a matrix has $n$ distinct eigenvalues, then it is diagonalizable.

- Inconclusive: If a matrix has $n$ eigenvalues, but with repetitions, then the test is inconclusive.

:::

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



