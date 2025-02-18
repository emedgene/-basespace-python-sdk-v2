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

class V2ResourcePresignedUrlCompleteRequestForEveryone(object):
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
        'upload_id': 'str',
        'file_path': 'str',
        'part_etags': 'list[V2PartEtag]',
        'size': 'int',
        'content_type': 'str'
    }

    attribute_map = {
        'upload_id': 'UploadId',
        'file_path': 'FilePath',
        'part_etags': 'PartEtags',
        'size': 'Size',
        'content_type': 'ContentType'
    }

    def __init__(self, upload_id=None, file_path=None, part_etags=None, size=None, content_type=None):  # noqa: E501
        """V2ResourcePresignedUrlCompleteRequestForEveryone - a model defined in Swagger"""  # noqa: E501
        self._upload_id = None
        self._file_path = None
        self._part_etags = None
        self._size = None
        self._content_type = None
        self.discriminator = None
        self.upload_id = upload_id
        self.file_path = file_path
        self.part_etags = part_etags
        self.size = size
        self.content_type = content_type

    @property
    def upload_id(self):
        """Gets the upload_id of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501


        :return: The upload_id of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this V2ResourcePresignedUrlCompleteRequestForEveryone.


        :param upload_id: The upload_id of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :type: str
        """
        if upload_id is None:
            raise ValueError("Invalid value for `upload_id`, must not be `None`")  # noqa: E501

        self._upload_id = upload_id

    @property
    def file_path(self):
        """Gets the file_path of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501


        :return: The file_path of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this V2ResourcePresignedUrlCompleteRequestForEveryone.


        :param file_path: The file_path of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :type: str
        """
        if file_path is None:
            raise ValueError("Invalid value for `file_path`, must not be `None`")  # noqa: E501

        self._file_path = file_path

    @property
    def part_etags(self):
        """Gets the part_etags of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501


        :return: The part_etags of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :rtype: list[V2PartEtag]
        """
        return self._part_etags

    @part_etags.setter
    def part_etags(self, part_etags):
        """Sets the part_etags of this V2ResourcePresignedUrlCompleteRequestForEveryone.


        :param part_etags: The part_etags of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :type: list[V2PartEtag]
        """
        if part_etags is None:
            raise ValueError("Invalid value for `part_etags`, must not be `None`")  # noqa: E501

        self._part_etags = part_etags

    @property
    def size(self):
        """Gets the size of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501


        :return: The size of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V2ResourcePresignedUrlCompleteRequestForEveryone.


        :param size: The size of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def content_type(self):
        """Gets the content_type of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501


        :return: The content_type of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this V2ResourcePresignedUrlCompleteRequestForEveryone.


        :param content_type: The content_type of this V2ResourcePresignedUrlCompleteRequestForEveryone.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

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
        if issubclass(V2ResourcePresignedUrlCompleteRequestForEveryone, dict):
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
        if not isinstance(other, V2ResourcePresignedUrlCompleteRequestForEveryone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
