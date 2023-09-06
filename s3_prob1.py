class Complex:
    """
    Complex number class.

    This class represents complex numbers and provides various operations on them.

    Attributes:
        real (float): The real part of the complex number.
        imaginary (float): The imaginary part of the complex number.

    Methods:
        __init__(self, real, imaginary):
            Initializes a complex number with the given real and imaginary parts.

        __str__(self):
            Returns a string representation of the complex number in the form "a + bi",
            where 'a' is the real part and 'b' is the imaginary part.

        __add__(self, other):
            Adds two complex numbers and returns a new complex number.

        __sub__(self, other):
            Subtracts two complex numbers and returns a new complex number.

        __mul__(self, other):
            Multiplies two complex numbers and returns a new complex number.
        mod(self):
            Returns the modulus (magnitude) of the complex number.

        __floordiv__(self, other):
            Divides two complex numbers using floor division and returns a new complex number.
    Example:
        c = Complex(3, 2)
        d = Complex(-4, -5)
        print(c + d)  # Output: -1 - 3i
    """
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __str__(self):
        return "{0} +{1}i".format(float(self.real),float(self.imaginary))
    def __add__(self,other):
        x_real=self.real+other.real
        y_img=self.imaginary+other.imaginary
        return Complex(x_real,y_img)
    def __sub__(self,other):
        x_real=self.real-other.real
        y_img=self.imaginary-other.imaginary
        return Complex(x_real,y_img)
    def __mul__(self,other):
        x_real=self.real*other.real - self.imaginary*other.imaginary
        y_img=self.real*other.imaginary + self.imaginary*other.real
        return Complex(x_real,y_img)
    def mod(self):
        """
        Calculate and return the modulus (magnitude) of the complex number.

        Returns:
            float: The modulus of the complex number.
        """
        return float((self.real)**2+(self.imaginary)**2)**0.5
    def __floordiv__(self,other):
        """
        Perform floor division of two complex numbers and return the result.

        Args:
            other (Complex): The complex number to divide by.

        Returns:
            Complex: The result of the floor division.
        """
        denominator=other.real**2+other.imaginary**2
        x_real=(self.real*other.real + self.imaginary*other.imaginary)/denominator
        y_img=(self.imaginary*other.real - self.real*other.imaginary)/denominator
        return Complex(x_real,y_img)
c=Complex(3,2)
d=Complex(-4,-5)
print(c+d)
print(c-d)
print(c*d)
print(c//d)
print(c.mod())
print(d.mod())
