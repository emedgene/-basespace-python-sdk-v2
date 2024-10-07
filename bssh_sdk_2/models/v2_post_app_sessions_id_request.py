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

class V2PostAppSessionsIdRequest(object):
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
        'execution_status': 'str',
        'status_summary': 'str',
        'qc_status': 'str',
        'delivery_status': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'execution_status': 'ExecutionStatus',
        'status_summary': 'StatusSummary',
        'qc_status': 'QcStatus',
        'delivery_status': 'DeliveryStatus',
        'comment': 'Comment'
    }

    def __init__(self, name=None, execution_status=None, status_summary=None, qc_status=None, delivery_status=None, comment=None):  # noqa: E501
        """V2PostAppSessionsIdRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._execution_status = None
        self._status_summary = None
        self._qc_status = None
        self._delivery_status = None
        self._comment = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if execution_status is not None:
            self.execution_status = execution_status
        if status_summary is not None:
            self.status_summary = status_summary
        if qc_status is not None:
            self.qc_status = qc_status
        if delivery_status is not None:
            self.delivery_status = delivery_status
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this V2PostAppSessionsIdRequest.  # noqa: E501

        The name of the appsession  # noqa: E501

        :return: The name of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2PostAppSessionsIdRequest.

        The name of the appsession  # noqa: E501

        :param name: The name of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def execution_status(self):
        """Gets the execution_status of this V2PostAppSessionsIdRequest.  # noqa: E501

        Immutable  # noqa: E501

        :return: The execution_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """Sets the execution_status of this V2PostAppSessionsIdRequest.

        Immutable  # noqa: E501

        :param execution_status: The execution_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._execution_status = execution_status

    @property
    def status_summary(self):
        """Gets the status_summary of this V2PostAppSessionsIdRequest.  # noqa: E501

        A summary of why or how the status changed, seen in the tooltip when clicking an analysis’ status  # noqa: E501

        :return: The status_summary of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this V2PostAppSessionsIdRequest.

        A summary of why or how the status changed, seen in the tooltip when clicking an analysis’ status  # noqa: E501

        :param status_summary: The status_summary of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def qc_status(self):
        """Gets the qc_status of this V2PostAppSessionsIdRequest.  # noqa: E501

        Possible values are: QcPassed, QcFailed, Discarded  # noqa: E501

        :return: The qc_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._qc_status

    @qc_status.setter
    def qc_status(self, qc_status):
        """Sets the qc_status of this V2PostAppSessionsIdRequest.

        Possible values are: QcPassed, QcFailed, Discarded  # noqa: E501

        :param qc_status: The qc_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._qc_status = qc_status

    @property
    def delivery_status(self):
        """Gets the delivery_status of this V2PostAppSessionsIdRequest.  # noqa: E501

        Possible values are: Undefined, DoNotDeliver, OnHold, ReadyForDelivery, DeliveryFailed, DeliveryInProgress, Delivered  # noqa: E501

        :return: The delivery_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this V2PostAppSessionsIdRequest.

        Possible values are: Undefined, DoNotDeliver, OnHold, ReadyForDelivery, DeliveryFailed, DeliveryInProgress, Delivered  # noqa: E501

        :param delivery_status: The delivery_status of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._delivery_status = delivery_status

    @property
    def comment(self):
        """Gets the comment of this V2PostAppSessionsIdRequest.  # noqa: E501

        Limited to 1024 characters  # noqa: E501

        :return: The comment of this V2PostAppSessionsIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V2PostAppSessionsIdRequest.

        Limited to 1024 characters  # noqa: E501

        :param comment: The comment of this V2PostAppSessionsIdRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(V2PostAppSessionsIdRequest, dict):
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
        if not isinstance(other, V2PostAppSessionsIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
