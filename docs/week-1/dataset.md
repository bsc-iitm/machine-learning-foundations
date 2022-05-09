# Datasets

!!! question
	What is a dataset and why is it important?



## Datasets

There are different kinds of datasets. The housing dataset that we saw in the last section is tabular data. Each column is called an attribute or a feature and each row represents one record or observation. By far, this is the most common form in which data is represented. Tabular data can be neatly packed into comma-separated files or CSVs. Few other forms of data:



- image
- text
- speech



Image, text and speech data cannot be packed into simple CSVs. Courses in the degree level will discuss each of these data-formats in more detail. 



## Whence comes data?

How do we obtain data? Where does data come from? This seems like a simple question but it doesn't have a simple answer. Here are some scenarios:



!!! note "Scenario-1"
    An FMCG company has given you some historical data concerning its sales over the last three years. It wants you to predict the average sales in the coming quarter.

Here we are lucky. Someone comes to our doorstep and gives us the data. In addition, we also have a very precise definition of the problem statement. We have to predict a real number by looking at the data. It is a regression problem.



!!! note "Scenario-2"
    Twitter is developing an algorithm to detect tweets that contain offensive content. As a data scientist, you are given a dump of $1$ million tweets and asked to develop an algorithm to solve the problem.

This is a much more challenging problem. First, this is a clear instance of a classification problem. For each tweet, the prediction is going to be binary: "offensive" or "not-offensive". In order to learn a classifier, we need to know which tweets are offensive and which are not. Unfortunately, we don't have that information. If that information is absent, how can we teach the computer to differentiate between the two? So, the first task here is to get the dataset labeled. [Amazon Mechanical Turk](https://www.mturk.com/) is a common solution that companies go for when they have to label massive quantities of data. Once the dataset is labeled, the problem becomes more tractable.



!!! note "Scenario-3"
    You are a research scientist at a manufacturing company. You want to set up a facility that automates the segregation of defective products from the non-defective ones.

This is by far the most challenging scenario. We don't have access to the data. We need to *gather* data in the first place. Once we have the data, we need to label it or annotate it. Only then can we start building classifiers.



## Supervision

Labeling is an important part of the ML pipeline, especially if we want to do some prediction on top of the data. However, there may be situations where labeling is not practically feasible. In such cases, we will have to settle with unlabeled data. Therefore, datasets in ML can be classified into two categories:



- labeled dataset
- unlabeled dataset



Techniques that work with labeled data fall under the category of supervised learning. Those that work with unlabeled data come under unsupervised learning. What is so special about the term "supervised"? 



[Cambridge dictionary](https://dictionary.cambridge.org/dictionary/english/supervise) defines the verb supervise as follows:

!!! note "Supervise: Definition"
	to watch a person or activity to make certain that everything is done correctly, safely



By a slight extension of this definition, we could say that a supervisor is a teacher who tells us whether we are right or wrong. In this sense, the label performs the role of a supervisor for the machine as it is learning. With unlabeled data, there is no supervision available.



## Partitioning the dataset

As humans, how do we if know if someone has learnt a skill or not? Tests or exams are the way to go. Exams are so ubiquitous that we often conflate learning and scoring well in an exam. However, for a machine, getting a good score in an exam is a good enough proxy for learning. For almost every skill that one can think of, there is some test or exam that evaluates the performance. Take the analogy that we have been working with: three-digit addition. To know if kids have learnt addition, we conduct a test that has problems on three digit addition.

An important feature of testing is to make sure that it is challenging. If we ask the same questions that are there in the textbook, kids might score high marks. But chances are that a lot of them would have memorized the answers. Therefore, whenever we have a dataset, we always partition it into two parts:



- train-dataset
- test-dataset



We train the model on the train-dataset and evaluate its performance on the test-dataset. But often, we don't stop with two partitions, we go for three partitions:



- train-dataset
- validation-dataset
- test-dataset



Think about the validation-dataset as additional problems for practice or a mock exam that helps the machine learn a good model. The test-dataset is not shown to the model during the learning stage. The learning algorithm has access to only the train-dataset and the validation-dataset. Once the learning process is complete, the model is then evaluated on the test-dataset.
