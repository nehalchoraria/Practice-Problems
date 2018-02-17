def sumofsquares(number):
    size = math.sqrt(number)
    size = math.floor(size)
    
    for i in range(0,size+1):
        for j in range(0,size+1):
            if i*i + j*j == number:
                return True
    
    return False

print(sumofsquares(17))
