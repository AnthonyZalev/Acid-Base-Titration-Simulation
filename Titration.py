from Solutions import Solution
from math import log10


# Titrant = Solution(input("Enter Name\n"),input("Enter KA\n"),input("Enter Molarity\n"),input("Enter Volume\n"))
# Analyte = Solution(input("Enter Name\n"),input("Enter KA\n"),input("Enter Molarity\n"),input("Enter Volume\n"))

Titrant = Solution("Acid", .000018, .1, .05)
Analyte = Solution("Base", .00000000000000000001, .1, .049)


def DeterminePH(Titrant, Analyte):
   #  Update Concentrations
   Titrant.addVolume(Analyte.getSolutionVolume())
   Analyte.addVolume(Titrant.getSolutionVolume())
   PH = 0
   #  If the analyte is the limiting reactant do the following
   if Titrant.getMoles() > Analyte.getMoles():
       hydroniumConcentration = AnalyteIsLimiting(Analyte, Titrant)
       if(Titrant.getSolutionKA() < (1 * 10**-7)):
           PH = 14 - (-1 * log10(hydroniumConcentration))
       else:
           PH = -1 * log10(hydroniumConcentration)

   elif Titrant.getMoles() < Analyte.getMoles():
       hydroniumConcentration = TitrantisLimiting(Analyte, Titrant)
       if (Analyte.getSolutionKA() < (1 * 10**-7)):
           PH = 14 - (-1 * log10(hydroniumConcentration))
       else:
           PH = -1 * log10(hydroniumConcentration)

   print(str(PH) + " " + str(Analyte.getSolutionVolume()))


def TitrantisLimiting(Sub_Analyte, Sub_Titrant):
   """
   At this point the Titrant has all reacted and the only thing left is the Analyte.
   This analyte can be weak or strong, acid or base.
   """
   #  This step assumes Titrant is limiting so the remaining moles of Analyte is their difference.
   Sub_Analyte.setMoles(Sub_Analyte.getMoles() - Sub_Titrant.getMoles())

   if (Sub_Analyte.isSolutionStrong() == True):
       return Sub_Analyte.getSolutionMolarity()
   elif (Sub_Analyte.isSolutionStrong() == False):
       return Sub_Analyte.getSolutionKA() * Sub_Analyte.getSolutionMolarity()


def AnalyteIsLimiting(Sub_Analyte, Sub_Titrant):
   #  Update with reaction in the reaction of 1 - x ,
   #  where 1 in the number of orignal moles and x is the reaction amount
   Sub_Titrant.setMoles(Sub_Titrant.getMoles() - Sub_Analyte.getMoles())

   #  Create the Conjugate Solution With a generic name, no need for KA,
   #  a molarity of x moles divided by the total volume
   ConjugateAcidSolution = Solution("Conjugate for" + Sub_Titrant.getName(), None,
                                    Sub_Analyte.getMoles() / Sub_Titrant.getSolutionVolume(),
                                    Sub_Titrant.getSolutionVolume())

   # If the Titrant(base solution) is weak, and the Analyte(in the barrette) is strong (Ex NAOH into Ascorbic(1))
   if (Sub_Titrant.isSolutionStrong() == False and Sub_Analyte.isSolutionStrong() == True):
       """
       1. The Hydronium, H30 is isolated in the equilibrium expression and comes to the generic equation of:
       note: Ka is that of the weak base solution(Titrant)
       [H30] = Ka * [HA]/[A-]
       """
       return float(Sub_Titrant.getSolutionKA() *
                    (Sub_Titrant.getSolutionMolarity() / ConjugateAcidSolution.getSolutionMolarity()))

   # If the Titrant(base solution) is strong, and the Analyte(in the barrette) is weak (Ex Ascorbic(1) into NAOH)
   elif (Sub_Titrant.isSolutionStrong() == True):
       """
       1. The Hydronium, H30 is isolated in the equilibrium expression and comes to the generic equation of:
       note: because the weak solution is all gone from this reaction, KA will simply be that of the concentration
       of whats left in the titrant. This works the same for strong solutions as there is nothing left of the analyte
       [H30] = [HA]
        """
       return Sub_Titrant.getSolutionMolarity()

   else:
       print("You should have never gotten this far.")
       return None


# print(Analynte.getMoles())
for x in range(25,70, 1):
   DeterminePH(Solution("Acid", .000018, .1, .05), Solution("Base", .00000000000000000001, .1, x/1000))



