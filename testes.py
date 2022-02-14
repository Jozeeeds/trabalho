import unittest
import Calculadora


class CalculadoraTests(unittest.TestCase):

    def setUp(self):
        self.Calculadora = Calculadora.Calculadora()

    def teste_soma(self):
        result = self.Calculadora.soma(8, 8)
        self.assertEqual(16, result)

    def teste_soma_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.soma, "", "")

    def teste_multiplicacao(self):
        result = self.Calculadora.multiplicacao(10, 3)
        self.assertEqual(30, result)

    def teste_multiplicacao_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.multiplicacao, "", "")

    def test_subtracao(self):
        result = self.Calculadora.subtracao(-6, 0)
        self.assertEqual(-6, result)

    def teste_subtracao_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.subtracao, "", "")

    def teste_dividir(self):
        result = self.Calculadora.dividir(25, 5)
        self.assertEqual(5, result)

    def teste_dividir_valor_invalido(self):
        self.assertRaises(ValueError, self.Calculadora.dividir, "", "") ## eu havia colocador coisas escritas aqui dentro pois na documentacao dos testes é necessario, porem se passar vazio tambem funciona

    def teste_dividir_por_zero(self):
        self.assertRaises(ZeroDivisionError, self.Calculadora.dividir, 5, 0)


if __name__ == '__main__':
    unittest.main()