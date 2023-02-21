import math
var = int(input("Enter the number : "))
varstring = str(var)
total = 0
for i in range(0,len(varstring)):
   total = total + math.pow(int(varstring[i]),3)
total=int(total)
if (total == var ):
    print("Armstong number")
else:
    print("Not Armstong number")
