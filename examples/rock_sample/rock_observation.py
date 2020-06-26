from __future__ import print_function
#from builtins import str
from pomdpy.discrete_pomdp import DiscreteObservation


class RockObservation(DiscreteObservation):
    """
    Default behavior is for the rock observation to say that the rock is empty
    """
    def __init__(self, is_good=False, is_empty=None, \
            is_falsified=False, is_deceived=False):
        super(RockObservation, self).__init__(0 if is_empty else (2, 1)[is_good])
        self.is_empty = (True, is_empty)[is_empty is not None]
        self.is_good = is_good
        self.is_falsified = is_falsified
        self.is_deceived = is_deceived

    def distance_to(self, other_rock_observation):
        return abs(self.is_good - other_rock_observation.is_good)

    def copy(self):
        return RockObservation(self.is_good, self.is_empty, \
            self.is_falsified, self.is_deceived)

    def __eq__(self, other_rock_observation):
        return self.is_good == other_rock_observation.is_good

    def __hash__(self):
        return (False, True)[self.is_good]

    def get_suffix(self):
        suffix = ""
        if self.is_falsified:
            suffix = suffix + "-F!"
        if self.is_deceived:
            suffix = suffix + "-D!"
        return suffix


    def print_observation(self):
        suffix = self.get_suffix()
        
        if self.is_empty:
            print("EMPTY"+suffix)
        elif self.is_good:
            print("Good"+suffix)
        elif not self.is_good:
            print("Bad"+suffix)
        else:
            print("Weird-"+str(self.is_good)+suffix)


    def to_string(self):
        suffix = self.get_suffix()

        if self.is_empty:
            obs = "EMPTY"
        elif self.is_good:
            obs = "Good"
        elif not self.is_good:
            obs = "Bad"
        else:
            obs = "Weird-"+str(self.is_good)

        return obs+suffix
