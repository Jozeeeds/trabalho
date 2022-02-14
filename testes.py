import unittest
import Calculadora


class CalculadoraTests(unittest.TestCase):

    def setUp(self):
        self.Calculadora = Calculadora.Calculadora()

    def teste_soma(self):
        result = self.Calculadora.soma(4, 2)
        self.assertEqual(6, result)

    def teste_soma_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.soma, "Quatro", "Cinco")

    def teste_multiplicacao(self):
        result = self.Calculadora.multiplicacao(5, 3)
        self.assertEqual(15, result)

    def teste_multiplicacao_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.multiplicacao, "Quatro", "Cinco")

    def test_subtracao(self):
        result = self.Calculadora.subtracao(6, 4)
        self.assertEqual(2, result)

    def teste_subtracao_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.subtracao, "Quatro", "Cinco")

    def teste_dividir(self):
        result = self.Calculadora.dividir(5, 1)
        self.assertEqual(5, result)

    def teste_dividir_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.dividir, "Cinco", "Quatro")

    def teste_dividir_por_zero(self):
        self.assertRaises(ZeroDivisionError, self.Calculadora.dividir, 5, 0)


if __name__ == '__main__':
    unittest.main()