import math
class Complex:

    def __init__(self, rea=0, ima=0): #it automatically manages (3,-4) to (rea) and (ima), self handles calling of 'a'.
        self.im = ima #ima is set to zero only when the is only real in 'self' i.e 'a'
        self.re = rea #similarly.
    
    def __str__(self): #handles print function
        if (self.im) < 0:
            return "("+str(self.re) + str(self.im) + "j"+")"
        else:
            return "("+str(self.re) + "+" + str(self.im) + "j"+")"

    def __add__(self, any): #manages addition of a+b
         return Complex(self.re+any.re, self.im+any.im)
    
    def __sub__(self,any):
         return Complex(self.re-any.re, self.im-any.im)

    def conjugate(self):
         return Complex(self.re, -self.re)

    '''
    def __mul__(self,any):
         a = 
         b = 
         c = 
         d =  
        '''

    def mag(self): #custom function
        return math.sqrt(self.re**2+self.im**2)

# subclass
class Polar(Complex):
    def __init__(self,mag, angle):
        self.re = mag + math.cos(angle)
        self.im = mag + math.sin(angle)

             
a = Complex(3,-4)
print(a.mag()) #mag is called.
print(a.re)
print(a.im)
b = Complex(5,12)
print(b.re)
print(b.im)

print(a,b) #calls line 6, also why is this diff. colour ?
print(a+b) #first calls l-12 then also calls l-6
print(b-a)
print(a*b)