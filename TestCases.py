import Titration
from Solutions import Solution

#TEST CASE 1
#My textbook reference goal is 5.69 here
addedsolution = Solution(name = "NAOH",SolutionKa = .000000000001,SolutionMolarity = .1, SolutionVolume = 45)
basesolution = Solution(name = "Acetic",SolutionKa = .000018,SolutionMolarity = .1,SolutionVolume = 50)

print(Titration.DeterminePH(addedsolution,basesolution))
