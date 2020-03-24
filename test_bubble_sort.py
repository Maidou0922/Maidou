#Bubble Sort
import time
import random
l1= [9,5,25,7, 8, 3, 255, 23,1,0, 99,2222,12,34,29,53,98,4,25,88]

#for i in range(1000):
#    l1.append(random.randint(1,255))

def bubbleSort(l):
    ''' This is a demo to implement Bubble Sort '''
    for j in range(len(l)):
        for i in range(len(l)-1-j):
            #print(l[i],l[i+1])
            if l[i] > l[i+1]:
                tmp = l[i+1] ### Swap , change
                l[i+1]=l[i]
                l[i] = tmp
        #print(l)
print("org  :",l1)
bubbleSort(l1)
print("after:",l1)

l2 = l1.copy()


t1=time.time()
bubbleSort(l1)
t2=time.time()
print (t2-t1)

t1=time.time()
l2.sort()
t2=time.time()
print (t2-t1)


#print (l1)
#print (l2)
for i in range(len(l2)):
    if(l1[i] != l2[i]):
        print("error")

