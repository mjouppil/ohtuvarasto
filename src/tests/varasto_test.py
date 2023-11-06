import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varastoNeg = Varasto(-1)
        self.varastoSaldoNeg = Varasto(10, -1)
        self.varastoOver = Varasto(10, 11)
        
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
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        
    def test_lisaa_negatiivinen_maara(self):
        sal1 = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, sal1)
        
    def test_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)
        
    def test_varastoNeg_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varastoNeg.tilavuus, 0)
        
    def test_varastoSaldoNeg_oikea_saldo(self):
        self.assertAlmostEqual(self.varastoSaldoNeg.saldo, 0)
        
    def test_varastoOver_oikea_saldo(self):
        self.assertAlmostEqual(self.varastoOver.saldo, 10)
        
    def test_ota_kaikki(self):
        sal1 = self.varasto.saldo
        saatu_maara = self.varasto.ota_varastosta(sal1)
        self.assertAlmostEqual(saatu_maara, sal1)
        
    def test_lisaa_tayteen(self):
        self.varasto.lisaa_varastoon(5)
        lis1 = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(lis1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        
    def test_ota_liikaa(self):
        self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus123)
        
    def test_tulosta_tiedot(self):
    	print(self.varasto)
        
        
        
        
