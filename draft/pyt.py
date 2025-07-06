num = int(input("Enter decimal value: "))   

base = int(input("Enter base 2-36: ")) 

num_tmp = num 

output = "" 

tmp = 0 

while num_tmp > 0: 

    tmp = num_tmp % base 

    if (tmp >= 10):
            output += chr(65-10+tmp)  
            print(tmp) 
    else:
            output += str(tmp) 

    num_tmp = num_tmp // base 

     

    #print(tmp, num_tmp) 

output = output[::-1] 

print(output) 