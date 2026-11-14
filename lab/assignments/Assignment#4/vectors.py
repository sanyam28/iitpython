import math

class Vectors:
    def returnstr(self, vecto):
        if(self.x ==0 and self.y==0 and self.z ==0):
            return "0i + 0j + 0k"
        else:
            return f"{str(vecto.x)+'i' if vecto.x!=0 else ''} {'' if vecto.x==0 and vecto.y>=0 else ('' if vecto.y==0 else('+' if vecto.y>0 else '-'))} {str(abs(vecto.y))+'j' if vecto.y!=0 else ''} {'' if vecto.y==0 and vecto.z>=0 else ('' if vecto.z==0 else('+' if vecto.z>0 else '-'))} {str(abs(vecto.z))+'k' if vecto.z!=0 else ''}"

    def isValid(self, gval):
        if((str(type(gval.x)) == "<class 'int'>" or str(type(gval.x)) == "<class 'float'>") and (str(type(gval.y)) == "<class 'int'>" or str(type(gval.y)) == "<class 'float'>") and (str(type(gval.z)) == "<class 'int'>" or str(type(gval.z)) == "<class 'float'>")):
            return True
        else:
            return False
        
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        if(self.isValid(self) == False):
            return 'All inputs must be either in float or int'
        return self.returnstr(self)

    def mag(self):
        if(self.isValid(self) ==False):
            return 'All inputs must be either in float or int'
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if(self.isValid(self) ==False or self.isValid(other) == False):
            return 'All inputs must be either in float or int'
        a=self.x + other.x
        b=self.y + other.y
        c=self.z + other.z
        return self.returnstr(Vectors(a,b,c))

    def __sub__(self, other):
        if(self.isValid(self) ==False or self.isValid(other) == False):
            return 'All inputs must be either in float or int'
        a=self.x - other.x
        b=self.y - other.y
        c=self.z - other.z
        return self.returnstr(Vectors(a,b,c))

    def dotproduct(self, other):
        if(self.isValid(self) ==False or self.isValid(other) == False):
            return 'All inputs must be either in float or int'
        return self.x*other.x + self.y*other.y + self.z*other.z

    def crossproduct(self, other):
        if(self.isValid(self) ==False or self.isValid(other) == False):
            return 'All inputs must be either in float or int'
        a = self.y*other.z - self.z*other.y
        b = other.x*self.z - self.x*other.z
        c = self.x*other.y - other.x*self.y
        return self.returnstr(Vectors(a,b,c))

    def __mul__(self,other):
        if(self.isValid(self) ==False or self.isValid(other) == False):
            return 'All inputs must be either in float or int'
        a = self.y*other.z - self.z*other.y
        b = other.x*self.z - self.x*other.z
        c = self.x*other.y - other.x*self.y
        return self.returnstr(Vectors(a,b,c))

# Examples

a= Vectors(1,2,-2)
b= Vectors(2,-1,0)
c= Vectors(10,9,0)
print(a)
print(c)
print('mag',Vectors.mag(b))
print('sum', a+b)
print('sub' ,a-b)
print('dotproduct',Vectors.dotproduct(a,b))
print('crossproduct',Vectors.crossproduct(a,b))
print(a*b)