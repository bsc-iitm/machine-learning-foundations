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
- **Fibonacci**
- Orthogonally Diagonalizable Matrices

:::



# Application

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

What is an application of diagonalization?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
0, 1, 1, 2, 3, 5, 8, \cdots
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

$F_k$ is the $k^{th}$ term of the sequence

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
F_{k + 2}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
F_{k + 2} = F_{k + 1} + F_{k}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
F_{k + 2} &= F_{k + 1} + F_{k}\\\\
F_{k + 1} &= F_{k + 1}
\end{aligned}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Fibonacci

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{aligned}
F_{k + 2} &= 1 \cdot F_{k + 1} + 1 \cdot F_{k}\\\\
F_{k + 1} &= 1 \cdot F_{k + 1} + 0 \cdot F_{k}
\end{aligned}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Matrix form

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\begin{bmatrix}
F_{k + 2}\\
F_{k + 1}
\end{bmatrix} = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix} \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Matrix form

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{bmatrix}
F_{k + 2}\\
F_{k + 1}
\end{bmatrix} = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix} \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Matrix form

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{bmatrix}
F_{k + 2}\\
F_{k + 1}
\end{bmatrix} = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix} \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}, u_k = \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

:::



# Matrix form

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{bmatrix}
F_{k + 2}\\
F_{k + 1}
\end{bmatrix} = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix} \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

::: {.column width="50%"}

<br>

<br>
$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}, u_k = \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


<br>
$$
u_{k + 1} = A u_k
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
<br>
$$
u_1 = Au_0
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
<br>
$$
u_1 = Au_0
$$
<br>
$$
\begin{aligned}
u_2 &= Au_1
\end{aligned}
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
<br>
$$
u_1 = Au_0
$$
<br>
$$
\begin{aligned}
u_2 &= Au_1\\
&= A^2 u_0
\end{aligned}
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
<br>
$$
u_1 = Au_0
$$
<br>
$$
\begin{aligned}
u_2 &= A^2u_0
\end{aligned}
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u_{k + 1} = A u_k
$$
:::

::: {.column width="50%"}

$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$
<br>
$$
u_1 = Au_0
$$
<br>
$$
\begin{aligned}
u_k &= A^ku_0
\end{aligned}
$$
:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\huge{u_k = A^k u_0}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\huge{u_k = A^k u_0}
$$
<br>

How do we compute $A^k$?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Recurrence Relation

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\huge{u_k = A^k u_0}
$$
<br>

How do we compute $A^k$?

<br>

Diagonalization

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalization

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}
$$
<br>

Is $A$ diagonalizable?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvalues

::: {.columns align=center}

::: {.column width="100%"}

