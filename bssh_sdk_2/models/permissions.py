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

class Permissions(object):
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
        'user_operations': 'list[str]',
        'access_token_operations': 'list[str]'
    }

    attribute_map = {
        'user_operations': 'UserOperations',
        'access_token_operations': 'AccessTokenOperations'
    }

    def __init__(self, user_operations=None, access_token_operations=None):  # noqa: E501
        """Permissions - a model defined in Swagger"""  # noqa: E501
        self._user_operations = None
        self._access_token_operations = None
        self.discriminator = None
        if user_operations is not None:
            self.user_operations = user_operations
        if access_token_operations is not None:
            self.access_token_operations = access_token_operations

    @property
    def user_operations(self):
        """Gets the user_operations of this Permissions.  # noqa: E501


        :return: The user_operations of this Permissions.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_operations

    @user_operations.setter
    def user_operations(self, user_operations):
        """Sets the user_operations of this Permissions.


        :param user_operations: The user_operations of this Permissions.  # noqa: E501
        :type: list[str]
        """

        self._user_operations = user_operations

    @property
    def access_token_operations(self):
        """Gets the access_token_operations of this Permissions.  # noqa: E501


        :return: The access_token_operations of this Permissions.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_token_operations

    @access_token_operations.setter
    def access_token_operations(self, access_token_operations):
        """Sets the access_token_operations of this Permissions.


        :param access_token_operations: The access_token_operations of this Permissions.  # noqa: E501
        :type: list[str]
        """

        self._access_token_operations = access_token_operations

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
        if issubclass(Permissions, dict):
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
        if not isinstance(other, Permissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
