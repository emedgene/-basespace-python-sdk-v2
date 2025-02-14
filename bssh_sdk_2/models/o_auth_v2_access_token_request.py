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

class OAuthV2AccessTokenRequest(object):
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
        'grant_type': 'str',
        'code': 'str',
        'redirect_uri': 'str',
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'code': 'code',
        'redirect_uri': 'redirect_uri',
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    }

    def __init__(self, grant_type=None, code=None, redirect_uri=None, client_id=None, client_secret=None):  # noqa: E501
        """OAuthV2AccessTokenRequest - a model defined in Swagger"""  # noqa: E501
        self._grant_type = None
        self._code = None
        self._redirect_uri = None
        self._client_id = None
        self._client_secret = None
        self.discriminator = None
        if grant_type is not None:
            self.grant_type = grant_type
        if code is not None:
            self.code = code
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def grant_type(self):
        """Gets the grant_type of this OAuthV2AccessTokenRequest.  # noqa: E501


        :return: The grant_type of this OAuthV2AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this OAuthV2AccessTokenRequest.


        :param grant_type: The grant_type of this OAuthV2AccessTokenRequest.  # noqa: E501
        :type: str
        """

        self._grant_type = grant_type

    @property
    def code(self):
        """Gets the code of this OAuthV2AccessTokenRequest.  # noqa: E501


        :return: The code of this OAuthV2AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this OAuthV2AccessTokenRequest.


        :param code: The code of this OAuthV2AccessTokenRequest.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this OAuthV2AccessTokenRequest.  # noqa: E501


        :return: The redirect_uri of this OAuthV2AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this OAuthV2AccessTokenRequest.


        :param redirect_uri: The redirect_uri of this OAuthV2AccessTokenRequest.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def client_id(self):
        """Gets the client_id of this OAuthV2AccessTokenRequest.  # noqa: E501


        :return: The client_id of this OAuthV2AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OAuthV2AccessTokenRequest.


        :param client_id: The client_id of this OAuthV2AccessTokenRequest.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this OAuthV2AccessTokenRequest.  # noqa: E501


        :return: The client_secret of this OAuthV2AccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OAuthV2AccessTokenRequest.


        :param client_secret: The client_secret of this OAuthV2AccessTokenRequest.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

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
        if issubclass(OAuthV2AccessTokenRequest, dict):
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
        if not isinstance(other, OAuthV2AccessTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
