# Linear Algebra for ML

!!! question
	Why should we study linear algebra in a course on data science?

## Data

The simplest answer to this question is that we choose vectors and matrices to represent data. Let us take a simple example of data coming from the housing industry. Every house in a locality has the following **features** or **attributes** associated with it:

- lattitude
- longitue
- age
- num_of_rooms
- area
- distance_from_school

A typical problem in ML is this:

> Given these attributes or features of a house, can we predict its selling price?

This is called a **regression problem**: given a set of features, map it to a real number. 



## Vectors

Let us take a concrete example of a single **data-point**:

| Attributes/Target            | Values |
| ---------------------------- | ------ |
| lattitude                    | 12.9   |
| longitude                    | 80.2   |
| age                          | 3      |
| num_of_rooms                 | 2      |
| area                         | 1000   |
| distance_from_nearest_school | 3      |
| selling_price                | 40     |



Lattitude and longitude are in degrees, age is in years, area is in square feet, distance is in kilometers, selling price is in lakhs. But none of these really matter for an ML algorithm: it is going to abstract out the details (such as units) and look at this as a column of numbers, which is nothing but a vector:


$$
\begin{bmatrix}
12.9\\
80.2\\
3\\
2\\
1000\\
3\\
\end{bmatrix}
$$


Note that the selling price is not included as an element in the vector as that is usually unkown to us. This unkown quantity which we have to estimate or **predict** is called the **target**. 

!!! note
	Vectors are usually represented as column vectors or $n \times 1$ matrices.

## Matrices

We cannot learn anything substantial from looking at the data of one house. We have to look at the data of multiple houses. That will give us an idea of the general picture. Rather than look at each vector in isolation, we can arrange them in a tablular form:



|      | lattitude | longitude | age  | rooms | area | distance | price |
| ---- | --------- | --------- | ---- | ----- | ---- | -------- | ----- |
| 1    | 12.9      | 80.2      | 3    | 2     | 1000 | 3        | 40    |
| …    | …         | …         | …    | …     | …    | …        | …     |
| 50   | 14.3      | 75.9      | 30   | 2     | 1200 | 5        | 20    |
| …    | …         | …         | …    | …     | …    | …        | …     |
| 100  | 20.8      | 90.5      | 1    | 3     | 1500 | 2        | 35    |



This data for $100$ houses is nothing but a $100 \times 6$ matrix:


$$
\begin{bmatrix}
12.9 & 80.2 & 3 & 2 & 1000 & 3\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
14.3 & 75.9 & 30 & 2 & 1200 & 5\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots\\
20.8 & 90.5 & 1 & 3 & 1500 & 2
\end{bmatrix}
$$

Each row of this matrix corresponds to one data-point. In general, if a dataset has $n$ features and $m$ data-points, it is represented as a $m \times n$ data-matrix.

!!! tip
    If you find yourself lost when working with matrices, remember that a matrix is a way to represent a collection of data-points (dataset).



## Summary

Data is represented as vectors and matrices. If we wish to extract insights from data, we need to know how to manipulate vectors and matrices. Therefore, we need to have a reasonable understanding of linear algebra — the study of vectors and matrices — if we wish to understand how ML algorithms work.

