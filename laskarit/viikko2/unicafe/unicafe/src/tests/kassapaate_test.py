import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti1 = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)
    
    def test_oikeat_alku_arvot_raha(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_oikeat_alku_arvot_myydyt(self):
        self.assertEqual((self.kassapaate.edulliset,self.kassapaate.maukkaat), (0,0))

    # Kateisella osto
    def test_edullinen_osto_kateisella_raha_riittaa_kassa_nousee_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
    
    def test_maukas_osto_kateisella_raha_riittaa_kassa_nousee_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
    
    def test_edullinen_osto_kateisella_raha_riittaa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300),60)
    
    def test_maukas_osto_kateisella_raha_riittaa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)

    def test_edullinen_osto_kateisella_raha_riittaa_myydyt_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset,2)
    
    def test_maukas_osto_kateisella_raha_riittaa_myydyt_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_edullinen_osto_kateisella_raha_ei_riitä_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_osto_kateisella_raha_ei_riitä_kassan_raha_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_edullinen_osto_kateisella_raha_ei_riitä_myydyt_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_osto_kateisella_raha_ei_riitä_myydyt_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_osto_kateisella_raha_ei_riitä_oikea_palautus(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)
    
    def test_maukas_osto_kateisella_raha_ei_riitä_oikea_palautus(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100),100)


    # Kortilla osto
    def test_edullinen_osto_kortilla_raha_riittää_kortin_arvo_laskee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.maksukortti1.saldo, 760)

    def test_edullinen_osto_kortilla_raha_riittää_kassan_raha_ei_nouse(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_osto_kortilla_raha_riittää_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1),True)

    def test_edullinen_osto_kortilla_raha_riittää_edulliset_nousee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukas_osto_kortilla_raha_riittää_kortin_arvo_laskee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(self.maksukortti1.saldo, 600)

    def test_maukas_osto_kortilla_raha_riittää_kassan_raha_ei_nouse(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_osto_kortilla_raha_riittää_palauttaa_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1),True)
    
    def test_maukas_osto_kortilla_raha_riittää_maukkaat_nousee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti1)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_edullinen_osto_kortilla_raha_ei_riitä(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2),self.kassapaate.edulliset,self.maksukortti2.saldo),(False,0,100))
    
    def test_maukas_osto_kortilla_raha_ei_riitä(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual((self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2),self.kassapaate.edulliset,self.maksukortti2.saldo),(False,0,100))

    def test_kortin_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti2,500)
        self.assertEqual((self.maksukortti2.saldo, self.kassapaate.kassassa_rahaa),(600,100500))

    def test_kortin_lataus_negatiivinen_raha(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti2,-500)
        self.assertEqual(self.maksukortti2.saldo,100)