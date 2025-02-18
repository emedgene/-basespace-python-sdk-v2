# coding: utf-8

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V2InstrumentStatsBin(object):
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
        'from_date': 'DateTimeOffset',
        'to_date': 'DateTimeOffset',
        'total_run_time': 'float'
    }

    attribute_map = {
        'from_date': 'FromDate',
        'to_date': 'ToDate',
        'total_run_time': 'TotalRunTime'
    }

    def __init__(self, from_date=None, to_date=None, total_run_time=None):  # noqa: E501
        """V2InstrumentStatsBin - a model defined in Swagger"""  # noqa: E501
        self._from_date = None
        self._to_date = None
        self._total_run_time = None
        self.discriminator = None
        self.from_date = from_date
        self.to_date = to_date
        self.total_run_time = total_run_time

    @property
    def from_date(self):
        """Gets the from_date of this V2InstrumentStatsBin.  # noqa: E501


        :return: The from_date of this V2InstrumentStatsBin.  # noqa: E501
        :rtype: DateTimeOffset
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this V2InstrumentStatsBin.


        :param from_date: The from_date of this V2InstrumentStatsBin.  # noqa: E501
        :type: DateTimeOffset
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this V2InstrumentStatsBin.  # noqa: E501


        :return: The to_date of this V2InstrumentStatsBin.  # noqa: E501
        :rtype: DateTimeOffset
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this V2InstrumentStatsBin.


        :param to_date: The to_date of this V2InstrumentStatsBin.  # noqa: E501
        :type: DateTimeOffset
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def total_run_time(self):
        """Gets the total_run_time of this V2InstrumentStatsBin.  # noqa: E501


        :return: The total_run_time of this V2InstrumentStatsBin.  # noqa: E501
        :rtype: float
        """
        return self._total_run_time

    @total_run_time.setter
    def total_run_time(self, total_run_time):
        """Sets the total_run_time of this V2InstrumentStatsBin.


        :param total_run_time: The total_run_time of this V2InstrumentStatsBin.  # noqa: E501
        :type: float
        """
        if total_run_time is None:
            raise ValueError("Invalid value for `total_run_time`, must not be `None`")  # noqa: E501

        self._total_run_time = total_run_time

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
        if issubclass(V2InstrumentStatsBin, dict):
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
        if not isinstance(other, V2InstrumentStatsBin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
