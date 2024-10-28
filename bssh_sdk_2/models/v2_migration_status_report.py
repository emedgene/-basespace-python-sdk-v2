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

class V2MigrationStatusReport(object):
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
        'total_entity_count': 'int',
        'unmigrated_count': 'int',
        'in_progress_count': 'int',
        'completed_count': 'int',
        'biosample_generation_code_feature_date': 'datetime'
    }

    attribute_map = {
        'total_entity_count': 'TotalEntityCount',
        'unmigrated_count': 'UnmigratedCount',
        'in_progress_count': 'InProgressCount',
        'completed_count': 'CompletedCount',
        'biosample_generation_code_feature_date': 'BiosampleGenerationCodeFeatureDate'
    }

    def __init__(self, total_entity_count=None, unmigrated_count=None, in_progress_count=None, completed_count=None, biosample_generation_code_feature_date=None):  # noqa: E501
        """V2MigrationStatusReport - a model defined in Swagger"""  # noqa: E501
        self._total_entity_count = None
        self._unmigrated_count = None
        self._in_progress_count = None
        self._completed_count = None
        self._biosample_generation_code_feature_date = None
        self.discriminator = None
        if total_entity_count is not None:
            self.total_entity_count = total_entity_count
        if unmigrated_count is not None:
            self.unmigrated_count = unmigrated_count
        if in_progress_count is not None:
            self.in_progress_count = in_progress_count
        if completed_count is not None:
            self.completed_count = completed_count
        if biosample_generation_code_feature_date is not None:
            self.biosample_generation_code_feature_date = biosample_generation_code_feature_date

    @property
    def total_entity_count(self):
        """Gets the total_entity_count of this V2MigrationStatusReport.  # noqa: E501


        :return: The total_entity_count of this V2MigrationStatusReport.  # noqa: E501
        :rtype: int
        """
        return self._total_entity_count

    @total_entity_count.setter
    def total_entity_count(self, total_entity_count):
        """Sets the total_entity_count of this V2MigrationStatusReport.


        :param total_entity_count: The total_entity_count of this V2MigrationStatusReport.  # noqa: E501
        :type: int
        """

        self._total_entity_count = total_entity_count

    @property
    def unmigrated_count(self):
        """Gets the unmigrated_count of this V2MigrationStatusReport.  # noqa: E501


        :return: The unmigrated_count of this V2MigrationStatusReport.  # noqa: E501
        :rtype: int
        """
        return self._unmigrated_count

    @unmigrated_count.setter
    def unmigrated_count(self, unmigrated_count):
        """Sets the unmigrated_count of this V2MigrationStatusReport.


        :param unmigrated_count: The unmigrated_count of this V2MigrationStatusReport.  # noqa: E501
        :type: int
        """

        self._unmigrated_count = unmigrated_count

    @property
    def in_progress_count(self):
        """Gets the in_progress_count of this V2MigrationStatusReport.  # noqa: E501


        :return: The in_progress_count of this V2MigrationStatusReport.  # noqa: E501
        :rtype: int
        """
        return self._in_progress_count

    @in_progress_count.setter
    def in_progress_count(self, in_progress_count):
        """Sets the in_progress_count of this V2MigrationStatusReport.


        :param in_progress_count: The in_progress_count of this V2MigrationStatusReport.  # noqa: E501
        :type: int
        """

        self._in_progress_count = in_progress_count

    @property
    def completed_count(self):
        """Gets the completed_count of this V2MigrationStatusReport.  # noqa: E501


        :return: The completed_count of this V2MigrationStatusReport.  # noqa: E501
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count):
        """Sets the completed_count of this V2MigrationStatusReport.


        :param completed_count: The completed_count of this V2MigrationStatusReport.  # noqa: E501
        :type: int
        """

        self._completed_count = completed_count

    @property
    def biosample_generation_code_feature_date(self):
        """Gets the biosample_generation_code_feature_date of this V2MigrationStatusReport.  # noqa: E501


        :return: The biosample_generation_code_feature_date of this V2MigrationStatusReport.  # noqa: E501
        :rtype: datetime
        """
        return self._biosample_generation_code_feature_date

    @biosample_generation_code_feature_date.setter
    def biosample_generation_code_feature_date(self, biosample_generation_code_feature_date):
        """Sets the biosample_generation_code_feature_date of this V2MigrationStatusReport.


        :param biosample_generation_code_feature_date: The biosample_generation_code_feature_date of this V2MigrationStatusReport.  # noqa: E501
        :type: datetime
        """

        self._biosample_generation_code_feature_date = biosample_generation_code_feature_date

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
        if issubclass(V2MigrationStatusReport, dict):
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
        if not isinstance(other, V2MigrationStatusReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
