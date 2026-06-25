# THERE ARE 4 TYPES OF USER-DEFINED FUNCTIONS IN PYTHON BASED ON PARAMETERS AND RETURN VALUE.

# 1. NO PARAMETERS, NO RETURN VALUE
# 2. NO PARAMETERS, WITH RETURN VALUE
# 3. PARAMETERS WITH NO RETURN VALUE
# 4. PARAMETERS WITH RETURN VALUE
#===========================================================================================#

def sum1():     # 1. NO PARAMETERS, NO RETURN VALUE
    a,b=3,4
    z=a+b
    print(z)
    
sum1()

#-------------------------------------------------------------------------------------------#

def sum2():     # 2. NO PARAMETERS, WITH RETURN VALUE
    a,b=3,4
    z=a+b
    return z

s=sum2()
print(s)

#-------------------------------------------------------------------------------------------#

def sum3(a,b):   # 3. PARAMETERS WITH NO RETURN VALUE
    z=a+b
    print(z)

sum3(3,4)

#-------------------------------------------------------------------------------------------#

def sum4(a,b):   # 4. PARAMETERS WITH RETURN VALUE
    z=a+b
    return z

s=sum4(3,4)
print(s)
