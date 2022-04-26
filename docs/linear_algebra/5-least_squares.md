# Ax ≈ b

!!! question
    How do we solve for $x$ in $Ax \approx b$?



## Approximation

So far we have seen the well behaved case of $Ax = b$. What if $b$ is not in the column space of $A$? Then $Ax \neq b$. This is by far the most interesting and relevant scenario from the perspective of the linear regression problem. Recall that we are trying to estimate a weight vector $x$, given the labeled dataset $(A, b)$. The relationship between inputs and outputs is assumed to be linear. But the real world doesn't behave exactly like we want it to. There are going to be obvious deviations from our ideal assumptions. In other words, our models can never be an entirely accurate representation of reality.

This is a typical scenario observed in engineering and the sciences. We don't abandon the problem because it doesn't admit an exact solution. Instead, we turn to a powerful weapon in our armoury: approximations. Can we find a $\hat{x}$ such that $A \hat{x} \approx b$? What do we mean by the symbol $\approx$ here? We are dealing with two vectors on either side of the symbol. Let us first understand what the symbol means when we have scalars.

Let us look at the following statements:

- $1.234 \approx 1$
- $1.234 \approx 1.2$
- $1.234 \approx 1.23$

These are three approximations. From experience, we know that the second approximation is better than the first, the third better than the second. If we plot these points on a real line, the goodness of an approximation can be interpreted using the distance between the original point and its approximation: smaller the distance, better the approximation.

This very idea is extended to an $n$ dimensional vector space. If $b$ and $\hat{b}$ are two vectors in $\mathbb{R}^m$, then the distance $d$ between them is a measure of the goodness of the approximation. To avoid taking square roots, we write down the expression for $d^2$:


$$
d^2 = ||\hat{b} - b||^2 = (\hat{b}_1 - b_1)^2 + \cdots + (\hat{b}_m - b_m)^2
$$


So, the key to solving the problem $Ax \approx b$, is to find a vector $\hat{x}$ such that $A\hat{x}$ is as close to $b$ as possible. This can be framed as an optimization problem:


$$
\hat{x} = \arg \min \limits_{x} ||Ax - b||^2
$$


If you are seeing $\arg \min$ for the first time, think about it like a function (in the programming sense):

- Find the value the minimizes the expression
- Return this value to the user



## Objective function

Let us go ahead and solve the minimization problem.


$$
\min \limits_{x} ||Ax - b||^2
$$


Let us call the expression to be minimized, $E$, this is also called the objective function of the optimization problem. It can be simplified as follows:


$$
\begin{align}
E &= ||Ax - b||^2\\\\
&= (Ax - b)^T(Ax - b)\\\\
\end{align}
$$



## Normal Equations

We now follow the usual procedure of finding the minima of a function. Take the derivatives and set them to zero. Since we are dealing with a multivariable function, we have to consider all the partial derivatives. The vector of such partial derivatives is called the gradient.


$$
\nabla E = \begin{bmatrix}
\cfrac{\partial E}{\partial x_1}\\
\vdots\\
\cfrac{\partial E}{\partial x_n}
\end{bmatrix}
$$


Let us now compute the gradient and set it to zero. If you want a detailed mathematical explanation of how the gradient is computed, refer to the [appendix](../appendix/0-gradients.md):



$$
\nabla E = 2(A^TA)x - 2A^Tb = 0
$$



This gives us the following equation:

$$
(A^TA) x = A^Tb
$$
This system is called the **normal equations**. If the matrix $A^TA$ is invertible, then we have the following solution:


$$
\hat{x} = (A^TA)^{-1} A^Tb
$$


We still don't know if this is corresponds to a minima. Rest assured that this is indeed a minima. But we won't take up the proof now. The other worrying part is what happens if the matrix $A^TA$ is singular or non-invertible. This is also something that we skip for the time being.



## Least Squares Problem

This is often called the least squares problem. To see why this name is used, let us revisit the objective function:


$$
E = (Ax - b)^T (Ax - b)
$$


Since $Ax$ is an approximation of $b$, $e = Ax - b$ can be seen as an error vector. So:


$$
E = e^T e = e_1^2 + \cdots + e_m^2
$$


From a ML standpoint, recall the housing dataset with which we started. $e_i$ is the difference between the actual selling price of the $i^{th}$ house and its predicted selling price as given by our linear model. In a sense, we are justified in calling $e$ the error vector. We are minimizing the sum of the squared errors, hence "least squares". $\hat{x}$ is that weight vector for the linear model which will give us the best possible fit. In the next few units, we shall try to understand the least squares problem from the lens of geometry.



## Summary

