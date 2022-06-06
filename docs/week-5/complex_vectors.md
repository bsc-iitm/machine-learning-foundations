# Complex vector

## Definition

Complex vector $C^n$ is equivalent of $R^n$ in real numbers space.

​                            ${C^n}^T=\begin{bmatrix}c_1&c_2&\cdots & c_{n-1}&c_n\end{bmatrix}$

where $c_i, i\in [1,n]$ is a complex number.  A complex vector just like real vector  is a $n$ dimensional vector but with complex numbers instead of real numbers.

Linear combination of $n$ complex vectors is just like combination of $n$ real vectors.

$c_1x_1+C_2x_2+\cdots+c_{n-1}x_{n-1}+c_nx_n, x_i \in C^n, 1\leq i \leq n$

## Properties

* Addition of two complex vectors works just like addition of complex numbers $C_1+C_2=\begin{bmatrix}c_{11} & c_{12}\cdots c_{1n} \end{bmatrix}^T+\begin{bmatrix}c_{21} & c_{22}\cdots c_{2n} \end{bmatrix}^T=\begin{bmatrix}c_{11}+c_{21} & c_{12}+c_{22}\cdots c_{1n}+c_{2n} \end{bmatrix}^T$
* Conjugate of complex vector $C_1=\begin{bmatrix}c_{1} & c_{2}\cdots c_{n} \end{bmatrix}^T $ is denoted as $\bar{C_1}=\begin{bmatrix}\bar{c_{1}} & \bar{c_{2}}\cdots \bar{c_{n}} \end{bmatrix}^T$
* Conjugate transpose of a complex vector is conjugate of the transpose or transpose of the conjugate complex vector.  Complex conjugate is denoted by $C^*$ and it is equal to $\bar{C^T}$.

##### Inner product of complex vectors. 

Inner product of two complex vectors is analogous to dot product of two vectors. 

​                                                                        $x.y=x^*y$

​                                                                        $x.y=\bar{x^T}y$

​                                                                      $x.y$ = $\bar{x^T}y= \begin{bmatrix}\bar{x_1} &\bar{x_2}\cdots \bar{x_n}\end{bmatrix}\begin{bmatrix}y_1 \\x_2\\. \\.\\. \\x_n\end{bmatrix}$

​                                                                     $x.y= \bar{x_1}y_1+\bar{x_2}y_2+\cdots+\bar{x_n}y_n=\sum_{i=1}^{i=n}\bar{x_i}y_i$

​                                                                        $y.x=\bar{y^T}x$

We can easily see that $y.x=\bar{x.y}$

Proof:    $\bar{x.y}=\sum_{i=1}^{i=n}\bar{\bar{x_i}y_i}=\sum_{i=1}^{i=n}{x_i}\bar{y_i}=y.x$

Length of complex vectors is inner product of complex vector to itself. $||x||^2=x.x=x^*x$

Length of real vector is $x^Tx$ but it is $\bar{x^T}x$ in complex vector case, the reason behind is that if we have taken naïve $x^Tx$ for complex vector, the length of vector could come out as zero which basically means it does not depict the length of complex vector.

Length of complex vector can be zero only if it is a zero vector, that all the values in vector are zero.



#### Hermitian matrices:

A matrix is said to be hermitian matrix if $A^*=A$, this is analogous to symmetric matrix in real numbers case. In fact, symmetric matrices is a real world case of hermitian matrices.









