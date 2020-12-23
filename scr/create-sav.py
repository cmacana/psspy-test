# Script to test the psspy function for creating a  Saved Case File (.sav)
import pssepath
pssepath.add_pssepath()

import psspy
psspy.psseinit(50)
psspy.newcase_2(options=[0,0], basemva=100.0, basefreq=50.0,titl1="",titl2="")
psspy.bus_data_4(ibus=1, inode=0, name="bus1")
psspy.load_data_5(ibus=1, id="l1")
psspy.save("basic_case.sav")
