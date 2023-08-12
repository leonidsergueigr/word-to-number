from unittest import TestCase
from api import convertir_en_nombre, convertir_en_lettre


class TestWord2Number(TestCase):
    def test_convert_words(self):
        self.assertEqual(convertir_en_nombre("Deux cent huit"),208)
        self.assertEqual(convertir_en_nombre("Neuf cent quatre-vingt milliard sept cent dix huit million cent quarante mille deux cent trente"),980718140230)
    def test_convert_words_with_error(self):
        self.assertEqual(convertir_en_nombre("Deux cent mill"), -1)
    def test_convert_integer(self):
        with self.assertRaises(ValueError):
            convertir_en_nombre(0)
    def test_convert_list(self):
        with self.assertRaises(ValueError):
            convertir_en_nombre(["Deux", "Mille","Quatre"])

class TestNumber2Word(TestCase):
    def test_convert_integer(self):
        self.assertEqual(convertir_en_lettre(120),"cent vingt")
        self.assertEqual(convertir_en_lettre(2840612),"deux million huit cent quarante mille six cent douze")
    def test_with_out_range_value(self):
        with self.assertRaises(ValueError):
            convertir_en_lettre(1000000000000000)
