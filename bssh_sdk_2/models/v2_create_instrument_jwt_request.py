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

class V2CreateInstrumentJwtRequest(object):
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
        'scope': 'str',
        'app_family_slug': 'str'
    }

    attribute_map = {
        'scope': 'Scope',
        'app_family_slug': 'AppFamilySlug'
    }

    def __init__(self, scope=None, app_family_slug=None):  # noqa: E501
        """V2CreateInstrumentJwtRequest - a model defined in Swagger"""  # noqa: E501
        self._scope = None
        self._app_family_slug = None
        self.discriminator = None
        self.scope = scope
        self.app_family_slug = app_family_slug

    @property
    def scope(self):
        """Gets the scope of this V2CreateInstrumentJwtRequest.  # noqa: E501


        :return: The scope of this V2CreateInstrumentJwtRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this V2CreateInstrumentJwtRequest.


        :param scope: The scope of this V2CreateInstrumentJwtRequest.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def app_family_slug(self):
        """Gets the app_family_slug of this V2CreateInstrumentJwtRequest.  # noqa: E501


        :return: The app_family_slug of this V2CreateInstrumentJwtRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_family_slug

    @app_family_slug.setter
    def app_family_slug(self, app_family_slug):
        """Sets the app_family_slug of this V2CreateInstrumentJwtRequest.


        :param app_family_slug: The app_family_slug of this V2CreateInstrumentJwtRequest.  # noqa: E501
        :type: str
        """
        if app_family_slug is None:
            raise ValueError("Invalid value for `app_family_slug`, must not be `None`")  # noqa: E501

        self._app_family_slug = app_family_slug

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
        if issubclass(V2CreateInstrumentJwtRequest, dict):
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
        if not isinstance(other, V2CreateInstrumentJwtRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
