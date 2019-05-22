from math import log10
class Solution:

   def __init__(self, Name, KA, Molarity, Volume):
       #  Initialize the solution instance
       self.SolutionName = Name

       try: #When the conjugate base froms no need for KA so this would crash
           self.SolutionKA = float(KA)
       except:
           self.SolutionKA = KA

       self.SolutionMolarity = float(Molarity)
       self.SolutionVolume = float(Volume) # In liter's
       self.SolutionMoles = (self.SolutionVolume*.001) * self.SolutionMolarity

   def getSolutionMolarity(self):
       return self.SolutionMolarity
   def setSolutionMolarity(self,amount):
       self.SolutionMolarity = amount

   def getSolutionVolume(self):
       return self.SolutionVolume

   def addVolume(self,AddedVolume):
       # This procedure adds volume to the solution and adjusts
       # the solution's molarity based off the new volume
       moles = self.SolutionMoles #set local variable
       self.SolutionVolume += AddedVolume #get new volume
       self.SolutionMolarity = (moles / (self.SolutionVolume*.001)) #update molarity

   def getName(self):
       return self.SolutionName #return name

   def getSolutionKA(self):
       return self.SolutionKA #return KA

   def returnConstructor(self):
       return self.SolutionName, self.SolutionKA , self.SolutionMolarity, self.SolutionVolume

   def getMoles(self):
       return self.SolutionMoles

   def setMoles(self, newAmount):
       self.SolutionMoles = newAmount
       self.SolutionMolarity = self.SolutionMoles / (self.SolutionVolume * .001)

   def isSolutionStrong(self):
       if -1*log10(self.getSolutionKA()) >= 12 or -1*log10(self.getSolutionKA()) <= 2:
           return True
       else:
           return False




