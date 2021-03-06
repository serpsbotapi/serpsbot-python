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

class StatsField(object):
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
        'jobs': 'AllOfStatsFieldJobs',
        'stats_reset': 'str',
        'alltimecalls': 'int',
        'monthlycalls': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'stats_reset': 'stats_reset',
        'alltimecalls': 'alltimecalls',
        'monthlycalls': 'monthlycalls'
    }

    def __init__(self, jobs=None, stats_reset=None, alltimecalls=None, monthlycalls=None):  # noqa: E501
        """StatsField - a model defined in Swagger"""  # noqa: E501
        self._jobs = None
        self._stats_reset = None
        self._alltimecalls = None
        self._monthlycalls = None
        self.discriminator = None
        self.jobs = jobs
        self.stats_reset = stats_reset
        self.alltimecalls = alltimecalls
        self.monthlycalls = monthlycalls

    @property
    def jobs(self):
        """Gets the jobs of this StatsField.  # noqa: E501

        Statistics on the jobs that the user has launched so far.  # noqa: E501

        :return: The jobs of this StatsField.  # noqa: E501
        :rtype: AllOfStatsFieldJobs
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this StatsField.

        Statistics on the jobs that the user has launched so far.  # noqa: E501

        :param jobs: The jobs of this StatsField.  # noqa: E501
        :type: AllOfStatsFieldJobs
        """
        if jobs is None:
            raise ValueError("Invalid value for `jobs`, must not be `None`")  # noqa: E501

        self._jobs = jobs

    @property
    def stats_reset(self):
        """Gets the stats_reset of this StatsField.  # noqa: E501

        The next statistics reset date when monthly calls count will be reset to zero.  # noqa: E501

        :return: The stats_reset of this StatsField.  # noqa: E501
        :rtype: str
        """
        return self._stats_reset

    @stats_reset.setter
    def stats_reset(self, stats_reset):
        """Sets the stats_reset of this StatsField.

        The next statistics reset date when monthly calls count will be reset to zero.  # noqa: E501

        :param stats_reset: The stats_reset of this StatsField.  # noqa: E501
        :type: str
        """
        if stats_reset is None:
            raise ValueError("Invalid value for `stats_reset`, must not be `None`")  # noqa: E501

        self._stats_reset = stats_reset

    @property
    def alltimecalls(self):
        """Gets the alltimecalls of this StatsField.  # noqa: E501

        The number of API calls the user has made so far since their sign up.  # noqa: E501

        :return: The alltimecalls of this StatsField.  # noqa: E501
        :rtype: int
        """
        return self._alltimecalls

    @alltimecalls.setter
    def alltimecalls(self, alltimecalls):
        """Sets the alltimecalls of this StatsField.

        The number of API calls the user has made so far since their sign up.  # noqa: E501

        :param alltimecalls: The alltimecalls of this StatsField.  # noqa: E501
        :type: int
        """
        if alltimecalls is None:
            raise ValueError("Invalid value for `alltimecalls`, must not be `None`")  # noqa: E501

        self._alltimecalls = alltimecalls

    @property
    def monthlycalls(self):
        """Gets the monthlycalls of this StatsField.  # noqa: E501

        The number of API calls the user has made since the last monthly stats reset date.  # noqa: E501

        :return: The monthlycalls of this StatsField.  # noqa: E501
        :rtype: int
        """
        return self._monthlycalls

    @monthlycalls.setter
    def monthlycalls(self, monthlycalls):
        """Sets the monthlycalls of this StatsField.

        The number of API calls the user has made since the last monthly stats reset date.  # noqa: E501

        :param monthlycalls: The monthlycalls of this StatsField.  # noqa: E501
        :type: int
        """
        if monthlycalls is None:
            raise ValueError("Invalid value for `monthlycalls`, must not be `None`")  # noqa: E501

        self._monthlycalls = monthlycalls

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
        if issubclass(StatsField, dict):
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
        if not isinstance(other, StatsField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
