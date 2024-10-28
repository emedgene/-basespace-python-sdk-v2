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

class V2SignAgreementRequest(object):
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
        'agreement_id': 'str'
    }

    attribute_map = {
        'agreement_id': 'AgreementId'
    }

    def __init__(self, agreement_id=None):  # noqa: E501
        """V2SignAgreementRequest - a model defined in Swagger"""  # noqa: E501
        self._agreement_id = None
        self.discriminator = None
        self.agreement_id = agreement_id

    @property
    def agreement_id(self):
        """Gets the agreement_id of this V2SignAgreementRequest.  # noqa: E501


        :return: The agreement_id of this V2SignAgreementRequest.  # noqa: E501
        :rtype: str
        """
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, agreement_id):
        """Sets the agreement_id of this V2SignAgreementRequest.


        :param agreement_id: The agreement_id of this V2SignAgreementRequest.  # noqa: E501
        :type: str
        """
        if agreement_id is None:
            raise ValueError("Invalid value for `agreement_id`, must not be `None`")  # noqa: E501

        self._agreement_id = agreement_id

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
        if issubclass(V2SignAgreementRequest, dict):
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
        if not isinstance(other, V2SignAgreementRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
