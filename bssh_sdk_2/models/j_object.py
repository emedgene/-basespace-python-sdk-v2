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

class JObject(object):
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
        'type': 'str',
        'item': 'JToken',
        'has_values': 'bool',
        'first': 'JToken',
        'last': 'JToken',
        'count': 'int',
        'parent': 'JContainer',
        'root': 'JToken',
        'next': 'JToken',
        'previous': 'JToken',
        'path': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'item': 'Item',
        'has_values': 'HasValues',
        'first': 'First',
        'last': 'Last',
        'count': 'Count',
        'parent': 'Parent',
        'root': 'Root',
        'next': 'Next',
        'previous': 'Previous',
        'path': 'Path'
    }

    def __init__(self, type=None, item=None, has_values=None, first=None, last=None, count=None, parent=None, root=None, next=None, previous=None, path=None):  # noqa: E501
        """JObject - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._item = None
        self._has_values = None
        self._first = None
        self._last = None
        self._count = None
        self._parent = None
        self._root = None
        self._next = None
        self._previous = None
        self._path = None
        self.discriminator = None
        self.type = type
        self.item = item
        self.has_values = has_values
        self.first = first
        self.last = last
        self.count = count
        self.parent = parent
        self.root = root
        self.next = next
        self.previous = previous
        self.path = path

    @property
    def type(self):
        """Gets the type of this JObject.  # noqa: E501


        :return: The type of this JObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JObject.


        :param type: The type of this JObject.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Object", "Array", "Constructor", "Property", "Comment", "Integer", "Float", "String", "Boolean", "Null", "Undefined", "Date", "Raw", "Bytes", "Guid", "Uri", "TimeSpan"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def item(self):
        """Gets the item of this JObject.  # noqa: E501


        :return: The item of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this JObject.


        :param item: The item of this JObject.  # noqa: E501
        :type: JToken
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def has_values(self):
        """Gets the has_values of this JObject.  # noqa: E501


        :return: The has_values of this JObject.  # noqa: E501
        :rtype: bool
        """
        return self._has_values

    @has_values.setter
    def has_values(self, has_values):
        """Sets the has_values of this JObject.


        :param has_values: The has_values of this JObject.  # noqa: E501
        :type: bool
        """
        if has_values is None:
            raise ValueError("Invalid value for `has_values`, must not be `None`")  # noqa: E501

        self._has_values = has_values

    @property
    def first(self):
        """Gets the first of this JObject.  # noqa: E501


        :return: The first of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this JObject.


        :param first: The first of this JObject.  # noqa: E501
        :type: JToken
        """
        if first is None:
            raise ValueError("Invalid value for `first`, must not be `None`")  # noqa: E501

        self._first = first

    @property
    def last(self):
        """Gets the last of this JObject.  # noqa: E501


        :return: The last of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this JObject.


        :param last: The last of this JObject.  # noqa: E501
        :type: JToken
        """
        if last is None:
            raise ValueError("Invalid value for `last`, must not be `None`")  # noqa: E501

        self._last = last

    @property
    def count(self):
        """Gets the count of this JObject.  # noqa: E501


        :return: The count of this JObject.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this JObject.


        :param count: The count of this JObject.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def parent(self):
        """Gets the parent of this JObject.  # noqa: E501


        :return: The parent of this JObject.  # noqa: E501
        :rtype: JContainer
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this JObject.


        :param parent: The parent of this JObject.  # noqa: E501
        :type: JContainer
        """
        if parent is None:
            raise ValueError("Invalid value for `parent`, must not be `None`")  # noqa: E501

        self._parent = parent

    @property
    def root(self):
        """Gets the root of this JObject.  # noqa: E501


        :return: The root of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this JObject.


        :param root: The root of this JObject.  # noqa: E501
        :type: JToken
        """
        if root is None:
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def next(self):
        """Gets the next of this JObject.  # noqa: E501


        :return: The next of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this JObject.


        :param next: The next of this JObject.  # noqa: E501
        :type: JToken
        """
        if next is None:
            raise ValueError("Invalid value for `next`, must not be `None`")  # noqa: E501

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this JObject.  # noqa: E501


        :return: The previous of this JObject.  # noqa: E501
        :rtype: JToken
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this JObject.


        :param previous: The previous of this JObject.  # noqa: E501
        :type: JToken
        """
        if previous is None:
            raise ValueError("Invalid value for `previous`, must not be `None`")  # noqa: E501

        self._previous = previous

    @property
    def path(self):
        """Gets the path of this JObject.  # noqa: E501


        :return: The path of this JObject.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this JObject.


        :param path: The path of this JObject.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if issubclass(JObject, dict):
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
        if not isinstance(other, JObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
