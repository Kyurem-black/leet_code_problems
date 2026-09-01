// 0 ms | 19.5 MB
from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0,1)
        expression = expression.replace('-','+-')

        for fraction in expression.split('+'):
            if fraction:
                result += Fraction(fraction)
        return f"{result.numerator}/{result.denominator}"