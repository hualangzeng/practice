def float_equal(a, b):
    error = 1.0e-2
    #print(error)
    if a - b < error and a - b > -error:
        return 0
    else:
        return 1

#float_equal(1, 2)

def Power(base, exponent):
    temp = isinstance(exponent, int)
    if temp is False :
        return False,0
    else:
        result = 1.0
        if exponent > 0:
            for i in list(range(0, exponent)):
                result *= base

            return True,result
        elif exponent == 0:
            return 1
        else:
            if float_equal(base, 0.0):
                return False, 0
            else:
                for i in list(range(exponent, 0)):
                    result *= 1/base

                return result

print(Power(3, 5))
print(float_equal(0.0015, 0))



#Power(2, 6)