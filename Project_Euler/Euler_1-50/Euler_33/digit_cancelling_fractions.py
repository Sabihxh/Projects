"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in
value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value 
of the denominator.
"""

from functools import reduce

class solution(object):

    def __init__(self):
        pass

    #Gets the greatest common divisor
    def gcd(self, a, b):
        small = min(a, b)
        large = max(a, b)

        if small == 0:
            return large
        elif small == 1:
            return 1
        else:
            return self.gcd(small, large % small)

    #Simplifies the fraction and returns a set consisting of two values, numerator and denominator
    def fractions(self, a, b):
        low_num = a/self.gcd(a, b)
        low_den = b/self.gcd(a, b)
        return low_num, low_den
        

    def main_loop(self, loop_limit):
        #This list gives all non-trivial fractions on types decrived in the problem. 
        a_list = []
        #x is numerator
        for x in range(11, loop_limit - 1):
            #y is denominator and loop from x + 1 since x/y < 1, 
            for y in range(x + 1, loop_limit):
                num_list = set(str(x))
                den_list = set(str(y))

                common_digit = [q for q in num_list if q in den_list and q != '0']
                # if common_digit: print x, y, common_digit

                if len(common_digit) == 1:
                    num_simplified_wrong = str(x).replace(common_digit[0], '', 1)
                    den_simplified_wrong = str(y).replace(common_digit[0], '', 1)

                    # print x, y, num_simplified_wrong, den_simplified_wrong
                    simplified_xy_fraction = self.fractions(x, y)
                    simplified_cancelled_fraction = self.fractions(int(num_simplified_wrong), int(den_simplified_wrong))
                    if simplified_xy_fraction[0] == simplified_cancelled_fraction[0] and simplified_xy_fraction[1] == simplified_cancelled_fraction[1]:
                        a_list.append([x, y])
        return a_list


    def final_solution(self, loop_limit):
        a_list = self.main_loop(loop_limit)

        numerator = reduce((lambda x, y: x * y), [item[0] for item in a_list])
        denominator = reduce((lambda x, y: x * y), [item[1] for item in a_list])

        #Item at index 1 is the denominator
        return self.fractions(numerator, denominator)[1]

i = solution()
print i.final_solution(100)






