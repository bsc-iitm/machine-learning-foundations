# Fibonacci

## Matrix form

We all know the Fibonacci sequence:


$$
0, 1, 1, 2, 3, 5, 8, \cdots
$$


Is there a closed form expression for the $n^{th}$ term in the Fibonacci sequence? In simpler terms, is there a formula that will give us the $n^{th}$ term? Let us try to use linear algebra to answer this question. $F_k$ is the $k^{th}$ term in the sequence. Then we have the following pair of equations:


$$
\begin{aligned}
F_{k + 2} &= 1 \cdot F_{k + 1} + 1 \cdot F_{k}\\
F_{k + 1} &= 1 \cdot F_{k + 1} + 0 \cdot F_k
\end{aligned}
$$


This can be represented as the following matrix equation:


$$
\begin{bmatrix}
F_{k + 2}\\
F_{k + 1}
\end{bmatrix} = 
\begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix} 
\begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


If we use the variables:


$$
A = \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}, u_k = \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}
$$


We can restate the equation as:


$$
u_{k + 1} = A u_{k}
$$


First, we start with $u_0$:


$$
u_0 = \begin{bmatrix}
1\\
0
\end{bmatrix}
$$


Then, the next set of terms can be obtained by pre-multiplying this equation by $A$:


$$
\begin{aligned}
u_1 &= Au_0\\\\
&= \begin{bmatrix}
1 & 1\\
1 & 0
\end{bmatrix}\begin{bmatrix}
1\\
0
\end{bmatrix}\\\\
&= \begin{bmatrix}
1\\
1
\end{bmatrix}
\end{aligned}
$$


And then $u_2$:


$$
\begin{aligned}
u_2 &= Au_1\\\\
&= A^2u_0\\\\
&= \begin{bmatrix}
2\\
1
\end{bmatrix}
\end{aligned}
$$


Generalizing this, we have:


$$
u_k = A^k u_0
$$



## Diagonalization

In the section on diagonalization, we have seen some useful properties of a diagonalizable matrix. If $A$ is diagonalizable, then $A^k$ can be computed quite easily. Is $A$ diagonalizable? Let us find out. First, we need to get hold of the eigenvalues of $A$:


$$
\begin{aligned}
\begin{vmatrix}
1 - \lambda & 1\\
1 & -\lambda
\end{vmatrix} &= 0\\\\\\
(1 - \lambda)(-\lambda) - 1 &= 0\\\\\\
\lambda^2 - \lambda - 1 &= 0\\\\\\
\lambda &= \cfrac{1 \pm \sqrt{5}}{2}
\end{aligned}
$$

We see that the eigenvalues are:



$$
\lambda_1 = \cfrac{1 - \sqrt{5}}{2}, \lambda_2 = \cfrac{1 + \sqrt{5}}{2}
$$



Since, we have two distinct eigenvalues for a $2 \times 2$ matrix, the matrix should have $2$ linearly independent eigenvectors, hence it is diagonalizable. Next we move to eigenvectors. If $\lambda$ is one of the two eigenvalues, then:



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



From this, we get two linearly independent eigenvectors corresponding to $\lambda_1$ and $\lambda_2$ respectively:



$$
\begin{bmatrix}
\lambda_1\\
1
\end{bmatrix}, \begin{bmatrix}
\lambda_2\\
1
\end{bmatrix}
$$



We let:



$$
Q = \begin{bmatrix}
\lambda_1 & \lambda_2\\ 
1 & 1
\end{bmatrix}, D = \begin{bmatrix}
\lambda_1 & 0\\
0 & \lambda_2
\end{bmatrix}
$$



Then:



$$
A = QDQ^{-1}
$$



Using Gaussian elimination, we can compute $Q^{-1}$ to be:



$$
Q^{-1} = \cfrac{1}{\lambda_1 - \lambda_2}\begin{bmatrix}
1 & -\lambda_2\\
-1 & \lambda_1
\end{bmatrix}
$$



## The Formula

The $k^{th}$ term of the Fibonacci sequence is:



$$
u_k = A^k u_0
$$



This translates to:



$$
\begin{aligned}
u_k &= (QDQ^{-1})^k u_0\\\\
&= Q D^k Q^{-1} u_0
\end{aligned}
$$



All the quantities on the RHS are known. Let us just plug them in:


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

Recall that $u_k = \begin{bmatrix}
F_{k + 1}\\
F_{k}
\end{bmatrix}$. Therefore, we have:

$$
F_k = \cfrac{1}{\lambda_1 - \lambda_2} \left(\lambda_1^k - \lambda_2^k \right)
$$


Substituting for $\lambda_1$ and $\lambda_2$:


$$
\boxed{F_k = \cfrac{1}{\sqrt{5}} \left[  \left(\cfrac{1 + \sqrt{5}}{2} \right)^k - \left(\cfrac{1 - \sqrt{5}}{2} \right)^k \right]}
$$


Isn't that a thing of beauty? Can you imagine that expression on the RHS being an integer for every value of $k$?





