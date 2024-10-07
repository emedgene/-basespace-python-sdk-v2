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

class V2BulkUnzipRequest(object):
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
        'run_ids': 'list[str]',
        'id': 'str'
    }

    attribute_map = {
        'run_ids': 'RunIds',
        'id': 'Id'
    }

    def __init__(self, run_ids=None, id=None):  # noqa: E501
        """V2BulkUnzipRequest - a model defined in Swagger"""  # noqa: E501
        self._run_ids = None
        self._id = None
        self.discriminator = None
        if run_ids is not None:
            self.run_ids = run_ids
        self.id = id

    @property
    def run_ids(self):
        """Gets the run_ids of this V2BulkUnzipRequest.  # noqa: E501

        Runs ids to unzip  # noqa: E501

        :return: The run_ids of this V2BulkUnzipRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._run_ids

    @run_ids.setter
    def run_ids(self, run_ids):
        """Sets the run_ids of this V2BulkUnzipRequest.

        Runs ids to unzip  # noqa: E501

        :param run_ids: The run_ids of this V2BulkUnzipRequest.  # noqa: E501
        :type: list[str]
        """

        self._run_ids = run_ids

    @property
    def id(self):
        """Gets the id of this V2BulkUnzipRequest.  # noqa: E501

        The Id of the resource  # noqa: E501

        :return: The id of this V2BulkUnzipRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2BulkUnzipRequest.

        The Id of the resource  # noqa: E501

        :param id: The id of this V2BulkUnzipRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(V2BulkUnzipRequest, dict):
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
        if not isinstance(other, V2BulkUnzipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
