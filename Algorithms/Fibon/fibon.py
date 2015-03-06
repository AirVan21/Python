result = 0

#Creating first values for Fibonacci array 
fibArr = [0,1]
order = int(raw_input("Please, input number: "))

# Linear algorithm
for i in range(2, order):
	fibArr.append(fibArr[i - 1] + fibArr[i - 2]) 

print fibArr
print "Fibon[%d] = %d" % (order, fibArr[order - 1])
