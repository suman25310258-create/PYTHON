#MULTIPLICATION TABLE UPTO 10-TIMES USING FOR 
num=int(input("Enter the Number :- "))
for i in range(1,11):
 print(num,"x",i, "=", num*i)
 
#MULTIPLICATION TABLE UPTO 10-TIMES USING WHILE LOOP
num=int(input("Enter the Number :- "))
i=1
while(i<11):
 print(num,"x",i, "=", num*i)
 i=i+1