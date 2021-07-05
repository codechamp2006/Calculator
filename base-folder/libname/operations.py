def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def coordinatePoint(p1,p2,q1,q2):
    import math
    # 4 parameters required
    # p1,p2 for coordinate of first point on graph
    # q1 and q2 for coordinate of second point on graph
    sqrDiff1 = (p1-p2)**2
    sqrDiff2 = (q1-q2)**2
    sqrtSum = math.sqrt(sqrDiff1 + sqrDiff2)
    return sqrtSum

def fibonacci(limit):
    # this function will print the fibonacci terms upto limit
    # initializing variables
    a = 1
    b = 0
    c = 0
    # run a for-loop
    for i in range(1,limit):
        c = a + b
        print(c)
        a = b
        b = c

def hcf2(num1,num2):
    # this function will print the hcf of 2 numbers
    # for-loop to obtain the highest common factor
    for i in range(1,num1*num2,+1):
        if (num1 % i == 0 and num2 % i == 0):
            HCF = i
    return HCF # returns the HCF        


def hcf(nums):
    # this function will take in any number of parameters
    # store this as a list in nums
    # then the algorithm begins
    count = 0
    min = nums[0] # this will anyhow consider the smallest number in 0th index
    # for-loop to count the number of elements in the lists
    # for-loop
    for num in range(1,min,+1):
        FactorCount = 0
        for i in range(nums[0],len(nums)):
            if (nums[i] % num == 0):
                FactorCount = FactorCount + 1
        if (FactorCount == nums.len()):
            hcf = num  
    return hcf # returns the hcf              




