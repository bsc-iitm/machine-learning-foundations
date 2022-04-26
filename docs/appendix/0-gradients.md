# Gradients

!!! question
	How do we compute the gradient of the expression $||Ax - b||^2$ with respect to $x$?



## Setting

Let us consider the objective function in the minimzation problem for linear regression:


$$
E = ||Ax - b||^2
$$


This can be expressed as:


$$
E = (Ax - b)^T(Ax - b)
$$


The gradient of $E$ with respect to $x$ is given by:


$$
\nabla_{x} E = \begin{bmatrix}
\cfrac{\partial E}{\partial x_1}\\
\vdots\\
\cfrac{\partial E}{\partial x_n}
\end{bmatrix}
$$


How do we compute this gradient? First, let us rewrite the expression by introducing an error vector, $e = Ax - b$:


$$
E = e^Te
$$


The gradient of $E$ with respect to $x$ can be obtained in a two step process:

- $\nabla_e E$: first compute the gradient of $E$ with respect to the error
- Use the chain rule of differentiation to compute the gradient of $E$ with respect to $x$

The chain rule when multiple variables are involved can be a bit tricky. This is what will take up next.



## Chain rule for multiple variables

!!! warning
    Heavy use of algebra. Go slowly.  

Intuitively, what does $\frac{\partial E}{\partial x_i}$ mean? This partial derivative measures the effect on the variable $E$ when $x_i$ is perturbed a little keeping all other variables constant. This perturbation propagates to $E$ via $e$. There is a chain reaction: $x_1$ affects some of the variables in the vector $e$, which in turn affects $E$. To get a better feel for this, let us take an example:


$$
\begin{aligned}
e &= Ax - b\\\\
\begin{bmatrix}
e_1\\
e_2\\
e_3
\end{bmatrix} &= \begin{bmatrix}
a_{11} & a_{12}\\
a_{21} & a_{12}\\
a_{11} & a_{12}\\
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2
\end{bmatrix} - \begin{bmatrix}
b_1\\
b_2
\end{bmatrix}\\\\
E &= e^T e = e_1^2 + e_2^2 + e_3^2
\end{aligned}
$$


The variable $x_1$ influences $E$ via three *independent* routes:



- $x_1 \rightarrow e_1 \rightarrow E$
- $x_1 \rightarrow e_2 \rightarrow E$
- $x_1 \rightarrow e_3 \rightarrow E$



The partial derivative needs to take into account the contributions from each of these three routes. Pictorially:



![](../assets/images/img_001.svg){width="1000"}



Symbolically:


$$
\cfrac{\partial E}{\partial x_1} = \cfrac{\partial E}{\partial e_1} \cfrac{\partial e_1}{\partial x_1} + \cfrac{\partial E}{\partial e_2} \cfrac{\partial e_2}{\partial x_1} + \cfrac{\partial E}{\partial e_3} \cfrac{\partial e_3}{\partial x_1}
$$


Observe that that the RHS is in the form of a dot product between two vectors:


$$
\cfrac{\partial E}{\partial x_1} = \begin{bmatrix}
\cfrac{\partial e_1}{\partial x_1} & \cfrac{\partial e_2}{\partial x_1} & 
\cfrac{\partial e_3}{\partial x_1}
\end{bmatrix} \begin{bmatrix}
\cfrac{\partial E}{\partial e_1}\\
\cfrac{\partial E}{\partial e_2}\\
\cfrac{\partial E}{\partial e_3}
\end{bmatrix}
$$


Notice, that the second vector is nothing but $\nabla_e E$:


$$
\cfrac{\partial E}{\partial x_1} = \begin{bmatrix}
\cfrac{\partial e_1}{\partial x_1} & \cfrac{\partial e_2}{\partial x_1} & 
\cfrac{\partial e_3}{\partial x_1}
\end{bmatrix} \nabla_e E
$$
We can now add $\cfrac{\partial E}{\partial x_2}$ to the mix:


$$
\begin{aligned}
\nabla_x E &= \begin{bmatrix}
\cfrac{\partial E}{\partial x_1}\\
\cfrac{\partial E}{\partial x_2}
\end{bmatrix}\\ \\
&= \begin{bmatrix}
\cfrac{\partial e_1}{\partial x_1} & \cfrac{\partial e_2}{\partial x_1} & 
\cfrac{\partial e_3}{\partial x_1}\\
\cfrac{\partial e_1}{\partial x_2} & \cfrac{\partial e_2}{\partial x_2} & 
\cfrac{\partial e_3}{\partial x_3}
\end{bmatrix} \nabla_e E\\\\
&= J\ \nabla_e E
\end{aligned}
$$


The matrix $J$ is called the Jacobian matrix. It represents the partial derivatives of each component of the vector $e$ with respect to each component of the vector, $x$. That is, every element of the Jacobian is of the form:


$$
J_{ij} = \cfrac{\partial e_j}{\partial x_i}
$$


## Back to the gradients

Let us resume our computation, but this time with a general $m \times n$ matrix $A$, $m$ dimensional vector $b$ and $n$ dimensional vector $x$:


$$
\nabla_e E = 2 e
$$


We now need to compute the Jacobian. We have $e = Ax - b$. Since $b$ is a constant, it will vanish while computing the derivatives. We only need to worry about $Ax$ for which we can use the following relationship. If $a_i$ is the $i^{th}$ column of $A$, then:


$$
Ax = x_1 a_1 + \cdots + x_n a_n
$$


 The $i^{th}$ row of the Jacobian is:


$$
\begin{bmatrix}
\cfrac{\partial e_1}{\partial x_i} & \cdots & 
\cfrac{\partial e_m}{\partial x_i}
\end{bmatrix} = a_i^T
$$


As simple as that: the $i^{th}$ row of the Jacobian is just the $i^{th}$ column of $A$. So, the Jacobian is nothing but $A^T$. We now have the complete expression for $\nabla_x E$:


$$
\nabla_x E = 2 A^T (Ax - b) = 2(A^TA x - A^T b)
$$



