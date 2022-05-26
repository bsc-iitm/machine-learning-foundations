---
title: MLF | Lecture | Week-4
---

# Lecture Outline

::: incremental

- Linear Transformations
- Eigenvectors and Eigenvalues
- Characteristic Polynomial
- Computing Eigenvectors
- Diagonalization
- Tests for Diagonalizability
- Fibonacci
- **Orthogonally Diagonalizable Matrices**

:::



# Orthogonality

::: {.columns align=left}

::: {.column width="50%"}

<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>

::: incremental

- $v_i ^ T v_j = 0$, $i \neq j$
- $v_i^T v_i = 1$

:::

:::

::: {.column width="50%"}

<br>

<br>

:::

:::

# Orthogonal matrices

::: {.columns align=left}

::: {.column width="50%"}

<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>

- $v_i ^ T v_j = 0$, $i \neq j$
- $v_i^T v_i = 1$

:::

::: {.column width="50%"}

$$
Q = \begin{bmatrix}
\vert &  & \vert\\
v_1 & \cdots & v_n\\
\vert &  & \vert
\end{bmatrix}
$$
:::

:::



# Orthogonal matrices

::: {.columns align=left}

::: {.column width="50%"}

<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>

- $v_i ^ T v_j = 0$, $i \neq j$
- $v_i^T v_i = 1$

:::

::: {.column width="50%"}

$$
Q = \begin{bmatrix}
\vert &  & \vert\\
v_1 & \cdots & v_n\\
\vert &  & \vert
\end{bmatrix}
$$
<br>
$$
Q^T Q = \begin{bmatrix}
- & v_1 & -\\
& \vdots & \\
- & v_n & -
\end{bmatrix} \begin{bmatrix}
\vert &  & \vert\\
v_1 & \cdots & v_n\\
\vert &  & \vert
\end{bmatrix}
$$
:::

:::



# Orthogonal matrices

::: {.columns align=left}

::: {.column width="50%"}

<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>

- $v_i ^ T v_j = 0$, $i \neq j$
- $v_i^T v_i = 1$

:::

::: {.column width="50%"}

$$
Q = \begin{bmatrix}
\vert &  & \vert\\
v_1 & \cdots & v_n\\
\vert &  & \vert
\end{bmatrix}
$$
<br>
$$
Q^T Q = I
$$
:::

:::



# Orthogonal matrices

::: {.columns align=left}

::: {.column width="50%"}

<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>

- $v_i ^ T v_j = 0$, $i \neq j$
- $v_i^T v_i = 1$

:::

::: {.column width="50%"}

$$
Q = \begin{bmatrix}
\vert &  & \vert\\
v_1 & \cdots & v_n\\
\vert &  & \vert
\end{bmatrix}
$$
<br>
$$
Q^T Q = I
$$
<br>
$$
Q^{-1} = Q^T
$$


:::

:::



# Orthogonally diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
A = QDQ^{-1}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Orthogonally diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
A = QDQ^T
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Orthogonally diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
A = QDQ^T
$$
:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
A^T =
$$


:::

:::



# Symmetric matrices

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
A = QDQ^T
$$
:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
A^T = A
$$


:::

:::



# Question

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If a matrix is orthogonally diagonalizable, it is symmetric.

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Question

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If a matrix is orthogonally diagonalizable, it is symmetric.

<br>

If a matrix is symmetric, is it orthogonally diagonalizable?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Question

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

If a matrix is orthogonally diagonalizable, it is symmetric.

<br>

If a matrix is symmetric, is it orthogonally diagonalizable?

<br>

Week-5

:::

::: {.column width="0%"}

<br>

<br>

:::

:::

