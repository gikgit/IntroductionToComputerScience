
def evaluate_poly(poly,x):
    result = 0
    for index in range(0,len(poly)):
        if index == 0:
            result += poly[index]
        elif index == 1:
            result += poly[index]*x
        else:
            tmp = x
            power = index - 1
            while power:
                tmp *= x
                power -= 1
            result += tmp * poly[index]      
    print result

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
evaluate_poly(poly,x)
print 'poly:' + ' ' + str(poly)
print 'x:' + ' ' + str(x)
