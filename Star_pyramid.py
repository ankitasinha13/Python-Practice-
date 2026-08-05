#left aligned pyramid
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
    

#mid pyramid
for i in range(1,6):
   print(" "*(5-i),end="")
   print("*"*(2*i-1))
print()

#right aligned pyramid
for i in range(1,6):
   print(" "*(5-i),end="")
   print("*"*i)
print()
