def compute_deriv(poly):
    ans = ()
    for index in range(1,len(poly)):
        ans = ans + (float(poly[index]*index),)
    return ans

deriv = ()
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
print 'poly: ' + str(poly)
deriv = compute_deriv(poly)
print 'return: ' + str(deriv)
