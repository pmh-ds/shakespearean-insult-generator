import unittest
import urllib2
from flask import Flask
from flask_testing import TestCase
from mock import mock_open, patch

from shakespearean_insult_generator import app
from shakespearean_insult_generator.views import read_insults, generate_insult


class ShakespeareanInsultGeneratorTests(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.test_name = 'Frodo'
        self.test_insults_start = ["artless"]
        self.test_insults_middle = ["base-court"]
        self.test_insults_end = ["apple-john"]
        self.test_insult_file = ','.join(self.test_insults_start
                                         + self.test_insults_middle
                                         + self.test_insults_end)
        self.test_insult = ' '.join(self.test_insults_start
                                    + self.test_insults_middle
                                    + self.test_insults_end)

    def tearDown(self):
        pass

    def test_insult_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_insult_name_route(self):
        response = self.client.get('/{test_name}'.format(test_name=self.test_name))
        self.assertEqual(response.status_code, 200)

    def test_insult(self):
        with patch('shakespearean_insult_generator.views.generate_insult',
                   return_value=self.test_insult):
            self.client.get('/')
            self.assert_template_used('index.html')
            self.assert_context('insult',  "Thou {insult}".format(insult=self.test_insult))

    def test_insult_name(self):
        with patch('shakespearean_insult_generator.views.generate_insult',
                   return_value=self.test_insult):
            self.client.get('/{name}'.format(name=self.test_name))
            self.assert_template_used('index.html')
            self.assert_context('insult',
                                "{test_name}, thou {insult}".format(test_name=self.test_name,
                                                                    insult=self.test_insult))

    def test_read_insult(self):
        mocked_open = mock_open(read_data=self.test_insult_file)
        with patch('shakespearean_insult_generator.views.open', mocked_open, create=True):
            insults_start, insults_middle, insults_end = read_insults("test.csv")
            self.assertEqual(len(insults_start), 1)
            self.assertEqual(len(insults_middle), 1)
            self.assertEqual(len(insults_end), 1)
            self.assertEqual(insults_start[0], self.test_insults_start[0])
            self.assertEqual(insults_middle[0], self.test_insults_middle[0])
            self.assertEqual(insults_end[0], self.test_insults_end[0])

    def test_generate_insult(self):
        self.assertEqual(generate_insult(self.test_insults_start,
                                         self.test_insults_middle,
                                         self.test_insults_end),
                         self.test_insult)


if __name__ == '__main__':
    unittest.main()
