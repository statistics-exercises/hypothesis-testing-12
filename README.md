# Hypothesis testing

This week we are going to take the ideas of hypothesis testing that were introduced in last weeks python tasks further.  Lets, therefore, start by revising what those exercises last week taught us about hypothesis testing.  If you remember we introduced the following flowchart to describe the workflow that is used to perform a hypothesis test:

![](hypo-testing.001.png)

__To complete this exercise I would like you to use this workflow to test the following__:

__null hypothesis__: `sample` is a normal random variable with expectation 20 and variance 4.
__alternative hypothesis__: `sample` is a normal random variable with an expectation that is less than 20

Your test should be performed for a __significance level__ of 5% by the function `performHypothesisTest`.  This function should return a single string that should state that _the null hypothesis is rejected_ or that _there is insufficient evidence to reject the null hypothesis_.  You will also need to complete the function `criticalRegion` which should return the size of the critical region.
