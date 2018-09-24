#
# Name: Carlos Garcia-Lemus
# ID: 014339295
# Date: 09/24/2018
# 
# Lab 0
# Section 13/14
# Purpose of lab: Environment, python, and testing
# Additional comments

# Function takes in a number which represents a weight on earth and outputs two numbers which represent that weight being converted to fit Mars’ and Jupiter’s atmospheres.
def weight_on_planets():
   weight = input("What do you weigh on earth? ")
   MarsW = float(weight) * 0.38
   JupiterW = float(weight) * 2.34
   MarsW = round(MarsW, 2)
   JupiterW = round(JupiterW, 2)
   q = "\nOn Mars you would weigh"
   w = "\nOn Jupiter you would weigh"
   print(q + ' ' +str(MarsW) + " pounds." + w + ' ' + str(JupiterW) + " pounds.")

   
   
   
if __name__ == '__main__':
   weight_on_planets()