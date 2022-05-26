---
title: MLF | Lecture | Week-4
---

# Lecture Outline

::: incremental

- Linear Transformations
- **Eigenvectors and Eigenvalues**
- Characteristic Polynomial
- Computing Eigenvectors
- Diagonalization
- Tests for Diagonalizability
- Fibonacci
- Orthogonally Diagonalizable Matrices

:::




# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>
$$
\huge{T = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}}
$$



:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenvectors

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_5.mp4">
</video>




# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u = \begin{bmatrix}
-1\\
1
\end{bmatrix}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{aligned}
Tu &= \begin{bmatrix}
-2\\
2
\end{bmatrix}
\end{aligned}
$$


:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u = \begin{bmatrix}
-1\\
1
\end{bmatrix}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{aligned}
Tu &= \begin{bmatrix}
-2\\
2
\end{bmatrix}\\\\
&= 2u
\end{aligned}
$$


:::

:::



# Eigenvectors

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_6.mp4">
</video>




# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u = \begin{bmatrix}
1\\
1
\end{bmatrix}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{aligned}
Tu &= \begin{bmatrix}
4\\
2
\end{bmatrix}
\end{aligned}
$$


:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
u = \begin{bmatrix}
1\\
1
\end{bmatrix}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
\begin{aligned}
Tu &= \begin{bmatrix}
4\\
2
\end{bmatrix}\\\\
&\neq \lambda u
\end{aligned}
$$


:::

:::



# Eigenpair

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

For a linear transformation $T$, a non-zero vector $v$ is called an eigenvector with eigenvalue $\lambda$ if:




:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenpair

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

For a linear transformation $T$, a non-zero vector $v$ is called an eigenvector with eigenvalue $\lambda$ if:

<br>
$$
\boxed{\huge{T v = \lambda v}}
$$


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenpair

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

For a linear transformation $T$, a non-zero vector $v$ is called an eigenvector with eigenvalue $\lambda$ if:

<br>
$$
\boxed{\huge{T v = \lambda v}}
$$


<br>

<br>

$(\lambda, v)$ is called an eigenpair of $T$

:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Eigenpair

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

For a matrix $T$, a non-zero vector $v$ is called an eigenvector with eigenvalue $\lambda$ if:

<br>
$$
\boxed{\huge{T v = \lambda v}}
$$


<br>

<br>

$(\lambda, v)$ is called an eigenpair of $T$

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
T = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



:::

::: {.column width="50%"}

<br>

<br>
$$
\left (2, \begin{bmatrix}-1\\1\end{bmatrix} \right)
$$
<br>
$$
\left (3, \begin{bmatrix}1\\0\end{bmatrix} \right)
$$


:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Why should an eigenvector be non-zero?


:::

::: {.column width="50%"}

<br>

<br>

:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Why should an eigenvector be non-zero?


:::

::: {.column width="50%"}

<br>

<br>
$$
T0 = \lambda 0
$$


:::

:::



# Eigenvectors

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

Why should an eigenvector be non-zero?


:::

::: {.column width="50%"}

<br>

<br>
$$
T0 = \lambda 0
$$
<br>

How many values can $\lambda$ take?

:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ is an eigenvector of $T$ with eigenvalue $\lambda$, then what can you say about $ku$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(ku) &= 
\end{aligned}
$$


:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ is an eigenvector of $T$ with eigenvalue $\lambda$, then what can you say about $ku$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(ku) &= k \cdot Tu
\end{aligned}
$$


:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ is an eigenvector of $T$ with eigenvalue $\lambda$, then what can you say about $ku$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(ku) &= k \cdot Tu\\\\
&= k \cdot \lambda u
\end{aligned}
$$


:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ is an eigenvector of $T$ with eigenvalue $\lambda$, then what can you say about $ku$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(ku) &= k \cdot Tu\\\\
&= k \cdot \lambda u\\\\
&= \lambda \cdot (ku)
\end{aligned}
$$


:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ is an eigenvector of $T$ with eigenvalue $\lambda$, then what can you say about $ku$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(ku) &= k \cdot Tu\\\\
&= k \cdot \lambda u\\\\
&= \lambda \cdot (ku)
\end{aligned}
$$


<br>

$ku$ is an eigenvector of $T$ with eigenvalue $\lambda$, where $k \neq 0$

:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ and $v$ are eigenvectors of $T$ with eigenvalue $\lambda$, then what can you say about $u + v$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(u + v) &= 
\end{aligned}
$$


<br>



:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ and $v$ are eigenvectors of $T$ with eigenvalue $\lambda$, then what can you say about $u + v$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(u + v) &= Tu + Tv
\end{aligned}
$$


<br>



:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ and $v$ are eigenvectors of $T$ with eigenvalue $\lambda$, then what can you say about $u + v$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(u + v) &= Tu + Tv\\\\
&= \lambda u + \lambda v
\end{aligned}
$$


<br>



:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ and $v$ are eigenvectors of $T$ with eigenvalue $\lambda$, then what can you say about $u + v$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(u + v) &= Tu + Tv\\\\
&= \lambda u + \lambda v\\\\
&= \lambda(u + v)
\end{aligned}
$$


<br>



:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

If $u$ and $v$ are eigenvectors of $T$ with eigenvalue $\lambda$, then what can you say about $u + v$?


:::

::: {.column width="50%"}

<br>

<br>
$$
\begin{aligned}
T(u + v) &= Tu + Tv\\\\
&= \lambda u + \lambda v\\\\
&= \lambda(u + v)
\end{aligned}
$$


<br>

$u + v$ is an eigenvector of $T$ with eigenvalue $\lambda$

:::

:::



# Eigenspace

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>
$$
\huge{E = \{u\ \vert\ Tu = \lambda u, u \in \mathbb{R}^n \}}
$$



:::

::: {.column width="0%"}

<br>

<br>

:::

:::
