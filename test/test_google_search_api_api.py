# coding: utf-8

"""
    SerpsBot

    Our APIs allow data miners to harvest huge volumes of data from Google and other search engines.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import serpsbot
from serpsbot.api.google_search_api_api import GoogleSearchAPIApi  # noqa: E501
from serpsbot.rest import ApiException


class TestGoogleSearchAPIApi(unittest.TestCase):
    """GoogleSearchAPIApi unit test stubs"""

    def setUp(self):
        self.api = GoogleSearchAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_organic_extended_google_organic_extended_post(self):
        """Test case for organic_extended_google_organic_extended_post

        Organic Extended  # noqa: E501
        """
        pass

    def test_organic_results_google_organic_search_post(self):
        """Test case for organic_results_google_organic_search_post

        Organic Results  # noqa: E501
        """
        pass

    def test_search_suggestions_google_search_suggestions_post(self):
        """Test case for search_suggestions_google_search_suggestions_post

        Search Suggestions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
