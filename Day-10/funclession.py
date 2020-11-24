# Without any paramter
def func1(a, b, c=10): # Parameters
    d = a * b * c
    print(d)
    return d

func1(5, 2, 4) # Arguments
# 100
# 40 # c: 10 = overrided by 4 which we pass into the function when call it
