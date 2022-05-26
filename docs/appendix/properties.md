# Some properties

Let us look at some properties of the matrix $X^TX$. First, if $X$ is an $m \times n$ matrix, then $X^TX$ is an $n \times n$ square matrix.

## Symmetric

!!! note "Property-1"
	$X^TX$ is symmetric.

To see why:


$$
(X^TX)^T = X^T(X^T)^T=X^TX
$$



## Nullspace

!!! note "Property-2"
	$X$ and $X^TX$ have the same nullspace.

To see why, let us take this in two steps:



If $\theta \in N(X)$, then:


$$
\begin{aligned}
X \theta &= 0\\\\
X^TX \theta &= 0\\\\
\end{aligned}
$$
So, $\theta \in N(X^TX$). Going the other way, if $\theta \in N(X^TX)$, then:


$$
\begin{aligned}
X^TX \theta &= 0\\\\
\theta^T X^TX \theta &= 0\\\\
(X \theta)^T (X \theta) &= 0\\\\
X \theta &= 0
\end{aligned}
$$


So, $\theta \in N(X)$.



## Invertibility

!!! note "Property-3"
	If $\text{rank}(X) = n$, then $X^TX$ is invertible.

To see why, note that if $\text{rank}(X) = n$, then the nullity of $X$ is zero. Since $X$ and $X^TX$ have the same nullspace, nullity of $X^TX$ is also zero. From this it follows that the rank of $X^TX$ is $n$. Since this is a full rank matrix, $X^TX$ is invertible.

