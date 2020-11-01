import numpy as np
import scipy.stats

def criticalRange( mu, sigma ) : 
  # Your code to calculate the critical region should go here
  
  return lower
  
def hypothesisTest( data, mu, sigma ) : 
  l = criticalRange( mu, sigma )
  # You need to use the l value that is returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  

# You should not need to adjust anything from here onwards
mu0, sigma, sample = 20, 2, 16.704
print( hypothesisTest( sample, mu0, sigma ) )

