# Script to test a basic integration with PSSE 34 nad python 2.7
import pssepath
pssepath.add_pssepath()

import psspy

#--------------------------------
# PSS/E Saved case

CASE = r"C:\Program Files (x86)\PTI\PSSEXplore34\EXAMPLE\savnw.sav"

if __name__ == '__main__':
    psspy.psseinit(2000)
    psspy.case(CASE)
    psspy.fnsl(
        options1=0, # disable tap stepping adjustment.
        options5=0, # disable switched shunt adjustment.
    )
