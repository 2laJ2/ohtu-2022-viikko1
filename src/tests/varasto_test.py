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
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_lisaa_tilaa2(self):
        self.varasto.lisaa_varastoon(11)

        self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran2(self):
        self.varasto.ota_varastosta(7)

        saatu_maara = self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_tayteen_ylimaara_hukkaan(self):
        self.varasto.lisaa_varastoon(11)

        self.varasto.ota_varastosta(5)

        self.varasto.lisaa_varastoon(2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 3)

    def test_tyhjasta_varastosta_ei_voi_ottaa(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(4), 0)

    def test_varastoon_ei_voi_lisata_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(4), 0)

    def test_varastosta_ei_voi_ottaa_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-8),0)

    def test_testataan_saldoa(self):
        saatu_maara = self.varasto.__str__()

        self.assertAlmostEqual(saatu_maara, "saldo = 0, vielä tilaa 10")

    def test_tehdaan_pienempi_varasto_kuin_saldo(container):
        container.varasto = Varasto(0, 5)

        container.assertAlmostEqual(container.varasto.paljonko_mahtuu(), 0)

    def test_tehdaan_negatiivinen_varasto(container):
        container.varasto = Varasto(-6, 0)

        container.assertAlmostEqual(container.varasto.paljonko_mahtuu(), 6)

    def test_tehdaan_negatiivinen_alku_saldo(container):
        container.varasto = Varasto(0, -6)

        container.assertAlmostEqual(container.varasto.paljonko_mahtuu(), 0)
