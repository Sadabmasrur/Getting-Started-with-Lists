l1=[3,4,7,2,56,67,32,1,77,99]
print(f"The original list is: {l1}")

sum=0

for i in l1:
    sum=sum+i
    
print(f"The sum of the number is: {sum}" )

avg=sum/len(l1)
print(f"The average of the numbers in the list is: {avg}")

l1.sort()
print(f"The sorted list in asending order: {l1}")

print(f"The smallest element: {l1[0]}")
print(f"The largest element: {l1[-1]}")    
    