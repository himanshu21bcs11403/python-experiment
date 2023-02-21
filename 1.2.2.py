import math
var = int(input("Enter the number : "))
varstring = str(var)
lengthvar = len(varstring)
total = 0
for i in range(0,len(varstring)):
   total = total + math.pow(int(varstring[i]),lengthvar)
total=int(total)
if (total == var ):
    print("Armstong number")
else:
    print("Not Armstong number")
