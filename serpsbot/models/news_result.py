# coding: utf-8

"""
    SerpsBot

    Our APIs allow data miners to harvest huge volumes of data from Google and other search engines.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NewsResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'url': 'str',
        'snippet': 'str',
        'source': 'object',
        'image': 'str',
        'date_time': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'snippet': 'snippet',
        'source': 'source',
        'image': 'image',
        'date_time': 'date_time'
    }

    def __init__(self, title=None, url=None, snippet=None, source=None, image=None, date_time=None):  # noqa: E501
        """NewsResult - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._url = None
        self._snippet = None
        self._source = None
        self._image = None
        self._date_time = None
        self.discriminator = None
        self.title = title
        self.url = url
        if snippet is not None:
            self.snippet = snippet
        self.source = source
        if image is not None:
            self.image = image
        self.date_time = date_time

    @property
    def title(self):
        """Gets the title of this NewsResult.  # noqa: E501

        Browser title of the news website page.  # noqa: E501

        :return: The title of this NewsResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewsResult.

        Browser title of the news website page.  # noqa: E501

        :param title: The title of this NewsResult.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def url(self):
        """Gets the url of this NewsResult.  # noqa: E501

        URL of the web page.  # noqa: E501

        :return: The url of this NewsResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NewsResult.

        URL of the web page.  # noqa: E501

        :param url: The url of this NewsResult.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def snippet(self):
        """Gets the snippet of this NewsResult.  # noqa: E501

        The short snippet (summary) of the news that's visible in search results.  # noqa: E501

        :return: The snippet of this NewsResult.  # noqa: E501
        :rtype: str
        """
        return self._snippet

    @snippet.setter
    def snippet(self, snippet):
        """Sets the snippet of this NewsResult.

        The short snippet (summary) of the news that's visible in search results.  # noqa: E501

        :param snippet: The snippet of this NewsResult.  # noqa: E501
        :type: str
        """

        self._snippet = snippet

    @property
    def source(self):
        """Gets the source of this NewsResult.  # noqa: E501

        Details (image and name) of the news source.  # noqa: E501

        :return: The source of this NewsResult.  # noqa: E501
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NewsResult.

        Details (image and name) of the news source.  # noqa: E501

        :param source: The source of this NewsResult.  # noqa: E501
        :type: object
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def image(self):
        """Gets the image of this NewsResult.  # noqa: E501

        Image associated to the news if available.  # noqa: E501

        :return: The image of this NewsResult.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NewsResult.

        Image associated to the news if available.  # noqa: E501

        :param image: The image of this NewsResult.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def date_time(self):
        """Gets the date_time of this NewsResult.  # noqa: E501

        The date & time when the news was published on the source.  # noqa: E501

        :return: The date_time of this NewsResult.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this NewsResult.

        The date & time when the news was published on the source.  # noqa: E501

        :param date_time: The date_time of this NewsResult.  # noqa: E501
        :type: str
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")  # noqa: E501

        self._date_time = date_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NewsResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