$$
\begin{aligned}
\quad \ \ \begin{vmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{vmatrix} &= 0
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvalues

::: {.columns align=center}

::: {.column width="100%"}

$$
\begin{aligned}
\begin{vmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{vmatrix} &= 0\\\\\\
(1 - \lambda)(-\lambda) - 1 &= 0
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvalues

::: {.columns align=center}

::: {.column width="100%"}

$$
\begin{aligned}
\begin{vmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{vmatrix} &= 0\\\\\\
(1 - \lambda)(-\lambda) - 1 &= 0\\\\\\
\lambda^2 - \lambda - 1 &= 0
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvalues

::: {.columns align=center}

::: {.column width="50%"}

$$
\begin{aligned}
\begin{vmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{vmatrix} &= 0\\\\\\
(1 - \lambda)(-\lambda) - 1 &= 0\\\\\\
\lambda^2 - \lambda - 1 &= 0\\\\
\end{aligned}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\lambda_1 = \cfrac{1 - \sqrt{5}}{2}, \lambda_2 = \cfrac{1 + \sqrt{5}}{2}
$$
:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="100%"}

<br>
$$
\begin{aligned}
\quad \quad\ \  (A - \lambda I)v &= 0\\\\
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="100%"}

<br>
$$
\begin{aligned}
(A - \lambda I)v &= 0\\\\
\begin{bmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{bmatrix}\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="100%"}

<br>
$$
\begin{aligned}
(A - \lambda I)v &= 0\\\\
\begin{bmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{bmatrix}\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
\cfrac{v_1}{v_2} &= \lambda
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
\begin{aligned}
(A - \lambda I)v &= 0\\\\
\begin{bmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{bmatrix}\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
\cfrac{v_1}{v_2} &= \lambda
\end{aligned}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{bmatrix}
\lambda_1\\
1
\end{bmatrix}, \begin{bmatrix}
\lambda_2\\
1
\end{bmatrix}
$$
:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>
$$
\begin{aligned}
(A - \lambda I)v &= 0\\\\
\begin{bmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{bmatrix}\begin{bmatrix}
v_1\\
v_2
\end{bmatrix} &= \begin{bmatrix}
0\\
0
\end{bmatrix}\\\\
\cfrac{v_1}{v_2} &= \lambda
\end{aligned}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{bmatrix}
\lambda_1\\
1
\end{bmatrix}, \begin{bmatrix}
\lambda_2\\
1
\end{bmatrix}
$$
<br>

We have two linearly independent eigenvectors.

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix}
$$
<br>
$$
D = \begin{bmatrix}
\lambda_1 & 0\\
0 & \lambda_2
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix}
$$
<br>
$$
D = \begin{bmatrix}
\lambda_1 & 0\\
0 & \lambda_2
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
A = QDQ^{-1}
$$
:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix}, Q^{-1} = \cfrac{1}{\lambda_1 - \lambda_2}\begin{bmatrix}
1 & -\lambda_2\\
-1 & \lambda_1
\end{bmatrix}
$$
<br>
$$
D = \begin{bmatrix}
\lambda_1 & 0\\
0 & \lambda_2
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
A = QDQ^{-1}
$$
:::

:::



# Formula

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
u_k = A^k u_0
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Formula

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
u_k = A^k u_0
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
u_k &= (QDQ^{-1})^k u_0
\end{aligned}
$$
:::

:::



# Formula

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
u_k = A^k u_0
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
u_k &= (QDQ^{-1})^k u_0\\\\
&= Q D^k Q^{-1} u_0
\end{aligned}
$$


:::

:::



# Formula

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
u_k &= Q D^k Q^{-1} u_0 \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad\ \ 
\end{aligned}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Formula

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
u_k &= Q D^k Q^{-1} u_0\\\\
&= \cfrac{1}{\lambda_1 - \lambda_2} \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix} \begin{bmatrix}
\lambda_1^k & 0\\
0 & \lambda_2^k
\end{bmatrix} \begin{bmatrix}
1 & -\lambda_2\\
-1 & \lambda_1
\end{bmatrix} \begin{bmatrix}
1\\
0
\end{bmatrix}
\end{aligned}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Formula

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
u_k &= Q D^k Q^{-1} u_0\\\\
&= \cfrac{1}{\lambda_1 - \lambda_2} \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix} \begin{bmatrix}
\lambda_1^k & 0\\
0 & \lambda_2^k
\end{bmatrix} \begin{bmatrix}
1 & -\lambda_2\\
-1 & \lambda_1
\end{bmatrix} \begin{bmatrix}
1\\
0
\end{bmatrix}\\\\
&= \cfrac{1}{\lambda_1 - \lambda_2}  \begin{bmatrix}
\lambda_1^{k + 1} - \lambda_2^{k + 1}\\
\lambda_1^{k} - \lambda_2^{k}
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Formula

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
u_k = \cfrac{1}{\lambda_1 - \lambda_2}  \begin{bmatrix}
\lambda_1^{k + 1} - \lambda_2^{k + 1}\\
\lambda_1^{k} - \lambda_2^{k}
\end{bmatrix}
$$


:::

::: {.column width="50%"}

<br>

<br>
$$
u_k = \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


:::

:::



# Formula

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
F_k = \cfrac{1}{\lambda_1 - \lambda_2} \left(\lambda_1^k - \lambda_2^k \right)
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Formula

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
\lambda_1 = \cfrac{1 - \sqrt{5}}{2}, \lambda_2 = \cfrac{1 + \sqrt{5}}{2}
$$


:::

::: {.column width="50%"}

<br>

<br>
$$
F_k = \cfrac{1}{\lambda_1 - \lambda_2} \left(\lambda_1^k - \lambda_2^k \right)
$$


:::

:::



# Formula

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\boxed{F_k = \cfrac{1}{\sqrt{5}} \left[  \left(\cfrac{1 + \sqrt{5}}{2} \right)^k - \left(\cfrac{1 - \sqrt{5}}{2} \right)^k \right]}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::

