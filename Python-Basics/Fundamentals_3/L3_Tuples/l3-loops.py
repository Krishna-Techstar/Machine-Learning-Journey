tup = (1, 2,3,4,5)
idx =0
x = 4
for val in tup:
    if(val == x ):
        print(idx)
        break
    idx +=1


for val in tup:
    print(val )


# to calculate sum 

sum = 0
for val in tup:
    sum += val

print(f"the Sum of {sum}")


