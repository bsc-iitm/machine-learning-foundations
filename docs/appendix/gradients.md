# Gradients

!!! question
	How do we compute the gradient of the expression $||X\theta - y||^2$ with respect to $\theta$?



## Setting

Let us consider the objective function in the minimzation problem for linear regression:


$$
L = ||X\theta - y||^2
$$


This can be expressed as:


$$
L = (X\theta - y)^T(X\theta - y)
$$


The gradient of $L$ with respect to $\theta$ is given by:


$$
\nabla_{\theta} L = \begin{bmatrix}
\cfrac{\partial L}{\partial \theta_1}\\
\vdots\\
\cfrac{\partial L}{\partial \theta_n}
\end{bmatrix}
$$


How do we compute this gradient? First, let us rewrite the expression by introducing an error vector, $e = X\theta - y$:


$$
L = e^Te
$$


The gradient of $L$ with respect to $\theta$ can be obtained in a two step process:

- $\nabla_e L$: first compute the gradient of $L$ with respect to the error
- Use the chain rule of differentiation to compute the gradient of $L$ with respect to $\theta$

The chain rule when multiple variables are involved can be a bit tricky. This is what will take up next.



## Chain rule for multiple variables

!!! warning
    Heavy use of algebra. Go slowly.  

Intuitively, what does $\frac{\partial L}{\partial \theta_i}$ mean? This partial derivative measures the effect on the loss $L$ when $x_i$ is perturbed a little keeping all other variables constant. This perturbation propagates to $L$ via $e$. There is a chain reaction: $\theta_1$ affects some of the variables in the vector $e$, which in turn affects $L$. To get a better feel for this, let us take an example:


$$
\begin{aligned}
e &= X\theta - y\\\\
\begin{bmatrix}
e_1\\
e_2\\
e_3
\end{bmatrix} &= \begin{bmatrix}
x_{11} & x_{12}\\
x_{21} & x_{22}\\
x_{31} & x_{32}\\
\end{bmatrix}
\begin{bmatrix}
\theta_1\\
\theta_2
\end{bmatrix} - \begin{bmatrix}
y_1\\
y_2
\end{bmatrix}\\\\
L &= e^T e = e_1^2 + e_2^2 + e_3^2
\end{aligned}
$$


The variable $\theta_1$ influences $L$ via three *independent* routes:



- $\theta_1 \rightarrow e_1 \rightarrow L$
- $\theta_1 \rightarrow e_2 \rightarrow L$
- $\theta_1 \rightarrow e_3 \rightarrow L$



The partial derivative needs to take into account the contributions from each of these three routes. Pictorially:



![](../assets/images/img_001.svg){width="1000"}



Symbolically:


$$
\cfrac{\partial L}{\partial \theta_1} = \cfrac{\partial L}{\partial e_1} \cfrac{\partial e_1}{\partial \theta_1} + \cfrac{\partial L}{\partial e_2} \cfrac{\partial e_2}{\partial \theta_1} + \cfrac{\partial L}{\partial e_3} \cfrac{\partial e_3}{\partial \theta_1}
$$


Observe that the RHS is in the form of a dot product between two vectors:


$$
\cfrac{\partial L}{\partial \theta_1} = \begin{bmatrix}
\cfrac{\partial e_1}{\partial \theta_1} & \cfrac{\partial e_2}{\partial \theta_1} & 
\cfrac{\partial e_3}{\partial \theta_1}
\end{bmatrix} \begin{bmatrix}
\cfrac{\partial L}{\partial e_1}\\
\cfrac{\partial L}{\partial e_2}\\
\cfrac{\partial L}{\partial e_3}
\end{bmatrix}
$$


Notice, that the second vector is nothing but $\nabla_e L$:


$$
\cfrac{\partial L}{\partial \theta_1} = \begin{bmatrix}
\cfrac{\partial e_1}{\partial \theta_1} & \cfrac{\partial e_2}{\partial \theta_1} & 
\cfrac{\partial e_3}{\partial \theta_1}
\end{bmatrix} \nabla_e L
$$
We can now add $\cfrac{\partial L}{\partial \theta_2}$ to the mix:



$$
\begin{aligned}
\nabla_{\theta} L &= \begin{bmatrix}
\cfrac{\partial L}{\partial \theta_1}\\
\cfrac{\partial L}{\partial \theta_2}
\end{bmatrix}\\ \\
&= \begin{bmatrix}
\cfrac{\partial e_1}{\partial \theta_1} & \cfrac{\partial e_2}{\partial \theta_1} & 
\cfrac{\partial e_3}{\partial \theta_1}\\
\cfrac{\partial e_1}{\partial \theta_2} & \cfrac{\partial e_2}{\partial \theta_2} & 
\cfrac{\partial e_3}{\partial \theta_2}
\end{bmatrix} \nabla_e L\\\\
&= J\ \nabla_e L
\end{aligned}
$$



The matrix $J$ is called the Jacobian matrix. It represents the partial derivatives of each component of the vector $e$ with respect to each component of the vector, $\theta$. That is, every element of the Jacobian is of the form:


$$
J_{ij} = \cfrac{\partial e_j}{\partial \theta_i}
$$


## Back to the gradients

Let us resume our computation, but this time with a general $m \times n$ matrix $X$, $m$ dimensional vector $y$ and $n$ dimensional vector $\theta$. Since $L = e^Te$, we have:



$$
\nabla_e L = 2 e
$$



We now need to compute the Jacobian. We have $e = X\theta - y$. Since $y$ is a constant, it will vanish while computing the derivatives. We only need to worry about $X\theta$ for which we can use the following relationship. If $x_i$ is the $i^{th}$ column of $A$, then:

$$
X\theta = \theta_1x_1 + \cdots + \theta_nx_n
$$


 The $i^{th}$ row of the Jacobian is:


$$
\begin{bmatrix}
\cfrac{\partial e_1}{\partial \theta_i} & \cdots & 
\cfrac{\partial e_m}{\partial \theta_i}
\end{bmatrix} = x_i^T
$$

As simple as that: the $i^{th}$ row of the Jacobian is just the $i^{th}$ column of $X$. So, the Jacobian is nothing but $X^T$. We now have the complete expression for $\nabla_{\theta} L$:



$$
\nabla_{\theta} L = 2 X^T (X\theta - y) = 2(X^TX \theta - X^T y)
$$



