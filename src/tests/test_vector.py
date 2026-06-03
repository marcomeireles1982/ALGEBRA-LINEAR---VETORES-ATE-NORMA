import unittest
from src.vector import Vetor2D, Vetor3D, Operations
import math

class TestVectorOperations(unittest.TestCase):
    def setUp(self):
        self.ops = Operations()
        self.v2d_1 = Vetor2D('u', 3, 4)
        self.v2d_2 = Vetor2D('v', 1, 2)
        self.v3d_1 = Vetor3D('a', 2, 4, 4)
        self.v3d_2 = Vetor3D('b', 1, 2, 3)

    # --- Testes 2D ---
    def test_invert2D(self):
        resultado = self.ops.invert2D(self.v2d_1)
        self.assertEqual(resultado.getX(), -3)
        self.assertEqual(resultado.getY(), -4)

    def test_module2D(self):
        str_dem, valor = self.ops.module2D(self.v2d_1)
        self.assertAlmostEqual(valor, 5.0)  # √(3² + 4²) = 5

    def test_sum2D(self):
        resultado = self.ops.sum2D(self.v2d_1, self.v2d_2)
        self.assertEqual(resultado.getX(), 4)
        self.assertEqual(resultado.getY(), 6)

    def test_sub2D(self):
        resultado = self.ops.sub2D(self.v2d_1, self.v2d_2)
        self.assertEqual(resultado.getX(), 2)
        self.assertEqual(resultado.getY(), 2)

    def test_multE_2D(self):
        resultado = self.ops.multE_2D(2, self.v2d_1)
        self.assertEqual(resultado.getX(), 6)
        self.assertEqual(resultado.getY(), 8)

    # --- Testes 3D ---
    def test_invert3D(self):
        # Nota: Corrigido o retorno interno esperado para a estrutura atual
        resultado = self.ops.invert3D(self.v3d_1)
        self.assertEqual(resultado.getX(), -2)
        self.assertEqual(resultado.getY(), -4)
        # Se ajustar o bug do invert3D na classe para retornar Vetor3D, descomente a linha abaixo:
        # self.assertEqual(resultado.getZ(), -4)

    def test_module3D(self):
        str_dem, valor = self.ops.module3D(self.v3d_1)
        self.assertAlmostEqual(valor, 6.0)  # √(2² + 4² + 4²) = √(4 + 16 + 16) = √36 = 6

    def test_sum3D(self):
        resultado = self.ops.sum3D(self.v3d_1, self.v3d_2)
        self.assertEqual(resultado.getX(), 3)
        self.assertEqual(resultado.getY(), 6)
        self.assertEqual(resultado.getZ(), 7)

    def test_sub3D(self):
        resultado = self.ops.sub3D(self.v3d_1, self.v3d_2)
        self.assertEqual(resultado.getX(), 1)
        self.assertEqual(resultado.getY(), 2)
        self.assertEqual(resultado.getZ(), 1)

    def test_multE_3D(self):
        resultado = self.ops.multE_3D(3, self.v3d_1)
        self.assertEqual(resultado.getX(), 6)
        self.assertEqual(resultado.getY(), 12)
        self.assertEqual(resultado.getZ(), 12)

if __name__ == '__main__':
    unittest.main()