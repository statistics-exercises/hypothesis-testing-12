import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_criticalRange(self) : 
        l = scipy.stats.norm.ppf(0.05,loc=20,scale=2 )
        lll= criticalRange( mu0, sigma )
        self.assertTrue( np.abs(l-lll)<1e-4, "your critical range function does not return the correct value") 

    def test_hypothesisTest(self) : 
        hhh = hypothesisTest( data, 4, 3 ) 
        self.assertTrue( hhh=="the null hypothesis is rejected in favour of the alternative", "the hypothesisTest function returns the wrong sentence"  )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not contain an if statement" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("there is insufficient evidence to reject the null hypothesis")>0, "The hypothesis test function does not contain the string there is insufficient evidence to reject the null hypothesis"  )
