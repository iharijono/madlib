#
# File:                              test_api.py
# Description:                       Unit Tests for api.py
# Created at:                        05/17/2021
# Owner:                             Indra G. Harijono
#
# Requires:                          python 3.x.x
#                                    requests
#                                    
# Remarks:                           none
#
#
#
#
# 
import unittest
from unittest.mock import patch
import api

class TestInvokeGlitchURL(unittest.TestCase):
    """
    Test api:get_glitch_data

    REMARKS: it is actually NOT a unit test, but it calls the URL for real
    """
    def test_url_error(self):
        data, msg = api.get_glitch_data(api.GLITCH_URL_ADJ + "_not_valid")
        self.assertNotEqual(msg, '')
        self.assertIsNone(data)
        self.assertTrue('Http Error: 404 Client Error: Not Found' in msg)

    def test_adjective_ok(self):
        data, msg = api.get_glitch_data(api.GLITCH_URL_ADJ)
        self.assertEqual(msg, '')
        self.assertIsNotNone(data)
        
    def test_verb_ok(self):
        data, msg = api.get_glitch_data(api.GLITCH_URL_VERB)
        self.assertEqual(msg, '')
        self.assertIsNotNone(data)

    def test_noun_ok(self):
        data, msg = api.get_glitch_data(api.GLITCH_URL_NOUN)
        self.assertEqual(msg, '')
        self.assertIsNotNone(data)

class TestMadlibAPI(unittest.TestCase):
    """
    Test api:madlib (or /madlib)

    REMARKS: it is actually NOT a unit test, but it calls the URL for real
        - the last test is using Mock (patch) to ensure the non-randomness of the result of requests GET on the URL.
          Without 'patch' the test will become undeterministic, which is not wanted for testing
    """
    def test_madlib_adj_error(self):
        GLITCH_URL_ADJ_ORG = api.GLITCH_URL_ADJ
        api.GLITCH_URL_ADJ = api.GLITCH_URL_ADJ + "_not_valid"
        templ = api.madlib()
        api.GLITCH_URL_ADJ = GLITCH_URL_ADJ_ORG
        self.assertTrue('adjective_not_valid received error with message Http Error: 404 Client Error: Not Found' in templ)

    def test_madlib_verb_error(self):
        GLITCH_URL_VERB_ORG = api.GLITCH_URL_VERB
        api.GLITCH_URL_VERB = api.GLITCH_URL_VERB + "_not_valid"
        templ = api.madlib()
        api.GLITCH_URL_VERB = GLITCH_URL_VERB_ORG
        self.assertTrue('verb_not_valid received error with message Http Error: 404 Client Error: Not Found' in templ)

    def test_madlib_noun_error(self):
        GLITCH_URL_NOUN_ORG = api.GLITCH_URL_NOUN
        api.GLITCH_URL_NOUN = api.GLITCH_URL_NOUN + "_not_valid"
        templ = api.madlib()
        api.GLITCH_URL_NOUN = GLITCH_URL_NOUN_ORG
        self.assertTrue('noun_not_valid received error with message Http Error: 404 Client Error: Not Found' in templ)

    @patch('api.get_glitch_data', side_effect=[("hot", ""), ("get", ""), ("vegetable", "")])
    def test_madlib_ok(self, mocked_get_glitch_data_func):
        templ = api.madlib()
        self.assertEqual(templ, 'It was a hot day. I went downstairs to see if I could get dinner. I asked, "Does the stew need fresh vegetable?"')


def run_tests():
    # Run the tests in all classes defined here
    test_classes_to_run = [TestInvokeGlitchURL, TestMadlibAPI]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_test_suites = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    results = runner.run(all_test_suites)

if __name__ == '__main__':
    unittest.main()