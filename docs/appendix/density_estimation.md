# Density Estimation

Let us say that we have a dataset given to us:

$$
D = \{x_1, \cdots, x_n\}
$$

We don't have access to the labels corresponding to these data points. What do we do in this case? One approach is to try and understand the data using probabilistic methods. The basic question we ask is this:

!!! question
	How is this dataset generated? 

We could think of some underlying probability distribution that is generating this data. In other words, there is some probability distribution from which this data is sampled. Let us call the density of probability distribution $P(x)$ and its parameters $\theta$. In this case, the likelihood of observing this data is:
$$
L(\theta\ |\ D) = P(x_1) \cdots P(x_n)
$$

One important assumption here is that the data-points are independently and identically distributed — **i.i.d**. This is what lets us use the same density for all the points and also express the likelihood as a product of the densities. Once we have this, we need to maximize the likelihood:

$$
\max L(\theta\ |\ D)
$$

 As probabilities are small numbers, it is easier to work with log probabilities:

$$
\max \log (L(\theta\ | \ D))
$$

Rather than maximizing the log likelihood, we choose to minimize the negative log likelihood:

$$
\min -\log(L(\theta\ |\ D))
$$

Expanding this out, we get:

$$
\min \sum \limits_{i = 1}^{n} -\log P(x_{i})
$$

The arguments of the optimization problem are the parameters of the probability distribution — $\theta$ — that we choose to model the data. For example, if we choose a Gaussian distribution, then the parameters would be the mean and the variance.