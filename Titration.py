from Solutions import Solution
from pHcalc.pHcalc import Acid, Neutral, System


def DeterminePH(titrant, analyte):  # Titrant is solution added #Analyte is Base

    solution_volume = titrant.SolutionVolume + analyte.SolutionVolume
    t_concentration = titrant.calculate_moles() / solution_volume
    a_concentration = analyte.calculate_moles() / solution_volume

    # Initialize titrant in system
    if titrant.SolutionKA is None:  # Strong Solution
        system_titrant = Neutral(charge=titrant.SolutionCharge, conc=t_concentration)
    else:
        system_titrant = Acid(Ka=titrant.SolutionKA, charge=titrant.SolutionCharge, conc=t_concentration)

    # Initialize analyte in system
    if analyte.SolutionKA is None:
        system_analyte = Neutral(charge=analyte.SolutionCharge, conc=a_concentration)
    else:
        system_analyte = Acid(Ka=analyte.SolutionKA, charge=analyte.SolutionCharge, conc=a_concentration)

    system = System(system_titrant, system_analyte);
    system.pHsolve();

    return system.pH;


def getCoordinatePairs(new_titrant, new_analyte):
    ml_X = []
    pH_Y = []
    for x in range(0, int(new_titrant.SolutionVolume * 10000)):
        titrant = Solution("titrant", new_titrant.SolutionKA, new_titrant.SolutionMolarity,
                           float(x) / 10000, new_titrant.SolutionCharge)
        pH_Y.append(DeterminePH(titrant, new_analyte));
        ml_X.append(float(x) / 10000)

    return pH_Y, ml_X
