# Quadratic Time O(n²)

n = [0,1,2,3,4]
for i in n:
    i += 1
    print(f"i = {i}")
    print("")
    for j in n:
        j += 1
        print(f"j = {j}")
    print("")


    

print("Example 2")

for i in n:
    i += 1
    print(f"i = {i}")
    print("")
    for j in n:
        j = i
        j += 1
        print(f"j = {j}")
    print("")
    