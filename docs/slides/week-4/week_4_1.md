---
title: MLF | Lecture | Week-4

---

# Lecture Outline

::: incremental

- **Linear Transformations**
- Eigenvectors and Eigenvalues
- Characteristic Polynomial
- Computing Eigenvectors
- Diagonalization
- Tests for Diagonalizability
- Fibonacci
- Orthogonally Diagonalizable Matrices

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="100%"}

<br>

<br>

<br>

What is a linear transformation?


:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="100%"}

<br><br>

<br>
$$
\huge{T: V \rightarrow W}
$$



:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="100%"}

<br><br>

<br>
$$
\huge{T: \mathbb{R}^{n} \rightarrow \mathbb{R}^m}
$$



:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="100%"}

<br><br>

<br>
$$
\huge{T: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}}
$$



:::

::: {.column width="0%"}

<br>

<br>

:::

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\beta = \left \{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>



:::

:::



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\beta = \left \{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
[T]_{\beta}^{\beta} = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}
$$


:::

:::



# Linear Transformation

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_1.mp4">
</video>




# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\beta = \left \{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
[T]_{\beta}^{\beta} = \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$


:::

:::





# Linear Transformation

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_2.mp4">
</video>




# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\beta = \left \{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
[T]_{\beta}^{\beta} = \begin{bmatrix}
0 & -2\\
2 & 0
\end{bmatrix}
$$


:::

:::



# Linear Transformation

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_3.mp4">
</video>




# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

What is the linear transformation that we just saw?


:::

::: {.column width="50%"}

<br>

<br>

:::

:::

<br>

<br>

<br>



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

What is the linear transformation that we just saw?

<br>

It is a composition of two transformations. What are they?


:::

::: {.column width="50%"}

<br>

<br>

:::

:::

<br>

<br>

<br>



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

What is the linear transformation that we just saw?

<br>

It is a composition of two transformations. What are they?


:::

::: {.column width="50%"}

<br>

<br>
$$
T_1 = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}, T_2 = \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$


:::

:::

<br>

<br>

<br>



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

What is the linear transformation that we just saw?

<br>

It is a composition of two transformations. What are they?


:::

::: {.column width="50%"}

<br>

<br>
$$
T_1 = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}, T_2 = \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix}
$$
<br>
$$
T_1 T_2 = \begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix} \begin{bmatrix}
0 & -1\\
1 & 0
\end{bmatrix} = \begin{bmatrix}
0 & -2\\
2 & 0
\end{bmatrix}
$$


:::

:::

<br>

<br>

<br>



# Linear Transformation

::: {.columns align=center}

::: {.column width="50%"}

<br>

<br>

<br>
$$
\beta = \left \{ \begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix} \right\}
$$

:::

::: {.column width="50%"}

<br>

<br>

<br>
$$
[T]_{\beta}^{\beta} = \begin{bmatrix}
2 & 1\\
1 & 2
\end{bmatrix}
$$


:::

:::



# Linear Transformation

<video controls width="1000" loop autoplay>
    <source src="../../assets/videos/mat_4.mp4">
</video>


