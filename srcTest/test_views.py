import unittest
from flask import Flask
from flask_testing import TestCase
import views



class TestIndex(TestCase):
    render_templates = False
    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app = views.app.test_client()
        self.client = self.app.test_client(use_cookie=True)

    def tearDown(self):
        self.app_context.pop()

    def test_get_index(self):
        response = self.app.get('/cadastros')
        self.assertTemplateUsed('consulta_cadastro.html')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

