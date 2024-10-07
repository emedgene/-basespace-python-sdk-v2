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

class V2UserAgreementCompact(object):
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
        'agreement': 'V2AgreementCompact',
        'status': 'str',
        'date_signed': 'datetime'
    }

    attribute_map = {
        'agreement': 'Agreement',
        'status': 'Status',
        'date_signed': 'DateSigned'
    }

    def __init__(self, agreement=None, status=None, date_signed=None):  # noqa: E501
        """V2UserAgreementCompact - a model defined in Swagger"""  # noqa: E501
        self._agreement = None
        self._status = None
        self._date_signed = None
        self.discriminator = None
        if agreement is not None:
            self.agreement = agreement
        if status is not None:
            self.status = status
        if date_signed is not None:
            self.date_signed = date_signed

    @property
    def agreement(self):
        """Gets the agreement of this V2UserAgreementCompact.  # noqa: E501


        :return: The agreement of this V2UserAgreementCompact.  # noqa: E501
        :rtype: V2AgreementCompact
        """
        return self._agreement

    @agreement.setter
    def agreement(self, agreement):
        """Sets the agreement of this V2UserAgreementCompact.


        :param agreement: The agreement of this V2UserAgreementCompact.  # noqa: E501
        :type: V2AgreementCompact
        """

        self._agreement = agreement

    @property
    def status(self):
        """Gets the status of this V2UserAgreementCompact.  # noqa: E501


        :return: The status of this V2UserAgreementCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V2UserAgreementCompact.


        :param status: The status of this V2UserAgreementCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def date_signed(self):
        """Gets the date_signed of this V2UserAgreementCompact.  # noqa: E501


        :return: The date_signed of this V2UserAgreementCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_signed

    @date_signed.setter
    def date_signed(self, date_signed):
        """Sets the date_signed of this V2UserAgreementCompact.


        :param date_signed: The date_signed of this V2UserAgreementCompact.  # noqa: E501
        :type: datetime
        """

        self._date_signed = date_signed

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
        if issubclass(V2UserAgreementCompact, dict):
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
        if not isinstance(other, V2UserAgreementCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
