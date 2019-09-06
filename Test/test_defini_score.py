from unittest import TestCase
from controllers.regra_score import gerar_credito, defini_score, formataDecimal, formataCpf, Decimal
import random


class TestDefini_score(TestCase):

    def test_se_score_esta_dentro_do_range(self):
        novo_score = defini_score()
        self.assertTrue( novo_score >= 1 and novo_score <= 999)

    def test_gerar_credito_credito_reprovado(self):
        renda = '1000,00'
        score = random.randint(1, 300)
        credito = gerar_credito(renda, score)
        self.assertEqual('Crédito Reprovado', credito)

    def test_gerar_credito_credito_limitado_de_mil(self):
        renda = '1000,00'
        score = random.randint(300, 600)
        credito = gerar_credito(renda, score)
        self.assertEqual('1000.00', credito)

    def test_gerar_credito_credito_metade_da_renda(self):
        renda = '3500,90'
        score = random.randint(600, 800)
        credito = gerar_credito(renda, score)
        self.assertEqual('1750.45', credito)


    def test_gerar_credito_credito_metade_da_renda_limitado_a_mil(self):
        renda = '1750,00'
        score = random.randint(600, 800)
        credito = gerar_credito(renda, score)
        self.assertEqual('1000.00', credito)

    def test_gerar_credito_credito_duas_vezes_valor_da_renda(self):
        renda = '7500,00'
        score = random.randint(800, 952)
        credito = gerar_credito(renda, score)
        self.assertEqual('15000.00', credito)

    def test_gerar_credito_credito_sem_limite(self):
        renda = '7500,00'
        score = random.randint(951, 999)
        credito = gerar_credito(renda, score)
        self.assertEqual('1000000.00', credito)
