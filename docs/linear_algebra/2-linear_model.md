# Linear Regression

!!! question
	What is a linear regression model?



## Motivation

Let us return to the housing dataset. Consider two houses, one which has $1000$ square feet and the other which has $2000$ square feet. As the area of the house increases, the selling price is going to go up. Take another feature, say the distance from the nearest school. If the distance increases, then the selling price goes down. Perhaps the effect may not be as drastic. If we have access to only these two features, one function or model could be as follows:
$$
\text{Selling-price} = 2 \times \text{Area} - 0.2 \times \text{Distance} + \text{Constant}
$$
This is what is called a linear model. The values $2$ and $-0.2$ are called the weights. The magnitude of a weight denotes the importance of the corresponding feature. Its sign denotes the effect it has on the output. For example, the distance feature has an adverse effect on the selling-price, but is not as important as the area. 

!!! note 
    We might be totally wrong about the choice of weights. Even worse, the relationship between the selling price and the two features may not even be linear! It is important to understand that a model is some approximation of the underlying reality. There is a nice quote that summarizes this idea: 

    !!! quote
    	All models are wrong, but some are useful.



## Vector form

Generalizing this, let us say that we have a feature vector $f$ and a weight vector $w$. Recall that the housing data has six features:


$$
f = \begin{bmatrix}
f_1\\
f_2\\
f_3\\
f_4\\
f_5\\
f_6
\end{bmatrix}, w = \begin{bmatrix}
w_1\\
w_2\\
w_3\\
w_4\\
w_5\\
w_6
\end{bmatrix}
$$


The function or model that maps a data-point to the label $b$ (selling-price) is:


$$
b = f_1w_1 + f_2w_2 + f_3w_3 + f_4w_4 + f_5w_5 + f_6w_6 + \text{constant}
$$


We can rewrite the constant as one more weight, say $w_0$:


$$
b = f_1w_1 + f_2w_2 + f_3w_3 + f_4w_4 + f_5w_5 + f_6w_6 + w_0
$$

Going back to the vectors, we add a feature $1$ to the feature vector and a $w_0$ to the weights:



$$
f = \begin{bmatrix}
1\\
f_1\\
f_2\\
f_3\\
f_4\\
f_5\\
f_6
\end{bmatrix}, w = \begin{bmatrix}
w_0\\
w_1\\
w_2\\
w_3\\
w_4\\
w_5\\
w_6
\end{bmatrix}
$$


If we now look at the expression for $b$, it is nothing but the dot-product of the two vectors:

$$
\begin{aligned}
b &= 1 \cdot w_0 + f_1w_1 + f_2w_2 + f_3w_3 + f_4w_4 + f_5w_5 + f_6w_6\\
&= f. w\\
\end{aligned}
$$


The dot-product can also be written as a $f^Tw$. The matrix-product of a row-vector and a column-vector:


$$
b = f^T w = \begin{bmatrix}
1 & f_1 & f_2 & f_3 & f_4 &  f_5 & f_6
\end{bmatrix}\begin{bmatrix}
w_0\\
w_1\\
w_2\\
w_3\\
w_4\\
w_5\\
w_6
\end{bmatrix}
$$

!!! note
    All vectors will be expressed as column vectors. If we want to express a row-vector, then it will be denoted as $x^T$, where $x$ is some column-vector.

 

## Matrix form

So much for one house. But we have several houses. All these can be clubbed into a data-matrix. This is nothing but stacking all feature-vectors one below the other. Likewise, we can stack all selling prices into a label-vector:





$$
\begin{bmatrix}
b_{1}\\
\vdots\\
b_{100}
\end{bmatrix}= \begin{bmatrix}
1 & f_{1,1} & f_{1,2} & f_{1,3} & f_{1,4} & f_{1,5} & f_{1,6}\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
1 & f_{100,1} & f_{100,2} & f_{100,3} & f_{100,4} & f_{100,5} & f_{100,6}\\
\end{bmatrix}\begin{bmatrix}
w_0\\
w_1\\
w_2\\
w_3\\
w_5\\
w_6
\end{bmatrix}
$$


If we call the feature matrix $A$, the label vector $b$ and the weight vector $w$, this is the equation we have:



$$
Ax = b
$$



We are given both $A$ and $b$. This is nothing but our labeled dataset. We have to find $x$. This leaves us with two questions:



- Does the equation $Ax = b$ have a solution?
- If it doesn't have a solution, then how do we estimate $x$?



We can see how a ML problem has now turned into a linear algebra problem! We will try to answer the first question and then move on to the second question.

!!! Note
    A lot of details about the linear regression model have been skipped. This presentation has tried to bring out the mathematical details. For a more accurate handling of this topic, please refer to week-2 of the MLT course. 



## Summary

A linear regression model assumes a linear relationship between inputs and outputs. This results in a system of linear equation of the form $Ax = b$.
