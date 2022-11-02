import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varastot = [Varasto(10), Varasto(-1, -1), Varasto(2, 5)]


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varastot[0].saldo, 0)
    
    def test_alkusaldo_ei_ole_negatiivinen(self):
        self.assertAlmostEqual(self.varastot[1].saldo, 0)
    
    def test_alkusaldo_ei_ylita_tilavuutta(self):
        self.assertAlmostEqual(self.varastot[2].saldo, 2)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varastot[0].tilavuus, 10)
    
    def test_tilavuus_ei_ole_negatiivinen(self):
        self.assertAlmostEqual(self.varastot[1].tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varastot[0].lisaa_varastoon(8)

        self.assertAlmostEqual(self.varastot[0].saldo, 8)

    def test_lisays_ei_pysty_vahentamaan_saldo(self):
        self.varastot[0].lisaa_varastoon(5)
        self.varastot[0].lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varastot[0].saldo, 5)
    
    def test_saldo_ei_ylita_tilavuutta_lisayksen_jalkeen(self):
        self.varastot[0].lisaa_varastoon(11)

        self.assertAlmostEqual(self.varastot[0].saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varastot[0].lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varastot[0].paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varastot[0].lisaa_varastoon(8)

        saatu_maara = self.varastot[0].ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_ottaminen_ei_kasva_saldoa(self):
        self.varastot[0].ota_varastosta(-1)

        self.assertAlmostEqual(self.varastot[0].saldo, 0)
    
    def test_saldo_rajoittaa_ottaminen(self):
        saatu_maara = self.varastot[2].ota_varastosta(8)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varastot[0].lisaa_varastoon(8)

        self.varastot[0].ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varastot[0].paljonko_mahtuu(), 4)
    
    def test_Varasto_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(self.varastot[2].__str__(), f"saldo = {2}, vielä tilaa {0}")
