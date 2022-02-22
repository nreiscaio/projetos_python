class Equacaco:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def conta(a, b, c):

        delta = (b ** 2) - (4 * a * c)

        x1 = (-b + (delta ** (1/2))) / (2 * a)
        x2 = (-b - (delta ** (1/2))) / (2 * a)

        return x1, x2