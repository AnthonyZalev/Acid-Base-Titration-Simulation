from Solutions import Solution
import math


def DeterminePH(Titrant, Analyte):  # Titrant is solution added #Analyte is Base
    #  Update Concentrations
    PH = 0  # PH of final reaction
    EquationKa = 0;

    # Calculate new concentration of solutions when combined.
    temp = Titrant.SolutionVolume;
    Titrant.add_volume(Analyte.SolutionVolume)
    Analyte.add_volume(temp)

    # Determine if there is a KA that we need to worry about
    if not Analyte.weak_or_strong():
        EquationKa = Analyte.SolutionKA;
    elif not Titrant.weak_or_strong():
        EquationKa = Titrant.SolutionKA;
    # If KA is 0 both are strong

    if EquationKa == 0:
        return strong_titration(Titrant, Analyte);

    #  If the analyte is the limiting reactant do the following
    if (Analyte.getMoles() > 0 and Titrant.getMoles() > 0):
        # If there is more solution to be added than base solution do the following
        ConjugateConcentrations = Analyte.getSolutionMolarity()
        if Titrant.getMoles() >= Analyte.getMoles():
            ConjugateConcentrations = Analyte.getSolutionMolarity()
            Titrant.setMoles(Titrant.getMoles() - Analyte.getMoles())
            hydroniumConcentration = Titrant.getSolutionKA() * (Titrant.getSolutionMolarity() / ConjugateConcentrations)
            if not (hydroniumConcentration == 0):
                return (-1 * math.log10(hydroniumConcentration))

        elif Titrant.getMoles() < Analyte.getMoles():
            ConjugateConcentration = Titrant.getSolutionMolarity()
            Analyte.setMoles(Analyte.getMoles() - Titrant.getMoles())
            hydroniumConcentration = Analyte.getSolutionKA() * (Analyte.getSolutionMolarity() / ConjugateConcentration)
            if not (hydroniumConcentration == 0):
                return (-1 * math.log10(hydroniumConcentration))
        return 0


def strong_titration(titrant, analyte):
    #  Strong Acid Added to Strong Acid
    if titrant.is_acid() and analyte.is_acid():
        h_concentration = (titrant.calculate_moles() + analyte.calculate_moles()) / titrant.SolutionVolume;
        return -1 * math.log10(h_concentration);

    #  Strong Base Added to Strong Base
    elif (not titrant.is_acid() and not analyte.is_acid()):
        oh_concentration = (titrant.calculate_moles() + analyte.calculate_moles()) / titrant.SolutionVolume;
        return 14 - (-1 * math.log10(oh_concentration));

    elif titrant.calculate_moles() > analyte.calculate_moles():  # More Titrant than Analyte
        #  Strong Acid titrant added to Strong Base analyte
        if titrant.is_acid() and not analyte.is_acid():
            h_concentration = (titrant.calculate_moles() - analyte.calculate_moles()) / titrant.SolutionVolume;
            return -1 * math.log10(h_concentration);
        #  Strong Base titrant Added to Strong Acid analyte
        if (not titrant.is_acid() and analyte.is_acid()):
            oh_concentration = (titrant.calculate_moles() - analyte.calculate_moles()) / titrant.SolutionVolume;
            return 14 - (-1 * math.log10(oh_concentration));

    elif titrant.calculate_moles() < analyte.calculate_moles():  # More Analyte than Titrant.
        #  Strong Acid titrant added to Strong Base analyte
        if titrant.is_acid() and not analyte.is_acid():
            h_concentration = (analyte.calculate_moles() - titrant.calculate_moles()) / titrant.SolutionVolume;
            return 14 - (-1 * math.log10(h_concentration));
        #  Strong Base titrant Added to Strong Acid analyte
        if (not titrant.is_acid() and analyte.is_acid()):
            oh_concentration = (analyte.calculate_moles() - titrant.calculate_moles()) / titrant.SolutionVolume;
            return -1 * math.log10(oh_concentration);


def getCoordinatePairs(new_titrant, new_analyte, increment):
    Ml = []
    PH = []
    maximum = 0
    for x in range(0, new_titrant.SolutionVolume * 10, 1):
        AddedSolution = Solution("blah", new_titrant.SolutionKA, new_titrant.SolutionMolarity, x / 10)
        baseSolution = Solution("haha", new_analyte.SolutionKA, analytemolarity, analytevolume)
        PH.append(DeterminePH(AddedSolution, baseSolution))
        Ml.append(x / 10)
    for x in PH:
        if (x == 0):
            PH[PH.index(x)] = (PH[PH.index(x) - 1] + PH[PH.index(x) + 1]) / 2
        if not (x == None):
            if (x < 0):
                PH[PH.index(x)] = (PH[PH.index(x) - 1] + PH[PH.index(x) + 1]) / 2
    return PH, Ml
