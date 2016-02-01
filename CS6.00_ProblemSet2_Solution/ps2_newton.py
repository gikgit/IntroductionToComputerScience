
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
    return result


def compute_deriv(poly):
    ans = ()
    for index in range(1,len(poly)):
        ans = ans + (float(poly[index]*index),)
    return ans


def compute_root(poly,x_0,epsilon):
    poly_deriv = ()
    poly_deriv = compute_deriv(poly)
    poly_value = 0
    poly_deriv_value = 0
    root = 0
    count = 1

    poly_value = evaluate_poly(poly,x_0)
    while abs(poly_value) > epsilon:
        count += 1
        poly_deriv_value = evaluate_poly(poly_deriv,x_0)
        x_0 = x_0 - poly_value / poly_deriv_value 
        poly_value = evaluate_poly(poly,x_0)

    root = x_0
    print (root,count)





poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
compute_root(poly,x_0,epsilon)
