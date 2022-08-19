num_list = []

for i in range (1, 11) :
    a = int(input())
    b = a % 42
    num_list.append(b)
result = dict.fromkeys(num_list)
result2 = list(result)    
    
print(len(result2))