import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)
        self.kassapaate = Kassapaate()

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_arvo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_oikea_vähenemisen_määrä_raahaa_riittää(self):
        self.maksukortti.lataa_rahaa(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_oikea_vähenemisen_määrä_liian_vähän_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_oikea_palautus_true(self):
        self.maksukortti.lataa_rahaa(240)
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_oikea_palautus_false(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)