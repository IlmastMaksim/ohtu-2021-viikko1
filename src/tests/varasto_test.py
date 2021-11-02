import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisaa_varastoon_nolla(self):
        saatu_maara = self.varasto.lisaa_varastoon(0)
        self.assertAlmostEqual(saatu_maara, None)
    
    def test_ota_varastosta_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(saatu_maara, 0.0)
        
    def test_merkkijono(self):
        saldo = self.varasto.saldo
        tilavuus = self.varasto.tilavuus - self.varasto.saldo

        self.assertEqual(str(self.varasto), f"saldo = {saldo}, vielä tilaa {tilavuus}")

    def test_negatiivisen_maaran_ottaiminen_ja_saaminen(self):
        ennen_ottoa = self.varasto.saldo
        self.varasto.ota_varastosta(-3)

        self.assertEqual(ennen_ottoa, self.varasto.saldo)

        ennen_lisaamista = self.varasto.saldo
        self.varasto.lisaa_varastoon(-3)

        self.assertEqual(ennen_lisaamista, self.varasto.saldo)

    def test_ottaa_lian_enemman_tilasta(self):
        self.varasto.ota_varastosta(self.varasto.saldo + 2)

        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_paljon(self):
        self.varasto.lisaa_varastoon(80)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_saldo_on_negatiivinen_tai_nolla(self):
        self.varasto = Varasto(tilavuus=8, alku_saldo=-1)

        self.assertEqual(self.varasto.saldo, 0)

        self.varasto = Varasto(tilavuus=-1)

        self.assertEqual(self.varasto.tilavuus, 0)

