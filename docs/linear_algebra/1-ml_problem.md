# ML problem

!!! question
	 What does a typical ML problem look like?

## Regression

### Analogy

Think about arithmetic classes in primary school. During the class hours, a student looks at solved examples in a textbook and **learns** how to solve simple three digit addition problems. Let us say that her textbook has the following problems along with the answers:

- $103 + 205 = 308$
- $123 + 409 = 532$
- $185 + 483 = 668$

The important point to note is that the student has access to both the questions and the answers. In the exam, she will not have access to the answers! But more importantly, she will not even be asked the same questions! So, just memorizing the answers will not help. She would have to learn how addition works. In other words, she would have to **learn a function** from the input (question) to the output (answer).

This is exactly what happens in a regression problem. The inputs are a set of data-points. The outputs corresponding to these inputs are real numbers called targets or **labels**. A regression model has to learn the mapping from input to output. Once this mapping or function is learnt, the model can then be used to predict the output on unseen inputs. The collection of data-points along with their targets is called a **labeled dataset**. A regression model makes use of this dataset to learn a function. A labeled dataset is nothing but the textbook problems in our analogy.

### Data Representation

We are given a collection of $m$ data-points and $m$ labels which are real numbers. Each data-point is described by $n$ features. For example, in the housing dataset, each house is a data-point and is described by features such as lattitude, longitude, area and so on. These features are clubbed together in a feature-vector of size $n$. Arranging the $m$ data-points in a matrix, we get a $m \times n$ data-matrix. Let us call this matrix $A$:


$$
A = \begin{bmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots & a_{ij} & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{bmatrix}
$$
 

The labels can be put together in a vector of size $n$. Let us call this $b$:


$$
b = \begin{bmatrix}
b_1\\
\vdots\\
b_m
\end{bmatrix}
$$


### Model

As stated earlier, a regression model is a function that transforms a data-point into a label. Formally:
$$
f: \mathbb{R}^{n} \rightarrow \mathbb{R}
$$
Each feature-vector is of size $n$. So, the feature-vectors reside in the $n$ dimensional space $\mathbb{R}^{n}$. The labels are real numbers, so they reside in $\mathbb{R}$.

!!!tip
	You can think about an ML model as a function that maps a feature-vector to a label.



### Learning

The heart of ML is learning from data. But who or what is learning? We can think of the model as the outcome of the learning process. For some regression models, once you have learnt the model, you can throw away the dataset (textbook). This is not true of all regression models though! Think about how you learnt three-digit addition. Do you still carry your primary school textbooks around? No! Your mind has a representation of what addition is. This is exactly what a model does. ML scientists have come up with a variety of models. The simplest such model is a linear model. We shall take this up in the next unit.

## Summary

Regression is a classic ML problem where we use labeled data to learn a mapping from a feature-vector to a real number. The data-points are arranged in a data-matrix called $A$. The labels are arranged in a label vector called $b$. A model is a function that transforms a feature-vector to a label.
