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

class Read(object):
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
        'read_number': 'int',
        'is_indexed': 'bool',
        'total_cycles': 'int',
        'yield_total': 'float',
        'projected_total_yield': 'float',
        'percent_aligned': 'float',
        'error_rate': 'float',
        'intensity_cycle1': 'float',
        'percent_gt_q30': 'float',
        'percent_gt_q30_last10_cycles': 'float'
    }

    attribute_map = {
        'read_number': 'ReadNumber',
        'is_indexed': 'IsIndexed',
        'total_cycles': 'TotalCycles',
        'yield_total': 'YieldTotal',
        'projected_total_yield': 'ProjectedTotalYield',
        'percent_aligned': 'PercentAligned',
        'error_rate': 'ErrorRate',
        'intensity_cycle1': 'IntensityCycle1',
        'percent_gt_q30': 'PercentGtQ30',
        'percent_gt_q30_last10_cycles': 'PercentGtQ30Last10Cycles'
    }

    def __init__(self, read_number=None, is_indexed=None, total_cycles=None, yield_total=None, projected_total_yield=None, percent_aligned=None, error_rate=None, intensity_cycle1=None, percent_gt_q30=None, percent_gt_q30_last10_cycles=None):  # noqa: E501
        """Read - a model defined in Swagger"""  # noqa: E501
        self._read_number = None
        self._is_indexed = None
        self._total_cycles = None
        self._yield_total = None
        self._projected_total_yield = None
        self._percent_aligned = None
        self._error_rate = None
        self._intensity_cycle1 = None
        self._percent_gt_q30 = None
        self._percent_gt_q30_last10_cycles = None
        self.discriminator = None
        if read_number is not None:
            self.read_number = read_number
        if is_indexed is not None:
            self.is_indexed = is_indexed
        if total_cycles is not None:
            self.total_cycles = total_cycles
        if yield_total is not None:
            self.yield_total = yield_total
        if projected_total_yield is not None:
            self.projected_total_yield = projected_total_yield
        if percent_aligned is not None:
            self.percent_aligned = percent_aligned
        if error_rate is not None:
            self.error_rate = error_rate
        if intensity_cycle1 is not None:
            self.intensity_cycle1 = intensity_cycle1
        if percent_gt_q30 is not None:
            self.percent_gt_q30 = percent_gt_q30
        if percent_gt_q30_last10_cycles is not None:
            self.percent_gt_q30_last10_cycles = percent_gt_q30_last10_cycles

    @property
    def read_number(self):
        """Gets the read_number of this Read.  # noqa: E501


        :return: The read_number of this Read.  # noqa: E501
        :rtype: int
        """
        return self._read_number

    @read_number.setter
    def read_number(self, read_number):
        """Sets the read_number of this Read.


        :param read_number: The read_number of this Read.  # noqa: E501
        :type: int
        """

        self._read_number = read_number

    @property
    def is_indexed(self):
        """Gets the is_indexed of this Read.  # noqa: E501


        :return: The is_indexed of this Read.  # noqa: E501
        :rtype: bool
        """
        return self._is_indexed

    @is_indexed.setter
    def is_indexed(self, is_indexed):
        """Sets the is_indexed of this Read.


        :param is_indexed: The is_indexed of this Read.  # noqa: E501
        :type: bool
        """

        self._is_indexed = is_indexed

    @property
    def total_cycles(self):
        """Gets the total_cycles of this Read.  # noqa: E501


        :return: The total_cycles of this Read.  # noqa: E501
        :rtype: int
        """
        return self._total_cycles

    @total_cycles.setter
    def total_cycles(self, total_cycles):
        """Sets the total_cycles of this Read.


        :param total_cycles: The total_cycles of this Read.  # noqa: E501
        :type: int
        """

        self._total_cycles = total_cycles

    @property
    def yield_total(self):
        """Gets the yield_total of this Read.  # noqa: E501


        :return: The yield_total of this Read.  # noqa: E501
        :rtype: float
        """
        return self._yield_total

    @yield_total.setter
    def yield_total(self, yield_total):
        """Sets the yield_total of this Read.


        :param yield_total: The yield_total of this Read.  # noqa: E501
        :type: float
        """

        self._yield_total = yield_total

    @property
    def projected_total_yield(self):
        """Gets the projected_total_yield of this Read.  # noqa: E501


        :return: The projected_total_yield of this Read.  # noqa: E501
        :rtype: float
        """
        return self._projected_total_yield

    @projected_total_yield.setter
    def projected_total_yield(self, projected_total_yield):
        """Sets the projected_total_yield of this Read.


        :param projected_total_yield: The projected_total_yield of this Read.  # noqa: E501
        :type: float
        """

        self._projected_total_yield = projected_total_yield

    @property
    def percent_aligned(self):
        """Gets the percent_aligned of this Read.  # noqa: E501


        :return: The percent_aligned of this Read.  # noqa: E501
        :rtype: float
        """
        return self._percent_aligned

    @percent_aligned.setter
    def percent_aligned(self, percent_aligned):
        """Sets the percent_aligned of this Read.


        :param percent_aligned: The percent_aligned of this Read.  # noqa: E501
        :type: float
        """

        self._percent_aligned = percent_aligned

    @property
    def error_rate(self):
        """Gets the error_rate of this Read.  # noqa: E501


        :return: The error_rate of this Read.  # noqa: E501
        :rtype: float
        """
        return self._error_rate

    @error_rate.setter
    def error_rate(self, error_rate):
        """Sets the error_rate of this Read.


        :param error_rate: The error_rate of this Read.  # noqa: E501
        :type: float
        """

        self._error_rate = error_rate

    @property
    def intensity_cycle1(self):
        """Gets the intensity_cycle1 of this Read.  # noqa: E501


        :return: The intensity_cycle1 of this Read.  # noqa: E501
        :rtype: float
        """
        return self._intensity_cycle1

    @intensity_cycle1.setter
    def intensity_cycle1(self, intensity_cycle1):
        """Sets the intensity_cycle1 of this Read.


        :param intensity_cycle1: The intensity_cycle1 of this Read.  # noqa: E501
        :type: float
        """

        self._intensity_cycle1 = intensity_cycle1

    @property
    def percent_gt_q30(self):
        """Gets the percent_gt_q30 of this Read.  # noqa: E501


        :return: The percent_gt_q30 of this Read.  # noqa: E501
        :rtype: float
        """
        return self._percent_gt_q30

    @percent_gt_q30.setter
    def percent_gt_q30(self, percent_gt_q30):
        """Sets the percent_gt_q30 of this Read.


        :param percent_gt_q30: The percent_gt_q30 of this Read.  # noqa: E501
        :type: float
        """

        self._percent_gt_q30 = percent_gt_q30

    @property
    def percent_gt_q30_last10_cycles(self):
        """Gets the percent_gt_q30_last10_cycles of this Read.  # noqa: E501


        :return: The percent_gt_q30_last10_cycles of this Read.  # noqa: E501
        :rtype: float
        """
        return self._percent_gt_q30_last10_cycles

    @percent_gt_q30_last10_cycles.setter
    def percent_gt_q30_last10_cycles(self, percent_gt_q30_last10_cycles):
        """Sets the percent_gt_q30_last10_cycles of this Read.


        :param percent_gt_q30_last10_cycles: The percent_gt_q30_last10_cycles of this Read.  # noqa: E501
        :type: float
        """

        self._percent_gt_q30_last10_cycles = percent_gt_q30_last10_cycles

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
        if issubclass(Read, dict):
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
        if not isinstance(other, Read):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
