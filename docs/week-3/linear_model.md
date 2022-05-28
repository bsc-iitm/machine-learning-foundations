# Linear Regression

!!! question
	What is a linear regression model?



## Motivation

Let us return to the [housing dataset](../week-1/linear_algebra.md). Consider two houses, one which has an area of $1000$ square feet and the other which has an area of $2000$ square feet. As the area of the house increases, the selling price is going to go up. Take another feature, say the distance from the nearest school. If the distance increases, then the selling price goes down. Perhaps the effect may not be as drastic. If we have access to only these two features, one function or model could be as follows:
$$
\text{Selling-price} = 2 \times \text{Area} - 0.2 \times \text{Distance} + \text{Constant}
$$
This is what is called a linear model. The values $2$ and $-0.2$ are called the weights. The magnitude of a weight denotes the importance of the corresponding feature. Its sign denotes the effect it has on the output. For example, the distance feature is negatively correlated with the selling-price, but it is not as important as the area.

!!! note 
    We might be totally wrong about the choice of weights. Even worse, the relationship between the selling price and the two features may not even be linear! It is important to understand that a model is some approximation of the underlying reality. There is a nice quote that summarizes this idea: 

    !!! quote
    	All models are wrong, but some are useful.



## Vector form

Generalizing this, let us say that we have a feature vector $x$ and a weight vector $\theta$. Recall that the housing data has six features:


$$
x = \begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
x_6
\end{bmatrix}, \theta = \begin{bmatrix}
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4\\
\theta_5\\
\theta_6
\end{bmatrix}
$$


The function or model that maps a data-point to the label $y$ (selling-price) is:


$$
y = x_1 \theta_1 + x_2 \theta_2 + x_3\theta_3 + x_4 \theta_4 + x_5 \theta_5 + x_6 \theta_6 + \text{constant}
$$


We can rewrite the constant as one more weight, say $\theta_0$:


$$
y = x_1 \theta_1 + x_2 \theta_2 + x_3\theta_3 + x_4 \theta_4 + x_5 \theta_5 + x_6 \theta_6 + \theta_0
$$

Going back to the vectors, we add a feature $1$ to the feature vector and a $\theta_0$ to the weights:



$$
x = \begin{bmatrix}
1\\
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
x_6
\end{bmatrix}, \theta = \begin{bmatrix}
\theta_0\\
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4\\
\theta_5\\
\theta_6
\end{bmatrix}
$$


If we now look at the expression for $y$, it is nothing but the dot-product of the two vectors:

$$
\begin{aligned}
y &= 1\cdot \theta_0 + x_1 \theta_1 + x_2 \theta_2 + x_3\theta_3 + x_4 \theta_4 + x_5 \theta_5 + x_6 \theta_6 \\\\
&= \theta^T x
\end{aligned}
$$


$\theta^Tx$ is the dot product between the two vectors $\theta$ and $x$. This is the notation that we will be using for the dot product from now on. This is the same as the matrix-product of a row-vector and a column-vector:


$$
y = \theta^T x = \begin{bmatrix}
\theta_0 & \theta_1 & \theta_2 & \theta_3 & \theta_4 & \theta_5 & \theta_6
\end{bmatrix}\begin{bmatrix}
1\\
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
x_6
\end{bmatrix}
$$

The linear model is therefore expressed as:


$$
\boxed{\huge{f(x) = \theta^T x}}
$$


If $x$ is the feature vector of a house, then $f(x)$ will be its predicted selling price. We call $\theta$ the weights or parameters of the model.



!!! note
    All vectors will be expressed as column vectors. If we want to express a row-vector, then it will be denoted as $x^T$, where $x$ is some column-vector.



## Matrix form

So much for one house. But we have several houses. All these can be clubbed into a data-matrix. This is nothing but stacking all feature-vectors one below the other. Likewise, we can stack all selling prices into a label-vector:





$$
\begin{bmatrix}
y_{1}\\
\vdots\\
y_{100}
\end{bmatrix}= \begin{bmatrix}
1 & x_{1,1} & x_{1,2} & x_{1,3} & x_{1,4} & x_{1,5} & x_{1,6}\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
1 & x_{100,1} & x_{100,2} & x_{100,3} & x_{100,4} & x_{100,5} & x_{100,6}\\
\end{bmatrix}\begin{bmatrix}
\theta_0\\
\theta_1\\
\theta_2\\
\theta_3\\
\theta_4\\
\theta_5\\
\theta_6
\end{bmatrix}
$$


If we call the feature matrix $X$, the label vector $y$ and the weight vector $\theta$, this is the equation we have:



$$
X\theta = y
$$



We are given both $X$ and $y$. This is nothing but our labeled dataset. We have to learn $\theta$. This leaves us with two questions:



- Does the equation $X\theta = y$ have a solution?
- If it doesn't have a solution, then how do we estimate $\theta$?



We can see how an ML problem has now turned into a linear algebra problem! We will try to answer the first question and then move on to the second question. **Readers are requested to understand this equation more from a mathematical standpoint.  Please spend some time on the following point before proceeding further:**

!!! important
    In general, even if the relationship between the features and label is linear, we will always have some noise. So, $X \theta \neq y$ is what we observe in practice. However, we will still study $X \theta = y$ from a purely mathematical standpoint. A lot of details about the linear regression model have been skipped. This presentation has tried to bring out the mathematical details. What has been presented here is just a motivation for studying the system of linear equations $X \theta = y$. For a more accurate handling of this topic, please refer to weeks 2 and 3 of the MLT course.



## Summary

A linear regression model assumes a linear relationship between inputs and outputs, where the model is expressed as $f(x) = \theta^T x$. If the labeled dataset is $(X, y)$, our task is to learn the parameters $\theta$. Before going there, we shall first study the system of equations $X \theta = y$.
