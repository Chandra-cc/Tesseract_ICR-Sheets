from random import randint
l = []

# Change this string to ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#,.-/ or according to your needs
parent_str = "1234"



for _ in range(200):
    
    s = ''
    for _ in range(100):
        
      s+= parent_str[randint(0,len(parent_str)-1)]*randint(0,1)+' '*randint(0,1)
      
    l.append(s+'\n')

with open("eng.training_text","w+") as f:
	f.writelines(l)