'''WAS to enter any number to print following pattern

 *****
  ****
   ***
    **
     *
#Name : Laxman Sirvi
#Date : 09-03-22'''
n=int(input("Enter the No. of rows : "))
i = 1
while i <= n :
      j = n
      while j >= i:
         print("*", end=" ")
         j = j - 1
      print()
      i = i + 1
