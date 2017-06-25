[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> import numpy
import thinkstats2
rand_nums = numpy.random.random(1000)
pmf = thinkstats2.Pmf(rand_nums, label = 'random numbers')
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='rand_nums', ylabel='PMF')
cdf = thinkstats2.Cdf(rand_nums, label = 'random numbers')
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='random numbers', ylabel='CDF')