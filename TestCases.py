import Titration
from Solutions import Solution

#TEST CASE 1
#My textbook reference goal is 5.69 here
NAOH = Solution("NAOH", .000000000001,.1, .0449);
HCL = Solution ("HCL",  1, .1, .045);
#asesolution = Solution(name = "Acetic",SolutionKa = .000018,SolutionMolarity = .1,SolutionVolume = 50);

print(Titration.DeterminePH(NAOH,HCL));
#print(Titration.DeterminePH(NAOH,basesolution))
