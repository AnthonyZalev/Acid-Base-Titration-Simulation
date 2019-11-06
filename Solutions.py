import math;


class Solution:


    def __init__(self, name, ka, molarity, volume, charge):
        #  Initialize the solution instance
        self.SolutionCharge = charge;
        self.SolutionName = name
        self.SolutionKA = ka;
        self.SolutionMolarity = float(molarity)
        self.SolutionVolume = float(volume)  # In liter's

    def calculate_moles(self):
        return self.SolutionMolarity * self.SolutionVolume;

    def change_moles(self, delta_moles):
        current_moles = self.SolutionMolarity * self.SolutionVolume;
        current_moles += delta_moles;
        self.SolutionMolarity = current_moles / self.SolutionVolume

    def add_volume_dilute(self, added_volume):  # Assumes water added
        temp_moles = self.calculate_moles();
        self.SolutionVolume += added_volume  # get new volume
        self.SolutionMolarity = (temp_moles / (self.SolutionVolume))  # update molarity

    def is_acid(self):
        if (-1 * math.log10(self.SolutionKA)) < 7:
            return True;
        else:
            return False;

    def weak_or_strong(self):
        if self.SolutionKA <= 1 * math.pow(10, - 14) or self.SolutionKA == 1:
            return True
        else:
            return False

    def get_solution_molarity(self):
        return self.SolutionMolarity;