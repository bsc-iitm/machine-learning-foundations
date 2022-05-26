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

# Diagonal Matrices

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D &= \begin{bmatrix}
a_1 & \\
& \ddots &\\
& & a_n
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::

# Diagonal Matrices

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D &= \begin{bmatrix}
a_1 & \\
& \ddots &\\
& & a_n
\end{bmatrix}\\\\
&= \text{diag}(a_1, \cdots, a_n)
\end{aligned}
$$
:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Property-1

::: {.columns align=center}

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_1 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_2 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
1\\
0
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_3 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
0\\
1
\end{bmatrix}
\end{aligned}
$$
:::

:::



# Property-1

::: {.columns align=center}

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_1 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
1\\
0\\
0
\end{bmatrix}\\\\
&= \begin{bmatrix}
a_1\\
0\\
0
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_2 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
1\\
0
\end{bmatrix}\\\\
&= \begin{bmatrix}
0\\
a_2\\
0
\end{bmatrix}
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_3 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
0\\
1
\end{bmatrix}\\\\
&= \begin{bmatrix}
0\\
0\\
a_3
\end{bmatrix}
\end{aligned}
$$
:::

:::



# Property-1

::: {.columns align=center}

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_1 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
1\\
0\\
0
\end{bmatrix}\\\\
&= \begin{bmatrix}
a_1\\
0\\
0
\end{bmatrix}\\\\
&= a_1 \cdot e_1
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_2 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
1\\
0
\end{bmatrix}\\\\
&= \begin{bmatrix}
0\\
a_2\\
0
\end{bmatrix}\\\\
&= a_2 \cdot e_2
\end{aligned}
$$
:::

::: {.column width="33%"}

<br>
$$
\begin{aligned}
De_3 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
0\\
0\\
1
\end{bmatrix}\\\\
&= \begin{bmatrix}
0\\
0\\
a_3
\end{bmatrix}\\\\
&= a_3 \cdot e_3
\end{aligned}
$$
:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D^2 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
\end{aligned}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D^2 &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}\\\\
&= \begin{bmatrix}
a_1^2 & \\
& a_2^2 &\\
& & a_3^2
\end{bmatrix}
\end{aligned}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D^k &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \cdots \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
\end{aligned}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
\begin{aligned}
D^k &= \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix} \cdots \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}\\\\
&= \begin{bmatrix}
a_1^k & \\
& a_2^k &\\
& & a_3^k
\end{bmatrix}
\end{aligned}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Property-3

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
D = \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
|D| = 
$$


:::

:::



# Property-3

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
D = \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
|D| = a_1 a_2a_3
$$


:::

:::



# Property-4

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
D = \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
D^{-1} = 
$$


:::

:::



# Property-4

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
D = \begin{bmatrix}
a_1 & \\
& a_2 &\\
& & a_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
D^{-1} &= \begin{bmatrix}
\frac{1}{a_1} & \\
& \frac{1}{a_2} &\\
& & \frac{1}{a_3}
\end{bmatrix} 
\end{aligned}
$$


:::

:::



# Diagonalizable

::: {.columns align=left}

::: {.column width="100%"}

<br>

<br>

::: incremental

- Diagonal matrices have excellent properties.
- Even if a matrix is not diagonal, can we hope that it is related in some way to a diagonal matrix?
- **Diagonalizable matrices** are not necessarily diagonal, yet share a close kinship with them.
- What are they and how are they related to diagonal matrices?

:::

:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

The vectors in the standard basis are ————— of a diagonal matrix.

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

The vectors in the standard basis are <span style="color:blue">eigenvectors</span> of a diagonal matrix.

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=left}

::: {.column width="100%"}

<br>

<br>

::: incremental

- $A$ is an $n \times n$ matrix
- **Condition:** $A$ has $n$ linearly independent eigenvectors $v_1, \cdots, v_n$
- $\beta = \{v_1, \cdots, v_n\}$ is a basis for $\mathbb{R}^{n}$
- We have a basis of eigenvectors of $A$

:::

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

**Definition-1**: An $n \times n$ matrix $A$ is diagonalizable if there is a basis of eigenvectors for $\mathbb{R}^n$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

**Definition-1**: An $n \times n$ matrix $A$ is diagonalizable if there is a basis of eigenvectors for $\mathbb{R}^n$

<br>

Ok, so what?

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="33%"}

<br>

<br>

<br>
$$
Av_1 = \lambda_1v_1
$$


:::

::: {.column width="33%"}

<br>

<br>

