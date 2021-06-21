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

class VideoResult(object):
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
        'image': 'str',
        'source': 'str',
        'uploader': 'str',
        'date_time': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'image': 'image',
        'source': 'source',
        'uploader': 'uploader',
        'date_time': 'date_time'
    }

    def __init__(self, title=None, url=None, image=None, source=None, uploader=None, date_time=None):  # noqa: E501
        """VideoResult - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._url = None
        self._image = None
        self._source = None
        self._uploader = None
        self._date_time = None
        self.discriminator = None
        self.title = title
        self.url = url
        if image is not None:
            self.image = image
        if source is not None:
            self.source = source
        if uploader is not None:
            self.uploader = uploader
        if date_time is not None:
            self.date_time = date_time

    @property
    def title(self):
        """Gets the title of this VideoResult.  # noqa: E501

        Browser title of the video source page.  # noqa: E501

        :return: The title of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VideoResult.

        Browser title of the video source page.  # noqa: E501

        :param title: The title of this VideoResult.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def url(self):
        """Gets the url of this VideoResult.  # noqa: E501

        URL of the video.  # noqa: E501

        :return: The url of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VideoResult.

        URL of the video.  # noqa: E501

        :param url: The url of this VideoResult.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def image(self):
        """Gets the image of this VideoResult.  # noqa: E501

        The preview image of the video if available.  # noqa: E501

        :return: The image of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this VideoResult.

        The preview image of the video if available.  # noqa: E501

        :param image: The image of this VideoResult.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def source(self):
        """Gets the source of this VideoResult.  # noqa: E501

        The platform that hosts the video.  # noqa: E501

        :return: The source of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this VideoResult.

        The platform that hosts the video.  # noqa: E501

        :param source: The source of this VideoResult.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def uploader(self):
        """Gets the uploader of this VideoResult.  # noqa: E501

        The entity who has uploaded the video.  # noqa: E501

        :return: The uploader of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """Sets the uploader of this VideoResult.

        The entity who has uploaded the video.  # noqa: E501

        :param uploader: The uploader of this VideoResult.  # noqa: E501
        :type: str
        """

        self._uploader = uploader

    @property
    def date_time(self):
        """Gets the date_time of this VideoResult.  # noqa: E501

        The date & time when the video was published on the source.  # noqa: E501

        :return: The date_time of this VideoResult.  # noqa: E501
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this VideoResult.

        The date & time when the video was published on the source.  # noqa: E501

        :param date_time: The date_time of this VideoResult.  # noqa: E501
        :type: str
        """

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
        if issubclass(VideoResult, dict):
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
        if not isinstance(other, VideoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other