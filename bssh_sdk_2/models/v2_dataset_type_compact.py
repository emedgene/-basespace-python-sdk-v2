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

class V2DatasetTypeCompact(object):
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
        'id': 'str',
        'href': 'str',
        'name': 'str',
        'conforms_to_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'name': 'Name',
        'conforms_to_ids': 'ConformsToIds'
    }

    def __init__(self, id=None, href=None, name=None, conforms_to_ids=None):  # noqa: E501
        """V2DatasetTypeCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._conforms_to_ids = None
        self.discriminator = None
        self.id = id
        self.href = href
        self.name = name
        self.conforms_to_ids = conforms_to_ids

    @property
    def id(self):
        """Gets the id of this V2DatasetTypeCompact.  # noqa: E501


        :return: The id of this V2DatasetTypeCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2DatasetTypeCompact.


        :param id: The id of this V2DatasetTypeCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this V2DatasetTypeCompact.  # noqa: E501


        :return: The href of this V2DatasetTypeCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2DatasetTypeCompact.


        :param href: The href of this V2DatasetTypeCompact.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def name(self):
        """Gets the name of this V2DatasetTypeCompact.  # noqa: E501


        :return: The name of this V2DatasetTypeCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2DatasetTypeCompact.


        :param name: The name of this V2DatasetTypeCompact.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def conforms_to_ids(self):
        """Gets the conforms_to_ids of this V2DatasetTypeCompact.  # noqa: E501


        :return: The conforms_to_ids of this V2DatasetTypeCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._conforms_to_ids

    @conforms_to_ids.setter
    def conforms_to_ids(self, conforms_to_ids):
        """Sets the conforms_to_ids of this V2DatasetTypeCompact.


        :param conforms_to_ids: The conforms_to_ids of this V2DatasetTypeCompact.  # noqa: E501
        :type: list[str]
        """
        if conforms_to_ids is None:
            raise ValueError("Invalid value for `conforms_to_ids`, must not be `None`")  # noqa: E501

        self._conforms_to_ids = conforms_to_ids

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
        if issubclass(V2DatasetTypeCompact, dict):
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
        if not isinstance(other, V2DatasetTypeCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