<br>
$$
Av_2 = \lambda_2v_2
$$


:::

::: {.column width="33%"}

<br>

<br>

<br>
$$
Av_3 = \lambda_3v_3
$$


:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="33%"}

<br>

<br>

<br>
$$
A\begin{bmatrix}
\vert\\
v_1\\
\vert
\end{bmatrix} = \begin{bmatrix}
\vert\\
\lambda_1 v_1\\
\vert
\end{bmatrix}
$$


:::

::: {.column width="33%"}

<br>

<br>

<br>
$$
A\begin{bmatrix}
\vert\\
v_2\\
\vert
\end{bmatrix} = \begin{bmatrix}
\vert\\
\lambda_2 v_2\\
\vert
\end{bmatrix}
$$


:::

::: {.column width="33%"}

<br>

<br>

<br>
$$
A\begin{bmatrix}
\vert\\
v_3\\
\vert
\end{bmatrix} = \begin{bmatrix}
\vert\\
\lambda_3 v_3\\
\vert
\end{bmatrix}
$$
:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
\lambda_1 v_1 & \lambda_2 v_2 & \lambda_3 v_3\\
\vert & \vert & \vert
\end{bmatrix}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$
:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
A Q = QD
$$


:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
A Q = QD
$$
<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
A Q = QD
$$
<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>
$$
A = QDQ^{-1}
$$


:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A\begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix} = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert
\end{bmatrix} \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$


<br>
$$
Q = \begin{bmatrix}
\vert & \vert & \vert\\
v_1 & v_2 & v_3\\
\vert & \vert & \vert\\
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & &\\
& \lambda_2 & \\
& & \lambda_3
\end{bmatrix}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
A Q = QD
$$
<br>
$$
\beta = \{v_1, \cdots, v_n\}
$$
<br>
$$
A = QDQ^{-1}
$$


<br>

$A$ and $D$ are similar matrices

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

**Definition-2**: An $n \times n$ matrix $A$ is diagonalizable if it is similar to a diagonal matrix.

<br>

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Diagonalizable

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$


:::

::: {.column width="50%"}

<br>

<br>

:::

:::

# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= 
\end{aligned}
$$


:::

:::





# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= |QDQ^{-1} - \lambda I|\\\\
\end{aligned}
$$


:::

:::





# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= |QDQ^{-1} - \lambda I|\\\\
&= |QDQ^{-1} - \lambda Q Q^{-1}|
\end{aligned}
$$


:::

:::





# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= |QDQ^{-1} - \lambda I|\\\\
&= |QDQ^{-1} - \lambda Q Q^{-1}|\\\\
&= |Q(D - \lambda I)Q^{-1}|
\end{aligned}
$$


:::

:::





# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= |QDQ^{-1} - \lambda I|\\\\
&= |QDQ^{-1} - \lambda Q Q^{-1}|\\\\
&= |Q(D - \lambda I)Q^{-1}|\\\\
&= |Q| \cdot |D - \lambda I| \cdot |Q^{-1}|
\end{aligned}
$$


:::

:::





# Property-1

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
|A - \lambda I| &= |QDQ^{-1} - \lambda I|\\\\
&= |QDQ^{-1} - \lambda Q Q^{-1}|\\\\
&= |Q(D - \lambda I)Q^{-1}|\\\\
&= |Q| \cdot |D - \lambda I| \cdot |Q^{-1}|\\\\
&= |D - \lambda I|
\end{aligned}
$$


:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
A^k &=
\end{aligned}
$$


:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
A^k &= (QDQ^{-1})^k
\end{aligned}
$$


:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
A^k &= (QDQ^{-1})^k\\\\
&= \underbrace{(QDQ^{-1}) \cdots (QDQ^{-1})}_{k \text{ blocks}}
\end{aligned}
$$


:::

:::



# Property-2

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
A = Q D Q^{-1}
$$
:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
A^k &= (QDQ^{-1})^k\\\\
&= \underbrace{(QDQ^{-1}) \cdots (QDQ^{-1})}_{k \text{ blocks}}\\\\
&= Q D^k Q^{-1}
\end{aligned}
$$


:::

:::



# Summary

::: {.columns align=left}

::: {.column width="100%"}

<br>

<br>

::: incremental

The following are equivalent definitions of diagonalizablity. A matrix $A$ is diagonalizable if

- $\mathbb{R}^n$ has a basis of eigenvectors of $A$
- $A$ is similar to a diagonal matrix

:::

:::

::: {.column width="0%"}

<br>

<br>

:::

:::

