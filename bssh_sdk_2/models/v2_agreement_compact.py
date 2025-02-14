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

class V2AgreementCompact(object):
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
        'id': 'int',
        'href': 'str',
        'title': 'str',
        'category': 'str',
        'expired_on': 'datetime',
        'application': 'V1pre3ApplicationCompact'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'title': 'Title',
        'category': 'Category',
        'expired_on': 'ExpiredOn',
        'application': 'Application'
    }

    def __init__(self, id=None, href=None, title=None, category=None, expired_on=None, application=None):  # noqa: E501
        """V2AgreementCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._title = None
        self._category = None
        self._expired_on = None
        self._application = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category
        if expired_on is not None:
            self.expired_on = expired_on
        if application is not None:
            self.application = application

    @property
    def id(self):
        """Gets the id of this V2AgreementCompact.  # noqa: E501


        :return: The id of this V2AgreementCompact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2AgreementCompact.


        :param id: The id of this V2AgreementCompact.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this V2AgreementCompact.  # noqa: E501


        :return: The href of this V2AgreementCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2AgreementCompact.


        :param href: The href of this V2AgreementCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def title(self):
        """Gets the title of this V2AgreementCompact.  # noqa: E501


        :return: The title of this V2AgreementCompact.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this V2AgreementCompact.


        :param title: The title of this V2AgreementCompact.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def category(self):
        """Gets the category of this V2AgreementCompact.  # noqa: E501


        :return: The category of this V2AgreementCompact.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this V2AgreementCompact.


        :param category: The category of this V2AgreementCompact.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def expired_on(self):
        """Gets the expired_on of this V2AgreementCompact.  # noqa: E501


        :return: The expired_on of this V2AgreementCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_on

    @expired_on.setter
    def expired_on(self, expired_on):
        """Sets the expired_on of this V2AgreementCompact.


        :param expired_on: The expired_on of this V2AgreementCompact.  # noqa: E501
        :type: datetime
        """

        self._expired_on = expired_on

    @property
    def application(self):
        """Gets the application of this V2AgreementCompact.  # noqa: E501


        :return: The application of this V2AgreementCompact.  # noqa: E501
        :rtype: V1pre3ApplicationCompact
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this V2AgreementCompact.


        :param application: The application of this V2AgreementCompact.  # noqa: E501
        :type: V1pre3ApplicationCompact
        """

        self._application = application

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
        if issubclass(V2AgreementCompact, dict):
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
        if not isinstance(other, V2AgreementCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
