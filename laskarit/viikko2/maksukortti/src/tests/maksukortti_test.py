import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        vastaus = str(self.kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)
        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)
        self.assertEqual(self.kortti.saldo_euroina(), 150.0)

    # ITSE TEHDYT

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_negatiivinen_summa_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-100)
        self.assertEqual(self.kortti.saldo_euroina(), 10)

    def test_edullinen_lounas_ostettavissa(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()
        self.assertEqual(kortti.saldo_euroina(), 0)

    def test_maukas_lounas_ostettavissa(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()
        self.assertEqual(kortti.saldo_euroina(), 0)