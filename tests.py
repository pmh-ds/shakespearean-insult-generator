from shakespearean_insult_generator import app
import unittest


class ShakespeareanInsultGeneratorTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_insult_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_insult_name_status_code(self):
        response = self.app.get('/Frodo')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
