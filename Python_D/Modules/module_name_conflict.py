from mathcalc import *
from calcMath import *


add(10,20) # Most recent module will be used , S its used calcMath

import mathcalc
import calcMath

mathcalc.add(10,20)
calcMath.add(30,40)


from mathcalc import add as a1
from calcMath import add as a2

a1(10,20)
a2(20,30)