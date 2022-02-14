tipos_num = (int, float, complex) ##


class Calculadora:

    @staticmethod
    def validate_args(x, y):
        if not isinstance(x, tipos_num) and not isinstance(y, tipos_num):
            raise ValueError

    def soma(self, x, y):
        self.validate_args(x, y)
        return x + y

    def multiplicacao(self, x, y):
        self.validate_args(x, y)
        return x*y

    def subtracao(self, x, y):
        self.validate_args(x, y)
        return x-y

    def dividir(self, x, y):
        self.validate_args(x, y)
        return x/y