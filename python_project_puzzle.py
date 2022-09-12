from itertools import count
from pickle import TRUE
import random

l1=["name","class","mouse"]
l2=["mane","asslc"]

while True:
    
    coutt=0
    cout=0
    uc=int(input('''PRESS 1 FOR STARTING GAME\PRESS 2 FOR exit GAME
             
             1 yes
             2 no
             
             '''))
    print(uc)
    if(uc==1):
      for a in range(1,6):
            
        print("Arrange the letters to form a valid word:")
        l2=["mane","asslc","msuoe"]
        ch=random.choice(l2)
        
        print(ch)
        # if(ch=="mane" or ch=="asslc"):
        #  print(l1[0])

        u=input("ENTER CORRECT FORM: \n") 
        if(u=="class" or u=="name" or u=="mouse"):
          print(" YOUR ANSWARE IS CORRECT")
          coutt=coutt+1
          print("")
        elif(u!="class" or u!="name" or u!="mouse"):
          print("YOUR ANSWARE IS NOT CORRECT")
          cout=cout-1
    else:
        break
   
    
    final=coutt+cout 
    print("")
    print("TOTAL SCORE IS",final) 
        
      
      
    
    

       



