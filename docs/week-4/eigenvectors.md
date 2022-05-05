# Eigenvectors and Eigenvalues

!!! question
	What are eigenvectors and eigenvalues?



Let us consider the following linear transformation[^1] from $\mathbb{R}^{2}$ to itself:



$$
T = \begin{bmatrix}
3 & 1\\
0 & 2
\end{bmatrix}
$$



We will look at how this linear transformation operates on vectors from the geometric point of view. Specifically, we will record these two quantities:

- direction of the vector before the transformation
- direction of the vector after the transformation



## Case-1

The vector $u = \begin{bmatrix}1\\1\end{bmatrix}$ is transformed into $Tu = \begin{bmatrix}4\\2\end{bmatrix}$. 



![type:video](../assets/videos/mat_6.mp4)



The vector $u$ was initially pointing in a particular direction. After the transformation, it points in a different direction. This case corresponds to vectors whose direction changes after the linear transformation.



## Case-2

The vector $u = \begin{bmatrix}-1\\1\end{bmatrix}$ is transformed into $Tu = \begin{bmatrix}-2\\2\end{bmatrix}$. 



![type:video](../assets/videos/mat_5.mp4)



The direction of the vector $Tu$ is the same as the direction of the vector $u$. In other words, the linear transformation has preserved the direction of this vector. However, its magnitude has changed. In this case, the vector $u$ has been stretched by a factor of $2$.


$$
Tu = \begin{bmatrix}-2\\2\end{bmatrix} = 2u
$$


Another example for this case is the basis vector $\begin{bmatrix}1\\0\end{bmatrix}$. For this vector:


$$
Tu = \begin{bmatrix}3\\0\end{bmatrix} = 3u
$$


This case corresponds to vectors whose direction remains unchanged after the linear transformation.



## Eigenvectors and Eigenvalues

A *non-zero* vector which point in the same direction before and after the linear transformation is called an **eigenvector**. Since the direction of an eigenvector is unchanged by the transformation, it makes sense to look at the magnitude by which it is scaled after the transformation. This scalar value is called the **eigenvalue**. The eigenvector and the corresponding eigenvalue make up an eigenpair. For the matrix (linear transformation) that we have been working with, $\left (2, \begin{bmatrix}-1\\1\end{bmatrix} \right)$ and $\left (3, \begin{bmatrix}1\\0\end{bmatrix} \right)$ are two eigenpairs.



## Eigenspace

We will now shift to matrices from linear transformations. Consider an arbitrary $n \times n$ matrix $A$. How big is the space of eigenvectors? Let $A$ be a matrix. If $u$ is an eigenvector of $A$ with  eigenvalue $\lambda$, what can we say about the vector $2u$?


$$
A(2u) = 2 Au = 2 \lambda u = \lambda(2u)
$$


We see that $2u$ is also an eigenvector with eigenvalue $\lambda$. In fact, $ku$ is an eigenvector for every non-zero $k$. Coming from another direction, let $u$ and $v$ be two eigenvectors for the same eigenvalue $\lambda$. Then:


$$
A(u + v) = Au + Av = \lambda u + \lambda v = \lambda(u + v)
$$


Therefore, $u + v$ is also an eigenvector of $A$ with eigenvalue of $\lambda$. From these two observations, we see that the set of all eigenvectors with eigenvalue $\lambda$, along with the zero vector, is a subspace of $\mathbb{R}^{n}$.



!!! note
    $0$ can never be an eigenvector. This is because if $A0 = \lambda 0$ then there is no fixed $\lambda$ that we can associate with $0$. Therefore, eigenvectors are non-zero vectors.



## Summary

For a matrix $A$, a non-zero $x$ is an eigenvector with eigenvalue $\lambda$ if $Ax = \lambda x$.



[^1]: The entire visual presentation has been borrowed from Grant Sanderson's videos on linear algebra. The specific example has been borrowed from this [video](https://youtu.be/PFDu9oVAE-g).

