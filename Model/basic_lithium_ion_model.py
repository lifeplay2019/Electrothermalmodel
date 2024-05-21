##
# the basic lithium ion battery model -chemistry
##

import pybamm

class BaseModel(pybamm.BaseBatteryModel):

    def __init__(self, options=None, name = "Unnamed lithium ion battery", build = False):
        super().__init__(options,name)
        self.param = pybamm.LithiumIonParameter(self.option)



