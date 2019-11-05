import Titration
from Solutions import Solution

#TEST CASE 1
#My textbook reference goal is 5.69 here
NAOH = Solution("NAOH", .00000000000001, .3, .025);
HF = Solution("HF", .00066, .3, .025)
H2O = Solution ("Water", .0000001 , 1 , 0)
HCL = Solution ("HCL",  1, .1, .045);
Acetic = Solution("Acetic",.000018,.1, .046);

print(Titration.DeterminePH(HF,NAOH));

print(Titration.DeterminePH(NAOH,HCL));
print(Titration.DeterminePH(NAOH,Acetic))
