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

class V2DatasetAttributeDefinition(object):
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
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'is_required': 'bool',
        'default': 'object',
        'type': 'str',
        'pattern': 'str',
        'min_length': 'int',
        'max_length': 'int',
        'minimum': 'float',
        'maximum': 'float'
    }

    attribute_map = {
        'name': 'Name',
        'title': 'Title',
        'description': 'Description',
        'is_required': 'IsRequired',
        'default': 'Default',
        'type': 'Type',
        'pattern': 'Pattern',
        'min_length': 'MinLength',
        'max_length': 'MaxLength',
        'minimum': 'Minimum',
        'maximum': 'Maximum'
    }

    def __init__(self, name=None, title=None, description=None, is_required=None, default=None, type=None, pattern=None, min_length=None, max_length=None, minimum=None, maximum=None):  # noqa: E501
        """V2DatasetAttributeDefinition - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._title = None
        self._description = None
        self._is_required = None
        self._default = None
        self._type = None
        self._pattern = None
        self._min_length = None
        self._max_length = None
        self._minimum = None
        self._maximum = None
        self.discriminator = None
        self.name = name
        self.title = title
        self.description = description
        self.is_required = is_required
        self.default = default
        self.type = type
        self.pattern = pattern
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum

    @property
    def name(self):
        """Gets the name of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The name of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2DatasetAttributeDefinition.


        :param name: The name of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The title of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this V2DatasetAttributeDefinition.


        :param title: The title of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The description of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V2DatasetAttributeDefinition.


        :param description: The description of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def is_required(self):
        """Gets the is_required of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The is_required of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this V2DatasetAttributeDefinition.


        :param is_required: The is_required of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: bool
        """
        if is_required is None:
            raise ValueError("Invalid value for `is_required`, must not be `None`")  # noqa: E501

        self._is_required = is_required

    @property
    def default(self):
        """Gets the default of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The default of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V2DatasetAttributeDefinition.


        :param default: The default of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: object
        """
        if default is None:
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def type(self):
        """Gets the type of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The type of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V2DatasetAttributeDefinition.


        :param type: The type of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def pattern(self):
        """Gets the pattern of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The pattern of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this V2DatasetAttributeDefinition.


        :param pattern: The pattern of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: str
        """
        if pattern is None:
            raise ValueError("Invalid value for `pattern`, must not be `None`")  # noqa: E501

        self._pattern = pattern

    @property
    def min_length(self):
        """Gets the min_length of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The min_length of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this V2DatasetAttributeDefinition.


        :param min_length: The min_length of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The max_length of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this V2DatasetAttributeDefinition.


        :param max_length: The max_length of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def minimum(self):
        """Gets the minimum of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The minimum of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this V2DatasetAttributeDefinition.


        :param minimum: The minimum of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: float
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this V2DatasetAttributeDefinition.  # noqa: E501


        :return: The maximum of this V2DatasetAttributeDefinition.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this V2DatasetAttributeDefinition.


        :param maximum: The maximum of this V2DatasetAttributeDefinition.  # noqa: E501
        :type: float
        """

        self._maximum = maximum

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
        if issubclass(V2DatasetAttributeDefinition, dict):
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
        if not isinstance(other, V2DatasetAttributeDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
