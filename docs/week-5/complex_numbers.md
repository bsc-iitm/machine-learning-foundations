# Complex numbers

Until now we have used real numbers. We will turn our attention to complex numbers and use them to understand different concepts. A complex number can be considered as an extension of real numbers. A complex number has real and imaginary part and is represented as:
$$
c = a + ib, \quad i = \sqrt{-1}
$$


## Complex Plane

We can represent the complex number $a + ib$ in a two dimensional plane as follows: 

- Real value $a$ is represented in $x$-axis. 
- Imaginary value $b$ in $y$-axis.

This is called the complex plane, also called the Argand plane. Every complex number can therefore be associated with a point in the complex plane. In this case:
$$
a + ib \equiv (a, b)
$$
For example, the point $(3, 2)$ is the complex number $3 + 2i$ which can be represented as:



![](../assets/images/img_009.svg){width="1000"}



Note that all real numbers can also be considered as complex numbers with $b=0$, thereby all real numbers fall on the $x$-axis. The length of a complex number $(a, b)$ can be considered as the length of the line joining the origin and the complex number:
$$
||x||^2=a^2+b^2
$$
Complex number can also be represented using the angle $\theta$ with respect to positive $x$-axis and length $r$.
$$
c=re^{i\theta}=r({cos\theta + i sin\theta})
$$
Graphically, we can represent this as follows:

![](../assets/images/img_010.svg){width=1000}

## Properties

Some basic operations and properties on complex numbers.

### Addition

If $c_1= a_1+ib_1$ and $c_2=a_2+ib_2$, then:
$$
c_1+c_2= (a_1+a_2)+i(b_1+b_2)
$$

### Multiplication

Multiplication of complex numbers works just like multiplication of real numbers, just note that $i=\sqrt{-1}$ and do multiplication using distributive property. Then:
$$
\begin{aligned}
c_1 c_2 &= (a_1+ib_1)(a_2+ib_2)\\\\ 
&= (a_1a_2-b_1b_2) +i(a_1b_2+a_2b_1)
\end{aligned}
$$

### Complex conjugate

The complex conjugate of $c = a + ib$ is given by:
$$
\bar{c} = a - ib
$$
We have the following property:
$$
\begin{aligned}
c \bar{c} &= (a + ib)(a - ib)\\\\
&= a^2 + b^2\\\\
&= ||c||^2
\end{aligned}
$$


If we look at it in another way:
$$
\begin{aligned}
\bar{c} &= r(\cos \theta - i \sin \theta)\\\\
&= re^{-i\theta}
\end{aligned}
$$




