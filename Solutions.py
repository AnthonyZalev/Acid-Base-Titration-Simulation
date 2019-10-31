from math import log10


class Solution:

    def __init__(self, name, ka, molarity, volume):
        #  Initialize the solution instance
        self.SolutionName = name
        self.SolutionKA = ka;
        self.SolutionMolarity = float(molarity)
        self.SolutionVolume = float(volume)  # In liter's

    def calculate_moles(self):
        return self.SolutionMolarity * (self.SolutionVolume * .001);

    def add_volume(self, added_volume):  # Assumes water added
        self.SolutionVolume += added_volume  # get new volume
        self.SolutionMolarity = (self.calculate_moles() / (self.SolutionVolume * .001))  # update molarity

    def weak_or_strong(self):
        if -1 * log10(self.SolutionKA) >= 12 or -1 * log10(self.SolutionKA) <= 2:
            return True
        else:
            return False
