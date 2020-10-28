import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) :
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      self.assertTrue( len(this_x)==200, "you have not drawn the correct number of points in your graph" )
      for i in range( len(this_x) ) :
          self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x coordinates in your plot are incorrect" )
          bar = np.sqrt(1/12/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
          self.assertTrue( np.fabs( this_y[i] - 0.5 )<bar, "the y-coordinates in your plot appear to be sampled from the wrong distribution" )
