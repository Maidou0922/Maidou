q=open('test12.txt', 'w')
q.write('''my name is luke,i'm nine years old,
i'm from china, china is a big country. 
                                       ''')

q.close()

q=open('test.txt', 'r')
s=q.read()
s1=s.upper()
print(s1)
q.close()


                

    
           
    

