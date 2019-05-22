from Solutions import Solution
import math

def DeterminePH(Titrant, Analyte):  #Titrant is solution added #Analyte is Base
    #  Update Concentrations
    hydroniumConcentration = 0
    temp = Titrant.getSolutionVolume()
    Titrant.addVolume(Analyte.getSolutionVolume())
    Analyte.addVolume(temp)


    PH = 0
    #  If the analyte is the limiting reactant do the following
    if(Analyte.getMoles() > 0 and Titrant.getMoles() > 0):
        if Titrant.getMoles() >= Analyte.getMoles(): #If there is more solution to be added than base solution do the following
            if(Titrant.isSolutionStrong() == True):
                Titrant.setMoles(Titrant.getMoles() - Analyte.getMoles())
                hydroniumConcentration = Titrant.getSolutionMolarity()
                if(Titrant.getSolutionKA() <= .0000001 and not(hydroniumConcentration==0)):
                    return 14 - (-1 * math.log10(hydroniumConcentration))
                elif not(hydroniumConcentration == 0):
                    return (-1 * math.log10(hydroniumConcentration))
            else:
                ConjugateConcentrations = Analyte.getSolutionMolarity()
                Titrant.setMoles(Titrant.getMoles() - Analyte.getMoles())
                hydroniumConcentration = Titrant.getSolutionKA() * (Titrant.getSolutionMolarity() / ConjugateConcentrations)
                if not(hydroniumConcentration==0):
                    return (-1 * math.log10(hydroniumConcentration))

        elif Titrant.getMoles() < Analyte.getMoles():
            if(Analyte.isSolutionStrong() == True):
                Analyte.setMoles(Analyte.getMoles() - Titrant.getMoles())
                hydroniumConcentration = Analyte.getSolutionMolarity()
                if (Analyte.getSolutionKA() <= .0000001 and not(hydroniumConcentration==0)):
                    return 14 - (-1 * math.log10(hydroniumConcentration))
                elif(not(hydroniumConcentration==0)):
                    return (-1 * math.log10(hydroniumConcentration))
            else:
                ConjugateConcentration = Titrant.getSolutionMolarity()
                Analyte.setMoles(Analyte.getMoles()-Titrant.getMoles())
                hydroniumConcentration = Analyte.getSolutionKA() * (Analyte.getSolutionMolarity() / ConjugateConcentration)
                if not(hydroniumConcentration == 0):
                    return (-1 * math.log10(hydroniumConcentration))
        return 0

def getCoordinatePairs(titrantsolution,TitrantKA,titrantmolarity,titrantvolume,analytesolution,AnalyteKA,analytemolarity,analytevolume):

    Ml = []
    PH = []
    maximum = 0
    for x in range(0,titrantvolume*10,1):
        AddedSolution = Solution("blah", TitrantKA, titrantmolarity, x/10)
        baseSolution = Solution("haha", AnalyteKA, analytemolarity, analytevolume)
        PH.append(DeterminePH(AddedSolution,baseSolution))
        Ml.append(x/10)
    for x in PH:
        if(x == 0):
            PH[PH.index(x)] = (PH[PH.index(x) - 1] + PH[PH.index(x) +1])/2
        if not(x == None):
            if (x < 0):
                PH[PH.index(x)] = (PH[PH.index(x) - 1] + PH[PH.index(x) + 1]) / 2
    return PH, Ml



