string = "abdbabdbadbbdb"
substr = "abd"

count = 0
for i in range(len(string) - len(substr) + 1): 
    if string[i] == substr[0]: 
        sub = True
        j = 0
        while j < len(substr) and string[i + j] == substr[j]: 
            j += 1
        if j != len(substr):  
            sub = False
        if sub: 
            count += 1
    
print(count)
