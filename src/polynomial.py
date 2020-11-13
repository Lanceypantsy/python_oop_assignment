# A Python class for polynomials
# Author: Lance Barto
# Date: 11/13/20

class Polynomial:
    def __init__(self, lst):
        self.coefficients = lst

    def __repr__(self):
       return f'Polynomial({self.coefficients})'

    def __add__(self, other):
        if len(self.coefficients) == len(other.coefficients):
            return Polynomial([self.coefficients[idx] + other.coefficients[idx] for idx in range(len(self.coefficients))])
        elif len(self.coefficients) > len(other.coefficients):
            lst = [0] * len(self.coefficients)

            for idx in range(len(lst)):
                lst[idx] += self.coefficients[idx]

                if idx < len(other.coefficients):
                    lst[idx] += other.coefficients[idx]

            return Polynomial(lst)

        else:
            lst = [0] * len(other.coefficients)

            for idx in range(len(lst)):
                lst[idx] += other.coefficients[idx]

                if idx < len(self.coefficients):
                    lst[idx] += self.coefficients[idx]

            return Polynomial(lst)

    def __sub__(self, other):
        return Polynomial([self_coef - other_coef for self_coef, other_coef in zip(self.coefficients, other.coefficients)])

    def __neg__(self):
        return Polynomial([-1 * coef for coef in self.coefficients])

    def __eq__(self, other):
        if self.coefficients == other.coefficients:
            return True
        elif len(self.coefficients) > len(other.coefficients):
            diff = len(self.coefficients) - len(other.coefficients)

            if self.coefficients[-diff:] == [0] * diff:
                return True
            else:
                return False
        else:
            diff = len(other.coefficients) - len(self.coefficients)

            if other.coefficients[-diff:] == [0] * diff:
                return True
            else:
                return False

    def __str__(self):
        str_lst = [f'{coef}x^{exp}' if exp != 0 else f'{coef}' for exp, coef in enumerate(self.coefficients)]
        return ' + '.join(reversed(str_lst))

    def evaluate(self, num):
        return sum([coef * num**exp for exp, coef in enumerate(self.coefficients)])


poly = Polynomial([4, 3, 2, 1])
poly1 = Polynomial([2, 3, 4, 5, 6])
print(poly)