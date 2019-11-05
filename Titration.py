from Solutions import Solution
from pHcalc.pHcalc import Acid, Neutral, System
import numpy as np
import math;

def DeterminePH(Titrant, Analyte):  # Titrant is solution added #Analyte is Base

    solution_volume = Titrant.SolutionVolume + Analyte.SolutionVolume
    t_conc = Titrant.calculate_moles() / solution_volume;
    a_conc = Analyte.calculate_moles() / solution_volume;
    titrant = Acid(Ka = Titrant.SolutionKA, charge = Titrant.SolutionCharge, conc = t_conc)
    analyte = Acid(Ka = Analyte.SolutionKA, charge = Analyte.SolutionCharge, conc = a_conc)

    system = System(titrant,analyte);
    system.pHsolve();

    return system.pH;

def getCoordinatePairs(new_titrant, new_analyte):
    Ml_X = []
    PH_Y = []
    for x in range(0, int(new_titrant.SolutionVolume * 1000)):
        titrant = Solution("titrant", new_titrant.SolutionKA, new_titrant.SolutionMolarity, float(x)/1000)
        PH_Y.append(DeterminePH(titrant, new_analyte));
        Ml_X.append(float(x) / 1000)

    return PH_Y, Ml_X
