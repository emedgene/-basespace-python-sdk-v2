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

class V2PostAppSessionsTrackRequest(object):
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
        'ica_analysis_id': 'str',
        'ica_project_id': 'str',
        'output_project_id': 'int',
        'id': 'str'
    }

    attribute_map = {
        'ica_analysis_id': 'IcaAnalysisId',
        'ica_project_id': 'IcaProjectId',
        'output_project_id': 'OutputProjectId',
        'id': 'Id'
    }

    def __init__(self, ica_analysis_id=None, ica_project_id=None, output_project_id=None, id=None):  # noqa: E501
        """V2PostAppSessionsTrackRequest - a model defined in Swagger"""  # noqa: E501
        self._ica_analysis_id = None
        self._ica_project_id = None
        self._output_project_id = None
        self._id = None
        self.discriminator = None
        self.ica_analysis_id = ica_analysis_id
        self.ica_project_id = ica_project_id
        if output_project_id is not None:
            self.output_project_id = output_project_id
        self.id = id

    @property
    def ica_analysis_id(self):
        """Gets the ica_analysis_id of this V2PostAppSessionsTrackRequest.  # noqa: E501


        :return: The ica_analysis_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :rtype: str
        """
        return self._ica_analysis_id

    @ica_analysis_id.setter
    def ica_analysis_id(self, ica_analysis_id):
        """Sets the ica_analysis_id of this V2PostAppSessionsTrackRequest.


        :param ica_analysis_id: The ica_analysis_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :type: str
        """
        if ica_analysis_id is None:
            raise ValueError("Invalid value for `ica_analysis_id`, must not be `None`")  # noqa: E501

        self._ica_analysis_id = ica_analysis_id

    @property
    def ica_project_id(self):
        """Gets the ica_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501


        :return: The ica_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :rtype: str
        """
        return self._ica_project_id

    @ica_project_id.setter
    def ica_project_id(self, ica_project_id):
        """Sets the ica_project_id of this V2PostAppSessionsTrackRequest.


        :param ica_project_id: The ica_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :type: str
        """
        if ica_project_id is None:
            raise ValueError("Invalid value for `ica_project_id`, must not be `None`")  # noqa: E501

        self._ica_project_id = ica_project_id

    @property
    def output_project_id(self):
        """Gets the output_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501

        Specifies the BSSH project that the BSSH appsession and BSSH datasets output by the ICA analysis will appear in.  # noqa: E501

        :return: The output_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :rtype: int
        """
        return self._output_project_id

    @output_project_id.setter
    def output_project_id(self, output_project_id):
        """Sets the output_project_id of this V2PostAppSessionsTrackRequest.

        Specifies the BSSH project that the BSSH appsession and BSSH datasets output by the ICA analysis will appear in.  # noqa: E501

        :param output_project_id: The output_project_id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :type: int
        """

        self._output_project_id = output_project_id

    @property
    def id(self):
        """Gets the id of this V2PostAppSessionsTrackRequest.  # noqa: E501

        The Id of the resource  # noqa: E501

        :return: The id of this V2PostAppSessionsTrackRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2PostAppSessionsTrackRequest.

        The Id of the resource  # noqa: E501

        :param id: The id of this V2PostAppSessionsTrackRequest.  # noqa: E501
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
        if issubclass(V2PostAppSessionsTrackRequest, dict):
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
        if not isinstance(other, V2PostAppSessionsTrackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
