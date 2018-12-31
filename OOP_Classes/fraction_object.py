class Fraction(object):
    def __init__(self,num,denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + '/' +str(self.denom)
    
    def __add__(self,other):
        top = self.num*other.denom + other.num*self.denom
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __sub__(self,other):
        self.num*other.denom - other.num*self.denom
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __float__(self):
        return self.num/self.denom
    def __inverse__(self,other):
        return Fraction(self.denom,self.num)


a=3/4

print(isinstance(a,Fraction))
    
