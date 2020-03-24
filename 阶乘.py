b=int(input("pls input number:"))      

def fact(a):
    result=1
    if a < 0:
        return("Error") #  should be Error
    elif a == 0 or a==1:
        return(str(a))
    while a > 1:
        tmp=a*(a-1)
        result=result*tmp
        a -=2
    return result  #return after loop
    
print(fact(b))
print("")

# 
#fact of 5 should be 120, not 20, 5*4*3*2*1 = 120   , pls check your logic of func