# Script to test the psspy function for creating a  Diagram (.sld)
import pssepath
pssepath.add_pssepath()

import psspy

psspy.psseinit(50)
psspy.newcase_2([0,1], 1.0, 50.0,"","")
psspy.newdiagfile()
psspy.bus_data_4(1,0,[1,1,1,1],[0.0, 1.0,0.0, 1.1, 0.9, 1.1, 0.9],"")
psspy.bus_data_4(101,0,[1,1,1,1],[0.0, 1.0,0.0, 1.1, 0.9, 1.1, 0.9],"")
psspy.bus_data_4(201,0,[1,1,1,1],[0.0, 1.0,0.0, 1.1, 0.9, 1.1, 0.9],"")
psspy.branch_data_3(1,201,r"""1""",[1,1,1,0,0,0],[0.0, 0.0001,0.0,0.0,0.0,0.0,0.0,0.0, 1.0, 1.0, 1.0, 1.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],"")
psspy.plant_data_3(1,0,0,[ 1.0, 100.0])
psspy.machine_data_2(1,r"""1""",[1,1,0,0,0,0],[0.0,0.0, 9999.0,-9999.0, 9999.0,-9999.0, 1.0,0.0, 1.0,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
psspy.load_data_5(201,r"""1""",[1,1,1,1,1,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.bsysinit(1)
psspy.bsyso(1,101)
psspy.extr(1,0,[0,0])
psspy.savediagfile(r"""basicFeeder2.sld""")


