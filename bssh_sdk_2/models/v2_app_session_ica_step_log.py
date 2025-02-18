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

class V2AppSessionIcaStepLog(object):
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
        'href_content': 'str',
        'id': 'str',
        'name': 'str',
        'href': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'href_content': 'HrefContent',
        'id': 'Id',
        'name': 'Name',
        'href': 'Href',
        'start_date': 'StartDate',
        'end_date': 'EndDate'
    }

    def __init__(self, href_content=None, id=None, name=None, href=None, start_date=None, end_date=None):  # noqa: E501
        """V2AppSessionIcaStepLog - a model defined in Swagger"""  # noqa: E501
        self._href_content = None
        self._id = None
        self._name = None
        self._href = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None
        if href_content is not None:
            self.href_content = href_content
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def href_content(self):
        """Gets the href_content of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The href_content of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: str
        """
        return self._href_content

    @href_content.setter
    def href_content(self, href_content):
        """Sets the href_content of this V2AppSessionIcaStepLog.


        :param href_content: The href_content of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: str
        """

        self._href_content = href_content

    @property
    def id(self):
        """Gets the id of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The id of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2AppSessionIcaStepLog.


        :param id: The id of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The name of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2AppSessionIcaStepLog.


        :param name: The name of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The href of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2AppSessionIcaStepLog.


        :param href: The href of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def start_date(self):
        """Gets the start_date of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The start_date of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this V2AppSessionIcaStepLog.


        :param start_date: The start_date of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this V2AppSessionIcaStepLog.  # noqa: E501


        :return: The end_date of this V2AppSessionIcaStepLog.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this V2AppSessionIcaStepLog.


        :param end_date: The end_date of this V2AppSessionIcaStepLog.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if issubclass(V2AppSessionIcaStepLog, dict):
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
        if not isinstance(other, V2AppSessionIcaStepLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
