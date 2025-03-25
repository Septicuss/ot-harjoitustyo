import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_merkkijono(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alussa_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_saldo_lataus_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.00)

    def test_kortin_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 9)

    def test_kortin_saldo_ei_vahene_suuremmalla_maaralla(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_rahan_ottaminen_palauttaa_oikean_tuloksen(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))

    def test_rahan_ottaminen_palauttaa_oikean_tuloksen_suuremmalla_maaralla(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1100))