a1= input("enter the starting year in the format dd/mm/yyyy : ")
b1= input("enter the ending year in the format dd/mm/yyyy : ")        
year=int(a1[-4:])
year2=int(b1[-4:])
s = []                                             
b = []                                             
for i in range(year,(year2)+1):                    
    if i % 4 == 0:                                 
        if i % 100 != 0:
            s.append(i)                            
                                                   
        elif i % 100 == 0:
            if i % 400 == 0:
                s.append(i)

            else:
                b.append(i)
    else:
        b.append(i)

print("leap year: ", s)                                           
print("Non leap year: " , b)
