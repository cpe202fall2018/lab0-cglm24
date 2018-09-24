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