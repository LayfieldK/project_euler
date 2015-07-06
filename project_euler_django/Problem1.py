
#running total of multiples
sumValue = 0

#loop from 1 - 999
for x in range(1,1000):
    #if number is multiple of 3 or 5, add to running total
    if x % 3 == 0 or x % 5 == 0 :
        sumValue += x

#output
print sumValue
